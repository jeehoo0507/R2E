# PROGRESS (갱신 2026-10-28 16:27 UTC, 라운드 6)

- 라운드 6 (15:51~): 상태 정상 (mem 15.8 GiB, oom_kill 0). **0단 distill 끝** (16:22, 2192 iter / 0.77 h, best iter 1600; resume.pt 1003·1961에 저장됨 = 20분 체크포인트 동작 확인). best iter 중간 val (보고서용 아님): count/g+p pcb 1.75 fail 0.56 / pkg 1.50 fail 0.56 / ip 0.77 fail 0.19 (`runs/2026-10-28/r0_coord_distill/log.txt`). 0단 RL 시작 (`runs/2026-10-28/r0_coord_rl/`).
- 관찰: distill loss는 iter 2000 무렵 0.0~0.4까지 내려가지만 val fail은 iter 200~2100 내내 0.19~0.94 사이에서 들쭉날쭉 (val 16문제라 잡음 큼) → 27개 풀의 선생님 행동을 외우는 쪽. RL 단계에서 val fail이 내려가는지가 첫 확인 포인트.
- 위험: 10·16칸 eval 풀 생성 (2 workers, 큰 판부터)이 15:15 시작 후 72분째 16칸 2개가 아직 하나도 안 끝남. 남은 7개(16칸 6 + ip10_1)가 끝나야 E0와 단 평가가 돌기 때문에, 0단 학습이 ~17:40에 끝나도 평가는 그 뒤로 밀린다. GPU 줄(1·2·3단 학습)은 영향 없음.
- 결정: 풀 생성은 그대로 둔다 — 지금 멈추면 72분 진행분을 버리고, workers를 늘리면 QUEUE 한도 4를 넘음. 다음 라운드에 첫 16칸 풀 시간이 찍히면 남은 시간을 그 숫자로 다시 계산하고, 너무 길면 (단 평가가 2시간 넘게 기다리면) 10칸 평가를 16칸 풀보다 먼저 하도록 드라이버 순서만 바꾸는 것을 검토.

- 라운드 5 (15:47~): 상태 정상 (mem 12.5 GiB, oom_kill 0). 0단 distill iter 500 중간 val (보고서용 아님): count/g+p pcb 2.66 fail 0.62 / pkg 1.50 fail 0.69 / ip 0.77 fail 0.25 (`runs/2026-10-28/r0_coord_distill/log.txt`). eval 풀 10·16칸 12개 중 5개 완료 (16칸 진행 중).
- 결정: CPU 줄 순서 변경 — E0를 (gp·modal_rule 전체) → (LS 10칸) → 단 평가가 기다리는 게 없을 때만 16칸 LS를 종류별로 하나씩. 이유: LS 4x32는 greedy를 판마다 수백 번 다시 돌리고 eval_policy가 큰 판부터 돌려서, 기존 순서면 16칸 LS가 끝날 때까지 0단 평가(~17:40 학습 끝)가 몇 시간 밀릴 수 있음. 실험 조건은 그대로, 순서만 바뀜. 드라이버 15:49 재시작 (r0·풀 생성 ATTACH, 끊김 없음).

- 라운드 4 (15:43~): 상태 정상 (mem 12 GiB, oom_kill 0). 0단 distill iter ~300, 중간 val (iter 200) fail pcb 0.44 / pkg 1.00 / ip 0.38 (`runs/2026-10-28/r0_coord_distill/log.txt`, 보고서용 아님). 10·16칸 eval 풀 12개 중 5개 완료 (ip10_1, 16칸 6개 진행 중).
- 3단 추가: 드라이버 GPU 줄에 `r3_loop` (`--model loop`, 같은 COMMON·시간 예산)을 2단 뒤에 넣음. 시작 전 같은 줄에서 `scripts/smoke_pipeline.py --arms loop --workers 2` (작은 판 전체 경로: 선생님→distill→rl→eval @R2/@R16) 통과해야 학습 시작, 실패면 3단 건너뜀 (`agent/logs/smoke_loop.log`). 3단 rl 평가는 테스트 R = 기본 8 + 2·4·16. 드라이버 재시작 15:45 (r0·풀 생성은 ATTACH, 끊김 없음). 예상: 3단 ~21:50 시작.
- 결정: 3단 smoke를 지금 따로 돌리지 않고 드라이버 GPU 줄의 2단 뒤에 둠 — 지금 돌리면 동시 프로세스가 QUEUE 한도 4를 넘음.
- 결정: 3단 학습에 `--grad_ckpt` 등 메모리 옵션을 넣지 않음 (다른 단과 조건 동일 유지). GPU OOM이 나면 다음 라운드에 기록하고 그때 판단.
- DAILY.md: 첫 라운드 05:24 UTC → 첫 DAILY.md는 10/29 05:30 UTC 무렵 라운드에서 작성.

