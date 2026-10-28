# PROGRESS (갱신 2026-10-28 23:24 UTC, 라운드 14)

## 라운드 14 (22:32~23:24 UTC)
- 상태 정상: 드라이버 살아 있음, pod mem 18.0 → 12.6 GiB / 60, oom_kill 0. CPU 프로세스 ≤4 → 새 실험 안 띄움.
- **r3 (3단 loop) distill 끝** (23:05): 1500 iter / 0.77 h, best iter 1400 (val score 1.743), gpu peak 12.1 GB, OOM 0. 같은 시간 예산이라 iter 수가 0단(2192)·1단(2109)보다 적음 (loop가 블록을 R번 돌려 ~1.6 s/iter) — 사다리 조건(시간 예산)은 같고 iter 수 차이는 metrics.json·RESULTS.md에 기록됨. best val (보고서용 아님): pcb 0.91/fail 0.50, pkg 1.00/0.56, ip 0.69/0.25 (`runs/2026-10-28/r3_loop_distill/log.txt`).
- **r3 RL 시작** (23:06): iter 75까지 OOM 0, gpu peak 13.3 (iter 25) → 14.6 GB (iter 75), ~13 s/iter, grid capped 3, 선생님 교체 134, λ 1.16 (`runs/2026-10-28/r3_loop_rl/log.txt`). 0~2단 RL과 같은 메모리 추세 → 24 GB 안에서 끝날 것으로 봄 (확인은 `done:`의 `cuda_oom_skipped`). 끝 예상 ~00:25.
- **eval 풀 `eval_pkg16_0` 완성** (18523 s = 5.1 h, F 284, g+p ok 0.64, count 25.9; `agent/logs/build_pools_v1_r3.log`) — 16칸 중 가장 김 (pcb16 2.8 h, pkg16_1 3.1 h). 남은 것: ip16 ×2, ip10_1.
- RESULTS.md 재생성 (r3 distill 행 추가, eval 기록 0개 — 풀 대기).
- 다음 라운드: r3 RL `done:` (~00:25)·`cuda_oom_skipped` 기록 → ip16 풀 시간 → 풀 다 끝나면 E0·단 평가 시작 확인 → 10/29 05:30 무렵 첫 DAILY.md.

## 라운드 13 (22:26 UTC~, 라운드 12 직후라 짧음)
- 상태 정상: 드라이버 살아 있음, pod mem 19.5~24.3 GiB / 60, oom_kill 0. CPU 프로세스 4 (풀 worker 2 + certify 2) → 새 실험 안 띄움.
- r3 (3단 loop) distill iter 425, gpu peak 12.1 GB 그대로, OOM 0, ~1.6 s/iter. iter 400 val (보고서용 아님): pcb 0.94/fail 0.75, pkg 1.17/0.88, ip 0.69/0.19, val score 2.139 (new best; iter 100 2.393) (`runs/2026-10-28/r3_loop_distill/log.txt`). 0~2단 distill과 같이 val fail이 들쭉날쭉.
- eval 풀: 새로 끝난 것 없음 (pkg16_0 ~4.2 h째, ip16 진행 중).
- 다음 라운드: r3 distill `done:`(~23:05)·RL 시작·RL gpu peak 확인 (loop는 블록을 R번 반복해 RL activation이 2단보다 클 수 있음; OOM이면 train.py가 step을 버리고 chunk를 반으로 줄임 → `chunk_final` 기록) → pkg16_0 완성 시간.

## 라운드 12 (22:22 UTC~, 라운드 11 직후라 짧음)
- 상태 정상: 드라이버 살아 있음, pod mem 17.6~19.0 GiB / 60, oom_kill 0. CPU 프로세스 4 (풀 worker 2 + certify 2) → 새 실험 안 띄움.
- r3 (3단 loop) distill iter 225, gpu peak 12.1 GB, OOM 0, ~1.6 s/iter. iter 200 val (보고서용 아님): pcb 3.13/fail 0.94, pkg 1.00/0.69, ip 0.69/0.25 (`runs/2026-10-28/r3_loop_distill/log.txt`).
- eval 풀: 새로 끝난 것 없음 (pkg16_0, ip16 진행 중).
- `scripts/fig_results.py` 수정: 기록을 풀 파일(set)별로 묶어 g+p와 **같은 파일끼리만** 짝지어 개수 비 계산. 이전 코드는 한 방법이 _0/_1 중 하나만 평가됐으면 배열 길이가 달라 그림이 죽었고, 같은 파일을 다시 평가하면 두 번 셌음. /tmp 가짜 기록으로 그림 2·3 실행 확인 (가짜 숫자는 runs/에 안 씀).
- 다음 라운드: r3 distill `done:`(~23:05)·RL 시작·OOM 확인 → pkg16_0 완성 시간 기록.

