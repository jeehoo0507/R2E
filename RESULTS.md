# RESULTS (자동 생성: `scripts/collect_results.py`, 2026-10-29 02:43 UTC)

성공 = `verify.py` 700점 + 피크 정밀화 정확 검사에서 최악 |Z| ≤ 1.01·Zt. 모든 방법은 cutting-plane 안에서 실행. 시간은 문제당 초(판 준비 제외, 같은 CPU 계산기). 손으로 적은 숫자는 없다.

## 평가 (정확 검사)

### 요약: 정확 검사 성공률 / 개수÷greedy+prune (둘 다 성공) [문제 수]

| 방법 | ip 10 | pcb 10 | pcb 16 | pkg 10 | pkg 16 |
|---|---|---|---|---|---|
| greedy+prune | 0.40 / 1.00 [50] | 0.90 / 1.00 [50] | – | 0.90 / 1.00 [50] | – |
| r0_coord_distill | – | – | 0.80 / – [25] | – | 0.80 / – [25] |
| r0_coord_rl | 1.00 / 1.05 [50] | 0.96 / 0.80 [50] | – | 0.76 / 0.79 [50] | 0.72 / – [25] |
| r1_modal_rl | 0.96 / 0.88 [50] | 0.98 / 0.75 [50] | – | 0.68 / 0.75 [50] | – |
| r2_mott_rl | 1.00 / 0.74 [50] | 0.88 / 0.88 [50] | – | 0.72 / 0.88 [50] | – |
| r3_loop_rl | 0.98 / 0.74 [50] | 0.84 / 0.84 [50] | – | 0.88 / 0.84 [50] | – |
| r3_loop_rl@R2 | – | – | – | 0.64 / 0.85 [25] | – |

### ip 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.40 | 10.30 | 1.000 | 2.944 | `runs/2026-10-28/baselines/eval/eval_ip10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_ip10_1__greedy+prune.json` |
| r0_coord_rl | 50 (0, 1) | 1.00 | 11.94 | 1.049 | 1.127 | `runs/2026-10-28/r0_coord_rl/eval/eval_ip10_0__r0_coord_rl.json`, `runs/2026-10-28/r0_coord_rl/eval/eval_ip10_1__r0_coord_rl.json` |
| r1_modal_rl | 50 (0, 1) | 0.96 | 10.12 | 0.878 | 0.982 | `runs/2026-10-28/r1_modal_rl/eval/eval_ip10_0__r1_modal_rl.json`, `runs/2026-10-28/r1_modal_rl/eval/eval_ip10_1__r1_modal_rl.json` |
| r2_mott_rl | 50 (0, 1) | 1.00 | 8.54 | 0.736 | 0.524 | `runs/2026-10-28/r2_mott_rl/eval/eval_ip10_0__r2_mott_rl.json`, `runs/2026-10-28/r2_mott_rl/eval/eval_ip10_1__r2_mott_rl.json` |
| r3_loop_rl | 50 (0, 1) | 0.98 | 8.39 | 0.736 | 0.574 | `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_1__r3_loop_rl.json` |

### pcb 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.90 | 12.02 | 1.000 | 4.838 | `runs/2026-10-28/baselines/eval/eval_pcb10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pcb10_1__greedy+prune.json` |
| r0_coord_rl | 50 (0, 1) | 0.96 | 6.92 | 0.796 | 2.375 | `runs/2026-10-28/r0_coord_rl/eval/eval_pcb10_0__r0_coord_rl.json`, `runs/2026-10-28/r0_coord_rl/eval/eval_pcb10_1__r0_coord_rl.json` |
| r1_modal_rl | 50 (0, 1) | 0.98 | 6.31 | 0.747 | 0.504 | `runs/2026-10-28/r1_modal_rl/eval/eval_pcb10_0__r1_modal_rl.json`, `runs/2026-10-28/r1_modal_rl/eval/eval_pcb10_1__r1_modal_rl.json` |
| r2_mott_rl | 50 (0, 1) | 0.88 | 6.77 | 0.877 | 0.683 | `runs/2026-10-28/r2_mott_rl/eval/eval_pcb10_0__r2_mott_rl.json`, `runs/2026-10-28/r2_mott_rl/eval/eval_pcb10_1__r2_mott_rl.json` |
| r3_loop_rl | 50 (0, 1) | 0.84 | 7.40 | 0.845 | 0.920 | `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_1__r3_loop_rl.json` |