- 사고: 13:45경 파드 두 번째 재시작 (QUEUE: 60 GiB 한도 OOM 의심). 당시 동시 실행 = eval 풀 생성 14개(20칸 포함) + 선생님 8개 = 22 프로세스. 재시작 후 oom_kill 카운터는 0 (리셋됨). 선생님 해는 27개 중 15개 완성 상태였음.
- QUEUE 반영 (14:20 지시): 드라이버 `scripts/pipeline_day1.py` 재작성 — CPU 작업 프로세스 합계 ≤4 (선생님 4 → 학습 CERTIFY_WORKERS=2 + CPU 줄 2; 20칸 eval 풀은 맨 끝에 2개), 단계마다 시작/끝 `memory.current`·`oom_kill` 로그 (`scripts/mem.py`), 45 GiB 넘으면 새 프로세스 대기. `train.py`에 `--ckpt_min 20` resume.pt (모델·옵티마이저·λ·RNG·선생님 교체 상태·추가된 격자점·사용 시간) → 재시작 시 이어서 학습 (`scripts/smoke_resume.py` 통과: iter 6→12 이어짐). `run_rung.py`는 resume.pt가 있으면 옮기지 않고 이어감.
- 선생님 완료 15:14 (27/27, 4 workers, 최대 mem 13.9 GiB, oom_kill 0). 마지막 `train_pcb12_1` 혼자 3235 s.
- 사고 2: 15:15 0·1단 동시 학습이 **GPU OOM** (27개 풀을 GPU에 dense로 올리면 프로세스당 >11 GB, 24 GB에 둘이 안 들어감) → 둘 다 rc=1, 드라이버가 2단으로 넘어감. 2단을 멈추고 (distill 1129 s 진행분, resume.pt 전이라 버림) 드라이버를 GPU 줄(0→1→2단 순차) + CPU 줄(2 workers: 10·16칸 eval 풀 → E0 → 단마다 끝나면 인증 평가 → 20칸 풀 → 20칸 평가)로 다시 짬.
- 돌고 있는 것: 0단 coord distill (15:36 시작, `runs/2026-10-28/r0_coord_distill/log.txt`), 10·16칸 eval 풀 (`agent/logs/build_pools_v1_r3.log`). 예상 순서: 0단 ~17:40, 1단 ~19:45, 2단 ~21:50 (각 distill 0.75 h + RL 1.25 h + 풀 로딩).
- 참고 (보고서용 아님): 중단된 2단 mott distill이 700 iter에서 val fail pcb 0.94 / pkg 0.56 / ip 0.25 — 2단 모델 자체는 학습 루프에서 돈다.
- 재시작 대응: 라운드 시작 때 `.venv/bin/python scripts/ensure_running.py` (죽었으면 드라이버만 다시 띄움; 모든 단계가 끝난 출력은 건너뜀).
- 끝난 것 (숫자, 보고서용 아님 — 학습 판의 선생님 통계): 27개 학습 풀에서 LS 해의 정확 검사 통과율 0.00~0.81 (g+p는 0.38~1.00) → LS가 실패한 문제는 선생님 = g+p 해. 표: RESULTS.md "선생님 해".
- 다음 라운드: `ensure_running.py` → 0단 distill/RL 중간 val (`runs/2026-10-28/r0_coord_*/log.txt`) 기록 → 10·16칸 풀 끝나면 E0 결과 RESULTS.md (`collect_results.py`는 단마다 드라이버가 자동 실행) → 1단 시작 확인.
- 결정: 단은 GPU에서 하나씩, 각 CERTIFY_WORKERS=2 + CPU 줄 2 workers = 합계 4 (QUEUE). 모든 단이 같은 학습 조건(시간 예산·workers)이라 사다리 비교 유지. 단, CPU 줄 작업(풀 생성/평가)이 단마다 달라 반복 수가 조금 다를 수 있음 → metrics.json의 iters로 기록.
- 결정: 큐 우선순위대로 2단보다 0·1단을 먼저 — 그래서 이미 돌던 2단을 멈춤.
- 결정: 20칸 eval 풀을 만든 뒤의 20칸 평가도 2 workers — 20칸 판의 메모리 사용이 OOM 원인으로 의심되므로 같은 한도.
- 결정 (이전 라운드 유지): 1단 = 좌표 + modal 특징, 정확 검사는 프로세스당 1스레드, 2단은 기존 `MoTT`, IP 난이도 EASY / PCB·PKG HARD, 풀 시드 고정.
