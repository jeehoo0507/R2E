# PROGRESS (갱신 2026-10-28 14:30 UTC, 라운드 3)

- 사고: 13:45경 파드 두 번째 재시작 (QUEUE: 60 GiB 한도 OOM 의심). 당시 동시 실행 = eval 풀 생성 14개(20칸 포함) + 선생님 8개 = 22 프로세스. 재시작 후 oom_kill 카운터는 0 (리셋됨). 선생님 해는 27개 중 15개 완성 상태였음.
- QUEUE 반영 (14:20 지시): 드라이버 `scripts/pipeline_day1.py` 재작성 — CPU 작업 프로세스 합계 ≤4 (선생님 4 → 0·1단 학습 CERTIFY_WORKERS=2씩 → 2단 학습 2 + 10·16칸 eval 풀 2 → 20칸 eval 풀은 맨 끝에 2개), 단계마다 시작/끝 `memory.current`·`oom_kill` 로그 (`scripts/mem.py`), 45 GiB 넘으면 새 프로세스 대기. `train.py`에 `--ckpt_min 20` resume.pt (모델·옵티마이저·λ·RNG·선생님 교체 상태·추가된 격자점·사용 시간) → 재시작 시 이어서 학습 (`scripts/smoke_resume.py` 통과: iter 6→12 이어짐). `run_rung.py`는 resume.pt가 있으면 옮기지 않고 이어감.
- 돌고 있는 것: 드라이버 `agent/logs/pipeline_day1.log` → 선생님 나머지 12개 (`agent/logs/make_teacher.log`, 4 workers, 14:20 시작, 시작 시 mem 0.8 GiB, 작업자당 RSS ≈2 GB) → 0·1단 학습 자동 시작.
- 재시작 대응: 라운드 시작 때 `.venv/bin/python scripts/ensure_running.py` (죽었으면 드라이버만 다시 띄움; 모든 단계가 끝난 출력은 건너뜀).
- 끝난 것 (숫자, 보고서용 아님 — 학습 판의 선생님 통계): 선생님 15개 파일에서 LS 해의 정확 검사 통과율이 0.00~0.56으로 낮음 → 선생님 = 대부분 g+p 해. `agent/logs/make_teacher.log`.
- 다음: 선생님 완료 확인 → 0·1단 학습 로그(`runs/2026-10-28/r*_distill/log.txt`) 중간 val 기록 → 10·16칸 eval 풀·E0.
- 결정: 학습 중 CERTIFY_WORKERS=2씩 (0·1단 동시 → 합계 4) — QUEUE의 "최대 4개"를 학습 정확 검사에도 적용. 0·1단이 같은 조건이라 사다리 비교는 유지. 이전 반복 수(6 workers)와는 다르지만 아직 끝난 학습이 없어 비교 대상 없음.
- 결정: 20칸 eval 풀을 만든 뒤의 20칸 평가도 2 workers — 20칸 판의 메모리 사용이 OOM 원인으로 의심되므로 같은 한도.
- 결정 (이전 라운드 유지): 1단 = 좌표 + modal 특징, 정확 검사는 프로세스당 1스레드, 2단은 기존 `MoTT`, IP 난이도 EASY / PCB·PKG HARD, 풀 시드 고정.