### pcb 16×16

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| r0_coord_distill | 25 (0) | 0.80 | 38.10 | – | 55.917 | `runs/2026-10-28/r0_coord_distill/eval/eval_pcb16_0__r0_coord_distill.json` |

### pkg 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.90 | 8.07 | 1.000 | 3.786 | `runs/2026-10-28/baselines/eval/eval_pkg10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pkg10_1__greedy+prune.json` |
| r0_coord_rl | 50 (0, 1) | 0.76 | 5.82 | 0.788 | 2.622 | `runs/2026-10-28/r0_coord_rl/eval/eval_pkg10_0__r0_coord_rl.json`, `runs/2026-10-28/r0_coord_rl/eval/eval_pkg10_1__r0_coord_rl.json` |
| r1_modal_rl | 50 (0, 1) | 0.68 | 5.44 | 0.753 | 1.866 | `runs/2026-10-28/r1_modal_rl/eval/eval_pkg10_0__r1_modal_rl.json`, `runs/2026-10-28/r1_modal_rl/eval/eval_pkg10_1__r1_modal_rl.json` |
| r2_mott_rl | 50 (0, 1) | 0.72 | 6.22 | 0.877 | 1.594 | `runs/2026-10-28/r2_mott_rl/eval/eval_pkg10_0__r2_mott_rl.json`, `runs/2026-10-28/r2_mott_rl/eval/eval_pkg10_1__r2_mott_rl.json` |
| r3_loop_rl | 50 (0, 1) | 0.88 | 6.27 | 0.840 | 1.763 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl.json` |
| r3_loop_rl@R2 | 25 (1) | 0.64 | 6.44 | 0.850 | 2.483 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl@R2.json` |

### pkg 16×16

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| r0_coord_distill | 25 (1) | 0.80 | 31.15 | – | 49.804 | `runs/2026-10-28/r0_coord_distill/eval/eval_pkg16_1__r0_coord_distill.json` |
| r0_coord_rl | 25 (1) | 0.72 | 7.94 | – | 18.971 | `runs/2026-10-28/r0_coord_rl/eval/eval_pkg16_1__r0_coord_rl.json` |

## decap 종류 비율 (놓인 decap 중, 정확 검사 성공/실패 문제별; 종류 0 = C가 가장 큰 것, `decap_loop/techs.py`)