## 라운드 11 (21:51 UTC~)
- 상태 정상: 드라이버 살아 있음, pod mem 14.6~20.2 GiB / 60, oom_kill 0. 동시 CPU 프로세스 4 (풀 worker 2 + certify 2) → 새 실험 안 띄움.
- **r2 (2단 mott) 학습 끝** (22:14, rc 0): RL 354 iter / 1.27 h, best iter 300 (val score 1.691), cuda_oom_skipped 0, chunk 2, gpu peak 16.8 GB, 선생님 교체 297, λ 1.52, grid capped 149 step (`runs/2026-10-28/r2_mott_rl/metrics.json`). RL 최종 val (보고서용 아님): pcb 0.88/fail 0.44, pkg 1.00/fail 0.62, ip 0.69/fail 0.19. 2단 distill best (iter 1300, score 1.759)보다 RL이 val score로는 나음 — 0·1단(RL이 distill보다 못하거나 비슷)과 다른 첫 단. 단 val 16문제라 잡음 큼, 결론은 eval 풀 평가 뒤.
- RL best val score (낮을수록 좋음, 보고서용 아님): 0단 1.999 → 1단 1.737 → 2단 1.691. 세 단 모두 같은 인자 (teacher gp, chunk 2, rl 1.25 h, git hash만 다름).
- **r3 loop smoke 통과** (22:14~22:16, `agent/logs/smoke_loop.log`, 5단계 모두 OK) → **r3 (3단 loop) 학습 시작** 22:16. distill iter 100: gpu peak 12.1 GB, ~1.5 s/iter, OOM 0 (`runs/2026-10-28/r3_loop_distill/log.txt`). 끝 예상 ~00:20 (distill 0.75 h + RL 1.25 h + 로딩).
- eval 풀: `eval_pkg16_0`은 22:25에도 진행 중 (~4.1 h째, 지금까지 16칸 중 가장 김), 다른 worker는 21:16부터 다음 풀(ip16) 진행. 남은 것 pkg16_0, ip16 ×2, ip10_1.
- RESULTS.md 재생성 (r2 RL 행 추가, eval 기록 0개 — 풀 대기).
- 다음 라운드: r3 distill `done:`·RL 시작·OOM 확인 → pkg16_0 완성 시간 기록 → 10/29 05:30 무렵 첫 DAILY.md.

## 라운드 10 (21:15 UTC~)
- 상태 정상: 드라이버 살아 있음, pod mem 20.8 GiB / 60, oom_kill 0, GPU 17.9 GB 사용 (r2 RL). 동시 CPU 프로세스 4 (풀 worker 2 + certify 2) → 새 실험 안 띄움.
- **eval 풀 `eval_pkg16_1` 완성** (11319 s = 3.1 h, F 298, g+p ok 0.68, count 16.2; `agent/logs/build_pools_v1_r3.log`). `eval_pkg16_0`은 21:38에도 진행 중 (~3.6 h째, pcb16 2.8 h보다 김). 남은 풀: pkg16_0, ip16 ×2, ip10_1 → 16칸 풀 3.1 h 실측 기준 10·16칸 전체 끝은 10/29 01시 전후, 그다음 E0·단 평가.
- r2 (2단 mott) RL: iter 100까지 OOM 0, gpu peak 15.5 GB, ~14.4 s/iter, grid capped 8. iter 100 val (보고서용 아님): pcb 0.83/fail 0.62, pkg 0.97/fail 0.69, ip 0.69/fail 0.12, val score 1.788 (new best) (`runs/2026-10-28/r2_mott_rl/log.txt`). 0·1단과 같은 양상 (학습 배치 fail 0.01~0.23 vs val fail 0.12~0.69).
- 다음 라운드: r2 RL `done:` (~22:15) 기록 → r3 loop smoke 통과·학습 시작 확인 (`agent/logs/smoke_loop.log`) → pkg16_0·ip16 풀 시간 기록.

