"""Figures 2 and 3 from the eval records (scripts/eval_policy.py JSON) — numbers come from the logs only.

fig 2 (big boards, 16x16 = 256 and 20x20 = 400 cells): per kind, two panels — seconds per instance
      (log axis) and decap count / greedy+prune (paired, jointly solved) — one bar per method.
fig 3 (ladder): per kind x size, success rate (exact check) and count / greedy+prune for the rungs
      in fixed order (rung 0, 1, 2, 3) plus the two classical baselines as reference lines.

Run: .venv/bin/python scripts/fig_results.py --fig 2 --records 'runs/2026-10-28/*/eval/*.json' \
         --methods greedy+prune,local_search,r0_coord_rl,r1_modal_rl --sizes 16,20 --out reports/fig2_bigboard.png
"""
import argparse
import glob
import json
import os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
INK, INK2, GRID = "#0b0b0b", "#52514e", "#dddcd7"
KIND = {"pcb": "PCB-like", "pkg": "package-like", "ip": "interposer-like"}


def load(pattern):
    """{(tech, size, method): merged record over the _0/_1 files of a set}."""
    out = defaultdict(lambda: dict(ok=[], count=[], sec=[], n=0))
    for f in sorted(glob.glob(pattern, recursive=True)):
        r = json.load(open(f))
        k = (r["tech"], int(r["size"]), r["method"])
        out[k]["ok"] += r["ok"]
        out[k]["count"] += r["count"]
        out[k]["sec"].append(r["sec_per_inst"])
        out[k]["n"] += r["n"]
    return out


def paired_ratio(rec, ref):
    ok, cnt = np.asarray(rec["ok"], bool), np.asarray(rec["count"], float)
    rok, rcnt = np.asarray(ref["ok"], bool), np.asarray(ref["count"], float)
    both = ok & rok
    if not both.any():
        return np.nan, np.nan
    r = cnt[both] / np.maximum(rcnt[both], 1)
    # paired bootstrap 95% CI of the mean ratio
    rng = np.random.default_rng(0)
    bs = [r[rng.integers(len(r), size=len(r))].mean() for _ in range(2000)]
    return float(r.mean()), (float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)))


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(colors=INK2, labelsize=8)
    ax.grid(True, axis="y", color=GRID, lw=0.5)
    ax.set_axisbelow(True)


def fig2(recs, methods, sizes, out):
    techs = [t for t in ("pcb", "pkg", "ip") if any(k[0] == t for k in recs)]
    fig, axes = plt.subplots(2, len(techs), figsize=(3.4 * len(techs), 5.6), squeeze=False)
    width = 0.8 / len(methods)
    for j, t in enumerate(techs):
        ax_t, ax_c = axes[0, j], axes[1, j]
        for i, m in enumerate(methods):
            xs, secs, rels, los, his = [], [], [], [], []
            for s_i, s in enumerate(sizes):
                rec = recs.get((t, s, m))
                ref = recs.get((t, s, "greedy+prune"))
                if rec is None or ref is None:
                    continue
                xs.append(s_i + (i - (len(methods) - 1) / 2) * width)
                secs.append(np.mean(rec["sec"]))
                mean, ci = paired_ratio(rec, ref)
                rels.append(mean)
                los.append(mean - ci[0] if ci == ci else 0)
                his.append(ci[1] - mean if ci == ci else 0)
            if not xs:
                continue
            ax_t.bar(xs, secs, width * 0.92, color=SERIES[i], label=m)
            ax_c.bar(xs, rels, width * 0.92, color=SERIES[i], yerr=[los, his], error_kw=dict(lw=0.8, color=INK2), label=m)
            for x, v in zip(xs, secs):
                ax_t.text(x, v, f"{v:.2g}", ha="center", va="bottom", fontsize=6, color=INK2)
        ax_t.set_yscale("log")
        ax_t.set_title(KIND[t], fontsize=10, color=INK, loc="left")
        ax_c.axhline(1.0, color=INK, lw=0.8)
        for ax in (ax_t, ax_c):
            style(ax)
            ax.set_xticks(range(len(sizes)))
            ax.set_xticklabels([f"{s}x{s} ({s*s} cells)" for s in sizes])
        if j == 0:
            ax_t.set_ylabel("seconds per board (1 CPU core)", color=INK2, fontsize=9)
            ax_c.set_ylabel("decap count / greedy+prune (paired, 95% CI)", color=INK2, fontsize=9)
    axes[0, 0].legend(fontsize=7, frameon=False)
    fig.suptitle("Big boards: time and decap count, same calculator for every method", fontsize=11, color=INK, x=0.02, ha="left")
    fig.tight_layout()
    fig.savefig(out, dpi=200)