| 판 | 방법 | 문제 | 문제 수 | 평균 개수 | 종류 0 | 종류 1 | 종류 2 |
|---|---|---|---|---|---|---|---|
| ip 10 | greedy+prune | 성공 | 20 | 10.3 | 0.46 | 0.05 | 0.50 |
| ip 10 | greedy+prune | 실패 | 30 | 78.6 | 0.07 | 0.02 | 0.90 |
| ip 10 | r0_coord_rl | 성공 | 50 | 11.9 | 0.98 | 0.02 | 0.00 |
| ip 10 | r1_modal_rl | 성공 | 48 | 10.1 | 0.98 | 0.02 | 0.00 |
| ip 10 | r1_modal_rl | 실패 | 2 | 23.0 | 1.00 | 0.00 | 0.00 |
| ip 10 | r2_mott_rl | 성공 | 50 | 8.5 | 0.97 | 0.00 | 0.03 |
| ip 10 | r3_loop_rl | 성공 | 49 | 8.4 | 0.99 | 0.00 | 0.00 |
| ip 10 | r3_loop_rl | 실패 | 1 | 13.0 | 0.92 | 0.00 | 0.08 |
| pcb 10 | greedy+prune | 성공 | 45 | 12.0 | 0.40 | 0.13 | 0.47 |
| pcb 10 | greedy+prune | 실패 | 5 | 55.2 | 0.76 | 0.05 | 0.19 |
| pcb 10 | r0_coord_rl | 성공 | 48 | 6.9 | 0.08 | 0.21 | 0.70 |
| pcb 10 | r0_coord_rl | 실패 | 2 | 45.0 | 0.00 | 0.23 | 0.77 |
| pcb 10 | r1_modal_rl | 성공 | 49 | 6.3 | 0.10 | 0.21 | 0.69 |
| pcb 10 | r1_modal_rl | 실패 | 1 | 10.0 | 0.10 | 0.10 | 0.80 |
| pcb 10 | r2_mott_rl | 성공 | 44 | 6.8 | 0.08 | 0.18 | 0.74 |
| pcb 10 | r2_mott_rl | 실패 | 6 | 9.7 | 0.21 | 0.10 | 0.69 |
| pcb 10 | r3_loop_rl | 성공 | 42 | 7.4 | 0.05 | 0.22 | 0.73 |
| pcb 10 | r3_loop_rl | 실패 | 8 | 10.1 | 0.07 | 0.38 | 0.54 |
| pcb 16 | r0_coord_distill | 성공 | 20 | 38.1 | 0.51 | 0.06 | 0.43 |
| pcb 16 | r0_coord_distill | 실패 | 5 | 54.0 | 0.35 | 0.04 | 0.61 |
| pkg 10 | greedy+prune | 성공 | 45 | 8.1 | 0.29 | 0.16 | 0.56 |
| pkg 10 | greedy+prune | 실패 | 5 | 49.2 | 0.09 | 0.04 | 0.87 |
| pkg 10 | r0_coord_rl | 성공 | 38 | 5.8 | 0.18 | 0.23 | 0.59 |
| pkg 10 | r0_coord_rl | 실패 | 12 | 25.1 | 0.77 | 0.08 | 0.16 |
| pkg 10 | r1_modal_rl | 성공 | 34 | 5.4 | 0.17 | 0.25 | 0.58 |
| pkg 10 | r1_modal_rl | 실패 | 16 | 11.6 | 0.45 | 0.33 | 0.22 |
| pkg 10 | r2_mott_rl | 성공 | 36 | 6.2 | 0.14 | 0.17 | 0.70 |
| pkg 10 | r2_mott_rl | 실패 | 14 | 12.1 | 0.51 | 0.11 | 0.38 |
| pkg 10 | r3_loop_rl | 성공 | 44 | 6.3 | 0.17 | 0.17 | 0.66 |
| pkg 10 | r3_loop_rl | 실패 | 6 | 18.7 | 0.73 | 0.06 | 0.21 |
| pkg 10 | r3_loop_rl@R2 | 성공 | 16 | 6.4 | 0.21 | 0.11 | 0.68 |
| pkg 10 | r3_loop_rl@R2 | 실패 | 9 | 15.7 | 0.66 | 0.03 | 0.31 |
| pkg 16 | r0_coord_distill | 성공 | 20 | 31.1 | 0.46 | 0.07 | 0.47 |
| pkg 16 | r0_coord_distill | 실패 | 5 | 37.4 | 0.21 | 0.06 | 0.73 |
| pkg 16 | r0_coord_rl | 성공 | 18 | 7.9 | 0.29 | 0.21 | 0.50 |
| pkg 16 | r0_coord_rl | 실패 | 7 | 15.1 | 0.56 | 0.11 | 0.33 |

## greedy+prune 실패 문제의 최악 주파수 (`scripts/analyze_ip_gp_fail.py`, 기록된 occ로 정확 검사 격자 재계산)

| 세트 | g+p 실패 문제 | g+p 최악 Z/Zt (중앙값) | g+p 최악 주파수 / 맨판 최악 주파수 (중앙값, 범위) | 맨판 최악보다 낮은 비율 | 같은 문제 정책 성공 | 총 C g+p / 정책 (중앙값) | 출처 |
|---|---|---|---|---|---|---|---|
| eval_ip10_0,eval_ip10_1 | 30 | 1.83 | 0.36 (0.28~0.45) | 1.00 | r3_loop_rl 29 | 0.95 | `runs/analysis/ip_gp_fail.json` |

## g+p 실패 문제에서 위치는 그대로, 모든 decap을 한 종류로 바꾸면 (`scripts/analyze_ip_swap.py`, 정확 검사 격자 재계산)