## 라운드 9 (19:56 UTC~)
- 상태 정상: 드라이버 살아 있음, pod mem 18.9 → 33.8 GiB / 60 (21:13, 16칸 풀 worker가 커지는 중), oom_kill 0. 동시 CPU 프로세스 = 풀 worker 2 + certify 2 = 4 (QUEUE 한도 꽉 참 → 새 실험 안 띄움).
- **r1 (1단) 학습 끝** (20:57, rc 0): RL 413 iter / 1.27 h, best iter 200 (val score 1.737), cuda_oom_skipped 0, chunk 2, gpu peak 17.2 GB, 선생님 교체 319, λ 1.64, grid capped 217 step, 27개 풀 모두 F 상한 1.5x 도달 (`runs/2026-10-28/r1_modal_rl/metrics.json`). RL best val (iter 200, 보고서용 아님): pcb 0.89/fail 0.44, pkg 0.92/fail 0.56, ip 0.66/fail 0.38 vs 1단 distill best (iter 600: 1.06/0.38, 1.10/0.44, 0.73/0.31) → 개수는 줄고 fail은 늘어남, val score로는 distill(1.714)이 RL(1.737)보다 약간 나음. r0와 같은 패턴 (작업 격자 과적합 의심). 평가는 드라이버가 distill·rl 둘 다 eval 풀 완성 후 실행.
- **r2 (2단 mott) RL 시작** (20:58): iter 50 OOM 0, gpu peak 13.8 GB, ~16.5 s/iter (0·1단 ~12 s보다 느림 → 1.25 h에 ~270 iter 예상; iter 수는 metrics.json에 기록). 끝 ~22:15 → 그다음 r3 smoke+학습.
- RESULTS.md 재생성 (`collect_results.py`, eval 기록은 아직 0개 — 10/16칸 풀 대기).
- 다음 라운드: r2 RL `done:` 기록 → r3 loop smoke 통과·학습 시작 확인 (`agent/logs/smoke_loop.log`) → pkg16 풀 완성 시간 기록.
- r1 (1단 modal) RL: iter 150까지 OOM 0, gpu peak 13.1 → 16.2 GB (r0와 같은 추세), ~11.8 s/iter, `grid capped` 1 (iter 75) → 29 (iter 150). iter 100 val (보고서용 아님): count/g+p pcb 0.92 fail 0.69 / pkg 0.90 fail 0.69 / ip 0.66 fail 0.38 (`runs/2026-10-28/r1_modal_rl/log.txt`). r0 RL iter 100 (fail 0.62 / 0.88 / 0.25)와 같은 양상: 학습 배치 fail 0.01~0.12 vs val 정확 검사 fail 0.38~0.69.
- eval 풀: pkg16 ×2 생성 중 (~18:08 시작, pcb16 실측 2.8 h 기준 ~21:00 전후 예상). 
- 다음: r1 RL `done:` (~21:00) 기록 → r2 RL 시작·OOM 확인.

