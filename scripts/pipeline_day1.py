"""Day-1 driver, launched detached (scripts/bg.py) so it survives the agent round ending.

Limits follow agent/QUEUE.md (2026-10-28 14:20 UTC, pod OOM restarts): at most 4 concurrent CPU worker
processes (pool build + exact checks + teacher), no new process while the pod is above 45 GiB, memory
logged at every stage start/end, the 20x20 eval pools last with 2 processes.
Rungs train one at a time: two train.py processes with all 27 pools dense on the GPU do not fit in
24 GB (CUDA OOM at load, 15:15 UTC 10/28).

  0. teacher: make_teacher.py, 4 workers (skips finished files)          -> data/teacher/
  GPU lane : r0 coord -> r1 modal -> r2 mott, each distill -> rl, CERTIFY_WORKERS=2   (2 workers)
  CPU lane : eval pools side 10/16 -> E0 (greedy+prune, LS, modal rule) -> certified eval of each rung
             as soon as it finishes -> collect_results -> eval pools side 20 -> everything on side 20
             -> collect_results                                                     (2 workers)
Every step skips work whose output already exists (pool/teacher files, eval records, finished
training stages; a killed training stage continues from its resume.pt), and a step whose process is
still alive from a previous driver is waited for instead of started twice, so after a pod restart
scripts/ensure_running.py just starts this again.
Run: .venv/bin/python scripts/bg.py agent/logs/pipeline_day1.log '.venv/bin/python scripts/pipeline_day1.py'
"""
import glob
import os
import subprocess
import sys
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mem import mem_line, wait_mem  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
POOL = "runs/pool_v1"
DAY = "2026-10-28"
N_TRAINVAL, N_EVAL20 = 30, 6     # side-20 eval pools: 3 kinds x 2 files
DISTILL_H, RL_H = 0.75, 1.25
RUNGS = (("r0_coord", "--feat coord"), ("r1_modal", "--feat modal"), ("r2_mott", "--model mott"))
DONE = {n: threading.Event() for n, _ in RUNGS}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {msg}", flush=True)


def n_pools(pattern):
    return len(glob.glob(os.path.join(ROOT, POOL, pattern)))


def alive(pat):
    """pid of a live process whose command line contains pat (a driver restarted while its children live)."""
    me = str(os.getpid())
    for pid in filter(str.isdigit, os.listdir("/proc")):
        if pid == me:
            continue
        try:
            cmd = open(f"/proc/{pid}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
        except OSError:
            continue
        if pat in cmd and "bash -c" not in cmd and "/bin/sh -c" not in cmd:
            return pid
    return None


def run(cmd, logfile, stage, attach=None, env=None):
    """Run cmd to completion; if a process matching `attach` is already alive, wait for it instead."""
    pid = alive(attach) if attach else None
    if pid:
        log(f"ATTACH {stage} (pid {pid} still running)")
        while alive(attach):
            time.sleep(60)
        log(f"END {stage} (attached) | {mem_line()}")
        return 0
    wait_mem(log)
    log(f"START {stage} | {mem_line()}")
    log(f"$ {cmd}  (log {logfile})")
    with open(os.path.join(ROOT, logfile), "a") as f:
        r = subprocess.run(cmd, shell=True, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT,
                           env=dict(os.environ, **(env or {})))
    log(f"END {stage} rc={r.returncode} | {mem_line()}")
    return r.returncode


def gpu_lane():
    for name, arm in RUNGS:
        if os.path.exists(os.path.join(ROOT, f"runs/{DAY}/{name}_rl/metrics.json")):
            log(f"{name}: rl stage finished, skip training")
        else:
            os.makedirs(os.path.join(ROOT, f"runs/{DAY}/{name}"), exist_ok=True)
            run(f"{PY} scripts/run_rung.py --name {name} --arm '{arm}' --day {DAY} --pool {POOL} "
                f"--distill_hours {DISTILL_H} --rl_hours {RL_H} --skip_eval", f"runs/{DAY}/{name}/rung_stdout.log",
                f"train {name} (CERTIFY_WORKERS=2)", attach=f"run_rung.py --name {name} ", env={"CERTIFY_WORKERS": "2"})
        DONE[name].set()


def eval_methods(stage):
    run(f"{PY} scripts/eval_policy.py --pool {POOL} --sets 'eval_*' --methods gp,ls,modal_rule --workers 2 "
        f"--out runs/{DAY}/baselines", f"runs/{DAY}/baselines_eval.log", f"E0 {stage}",
        attach=f"--workers 2 --out runs/{DAY}/baselines")


def eval_rung(name):
    for tag in ("distill", "rl"):
        run_dir = f"runs/{DAY}/{name}_{tag}"
        if os.path.exists(os.path.join(ROOT, run_dir, "metrics.json")):
            run(f"{PY} scripts/eval_policy.py --pool {POOL} --sets 'eval_*' --policy {name}_{tag}={run_dir}/best.pt "
                f"--workers 2 --out {run_dir}", f"{run_dir}/eval.log", f"eval {name}_{tag}", attach=f"--workers 2 --out {run_dir}")
        else:
            log(f"{run_dir} not finished (no metrics.json), skip eval")


def build_pools(sizes):
    run(f"{PY} scripts/build_pools.py --out {POOL} --workers 2 --only eval --eval_sizes {sizes}",
        "agent/logs/build_pools_v1_r3.log", f"build eval pools side {sizes}", attach="scripts/build_pools.py")


def collect():
    run(f"{PY} scripts/collect_results.py", "agent/logs/collect_results.log", "collect_results")


def cpu_lane():
    build_pools("10,16")
    eval_methods("side 10/16")
    for name, _ in RUNGS:
        DONE[name].wait()
        eval_rung(name)
        collect()
    build_pools("20")
    if n_pools("eval_*20_*.pkl") < N_EVAL20:
        log("side-20 eval pools incomplete")
    eval_methods("side 20")
    for name, _ in RUNGS:
        eval_rung(name)
    collect()


def main():
    log(f"driver start | {mem_line()}")
    while n_pools("train_*.pkl") + n_pools("val_*.pkl") < N_TRAINVAL:
        time.sleep(60)
    run(f"{PY} scripts/make_teacher.py --pool {POOL} --out data/teacher --workers 4", "agent/logs/make_teacher.log",
        "teacher", attach="scripts/make_teacher.py")
    if len(glob.glob(os.path.join(ROOT, "data/teacher/train_*.npz"))) < n_pools("train_*.pkl"):
        log("teacher incomplete, stop (training would silently fall back to greedy+prune)")
        return
    lanes = [threading.Thread(target=gpu_lane), threading.Thread(target=cpu_lane)]
    for t in lanes:
        t.start()
    for t in lanes:
        t.join()
    log("PIPELINE DAY1 DONE")


if __name__ == "__main__":
    main()