| 세트 | 위치 출처 | 문제 수 | 기록 그대로: 성공률 / 최악 Z/Zt 중앙값 | 모두 종류 0: 성공률 / 최악 중앙값 | 모두 종류 1: 성공률 / 최악 중앙값 | 모두 종류 2: 성공률 / 최악 중앙값 | 출처 |
|---|---|---|---|---|---|---|---|
| eval_ip10_0,eval_ip10_1 | greedy+prune | 30 | 0.00 / 1.83 | 1.00 / 0.42 | 0.00 / 1.66 | 0.00 / 4.57 | `runs/analysis/ip_swap.json` |
| eval_ip10_0,eval_ip10_1 | r3_loop_rl | 29 | 1.00 / 0.97 | 0.93 / 0.97 | 0.00 / 3.97 | 0.00 / 8.67 | `runs/analysis/ip_swap.json` |

## greedy+prune을 한 종류만 쓰게 하면 (`scripts/analyze_gp_one_type.py`, 같은 규칙·cutting-plane·정확 검사; 분석용, 보고 기준선 아님)

| 세트 | 허용 종류 (C, ESL, ESR) | 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공) | 개수 / r3_loop_rl (둘 다 성공) | greedy+prune 성공률 | r3_loop_rl 성공률 | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|---|---|
| eval_ip10_0 | 0 (100 pF, 5 pH, 0.05 Ω) | 1.00 | 7.92 | 0.765 | 0.982 | 0.40 | 1.00 | 0.436 | `runs/analysis/gp_one_type/eval_ip10_0__greedy+prune@type0.json` |
| eval_ip10_1 | 0 (100 pF, 5 pH, 0.05 Ω) | 1.00 | 8.68 | 0.707 | 1.000 | 0.40 | 0.96 | 0.135 | `runs/analysis/gp_one_type/eval_ip10_1__greedy+prune@type0.json` |
| eval_pcb10_0 | 0 (10000 pF, 100 pH, 0.02 Ω) | 0.04 | 32.00 | 4.571 | 4.571 | 1.00 | 0.84 | 9.110 | `runs/analysis/gp_one_type/eval_pcb10_0__greedy+prune@type0.json` |

## 학습 기록 (train.py metrics.json)

| run | feat / model | stage | iters | 시간 (h) | 최종 val (count/g+p, fail) | 출처 |
|---|---|---|---|---|---|---|
| runs/2026-10-28/r0_coord_distill | coord / grid | distill | 2192 | 0.77 | val_pcb10_0: 1.76/0.75, val_pkg10_0: 1.04/0.69, val_ip10_0: 0.91/0.19 | `runs/2026-10-28/r0_coord_distill/metrics.json` |
| runs/2026-10-28/r0_coord_rl | coord / grid | rl | 350 | 1.27 | val_pcb10_0: 1.06/0.56, val_pkg10_0: 0.67/0.94, val_ip10_0: 0.77/0.25 | `runs/2026-10-28/r0_coord_rl/metrics.json` |
| runs/2026-10-28/r1_modal_distill | modal / grid | distill | 2109 | 0.77 | val_pcb10_0: 0.97/0.81, val_pkg10_0: 1.44/0.56, val_ip10_0: 0.84/0.38 | `runs/2026-10-28/r1_modal_distill/metrics.json` |
| runs/2026-10-28/r1_modal_rl | modal / grid | rl | 413 | 1.27 | val_pcb10_0: 0.97/0.62, val_pkg10_0: 1.00/0.75, val_ip10_0: 0.72/0.38 | `runs/2026-10-28/r1_modal_rl/metrics.json` |
| runs/2026-10-28/r2_mott_distill | mott / mott | distill | 1595 | 0.77 | val_pcb10_0: 1.08/0.75, val_pkg10_0: 1.07/0.56, val_ip10_0: 0.69/0.12 | `runs/2026-10-28/r2_mott_distill/metrics.json` |
| runs/2026-10-28/r2_mott_rl | mott / mott | rl | 354 | 1.27 | val_pcb10_0: 0.88/0.44, val_pkg10_0: 1.00/0.62, val_ip10_0: 0.69/0.19 | `runs/2026-10-28/r2_mott_rl/metrics.json` |
| runs/2026-10-28/r3_loop_distill | mott / loop | distill | 1500 | 0.77 | val_pcb10_0: 1.05/0.62, val_pkg10_0: 1.00/0.75, val_ip10_0: 0.69/0.19 | `runs/2026-10-28/r3_loop_distill/metrics.json` |
| runs/2026-10-28/r3_loop_rl | mott / loop | rl | 352 | 1.27 | val_pcb10_0: 0.99/0.81, val_pkg10_0: 1.00/0.50, val_ip10_0: 0.69/0.19 | `runs/2026-10-28/r3_loop_rl/metrics.json` |
| runs/smoke_chunk0 | coord / grid | rl | 4 | 0.01 | val_ip10_0: 0.75/0.81 | `runs/smoke_chunk0/metrics.json` |
| runs/smoke_chunk2 | coord / grid | rl | 4 | 0.01 | val_ip10_0: 0.46/0.88 | `runs/smoke_chunk2/metrics.json` |
| runs/smoke_rl_grid_cap | coord / grid | rl | 6 | 0.01 | val_ip10_0: 0.75/0.81 | `runs/smoke_rl_grid_cap/metrics.json` |
| runs/smoke_rl_grid_oom | coord / grid | rl | 6 | 0.03 | val_ip10_0: 1.79/0.75 | `runs/smoke_rl_grid_oom/metrics.json` |