## 라운드 8 (18:52 UTC~)
- 상태 정상: 드라이버 살아 있음, pod mem 15.5 GiB / 60, oom_kill 0. GPU 줄 r0 RL 진행 중 (18:25~).
- r0 RL (격자 수정 후): iter 225까지 OOM 0, gpu peak 16.6 GB (iter 100 15.2 → 천천히 증가, 상한 1.5x F0이 걸려서 더 안 커질 것), ~13 s/iter. `grid capped` 6 (iter 100) → 73 (iter 225): 상한 뒤 실패가 빠르게 쌓임.
- r0 RL iter 200 val (보고서용 아님): pcb count/g+p 1.00 fail 0.50 / pkg fail 1.00 (성공 0개라 count nan) / ip 0.85 fail 0.25. iter 100 대비 pcb fail 0.62→0.50, pkg 0.88→1.00. 학습 배치의 fail (작업 격자 기준) 0.05~0.21 vs val 정확 검사 fail 0.25~1.00 → **정책 해가 작업 격자에는 맞지만 700점 검사에서 떨어지는 간극**이 RL에서도 그대로. 보고서 고찰 후보 (격자 과적합). λ 1.0→1.62 계속 상승 (목표 0.02).
- eval 풀: `eval_pcb16_0` 9941 s, `eval_pcb16_1` 10392 s에 완성 (g+p ok 0.80·0.76). 지금 pkg16 ×2 진행 → 그다음 ip16 ×2, ip10_1. 실측으로 16칸 시간 추정을 고침 (PROPOSALS.md 갱신: 이전 6~9 h/개 추정 → 실제 ~2.8 h). 10·16칸 풀 전체 끝은 10/29 새벽 예상 → 그때 E0·단 평가 시작.
- **r0 (0단) 학습 끝** (19:41, rc 0): RL 350 iter / 1.27 h, best iter 300, cuda_oom_skipped 0, chunk 2 유지, gpu peak 17.1 GB, 선생님 교체 352, λ 1.79, grid capped 176 step. 풀별 F 처음→끝은 모두 상한 1.5x에 도달 (`metrics.json` `pool_F`, 예: pcb12_0 280→420). RL 최종 val (보고서용 아님): pcb 1.06/fail 0.56, pkg 0.67/fail 0.94, ip 0.77/fail 0.25 — distill 최종 (0.75 / 0.69 / 0.19 fail)과 비교해 pcb만 나아지고 pkg·ip는 나빠짐. 원인 후보 (학습법은 안 바꿈): (1) 작업 격자 과적합 — 상한 뒤엔 격자로 못 고침, (2) λ가 목표 0.02에 못 미쳐 계속 오름, (3) ip 선생님이 대부분 g+p로 떨어진 풀(ip8_x LS 2.1~2.5개 vs g+p 22~30개)에서 교체로 기준이 급변. 학습 기록 표는 RESULTS.md (자동 생성 갱신).
- 기록: r0 RL의 `config.json`/`metrics.json` git hash는 `31d36bc`이지만 실제로는 커밋 전 작업 트리(= `d4241f7`의 격자 수정, `grid_growth` 인자가 args에 있음)로 실행됨. r1·r2 RL은 `d4241f7` 이후 커밋에서 시작.
- **지금:** r1 (1단 modal) RL 19:41 시작, iter 50 gpu peak 13.8 GB, OOM 0 (`runs/2026-10-28/r1_modal_rl/log.txt`). GPU 줄 다음: r2 RL (~21:00) → r3 smoke+학습 (~22:20). CPU 줄: pkg16 ×2 풀 생성 중.
- 다음 라운드: r1 RL `done:` (~21:00) 확인·기록 → r2 RL 시작·OOM 없는지 확인 → pkg16 풀 완성 시간 기록.
- 결정: 아무 설정도 바꾸지 않음 — RL 중간 val이 나빠도 학습법 변경은 금지 (AGENT_PROMPT), r0 RL 끝 체크포인트로 평가한다.