def fig3(recs, methods, sizes, out):
    techs = [t for t in ("pcb", "pkg", "ip") if any(k[0] == t for k in recs)]
    base = ["greedy+prune", "local_search"]
    rungs = [m for m in methods if m not in base]
    fig, axes = plt.subplots(2, len(techs), figsize=(3.4 * len(techs), 5.6), squeeze=False)
    width = 0.8 / max(1, len(rungs))
    for j, t in enumerate(techs):
        ax_s, ax_c = axes[0, j], axes[1, j]
        for i, m in enumerate(rungs):
            xs, succ, rels, los, his = [], [], [], [], []
            for s_i, s in enumerate(sizes):
                rec, ref = recs.get((t, s, m)), recs.get((t, s, "greedy+prune"))
                if rec is None or ref is None:
                    continue
                xs.append(s_i + (i - (len(rungs) - 1) / 2) * width)
                succ.append(np.mean(rec["ok"]))
                mean, ci = paired_ratio(rec, ref)
                rels.append(mean)
                los.append(mean - ci[0] if ci == ci else 0)
                his.append(ci[1] - mean if ci == ci else 0)
            if xs:
                ax_s.bar(xs, succ, width * 0.92, color=SERIES[i], label=m)
                ax_c.bar(xs, rels, width * 0.92, color=SERIES[i], yerr=[los, his], error_kw=dict(lw=0.8, color=INK2), label=m)
        for bi, m in enumerate(base):
            ys, yc = [], []
            for s in sizes:
                rec, ref = recs.get((t, s, m)), recs.get((t, s, "greedy+prune"))
                ys.append(np.mean(rec["ok"]) if rec else np.nan)
                yc.append(paired_ratio(rec, ref)[0] if rec and ref else np.nan)
            ax_s.plot(range(len(sizes)), ys, ls="--" if bi else "-", color=INK, lw=1, marker="_", ms=14, label=m)
            ax_c.plot(range(len(sizes)), yc, ls="--" if bi else "-", color=INK, lw=1, marker="_", ms=14, label=m)
        ax_s.set_ylim(0, 1.05)
        ax_s.set_title(KIND[t], fontsize=10, color=INK, loc="left")
        for ax in (ax_s, ax_c):
            style(ax)
            ax.set_xticks(range(len(sizes)))
            ax.set_xticklabels([f"{s}x{s}" for s in sizes])
        if j == 0:
            ax_s.set_ylabel("success rate (exact 700-pt check)", color=INK2, fontsize=9)
            ax_c.set_ylabel("decap count / greedy+prune (paired, 95% CI)", color=INK2, fontsize=9)
    axes[0, 0].legend(fontsize=7, frameon=False, loc="lower left")
    fig.suptitle("Ladder ablation: same data, same training, one component added per rung", fontsize=11, color=INK, x=0.02, ha="left")
    fig.tight_layout()
    fig.savefig(out, dpi=200)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fig", type=int, choices=[2, 3], required=True)
    ap.add_argument("--records", required=True, help="glob of eval JSON records")
    ap.add_argument("--methods", required=True, help="comma list, in display order")
    ap.add_argument("--sizes", default="16,20")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    recs = load(a.records)
    methods = a.methods.split(",")
    sizes = [int(s) for s in a.sizes.split(",")]
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    plt.rcParams["font.family"] = ["DejaVu Sans"]
    (fig2 if a.fig == 2 else fig3)(recs, methods, sizes, a.out)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