## 선생님 해 (학습 풀, LS vs greedy+prune)

| 풀 | g+p 성공 | LS 정확 성공 | LS/g+p 개수 | LS가 줄인 비율 | 선생님 평균 개수 | LS 시간 (s) |
|---|---|---|---|---|---|---|
| train_ip10_0 | 0.69 | 0.69 | 0.803 | 0.36 | 3.00 | 101 |
| train_ip10_1 | 0.38 | 0.19 | 0.710 | 0.33 | 14.50 | 511 |
| train_ip10_2 | 0.62 | 0.62 | 0.844 | 0.20 | 2.80 | 45 |
| train_ip12_0 | 0.56 | 0.50 | 0.340 | 0.88 | 11.00 | 615 |
| train_ip12_1 | 0.69 | 0.69 | 0.735 | 0.45 | 4.00 | 681 |
| train_ip12_2 | 0.62 | 0.56 | 0.700 | 0.67 | 6.20 | 1226 |
| train_ip8_0 | 0.62 | 0.62 | 0.975 | 0.10 | 2.50 | 10 |
| train_ip8_1 | 0.56 | 0.56 | 0.852 | 0.22 | 2.44 | 99 |
| train_ip8_2 | 0.44 | 0.44 | 0.952 | 0.14 | 2.14 | 6 |
| train_pcb10_0 | 1.00 | 0.56 | 0.798 | 0.56 | 4.94 | 242 |
| train_pcb10_1 | 0.81 | 0.25 | 0.511 | 0.75 | 17.92 | 1279 |
| train_pcb10_2 | 0.88 | 0.31 | 0.633 | 0.60 | 6.36 | 706 |
| train_pcb12_0 | 0.75 | 0.31 | 0.735 | 0.80 | 11.92 | 1621 |
| train_pcb12_1 | 0.75 | 0.31 | 0.632 | 0.80 | 27.08 | 3219 |
| train_pcb12_2 | 0.75 | 0.31 | 0.681 | 0.60 | 11.67 | 921 |
| train_pcb8_0 | 1.00 | 0.81 | 0.940 | 0.23 | 3.88 | 25 |
| train_pcb8_1 | 0.94 | 0.50 | 0.951 | 0.25 | 4.40 | 266 |
| train_pcb8_2 | 1.00 | 0.56 | 0.815 | 0.67 | 6.12 | 83 |
| train_pkg10_0 | 0.94 | 0.00 | – | – | 9.00 | 1859 |
| train_pkg10_1 | 0.38 | 0.12 | 0.733 | 1.00 | 8.67 | 681 |
| train_pkg10_2 | 0.75 | 0.25 | 0.796 | 0.75 | 6.33 | 517 |
| train_pkg12_0 | 0.75 | 0.25 | 1.000 | 0.00 | 3.92 | 492 |
| train_pkg12_1 | 0.44 | 0.06 | 1.000 | 0.00 | 11.00 | 1113 |
| train_pkg12_2 | 0.56 | 0.25 | 0.854 | 0.50 | 5.67 | 567 |
| train_pkg8_0 | 0.75 | 0.06 | 0.800 | 1.00 | 5.42 | 362 |
| train_pkg8_1 | 0.81 | 0.19 | 0.933 | 0.33 | 4.15 | 107 |
| train_pkg8_2 | 0.81 | 0.12 | 0.900 | 0.50 | 5.31 | 241 |