- **RL OOM 원인 찾음 (이전 STUCK 해제, 확인 중):** RL은 정확 검사가 실패할 때마다 풀에 격자점을 추가하는데 (`batch.add_freqs`), `--chunk` 도입 후 chunk마다 따로 호출되어 매번 그 chunk의 가장 긴 목록으로 모든 인스턴스를 패딩 → step당 F가 chunk 수만큼 더 늘어남. 2단 RL(18:10, chunk 2)에서 pkg10_1 F 267→511 (iter 25), gpu peak 18.3 GB, 18:17 메모리 매핑 실패 경고. dense 풀과 rollout 블록 [E,F,n,k]가 모두 F에 비례하므로 chunk를 줄여도 결국 OOM. 즉 "같은 갱신"이라는 라운드 6 설명이 틀렸었음 (격자 증가가 달랐다).
- 수정 3 (`train.py`): (1) 격자점은 step 끝에 한 번만 추가 (chunk 전 1-pass와 같은 동작), (2) `--grid_growth 0.5`: 풀마다 처음 F의 1.5배까지만 (넘는 실패도 정확 검사로 실패 처리 → 보상은 정직), (3) step 안 CUDA OOM이면 그 step을 버리고 (갱신 없음) chunk 반으로, 20번 넘으면 중단. iter 로그에 `grid capped`·`oom`, metrics.json에 `pool_F`(풀별 처음/끝 F)·`cuda_oom_skipped`·`chunk_final`. CPU smoke `scripts/smoke_rl_grid.py` 통과 (OOM 주입 → step 건너뜀·chunk 2→1·F 불변 / 상한 0.5 지킴). 상한 없이도 작은 smoke에서 pcb8_0 F 187→259 (6 iter) → 상한은 필요.
- 2단 RL은 18:20에 멈춤 (12분 진행, 옛 코드라 다른 단과 조건이 달라짐 → `r2_mott_rl_killed_182000_addfreqs`). distill 3개는 그대로. 드라이버 18:25 재시작 → GPU 줄: **r0 RL (18:25~) → r1 RL → r2 RL → r3** (각 RL 1.25 h).
- 확인: r0 RL iter 25 pkg10_1 F=310, gpu peak 13.0 GB → iter 100 peak 15.2 GB, OOM 0, ~14 s/iter (1.25 h ≈ 320 iter), resume.pt iter 84 (`runs/2026-10-28/r0_coord_rl/log.txt`). 상한이 벌써 걸림 (iter 100까지 `grid capped 6`, pcb12_2 F 378/385) → 상한 뒤의 실패는 격자로 고쳐지지 않으므로 best가 아닌 샘플의 작업 격자 보상은 낙관적일 수 있음 (보고서 방법 장에 적을 것).
- r0 RL iter 100 val (보고서용 아님): pcb count/g+p 1.07 fail 0.62 / pkg 1.00 fail 0.88 / ip 0.76 fail 0.25 — distill best (iter 1600: 1.75/0.56, 1.50/0.56, 0.77/0.19)보다 fail은 아직 나음 없음. λ 1.0→1.38 (목표 fail 0.02보다 훨씬 높음), 선생님 교체 180회.
- 다음 라운드: `ensure_running.py` → r0 RL `done:` (~19:45) 확인, metrics.json `pool_F`·`cuda_oom_skipped` 기록 → r1 RL 시작 확인. RL이 val fail을 못 낮추면 (r0 끝에서 distill best보다 나쁘면) 그대로 기록하고 원인 후보(λ·선생님 교체·격자 상한)를 적되 학습법은 바꾸지 않음.
- 2단 distill 끝 (17:22~18:09, rc 0). 중간 val (보고서용 아님: val 풀 종류당 16문제, 정확 검사, checkpoint 고르는 데 쓴 세트): best iter 1300 count/g+p pcb 0.89 fail 0.56 / pkg 1.07 fail 0.56 / ip 0.69 fail 0.19 (`runs/2026-10-28/r2_mott/driver.log`).
- 결정: 상한 0.5 — 풀 9.5 GB × 1.5 ≈ 14.3 GB + chunk 2 rollout이 24 GB 안에 들어가는 쪽. 모든 단의 RL이 같은 값 (r0·r1·r2 RL 모두 새 코드로 처음부터).
- 결정: 2단 RL을 12분 만에 버리고 재시작 — 다른 단과 격자 증가 규칙이 달라지면 사다리 비교가 깨짐.
- **위험: eval 풀 시간.** 16칸 풀 하나 ~6~9 h (1스레드, 판 변 ~6제곱), 6개 2 workers로 ~18~27 h → 10칸 E0·단 평가도 10/29 낮까지 밀림; 20칸은 ~90 h로 사실상 불가. 결정: 풀 생성은 그대로 (멈추면 진행분 손실, 늘리면 QUEUE 한도 4 위반). 사람 선택지 (a)(b)(c)를 PROPOSALS.md "사람 결정이 필요한 것"에 적음.

## 라운드 6 (17:40 UTC)

