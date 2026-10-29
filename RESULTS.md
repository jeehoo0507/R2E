# RESULTS (자동 생성: `scripts/collect_results.py`, 2026-10-29 01:39 UTC)

성공 = `verify.py` 700점 + 피크 정밀화 정확 검사에서 최악 |Z| ≤ 1.01·Zt. 모든 방법은 cutting-plane 안에서 실행. 시간은 문제당 초(판 준비 제외, 같은 CPU 계산기). 손으로 적은 숫자는 없다.

## 평가 (정확 검사)

### 요약: 정확 검사 성공률 / 개수÷greedy+prune (둘 다 성공) [문제 수]

| 방법 | ip 10 | pcb 10 | pkg 10 |
|---|---|---|---|
| greedy+prune | 0.40 / 1.00 [50] | 0.90 / 1.00 [50] | 0.90 / 1.00 [50] |
| r2_mott_rl | – | – | 0.60 / 0.88 [25] |
| r3_loop_rl | 0.98 / 0.74 [50] | 0.84 / 0.84 [50] | 0.88 / 0.84 [50] |

### ip 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.40 | 10.30 | 1.000 | 2.944 | `runs/2026-10-28/baselines/eval/eval_ip10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_ip10_1__greedy+prune.json` |
| r3_loop_rl | 50 (0, 1) | 0.98 | 8.39 | 0.736 | 0.574 | `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_1__r3_loop_rl.json` |

### pcb 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.90 | 12.02 | 1.000 | 4.838 | `runs/2026-10-28/baselines/eval/eval_pcb10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pcb10_1__greedy+prune.json` |
| r3_loop_rl | 50 (0, 1) | 0.84 | 7.40 | 0.845 | 0.920 | `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_1__r3_loop_rl.json` |

### pkg 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.90 | 8.07 | 1.000 | 3.786 | `runs/2026-10-28/baselines/eval/eval_pkg10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pkg10_1__greedy+prune.json` |
| r2_mott_rl | 25 (1) | 0.60 | 6.67 | 0.877 | 2.734 | `runs/2026-10-28/r2_mott_rl/eval/eval_pkg10_1__r2_mott_rl.json` |
| r3_loop_rl | 50 (0, 1) | 0.88 | 6.27 | 0.840 | 1.763 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl.json` |

## decap 종류 비율 (놓인 decap 중, 정확 검사 성공/실패 문제별; 종류 0 = C가 가장 큰 것, `decap_loop/techs.py`)

| 판 | 방법 | 문제 | 문제 수 | 평균 개수 | 종류 0 | 종류 1 | 종류 2 |
|---|---|---|---|---|---|---|---|
| ip 10 | greedy+prune | 성공 | 20 | 10.3 | 0.46 | 0.05 | 0.50 |
| ip 10 | greedy+prune | 실패 | 30 | 78.6 | 0.07 | 0.02 | 0.90 |
| ip 10 | r3_loop_rl | 성공 | 49 | 8.4 | 0.99 | 0.00 | 0.00 |
| ip 10 | r3_loop_rl | 실패 | 1 | 13.0 | 0.92 | 0.00 | 0.08 |
| pcb 10 | greedy+prune | 성공 | 45 | 12.0 | 0.40 | 0.13 | 0.47 |
| pcb 10 | greedy+prune | 실패 | 5 | 55.2 | 0.76 | 0.05 | 0.19 |
| pcb 10 | r3_loop_rl | 성공 | 42 | 7.4 | 0.05 | 0.22 | 0.73 |
| pcb 10 | r3_loop_rl | 실패 | 8 | 10.1 | 0.07 | 0.38 | 0.54 |
| pkg 10 | greedy+prune | 성공 | 45 | 8.1 | 0.29 | 0.16 | 0.56 |
| pkg 10 | greedy+prune | 실패 | 5 | 49.2 | 0.09 | 0.04 | 0.87 |
| pkg 10 | r2_mott_rl | 성공 | 15 | 6.7 | 0.15 | 0.16 | 0.69 |
| pkg 10 | r2_mott_rl | 실패 | 10 | 14.4 | 0.58 | 0.09 | 0.33 |
| pkg 10 | r3_loop_rl | 성공 | 44 | 6.3 | 0.17 | 0.17 | 0.66 |
| pkg 10 | r3_loop_rl | 실패 | 6 | 18.7 | 0.73 | 0.06 | 0.21 |

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

