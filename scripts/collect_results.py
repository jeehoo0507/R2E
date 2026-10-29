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


def merged(recs):
    """{(tech, size): {method: merged record}}. A (tech, size) has several pool files (eval_pcb10_0, _1, ...);
    each method's files are concatenated, and the count ratio to greedy+prune is paired only within the same
    pool file (same problems), never across files. The latest record per (file, method) wins."""
    by = defaultdict(lambda: defaultdict(dict))
    for r in recs:
        by[(r["tech"], int(r["size"]))][r["method"]][r["set"]] = r
    out = defaultdict(dict)
    for key, ms in by.items():
        gp = ms.get("greedy+prune", {})
        for m, sets in ms.items():
            ok, cnt, ratio, sec, files = [], [], [], [], []
            for s in sorted(sets):
                r = sets[s]
                o = np.asarray(r["ok"], bool)
                c = np.asarray(r["count"], float)
                ok.append(o)
                cnt.append(c)
                sec.append((r.get("sec_per_inst", float("nan")), len(o)))
                files.append(r["_file"])
                if s in gp:
                    g = gp[s]
                    both = o & np.asarray(g["ok"], bool)
                    ratio.append(c[both] / np.maximum(np.asarray(g["count"], float)[both], 1))
            ok, cnt = np.concatenate(ok), np.concatenate(cnt)
            ratio = np.concatenate(ratio) if ratio else np.zeros(0)
            out[key][m] = dict(ok=ok, cnt=cnt, rel=float(ratio.mean()) if ratio.size else None,
                               sec=sum(t * n for t, n in sec) / sum(n for _, n in sec), sets=sorted(sets), files=files)
    return out


def eval_tables(recs):
    """One table per (tech, size): rows = methods. Columns: problems evaluated (all pool files of that size),
    success (exact), count on solved, count / greedy+prune (paired within a file, on instances both solve),
    sec per instance."""
    by = merged(recs)
    lines = []
    for (tech, size) in sorted(by):
        ms = by[(tech, size)]
        lines += [f"### {tech} {size}×{size}", "",
                  "| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |",
                  "|---|---|---|---|---|---|---|"]
        for m in sorted(ms, key=lambda k: (k != "greedy+prune", k != "local_search", k)):
            r = ms[m]
            ok, cnt = r["ok"], r["cnt"]
            sets = ", ".join(s.rsplit("_", 1)[1] for s in r["sets"])
            lines.append(f"| {m} | {len(ok)} ({sets}) | {ok.mean():.2f} | {fmt(cnt[ok].mean() if ok.any() else None)} | "
                         f"{fmt(r['rel'], 3)} | {fmt(r['sec'], 3)} | " + ", ".join(f"`{f}`" for f in r["files"]) + " |")
        lines.append("")
    return lines


def ladder_table(recs):
    """Success / count ratio per method across kinds and sizes (one row per method; all pool files merged)."""
    by = merged(recs)
    keys = sorted(by)
    if not keys:
        return []
    methods = sorted({m for k in keys for m in by[k]}, key=lambda k: (k != "greedy+prune", k != "local_search", k))
    head = "| 방법 | " + " | ".join(f"{t} {s}" for t, s in keys) + " |"
    lines = ["### 요약: 정확 검사 성공률 / 개수÷greedy+prune (둘 다 성공) [문제 수]", "", head, "|---|" + "---|" * len(keys)]
    for m in methods:
        cells = []
        for k in keys:
            r = by[k].get(m)
            cells.append("–" if r is None else f"{r['ok'].mean():.2f} / {fmt(r['rel'])} [{len(r['ok'])}]")
        lines.append(f"| {m} | " + " | ".join(cells) + " |")
    return lines + [""]


def type_table(recs):
    """Share of each decap type among the placed decaps (record occ: cell -> type, -1 empty), split by
    whether the exact check passed. Library per kind in decap_loop/techs.py (type 0 = largest C)."""
    acc = defaultdict(lambda: defaultdict(list))
    for r in recs:
        if "occ" not in r:
            continue
        occ, ok = np.asarray(r["occ"]), np.asarray(r["ok"], bool)
        for tag, sel in (("성공", ok), ("실패", ~ok)):
            acc[(r["tech"], int(r["size"]))][(r["method"], tag)].append(occ[sel])
    if not acc:
        return []
    lines = ["## decap 종류 비율 (놓인 decap 중, 정확 검사 성공/실패 문제별; 종류 0 = C가 가장 큰 것, `decap_loop/techs.py`)", "",
             "| 판 | 방법 | 문제 | 문제 수 | 평균 개수 | 종류 0 | 종류 1 | 종류 2 |", "|---|---|---|---|---|---|---|---|"]
    for key in sorted(acc):
        for (m, tag) in sorted(acc[key], key=lambda k: (k[0] != "greedy+prune", k[0], k[1])):
            o = np.concatenate(acc[key][(m, tag)])
            if len(o) == 0:
                continue
            placed = o[o >= 0]
            share = np.bincount(placed, minlength=3) / max(len(placed), 1)
            lines.append(f"| {key[0]} {key[1]} | {m} | {tag} | {len(o)} | {(o >= 0).sum(1).mean():.1f} | "
                         + " | ".join(f"{s:.2f}" for s in share[:3]) + " |")
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
    lines += type_table(recs)
    lines += train_table()
    lines += teacher_table()
    open(a.out, "w").write("\n".join(lines) + "\n")
    print(f"wrote {a.out}: {len(recs)} eval records")


if __name__ == "__main__":
    main()
