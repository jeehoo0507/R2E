"""Generate RESULTS.md from metrics.json files (never type numbers by hand).

Sources
  runs/**/eval/*.json          evaluation records written by scripts/eval_policy.py:
                               {set, method, tech, size, n, ok[], count[], sec_per_inst, ...}
  runs/**/metrics.json         training records written by train.py (final / best validation)
  data/teacher/*.json          teacher statistics (LS vs greedy+prune on the training pools)

Run: .venv/bin/python scripts/collect_results.py [--out RESULTS.md]
"""
import argparse
import glob
import json
import os
import sys
import time
from collections import OrderedDict, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load_evals():
    recs = []
    for f in sorted(glob.glob("runs/**/eval/*.json", recursive=True)):
        try:
            d = json.load(open(f))
            d["_file"] = f
            recs.append(d)
        except Exception as e:  # noqa: BLE001
            print("skip", f, e, file=sys.stderr)
    return recs


def fmt(x, nd=2):
    return "–" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:.{nd}f}"


def eval_tables(recs):
    """One table per (tech, size): rows = methods. Columns: success (exact), count on jointly solved,
    count / greedy+prune (paired, on instances both solve), sec per instance."""
    by_set = defaultdict(dict)
    for r in recs:
        key = (r["tech"], int(r["size"]))
        by_set[key][r["method"]] = r
    lines = []
    for (tech, size) in sorted(by_set, key=lambda k: (k[0], k[1])):
        ms = by_set[(tech, size)]
        gp = ms.get("greedy+prune")
        n = next(iter(ms.values()))["n"]
        lines += [f"### {tech} {size}×{size} (문제 {n}개)", "",
                  "| 방법 | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 짝지음) | 문제당 시간 (s) | 출처 |",
                  "|---|---|---|---|---|---|"]
        for m in sorted(ms, key=lambda k: (k != "greedy+prune", k != "local_search", k)):
            r = ms[m]
            ok = np.asarray(r["ok"], bool)
            cnt = np.asarray(r["count"], float)
            rel = None
            if gp is not None:
                gok = np.asarray(gp["ok"], bool)
                gcnt = np.asarray(gp["count"], float)
                both = ok & gok
                rel = float(np.mean(cnt[both] / np.maximum(gcnt[both], 1))) if both.any() else None
            lines.append(f"| {m} | {ok.mean():.2f} | {fmt(cnt[ok].mean() if ok.any() else None)} | {fmt(rel, 3)} | "
                         f"{fmt(r.get('sec_per_inst'), 3)} | `{r['_file']}` |")
        lines.append("")
    return lines


def ladder_table(recs):
    """Success / count ratio per method across kinds and sizes (one row per method)."""
    by_method = defaultdict(dict)
    gp = {}
    for r in recs:
        key = (r["tech"], int(r["size"]))
        by_method[r["method"]][key] = r
        if r["method"] == "greedy+prune":
            gp[key] = r
    keys = sorted({k for m in by_method.values() for k in m}, key=lambda k: (k[0], k[1]))
    if not keys:
        return []
    head = "| 방법 | " + " | ".join(f"{t} {s}" for t, s in keys) + " |"
    lines = ["### 요약: 정확 검사 성공률 / 개수÷greedy+prune (둘 다 성공)", "", head, "|---|" + "---|" * len(keys)]
    for m in sorted(by_method, key=lambda k: (k != "greedy+prune", k != "local_search", k)):
        cells = []
        for k in keys:
            r = by_method[m].get(k)
            if r is None:
                cells.append("–")
                continue
            ok = np.asarray(r["ok"], bool)
            rel = "–"
            if k in gp:
                gok = np.asarray(gp[k]["ok"], bool)
                both = ok & gok
                if both.any():
                    rel = f"{np.mean(np.asarray(r['count'], float)[both] / np.maximum(np.asarray(gp[k]['count'], float)[both], 1)):.2f}"
            cells.append(f"{ok.mean():.2f} / {rel}")
        lines.append(f"| {m} | " + " | ".join(cells) + " |")
    return lines + [""]


def train_table():
    lines = []
    files = sorted(glob.glob("runs/**/metrics.json", recursive=True))
    if not files:
        return lines
    lines += ["## 학습 기록 (train.py metrics.json)", "",
              "| run | feat / model | stage | iters | 시간 (h) | 최종 val (count/g+p, fail) | 출처 |", "|---|---|---|---|---|---|---|"]
    for f in files:
        try:
            d = json.load(open(f))
        except Exception:  # noqa: BLE001
            continue
        a = d.get("args", {})
        val = d.get("final_val", {})
        vs = ", ".join(f"{k}: {fmt(v[0])}/{fmt(v[1])}" for k, v in val.items())
        lines.append(f"| {os.path.dirname(f)} | {a.get('feat')} / {a.get('model')} | {a.get('stage')} | {d.get('iters')} | "
                     f"{fmt(d.get('hours'), 2)} | {vs} | `{f}` |")
    return lines + [""]


def teacher_table():
    files = sorted(glob.glob("data/teacher/*.json"))
    if not files:
        return []
    lines = ["## 선생님 해 (학습 풀, LS vs greedy+prune)", "",
             "| 풀 | g+p 성공 | LS 정확 성공 | LS/g+p 개수 | LS가 줄인 비율 | 선생님 평균 개수 | LS 시간 (s) |", "|---|---|---|---|---|---|---|"]
    for f in files:
        d = json.load(open(f))
        lines.append(f"| {d['name']} | {fmt(d['gp_ok'])} | {fmt(d['ls_ok'])} | {fmt(d['ls_over_gp'], 3)} | "
                     f"{fmt(d['improved_frac'])} | {fmt(d['teacher_count_mean'])} | {fmt(d['t_ls'], 0)} |")
    return lines + [""]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="RESULTS.md")
    a = ap.parse_args()
    recs = load_evals()
    lines = [f"# RESULTS (자동 생성: `scripts/collect_results.py`, {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", "",
             "성공 = `verify.py` 700점 + 피크 정밀화 정확 검사에서 최악 |Z| ≤ 1.01·Zt. 모든 방법은 cutting-plane 안에서 실행. "
             "시간은 문제당 초(판 준비 제외, 같은 CPU 계산기). 손으로 적은 숫자는 없다.", "",
             "## 평가 (정확 검사)", ""]
    lines += ladder_table(recs)
    lines += eval_tables(recs)
    lines += train_table()
    lines += teacher_table()
    open(a.out, "w").write("\n".join(lines) + "\n")
    print(f"wrote {a.out}: {len(recs)} eval records")


if __name__ == "__main__":
    main()
