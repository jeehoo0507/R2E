"""End-to-end smoke test of the day-1 pipeline on tiny boards (a few minutes):
  1. tiny certified pools for the three kinds (6x6): train_*, val_*, eval_*
  2. scripts/make_teacher.py on them
  3. train.py --stage distill (feat coord / modal / model mott), 3 iterations each
  4. train.py --stage rl --init <distill>, 3 iterations
  5. scripts/eval_policy.py (gp, ls, policies) + scripts/collect_results.py
Stops at the first failure. Run: .venv/bin/python scripts/smoke_pipeline.py [--keep]
"""
import argparse
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
POOL, TEACH, RUNS = "runs/smoke_pipe/pool", "runs/smoke_pipe/teacher", "runs/smoke_pipe/runs"
PY = sys.executable


def step(name, fn):
    t = time.time()
    try:
        msg = fn()
    except Exception as e:  # noqa: BLE001
        print(f"[FAIL] {name}: {type(e).__name__}: {e}", flush=True)
        sys.exit(1)
    print(f"[ OK ] {name} ({time.time() - t:.1f}s){' — ' + str(msg) if msg else ''}", flush=True)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        raise RuntimeError(" ".join(cmd) + "\n" + (r.stdout + r.stderr)[-3000:])
    return r.stdout


def build_pools():
    import numpy as np
    import torch
    torch.set_num_threads(1)
    from decap_loop.bank import save_bank
    from decap_loop.baselines import greedy
    from decap_loop.pdn import sample_batch
    from decap_loop.techs import DIFFICULTY, TECHS
    from decap_loop.verify import cutting_plane
    os.makedirs(POOL, exist_ok=True)
    out = []
    for i, (t, cfg) in enumerate(TECHS.items()):
        for kind in ("train", "val", "eval"):
            name = f"{kind}_{t}6_0"
            b = sample_batch(4, 6, 6, cfg, np.random.default_rng(10 * i + len(kind)), difficulty=DIFFICULTY[t])
            r, info = cutting_plane(lambda bb: greedy(bb, cfg), b, cfg, max_rounds=3)
            ok = info["worst"] <= np.log10(1.01)
            res = {"greedy+prune": dict(occ=r["occ"].cpu().numpy(), worst=info["worst"], ok=ok, count=(r["occ"] >= 0).sum(1).cpu().numpy())}
            save_bank(os.path.join(POOL, name + ".pkl"), b, res)
            out.append(f"{name} F={b.freqs.shape[1]} ok {ok.mean():.2f}")
    return ", ".join(out)


def teacher():
    return run([PY, "scripts/make_teacher.py", "--pool", POOL, "--out", TEACH, "--ls", "1x4", "--workers", "3"]).strip().splitlines()[-2]


def train(dev):
    common = ["--pool", POOL, "--teacher_dir", TEACH, "--val_pools", "val_pcb6_0,val_pkg6_0,val_ip6_0", "--iters", "3",
              "--val_every", "3", "--B", "4", "--M", "2", "--d", "32", "--layers", "1", "--heads", "2", "--device", dev]
    arms = {"coord": ["--feat", "coord"], "modal": ["--feat", "modal"], "mott": ["--model", "mott"]}
    for name, extra in arms.items():
        run([PY, "train.py", "--stage", "distill", "--out", f"{RUNS}/{name}_distill"] + common + extra)
        assert os.path.exists(f"{RUNS}/{name}_distill/best.pt"), name
        run([PY, "train.py", "--stage", "rl", "--init", f"{RUNS}/{name}_distill/best.pt", "--out", f"{RUNS}/{name}_rl"] + common + extra)
        assert os.path.exists(f"{RUNS}/{name}_rl/metrics.json"), name
    return "coord / modal / mott: distill + rl, metrics written"


def evaluate():
    run([PY, "scripts/eval_policy.py", "--pool", POOL, "--sets", "eval_*", "--methods", "gp,ls", "--ls", "1x4",
         "--policy", f"coord={RUNS}/coord_rl/best.pt", f"modal={RUNS}/modal_rl/best.pt", f"mott={RUNS}/mott_rl/best.pt",
         "--rounds", "1", "--workers", "6", "--out", f"{RUNS}/eval_smoke"])
    n = len(os.listdir(f"{RUNS}/eval_smoke/eval"))
    assert n == 3 * 5, n
    return f"{n} eval records"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--device", default="cuda")
    a = ap.parse_args()
    shutil.rmtree("runs/smoke_pipe", ignore_errors=True)
    step("1 tiny pools (3 kinds)", build_pools)
    step("2 teacher (g+p -> LS, certified)", teacher)
    step("3+4 train distill -> rl (coord, modal, mott)", lambda: train(a.device))
    step("5 eval_policy (gp, ls, 3 policies)", evaluate)
    if not a.keep:
        shutil.rmtree("runs/smoke_pipe", ignore_errors=True)
    print("PIPELINE SMOKE PASSED", flush=True)


if __name__ == "__main__":
    main()
