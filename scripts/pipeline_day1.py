"""Day-1 driver, launched detached (scripts/bg.py) so it survives the agent round ending.

Order (each step skips work whose output already exists, so the driver can be restarted):
  1. wait for train_*/val_* pools (scripts/build_pools.py, started separately)
  2. teacher: make_teacher.py (g+p -> LS, certified)                     -> data/teacher/
  3. rungs 0 (coord) and 1 (modal) in parallel on the GPU, same budget: distill -> rl, no eval yet
  4. wait for eval_* pools; E0 baselines (greedy+prune, LS, modal rule)  -> runs/<day>/baselines
  5. certified eval of rung 0/1 distill + rl checkpoints                  -> runs/<day>/<rung>_{distill,rl}
  6. rung 2 (mott) distill -> rl -> eval
  7. collect_results.py -> RESULTS.md
Run: .venv/bin/python scripts/bg.py agent/logs/pipeline_day1.log '.venv/bin/python scripts/pipeline_day1.py'
"""
import glob
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
POOL = "runs/pool_v1"
DAY = "2026-10-28"
N_TRAINVAL, N_EVAL = 30, 18
DISTILL_H, RL_H = 0.75, 1.25


def log(msg):
    print(f"[{time.strftime('%H:%M:%S', time.gmtime())}] {msg}", flush=True)


def wait_pools(pattern, n):
    while len(glob.glob(os.path.join(ROOT, POOL, pattern))) < n:
        time.sleep(60)


def run(cmd, logfile):
    log(f"$ {cmd}  (log {logfile})")
    with open(os.path.join(ROOT, logfile), "a") as f:
        r = subprocess.run(cmd, shell=True, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
    log(f"rc={r.returncode}")
    return r.returncode


def start_rung(name, arm):
    if os.path.exists(os.path.join(ROOT, f"runs/{DAY}/{name}_rl/best.pt")):
        log(f"{name}: rl checkpoint exists, skip training")
        return None
    cmd = (f"{PY} scripts/run_rung.py --name {name} --arm '{arm}' --day {DAY} --pool {POOL} "
           f"--distill_hours {DISTILL_H} --rl_hours {RL_H} --skip_eval")
    log(f"start {name}: {cmd}")
    os.makedirs(os.path.join(ROOT, f"runs/{DAY}/{name}"), exist_ok=True)
    f = open(os.path.join(ROOT, f"runs/{DAY}/{name}/rung_stdout.log"), "a")
    env = dict(os.environ, CERTIFY_WORKERS="6")   # two rungs + pool build share 16 cores
    return subprocess.Popen(cmd, shell=True, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT, env=env)


def eval_rung(name):
    for tag in ("distill", "rl"):
        run_dir = f"runs/{DAY}/{name}_{tag}"
        if os.path.exists(os.path.join(ROOT, run_dir, "best.pt")):
            run(f"{PY} scripts/eval_policy.py --pool {POOL} --sets 'eval_*' --policy {name}_{tag}={run_dir}/best.pt "
                f"--workers 14 --out {run_dir}", f"{run_dir}/eval.log")
        else:
            log(f"{run_dir}/best.pt missing, skip eval")


def main():
    log("wait for train/val pools")
    wait_pools("train_*.pkl", N_TRAINVAL - 3)
    wait_pools("val_*.pkl", 3)
    run(f"{PY} scripts/make_teacher.py --pool {POOL} --out data/teacher --workers 8", "agent/logs/make_teacher.log")
    procs = {n: start_rung(n, arm) for n, arm in (("r0_coord", "--feat coord"), ("r1_modal", "--feat modal"))}
    log("wait for eval pools")
    wait_pools("eval_*.pkl", N_EVAL)
    run(f"{PY} scripts/eval_policy.py --pool {POOL} --sets 'eval_*' --methods gp,ls,modal_rule --workers 12 "
        f"--out runs/{DAY}/baselines", f"runs/{DAY}/baselines_eval.log")
    for n, p in procs.items():
        if p is not None:
            log(f"wait {n}: rc={p.wait()}")
        eval_rung(n)
    run(f"{PY} scripts/collect_results.py", "agent/logs/collect_results.log")
    p = start_rung("r2_mott", "--model mott")
    if p is not None:
        log(f"wait r2_mott: rc={p.wait()}")
    eval_rung("r2_mott")
    run(f"{PY} scripts/collect_results.py", "agent/logs/collect_results.log")
    log("PIPELINE DAY1 DONE")


if __name__ == "__main__":
    main()
