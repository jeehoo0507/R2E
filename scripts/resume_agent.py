"""Restart the agent loop by itself once the GPU queue is done (QUEUE 2026-10-31 11:40 UTC).

Every 10 min: when every `train` entry of agent/day2_queue.json has finished RL (runs/<DAY>/<name>_rl/metrics.json,
the driver's own test), remove agent/STOP (commit, push to r2e main) and start `bash agent/loop.sh` in tmux session
"agent", then exit. If STOP is already gone but the loop is not running (a workspace restart killed it), it starts the
loop right away. Started by scripts/ensure_running.py, so a restart brings it back.
Run: .venv/bin/python scripts/bg.py agent/logs/resume_agent.log '.venv/bin/python scripts/resume_agent.py'
"""
import json
import os
import subprocess
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAY = "2026-10-29"
QUEUE = os.path.join(ROOT, "agent/day2_queue.json")
STOP = os.path.join(ROOT, "agent/STOP")
PERIOD_S = 600
GIT_ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="true")


def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}] {msg}", flush=True)


def sh(*cmd, check=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=300, env=GIT_ENV)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])} rc={r.returncode}: {(r.stderr or r.stdout).strip()[-400:]}")
    return r


def queue_left():
    try:
        train = json.load(open(QUEUE))["train"]
    except (OSError, ValueError) as e:
        log(f"queue unreadable ({e})")
        return None
    return [t["name"] for t in train if not os.path.exists(os.path.join(ROOT, f"runs/{DAY}/{t['name']}_rl/metrics.json"))]


def loop_running():
    return sh("tmux", "has-session", "-t", "agent", check=False).returncode == 0


def start_loop():
    sh("tmux", "new", "-d", "-s", "agent", "bash agent/loop.sh")
    log("agent loop started (tmux session agent, log agent/logs/loop.log)")


def main():
    log("resume_agent start")
    while True:
        try:
            if not os.path.exists(STOP):
                if not loop_running():
                    start_loop()
                return
            left = queue_left()
            if left == []:
                sh("git", "rm", "-q", "agent/STOP")
                sh("git", "commit", "-q", "-m", "agent: GPU queue done, loop resumes (scripts/resume_agent.py)", "--", "agent/STOP")
                sh("git", "pull", "-q", "--rebase", "--autostash", "r2e", "main")
                sh("git", "push", "-q", "r2e", "HEAD:main", check=False)
                log("queue done, agent/STOP removed")
                if not loop_running():
                    start_loop()
                return
            if left is not None:
                log(f"waiting: {len(left)} train entries left (next {left[0]})")
        except Exception as e:  # noqa: BLE001 — log and retry; never touch the driver
            log(f"check failed: {e}")
        time.sleep(PERIOD_S)


if __name__ == "__main__":
    main()
