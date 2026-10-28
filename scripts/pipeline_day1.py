"""Day-1 driver, launched detached (scripts/bg.py) so it survives the agent round ending.

Order and limits follow agent/QUEUE.md (2026-10-28 14:20 UTC, pod OOM restarts): at most 4 concurrent
CPU worker processes (pool build + exact checks + teacher), no new process while the pod is above
45 GiB, memory logged at every stage start/end, the 20x20 eval pools last with 2 processes.
  1. teacher: make_teacher.py, 4 workers                                   -> data/teacher/
  2. rungs 0 (coord) and 1 (modal) in parallel on the GPU, same budget, CERTIFY_WORKERS=2 each (= 4)
  3. rung 2 (mott) training (CERTIFY_WORKERS=2) while the eval pools of side 10/16 are built (2 workers),
     then E0 (greedy+prune, LS, modal rule) and rung 0/1 certified evals on them (2 workers)
  4. rung 2 eval (4 workers), collect_results.py
  5. eval pools of side 20 (2 workers), then all methods on them (2 workers), collect_results.py
Every step skips work whose output already exists (pool/teacher files, eval records, finished
training stages; a killed training stage continues from its resume.pt), so after a pod restart
scripts/ensure_running.py just starts this again.
Run: .venv/bin/python scripts/bg.py agent/logs/pipeline_day1.log '.venv/bin/python scripts/pipeline_day1.py'
"""
import glob
import os
import subprocess
import sys
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
        if pat in cmd and "bash -c" not in cmd:
            return pid
    return None


def run(cmd, logfile, stage):
    wait_mem(log)
    log(f"START {stage} | {mem_line()}")
    log(f"$ {cmd}  (log {logfile})")
    with open(os.path.join(ROOT, logfile), "a") as f:
        r = subprocess.run(cmd, shell=True, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
    log(f"END {stage} rc={r.returncode} | {mem_line()}")
    return r.returncode


def start_rung(name, arm, certify_workers=2):
    if os.path.exists(os.path.join(ROOT, f"runs/{DAY}/{name}_rl/metrics.json")):
        log(f"{name}: rl stage finished, skip training")
        return None
    pid = alive(f"run_rung.py --name {name} ")
    if pid:
        log(f"{name}: already running (pid {pid}), attach")
        return pid
    cmd = (f"{PY} scripts/run_rung.py --name {name} --arm '{arm}' --day {DAY} --pool {POOL} "
           f"--distill_hours {DISTILL_H} --rl_hours {RL_H} --skip_eval")
    wait_mem(log)
    log(f"START train {name} (CERTIFY_WORKERS={certify_workers}) | {mem_line()}")
    log(f"$ {cmd}")
    os.makedirs(os.path.join(ROOT, f"runs/{DAY}/{name}"), exist_ok=True)
    f = open(os.path.join(ROOT, f"runs/{DAY}/{name}/rung_stdout.log"), "a")
    env = dict(os.environ, CERTIFY_WORKERS=str(certify_workers))
    return subprocess.Popen(cmd, shell=True, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT, env=env)


def wait_rung(name, p):
    if p is None:
        return
    if isinstance(p, subprocess.Popen):
        rc = p.wait()
    else:
        while alive(f"run_rung.py --name {name} "):
            time.sleep(60)
        rc = "?"
    log(f"END train {name} rc={rc} | {mem_line()}")


def eval_methods(sets, workers, stage):
    run(f"{PY} scripts/eval_policy.py --pool {POOL} --sets '{sets}' --methods gp,ls,modal_rule --workers {workers} "
        f"--out runs/{DAY}/baselines", f"runs/{DAY}/baselines_eval.log", f"E0 {stage}")


def eval_rung(name, sets, workers):
    for tag in ("distill", "rl"):
        run_dir = f"runs/{DAY}/{name}_{tag}"
        if os.path.exists(os.path.join(ROOT, run_dir, "metrics.json")):
            run(f"{PY} scripts/eval_policy.py --pool {POOL} --sets '{sets}' --policy {name}_{tag}={run_dir}/best.pt "
                f"--workers {workers} --out {run_dir}", f"{run_dir}/eval.log", f"eval {name}_{tag}")
        else:
            log(f"{run_dir} not finished (no metrics.json), skip eval")


def build_pools(sizes, workers):
    run(f"{PY} scripts/build_pools.py --out {POOL} --workers {workers} --only eval --eval_sizes {sizes}",
        "agent/logs/build_pools_v1_r3.log", f"build eval pools side {sizes}")


def main():
    log(f"driver start | {mem_line()}")
    while n_pools("train_*.pkl") + n_pools("val_*.pkl") < N_TRAINVAL:
        time.sleep(60)
    run(f"{PY} scripts/make_teacher.py --pool {POOL} --out data/teacher --workers 4", "agent/logs/make_teacher.log",
        "teacher")
    if len(glob.glob(os.path.join(ROOT, "data/teacher/train_*.npz"))) < n_pools("train_*.pkl"):
        log("teacher incomplete, stop (training would silently fall back to greedy+prune)")
        return
    procs = {n: start_rung(n, arm) for n, arm in RUNGS[:2]}
    for n, p in procs.items():
        wait_rung(n, p)
    p2 = start_rung(*RUNGS[2])
    build_pools("10,16", 2)
    eval_methods("eval_*", 2, "side 10/16")
    for n, _ in RUNGS[:2]:
        eval_rung(n, "eval_*", 2)
    wait_rung(RUNGS[2][0], p2)
    eval_rung(RUNGS[2][0], "eval_*", 4)
    run(f"{PY} scripts/collect_results.py", "agent/logs/collect_results.log", "collect_results")
    build_pools("20", 2)
    if n_pools("eval_*20_*.pkl") < N_EVAL20:
        log("side-20 eval pools incomplete")
    eval_methods("eval_*", 2, "side 20")
    for n, _ in RUNGS:
        eval_rung(n, "eval_*", 2)
    run(f"{PY} scripts/collect_results.py", "agent/logs/collect_results.log", "collect_results")
    log("PIPELINE DAY1 DONE")


if __name__ == "__main__":
    main()
