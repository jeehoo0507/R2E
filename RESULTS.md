# RESULTS (자동 생성: `scripts/collect_results.py`, 2026-10-28 19:44 UTC)

성공 = `verify.py` 700점 + 피크 정밀화 정확 검사에서 최악 |Z| ≤ 1.01·Zt. 모든 방법은 cutting-plane 안에서 실행. 시간은 문제당 초(판 준비 제외, 같은 CPU 계산기). 손으로 적은 숫자는 없다.

## 평가 (정확 검사)

## 학습 기록 (train.py metrics.json)

| run | feat / model | stage | iters | 시간 (h) | 최종 val (count/g+p, fail) | 출처 |
|---|---|---|---|---|---|---|
| runs/2026-10-28/r0_coord_distill | coord / grid | distill | 2192 | 0.77 | val_pcb10_0: 1.76/0.75, val_pkg10_0: 1.04/0.69, val_ip10_0: 0.91/0.19 | `runs/2026-10-28/r0_coord_distill/metrics.json` |
| runs/2026-10-28/r0_coord_rl | coord / grid | rl | 350 | 1.27 | val_pcb10_0: 1.06/0.56, val_pkg10_0: 0.67/0.94, val_ip10_0: 0.77/0.25 | `runs/2026-10-28/r0_coord_rl/metrics.json` |
| runs/2026-10-28/r1_modal_distill | modal / grid | distill | 2109 | 0.77 | val_pcb10_0: 0.97/0.81, val_pkg10_0: 1.44/0.56, val_ip10_0: 0.84/0.38 | `runs/2026-10-28/r1_modal_distill/metrics.json` |
| runs/2026-10-28/r2_mott_distill | mott / mott | distill | 1595 | 0.77 | val_pcb10_0: 1.08/0.75, val_pkg10_0: 1.07/0.56, val_ip10_0: 0.69/0.12 | `runs/2026-10-28/r2_mott_distill/metrics.json` |
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