- **사고 4 (=STUCK): chunk 4도 RL에서 OOM.** 1단 RL 17:11 시작 → 17:15 OOM (할당 17.2 GB + 단편화로 놀던 5.7 GB), 드라이버 순서대로 0단 RL 재실행 17:16 → 17:22 같은 OOM (15.9 + 6.5 GB). 원인: `sim.loaded_state`가 [E,F,n,k] complex128 블록을 step마다 다른 k로 여러 개 잡음 (16 env·F 251·n 144·k 64면 블록 하나 0.6 GB) + 크기가 계속 바뀌어 단편화. 1·0단 distill 체크포인트는 그대로 있음 (`runs/2026-10-28/r{0,1}_*_distill/best.pt`; 1단 distill 2109 iter, best iter 600).
- 수정 2: `--chunk` 기본 2 (16 env = distill의 선생님 replay와 같은 크기, 그건 풀 전체를 올린 채 0·1단 각 0.75 h 문제없이 돌았음) + `train.py`에서 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` (단편화 제거). iter 로그·`done:`에 `gpu peak` 표시 추가. CPU smoke (`scripts/smoke_chunk.py`) 통과. 2단 distill이 GPU를 15.4 GB 쓰는 중이라 GPU에서 실제 크기 smoke는 못 함 (남은 8 GB로는 선생님 replay도 안 들어가 대표성 없음 → 지움).
- 드라이버 17:38 재시작 → GPU 줄: r2 distill (ATTACH, 17:22 시작) → r2 RL (~18:10, 새 train.py) → **r0 RL → r1 RL** (distill 재사용) → r3.
- 결정: chunk 2 (1이 아니라) — 16 env는 distill에서 실제로 검증된 크기이고, chunk 1은 RL iter 수를 더 줄임. 모든 단이 같은 값.
- eval 풀: 17:38에도 16칸 첫 파일이 안 끝남 (2시간 23분째, 5/12 그대로). pod 메모리 29 GiB (풀 worker 둘이 8.8·8.1 GB로 커지는 중), oom_kill 0.

- 라운드 6 (15:51~): 상태 정상 (mem 15.8 GiB, oom_kill 0). **0단 distill 끝** (16:22, 2192 iter / 0.77 h, best iter 1600; resume.pt 1003·1961에 저장됨 = 20분 체크포인트 동작 확인). best iter 중간 val (보고서용 아님): count/g+p pcb 1.75 fail 0.56 / pkg 1.50 fail 0.56 / ip 0.77 fail 0.19 (`runs/2026-10-28/r0_coord_distill/log.txt`). 0단 RL 시작 (`runs/2026-10-28/r0_coord_rl/`).
- **사고 3: 0단 RL이 GPU OOM** (16:23, 첫 iter; B=16×G=8=128 env를 한 번에 rollout → `sim.loaded_state`가 2 GB를 더 할당하다 실패, 풀 9.5 GB + 18.4 GB 사용). 드라이버는 그대로 1단 distill로 넘어감 (16:24). 수정: `train.py --chunk` (기본 4) — RL 한 step의 16개 문제를 4개씩 rollout+backward 하고 gradient를 누적해 optimizer step 1번. 기준선은 문제별 G=8 샘플 안에서 정규화, loss scale은 전체 배치 기준(1/(B·G), 1/B) 그대로 → 같은 갱신, 메모리만 줄어듦. `scripts/smoke_chunk.py` 통과 (CPU, chunk 2 / 0). 1단 RL(~17:10 시작)부터 적용 (이미 떠 있는 run_rung이 새 train.py를 부름).
- 드라이버 GPU 줄 순서: 살아 있는 단 먼저 ATTACH → 나머지 사다리 순서. 그래서 r1 → **r0 RL 재실행** (distill은 유지, OOM 난 rl 폴더는 `_killed_`로 옮김) → r2 → r3. 드라이버 16:39 재시작 (r1·풀 생성 ATTACH).
- 결정: chunk=4 (가장 메모리 안전한 쪽). 대가는 step당 시간이 늘어 1.25 h 안의 RL iter 수가 줄 수 있음 — 모든 단이 같은 chunk라 사다리 비교는 유지, iter 수는 metrics.json에 기록.
- 결정: 0단 RL을 1단 뒤로 미룸 — 지금 1단 distill이 GPU를 쓰고 있고, 둘을 같이 올리면 GPU OOM (15:15 사고 1).
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
