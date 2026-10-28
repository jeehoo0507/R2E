"""Run one ladder rung end to end: stage 2 (distill) -> stage 3 (rl, init from the distilled best.pt)
-> certified evaluation of both checkpoints on the eval pools. One process; meant to be launched in
the background, one per rung (several rungs can share the GPU).

Run: .venv/bin/python scripts/run_rung.py --name r1_modal --arm "--feat modal" --day 2026-10-28 \
         --distill_hours 0.75 --rl_hours 1.25 [--common "..."] [--pool runs/pool_v1] [--skip_eval]
"""
import argparse
import os
import shlex
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
COMMON = "--d 128 --layers 4 --heads 8 --B 16 --M 8 --lr 3e-4 --iters 1000000 --val_every 100 --max_steps 64"


def sh(cmd, log):
    with open(log, "a") as f:
        f.write(f"\n$ {cmd}\n")
        f.flush()
        t = time.time()
        r = subprocess.run(shlex.split(cmd), cwd=ROOT, stdout=f, stderr=subprocess.STDOUT)
        f.write(f"[rc={r.returncode} {time.time()-t:.0f}s]\n")
    if r.returncode != 0:
        raise SystemExit(f"failed: {cmd} (see {log})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--arm", required=True, help='e.g. "--feat coord" | "--feat modal" | "--model mott" | "--model loop"')
    ap.add_argument("--day", default=time.strftime("%Y-%m-%d"))
    ap.add_argument("--pool", default="runs/pool_v1")
    ap.add_argument("--teacher_dir", default="data/teacher")
    ap.add_argument("--common", default=COMMON)
    ap.add_argument("--distill_hours", type=float, default=0.75)
    ap.add_argument("--rl_hours", type=float, default=1.25)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--eval_sets", default="eval_*")
    ap.add_argument("--eval_workers", type=int, default=6)
    ap.add_argument("--skip_eval", action="store_true")
    ap.add_argument("--skip_distill", action="store_true")
    a = ap.parse_args()
    base = f"runs/{a.day}/{a.name}"
    os.makedirs(base, exist_ok=True)
    log = os.path.join(base, "driver.log")
    pools = f"--pool {a.pool} --teacher_dir {a.teacher_dir} --seed {a.seed}"
    dist, rl = f"{base}_distill", f"{base}_rl"
    if not a.skip_distill:
        sh(f"{PY} train.py --stage distill {a.arm} {a.common} {pools} --hours {a.distill_hours} --out {dist}", log)
    sh(f"{PY} train.py --stage rl {a.arm} {a.common} {pools} --hours {a.rl_hours} --init {dist}/best.pt --out {rl}", log)
    if not a.skip_eval:
        for tag, run in (("distill", dist), ("rl", rl)):
            sh(f"{PY} scripts/eval_policy.py --pool {a.pool} --sets {a.eval_sets} --policy {a.name}_{tag}={run}/best.pt "
               f"--workers {a.eval_workers} --out {run}", log)
    with open(log, "a") as f:
        f.write("RUNG DONE\n")


if __name__ == "__main__":
    main()
