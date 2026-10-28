"""Relaunch the detached day jobs if a workspace restart killed them (happened 06:41 and ~13:45 UTC on 10/28).

Every job it starts skips finished outputs, so running this when the jobs are alive is a no-op and
running it after a restart resumes where the files left off. Run at the start of every round:
  .venv/bin/python scripts/ensure_running.py
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = ".venv/bin/python"
JOBS = [  # (pattern in cmdline, log, command); the driver builds the eval pools itself (QUEUE memory rule)
    ("scripts/pipeline_day1.py", "agent/logs/pipeline_day1.log", f"{PY} scripts/pipeline_day1.py"),
]


def running(pat):
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


def main():
    for pat, log, cmd in JOBS:
        pid = running(pat)
        if pid:
            print(f"alive   {pat} (pid {pid})")
            continue
        out = subprocess.check_output([sys.executable, "scripts/bg.py", log, cmd], cwd=ROOT, text=True).strip()
        print(f"started {pat} (pid {out}) -> {log}")


if __name__ == "__main__":
    main()
