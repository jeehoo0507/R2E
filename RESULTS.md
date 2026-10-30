# RESULTS (자동 생성: `scripts/collect_results.py`, 2026-10-30 02:37 UTC)

성공 = `verify.py` 700점 + 피크 정밀화 정확 검사에서 최악 |Z| ≤ 1.01·Zt. 모든 방법은 cutting-plane 안에서 실행. 시간은 문제당 초(판 준비 제외, 같은 CPU 계산기). 손으로 적은 숫자는 없다.

## 평가 (정확 검사)

### 요약: 정확 검사 성공률 / 개수÷greedy+prune / 개수÷종류 인식 greedy (각각 둘 다 성공한 문제) [문제 수]

종류 인식 greedy (`gp_type_aware`) = 종류 하나만 쓰는 greedy+prune을 종류마다 돌려 문제마다 성공한 해 중 가장 적은 것 (`scripts/make_type_aware.py`). 10/29부터 모든 비교의 기준선.

| 방법 | ip 10 | ip 16 | pcb 10 | pcb 16 | pkg 10 | pkg 16 |
|---|---|---|---|---|---|---|
| greedy+prune | 0.40 / 1.00 / 2.03 [50] | 0.56 / 1.00 / – [50] | 0.90 / 1.00 / 0.34 [50] | 0.92 / 1.00 / – [50] | 0.90 / 1.00 / 0.75 [50] | 0.82 / 1.00 / – [50] |
| gp_type_aware | 1.00 / 0.74 / 1.00 [50] | – | 0.66 / 4.83 / 1.00 [50] | – | 0.82 / 1.59 / 1.00 [50] | – |
| bm_manoharan_rl | 0.00 / – / – [50] | – | 0.00 / – / – [50] | – | 0.00 / – / – [50] | – |
| bp_park_rl | 0.72 / 0.97 / 1.38 [50] | – | 0.46 / 4.86 / 1.13 [50] | – | 0.16 / 3.39 / 3.04 [50] | – |
| modal_rule | 0.94 / 1.10 / 1.56 [50] | – | 1.00 / 0.84 / 0.21 [50] | – | 0.88 / 0.86 / 0.61 [50] | – |
| r0_coord_distill | 0.96 / 1.17 / 2.04 [50] | – | 0.76 / 1.78 / 0.48 [50] | 0.80 / 3.63 / – [25] | 0.90 / 1.59 / 1.16 [50] | 0.80 / 2.67 / – [25] |
| r0_coord_rl | 1.00 / 1.05 / 1.45 [50] | – | 0.96 / 0.80 / 0.20 [50] | – | 0.76 / 0.79 / 0.58 [50] | 0.72 / 0.61 / – [25] |
| r0_coord_s1_rl | 0.96 / 0.97 / 1.29 [50] | – | 0.94 / 0.91 / 0.22 [50] | – | 0.74 / 0.77 / 0.54 [50] | – |
| r1_modal_distill | 1.00 / 0.91 / 1.59 [50] | – | 0.88 / 1.08 / 0.24 [50] | – | 0.90 / 1.13 / 0.82 [50] | – |
| r1_modal_rl | 0.96 / 0.88 / 1.23 [50] | – | 0.98 / 0.75 / 0.18 [50] | – | 0.68 / 0.75 / 0.53 [50] | – |
| r2_mott_distill | 0.92 / 0.74 / 1.02 [50] | – | 0.78 / 0.94 / 0.23 [50] | – | 0.70 / 0.97 / 0.69 [50] | – |
| r2_mott_rl | 1.00 / 0.74 / 1.02 [50] | – | 0.88 / 0.88 / 0.21 [50] | – | 0.72 / 0.88 / 0.59 [50] | – |
| r2a_rl | 1.00 / 0.74 / 1.03 [50] | – | 0.96 / 0.82 / 0.20 [50] | – | 0.84 / 0.87 / 0.58 [50] | – |
| r2am_rl | 1.00 / 0.74 / 1.01 [50] | – | 0.94 / 0.83 / 0.19 [50] | – | 0.86 / 0.85 / 0.61 [50] | – |
| r3_loop_distill | 0.82 / 0.77 / 1.03 [50] | – | 0.84 / 0.86 / 0.24 [50] | – | 0.80 / 0.89 / 0.65 [50] | – |
| r3_loop_rl | 0.98 / 0.74 / 1.01 [50] | – | 0.84 / 0.84 / 0.22 [50] | – | 0.88 / 0.84 / 0.59 [50] | – |
| r3_loop_rl@R16 | 1.00 / 0.74 / 1.01 [50] | – | 0.78 / 0.89 / 0.26 [50] | – | 0.78 / 0.83 / 0.57 [50] | – |
| r3_loop_rl@R2 | 1.00 / 0.74 / 1.01 [50] | – | 0.90 / 0.88 / 0.20 [50] | – | 0.74 / 0.84 / 0.59 [50] | – |
| r3_loop_rl@R4 | 1.00 / 0.74 / 1.01 [50] | – | 0.88 / 0.85 / 0.21 [50] | – | 0.88 / 0.82 / 0.59 [50] | – |
| r3a_rl | 1.00 / 0.74 / 1.02 [50] | – | 0.92 / 0.86 / 0.20 [50] | – | 0.86 / 0.83 / 0.61 [50] | – |

## 종류 인식 greedy 대비 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | 방법 | 문제 수 | 성공률 차 (방법 − 기준) [95% CI] | 개수 비 방법/기준 (둘 다 성공) [95% CI] |
|---|---|---|---|---|
| ip 10 | greedy+prune | 50 | -0.60 [-0.72, -0.46] | 2.034 [1.363, 2.797] |
| ip 10 | bm_manoharan_rl | 50 | -1.00 [-1.00, -1.00] | – [–, –] |
| ip 10 | bp_park_rl | 50 | -0.28 [-0.42, -0.16] | 1.383 [1.216, 1.567] |
| ip 10 | modal_rule | 50 | -0.06 [-0.14, +0.00] | 1.556 [1.424, 1.693] |
| ip 10 | r0_coord_distill | 50 | -0.04 [-0.10, +0.00] | 2.037 [1.646, 2.505] |
| ip 10 | r0_coord_rl | 50 | +0.00 [+0.00, +0.00] | 1.449 [1.314, 1.595] |
| ip 10 | r0_coord_s1_rl | 50 | -0.04 [-0.10, +0.00] | 1.292 [1.203, 1.390] |
| ip 10 | r1_modal_distill | 50 | +0.00 [+0.00, +0.00] | 1.587 [1.289, 1.991] |
| ip 10 | r1_modal_rl | 50 | -0.04 [-0.10, +0.00] | 1.228 [1.140, 1.335] |
| ip 10 | r2_mott_distill | 50 | -0.08 [-0.16, -0.02] | 1.023 [1.004, 1.051] |
| ip 10 | r2_mott_rl | 50 | +0.00 [+0.00, +0.00] | 1.017 [0.995, 1.046] |
| ip 10 | r2a_rl | 50 | +0.00 [+0.00, +0.00] | 1.029 [1.000, 1.067] |
| ip 10 | r2am_rl | 50 | +0.00 [+0.00, +0.00] | 1.013 [0.998, 1.035] |
| ip 10 | r3_loop_distill | 50 | -0.18 [-0.28, -0.08] | 1.026 [1.001, 1.061] |
| ip 10 | r3_loop_rl | 50 | -0.02 [-0.06, +0.00] | 1.013 [0.998, 1.038] |
| ip 10 | r3_loop_rl@R16 | 50 | +0.00 [+0.00, +0.00] | 1.009 [0.990, 1.035] |
| ip 10 | r3_loop_rl@R2 | 50 | +0.00 [+0.00, +0.00] | 1.010 [0.995, 1.034] |
| ip 10 | r3_loop_rl@R4 | 50 | +0.00 [+0.00, +0.00] | 1.014 [0.999, 1.039] |
| ip 10 | r3a_rl | 50 | +0.00 [+0.00, +0.00] | 1.016 [0.998, 1.042] |
| pcb 10 | greedy+prune | 50 | +0.24 [+0.08, +0.40] | 0.341 [0.247, 0.449] |
| pcb 10 | bm_manoharan_rl | 50 | -0.66 [-0.78, -0.54] | – [–, –] |
| pcb 10 | bp_park_rl | 50 | -0.20 [-0.36, -0.02] | 1.131 [0.701, 1.725] |
| pcb 10 | modal_rule | 50 | +0.34 [+0.22, +0.46] | 0.208 [0.167, 0.255] |
| pcb 10 | r0_coord_distill | 50 | +0.10 [-0.08, +0.26] | 0.481 [0.317, 0.699] |
| pcb 10 | r0_coord_rl | 50 | +0.30 [+0.18, +0.42] | 0.196 [0.156, 0.242] |
| pcb 10 | r0_coord_s1_rl | 50 | +0.28 [+0.14, +0.42] | 0.216 [0.170, 0.272] |
| pcb 10 | r1_modal_distill | 50 | +0.22 [+0.08, +0.36] | 0.240 [0.188, 0.296] |
| pcb 10 | r1_modal_rl | 50 | +0.32 [+0.18, +0.46] | 0.176 [0.144, 0.216] |
| pcb 10 | r2_mott_distill | 50 | +0.12 [-0.06, +0.30] | 0.230 [0.167, 0.307] |
| pcb 10 | r2_mott_rl | 50 | +0.22 [+0.04, +0.40] | 0.206 [0.164, 0.256] |
| pcb 10 | r2a_rl | 50 | +0.30 [+0.16, +0.44] | 0.203 [0.161, 0.252] |
| pcb 10 | r2am_rl | 50 | +0.28 [+0.12, +0.42] | 0.195 [0.158, 0.238] |
| pcb 10 | r3_loop_distill | 50 | +0.18 [+0.02, +0.34] | 0.243 [0.181, 0.325] |
| pcb 10 | r3_loop_rl | 50 | +0.18 [+0.00, +0.36] | 0.223 [0.171, 0.284] |
| pcb 10 | r3_loop_rl@R16 | 50 | +0.12 [-0.08, +0.30] | 0.264 [0.190, 0.356] |
| pcb 10 | r3_loop_rl@R2 | 50 | +0.24 [+0.08, +0.38] | 0.203 [0.160, 0.254] |
| pcb 10 | r3_loop_rl@R4 | 50 | +0.22 [+0.06, +0.38] | 0.211 [0.171, 0.254] |
| pcb 10 | r3a_rl | 50 | +0.26 [+0.10, +0.42] | 0.204 [0.163, 0.252] |
| pkg 10 | greedy+prune | 50 | +0.08 [-0.04, +0.20] | 0.745 [0.661, 0.834] |
| pkg 10 | bm_manoharan_rl | 50 | -0.82 [-0.92, -0.70] | – [–, –] |
| pkg 10 | bp_park_rl | 50 | -0.66 [-0.78, -0.52] | 3.040 [1.252, 6.016] |
| pkg 10 | modal_rule | 50 | +0.06 [-0.06, +0.18] | 0.605 [0.533, 0.683] |
| pkg 10 | r0_coord_distill | 50 | +0.08 [-0.04, +0.20] | 1.156 [0.889, 1.507] |
| pkg 10 | r0_coord_rl | 50 | -0.06 [-0.22, +0.10] | 0.583 [0.506, 0.664] |
| pkg 10 | r0_coord_s1_rl | 50 | -0.08 [-0.22, +0.06] | 0.541 [0.478, 0.605] |
| pkg 10 | r1_modal_distill | 50 | +0.08 [-0.02, +0.20] | 0.816 [0.709, 0.923] |
| pkg 10 | r1_modal_rl | 50 | -0.14 [-0.30, +0.04] | 0.533 [0.472, 0.600] |
| pkg 10 | r2_mott_distill | 50 | -0.12 [-0.24, +0.00] | 0.688 [0.618, 0.763] |
| pkg 10 | r2_mott_rl | 50 | -0.10 [-0.24, +0.06] | 0.587 [0.509, 0.671] |
| pkg 10 | r2a_rl | 50 | +0.02 [-0.10, +0.16] | 0.583 [0.520, 0.652] |
| pkg 10 | r2am_rl | 50 | +0.04 [-0.08, +0.18] | 0.606 [0.542, 0.677] |
| pkg 10 | r3_loop_distill | 50 | -0.02 [-0.14, +0.10] | 0.650 [0.564, 0.737] |
| pkg 10 | r3_loop_rl | 50 | +0.06 [-0.06, +0.20] | 0.591 [0.525, 0.663] |
| pkg 10 | r3_loop_rl@R16 | 50 | -0.04 [-0.18, +0.10] | 0.574 [0.510, 0.640] |
| pkg 10 | r3_loop_rl@R2 | 50 | -0.08 [-0.22, +0.08] | 0.594 [0.517, 0.681] |
| pkg 10 | r3_loop_rl@R4 | 50 | +0.06 [-0.08, +0.20] | 0.590 [0.521, 0.663] |
| pkg 10 | r3a_rl | 50 | +0.04 [-0.08, +0.16] | 0.608 [0.552, 0.667] |

## greedy+prune 대비 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | 방법 | 문제 수 | 성공률 차 (방법 − 기준) [95% CI] | 개수 비 방법/기준 (둘 다 성공) [95% CI] |
|---|---|---|---|---|
| ip 10 | gp_type_aware | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | bm_manoharan_rl | 50 | -0.40 [-0.54, -0.28] | – [–, –] |
| ip 10 | bp_park_rl | 50 | +0.32 [+0.14, +0.48] | 0.975 [0.689, 1.266] |
| ip 10 | modal_rule | 50 | +0.54 [+0.38, +0.68] | 1.102 [0.835, 1.374] |
| ip 10 | r0_coord_distill | 50 | +0.56 [+0.40, +0.70] | 1.171 [0.829, 1.541] |
| ip 10 | r0_coord_rl | 50 | +0.60 [+0.46, +0.72] | 1.049 [0.807, 1.310] |
| ip 10 | r0_coord_s1_rl | 50 | +0.56 [+0.42, +0.70] | 0.968 [0.740, 1.201] |
| ip 10 | r1_modal_distill | 50 | +0.60 [+0.46, +0.72] | 0.910 [0.666, 1.220] |
| ip 10 | r1_modal_rl | 50 | +0.56 [+0.40, +0.70] | 0.878 [0.642, 1.168] |
| ip 10 | r2_mott_distill | 50 | +0.52 [+0.38, +0.66] | 0.736 [0.578, 0.887] |
| ip 10 | r2_mott_rl | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | r2a_rl | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | r2am_rl | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | r3_loop_distill | 50 | +0.42 [+0.26, +0.56] | 0.770 [0.615, 0.909] |
| ip 10 | r3_loop_rl | 50 | +0.58 [+0.44, +0.70] | 0.736 [0.578, 0.887] |
| ip 10 | r3_loop_rl@R16 | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | r3_loop_rl@R2 | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | r3_loop_rl@R4 | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| ip 10 | r3a_rl | 50 | +0.60 [+0.46, +0.72] | 0.736 [0.578, 0.887] |
| pcb 10 | gp_type_aware | 50 | -0.24 [-0.40, -0.08] | 4.834 [3.848, 5.842] |
| pcb 10 | bm_manoharan_rl | 50 | -0.90 [-0.98, -0.82] | – [–, –] |
| pcb 10 | bp_park_rl | 50 | -0.44 [-0.60, -0.26] | 4.860 [3.000, 6.976] |
| pcb 10 | modal_rule | 50 | +0.10 [+0.02, +0.18] | 0.841 [0.742, 0.938] |
| pcb 10 | r0_coord_distill | 50 | -0.14 [-0.28, +0.00] | 1.783 [1.321, 2.308] |
| pcb 10 | r0_coord_rl | 50 | +0.06 [-0.04, +0.16] | 0.796 [0.699, 0.891] |
| pcb 10 | r0_coord_s1_rl | 50 | +0.04 [-0.06, +0.14] | 0.906 [0.781, 1.053] |
| pcb 10 | r1_modal_distill | 50 | -0.02 [-0.14, +0.10] | 1.085 [0.899, 1.297] |
| pcb 10 | r1_modal_rl | 50 | +0.08 [+0.02, +0.16] | 0.747 [0.668, 0.825] |
| pcb 10 | r2_mott_distill | 50 | -0.12 [-0.26, +0.00] | 0.938 [0.819, 1.060] |
| pcb 10 | r2_mott_rl | 50 | -0.02 [-0.12, +0.10] | 0.877 [0.772, 0.982] |
| pcb 10 | r2a_rl | 50 | +0.06 [-0.04, +0.16] | 0.819 [0.731, 0.901] |
| pcb 10 | r2am_rl | 50 | +0.04 [-0.06, +0.14] | 0.830 [0.739, 0.914] |
| pcb 10 | r3_loop_distill | 50 | -0.06 [-0.18, +0.06] | 0.864 [0.763, 0.957] |
| pcb 10 | r3_loop_rl | 50 | -0.06 [-0.20, +0.08] | 0.845 [0.738, 0.949] |
| pcb 10 | r3_loop_rl@R16 | 50 | -0.12 [-0.24, +0.00] | 0.887 [0.778, 0.998] |
| pcb 10 | r3_loop_rl@R2 | 50 | +0.00 [-0.10, +0.10] | 0.881 [0.772, 0.991] |
| pcb 10 | r3_loop_rl@R4 | 50 | -0.02 [-0.12, +0.08] | 0.845 [0.752, 0.930] |
| pcb 10 | r3a_rl | 50 | +0.02 [-0.10, +0.14] | 0.860 [0.759, 0.956] |
| pcb 16 | r0_coord_distill | 25 | -0.16 [-0.36, +0.00] | 3.627 [2.160, 5.404] |
| pkg 10 | gp_type_aware | 50 | -0.08 [-0.20, +0.04] | 1.586 [1.372, 1.836] |
| pkg 10 | bm_manoharan_rl | 50 | -0.90 [-0.98, -0.82] | – [–, –] |
| pkg 10 | bp_park_rl | 50 | -0.74 [-0.84, -0.62] | 3.392 [2.206, 4.938] |
| pkg 10 | modal_rule | 50 | -0.02 [-0.14, +0.08] | 0.863 [0.810, 0.921] |
| pkg 10 | r0_coord_distill | 50 | +0.00 [-0.08, +0.10] | 1.593 [1.307, 1.954] |
| pkg 10 | r0_coord_rl | 50 | -0.14 [-0.28, +0.00] | 0.788 [0.723, 0.859] |
| pkg 10 | r0_coord_s1_rl | 50 | -0.16 [-0.30, -0.04] | 0.772 [0.711, 0.829] |
| pkg 10 | r1_modal_distill | 50 | +0.00 [-0.08, +0.08] | 1.127 [1.027, 1.235] |
| pkg 10 | r1_modal_rl | 50 | -0.22 [-0.38, -0.06] | 0.753 [0.700, 0.805] |
| pkg 10 | r2_mott_distill | 50 | -0.20 [-0.32, -0.08] | 0.966 [0.871, 1.077] |
| pkg 10 | r2_mott_rl | 50 | -0.18 [-0.34, -0.02] | 0.877 [0.813, 0.945] |
| pkg 10 | r2a_rl | 50 | -0.06 [-0.18, +0.06] | 0.872 [0.807, 0.943] |
| pkg 10 | r2am_rl | 50 | -0.04 [-0.14, +0.06] | 0.855 [0.802, 0.907] |
| pkg 10 | r3_loop_distill | 50 | -0.10 [-0.22, +0.02] | 0.895 [0.835, 0.957] |
| pkg 10 | r3_loop_rl | 50 | -0.02 [-0.14, +0.10] | 0.840 [0.786, 0.897] |
| pkg 10 | r3_loop_rl@R16 | 50 | -0.12 [-0.28, +0.02] | 0.833 [0.774, 0.894] |
| pkg 10 | r3_loop_rl@R2 | 50 | -0.16 [-0.30, -0.04] | 0.843 [0.781, 0.905] |
| pkg 10 | r3_loop_rl@R4 | 50 | -0.02 [-0.14, +0.10] | 0.820 [0.770, 0.871] |
| pkg 10 | r3a_rl | 50 | -0.04 [-0.16, +0.08] | 0.827 [0.777, 0.884] |
| pkg 16 | r0_coord_distill | 25 | -0.04 [-0.24, +0.16] | 2.669 [1.086, 4.562] |
| pkg 16 | r0_coord_rl | 25 | -0.12 [-0.36, +0.12] | 0.611 [0.479, 0.750] |

## 비학습 모달 규칙 `modal_rule` (US 6789241식, 공진 피크에 SRF 맞는 decap) 대비 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | 방법 | 문제 수 | 성공률 차 (방법 − 기준) [95% CI] | 개수 비 방법/기준 (둘 다 성공) [95% CI] |
|---|---|---|---|---|
| ip 10 | bm_manoharan_rl | 50 | -0.94 [-1.00, -0.86] | – [–, –] |
| ip 10 | bp_park_rl | 50 | -0.22 [-0.36, -0.10] | 0.995 [0.816, 1.180] |
| ip 10 | r0_coord_rl | 50 | +0.06 [+0.00, +0.14] | 1.023 [0.888, 1.179] |
| ip 10 | r1_modal_rl | 50 | +0.02 [-0.06, +0.10] | 0.843 [0.776, 0.914] |
| ip 10 | r2_mott_rl | 50 | +0.06 [+0.00, +0.14] | 0.712 [0.653, 0.770] |
| ip 10 | r2a_rl | 50 | +0.06 [+0.00, +0.14] | 0.719 [0.659, 0.780] |
| ip 10 | r2am_rl | 50 | +0.06 [+0.00, +0.14] | 0.711 [0.654, 0.771] |
| ip 10 | r3_loop_rl | 50 | +0.04 [-0.04, +0.12] | 0.710 [0.650, 0.771] |
| ip 10 | r3a_rl | 50 | +0.06 [+0.00, +0.14] | 0.714 [0.656, 0.775] |
| pcb 10 | bm_manoharan_rl | 50 | -1.00 [-1.00, -1.00] | – [–, –] |
| pcb 10 | bp_park_rl | 50 | -0.54 [-0.68, -0.40] | 5.337 [4.241, 6.630] |
| pcb 10 | r0_coord_rl | 50 | -0.04 [-0.10, +0.00] | 0.971 [0.915, 1.033] |
| pcb 10 | r1_modal_rl | 50 | -0.02 [-0.06, +0.00] | 0.904 [0.866, 0.943] |
| pcb 10 | r2_mott_rl | 50 | -0.12 [-0.20, -0.04] | 1.015 [0.943, 1.101] |
| pcb 10 | r2a_rl | 50 | -0.04 [-0.10, +0.00] | 0.983 [0.941, 1.022] |
| pcb 10 | r2am_rl | 50 | -0.06 [-0.14, +0.00] | 0.996 [0.948, 1.043] |
| pcb 10 | r3_loop_rl | 50 | -0.16 [-0.26, -0.06] | 1.036 [0.978, 1.100] |
| pcb 10 | r3a_rl | 50 | -0.08 [-0.16, -0.02] | 1.047 [0.995, 1.093] |
| pkg 10 | bm_manoharan_rl | 50 | -0.88 [-0.96, -0.78] | – [–, –] |
| pkg 10 | bp_park_rl | 50 | -0.72 [-0.84, -0.60] | 3.839 [2.496, 5.729] |
| pkg 10 | r0_coord_rl | 50 | -0.12 [-0.26, +0.02] | 0.928 [0.869, 0.992] |
| pkg 10 | r1_modal_rl | 50 | -0.20 [-0.34, -0.04] | 0.889 [0.846, 0.929] |
| pkg 10 | r2_mott_rl | 50 | -0.16 [-0.30, -0.02] | 1.021 [0.984, 1.058] |
| pkg 10 | r2a_rl | 50 | -0.04 [-0.14, +0.06] | 1.005 [0.950, 1.058] |
| pkg 10 | r2am_rl | 50 | -0.02 [-0.14, +0.10] | 1.004 [0.956, 1.050] |
| pkg 10 | r3_loop_rl | 50 | +0.00 [-0.10, +0.10] | 0.982 [0.932, 1.031] |
| pkg 10 | r3a_rl | 50 | -0.02 [-0.14, +0.10] | 1.001 [0.951, 1.049] |

## 3단 + 주파수 궁합 편향 (dec_from_mode): `r3a_rl` vs 같은 단 편향 없는 `r3_loop_rl` 대비 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | 방법 | 문제 수 | 성공률 차 (방법 − 기준) [95% CI] | 개수 비 방법/기준 (둘 다 성공) [95% CI] |
|---|---|---|---|---|
| ip 10 | r3a_rl | 50 | +0.02 [+0.00, +0.06] | 1.003 [0.997, 1.013] |
| pcb 10 | r3a_rl | 50 | +0.08 [-0.02, +0.20] | 1.027 [0.964, 1.089] |
| pkg 10 | r3a_rl | 50 | -0.02 [-0.12, +0.08] | 1.040 [0.998, 1.084] |

## 2단 + 주파수 궁합 편향 (dec_from_mode): `r2a_rl` vs 같은 단 편향 없는 `r2_mott_rl` 대비 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | 방법 | 문제 수 | 성공률 차 (방법 − 기준) [95% CI] | 개수 비 방법/기준 (둘 다 성공) [95% CI] |
|---|---|---|---|---|
| ip 10 | r2a_rl | 50 | +0.00 [+0.00, +0.00] | 1.011 [0.995, 1.027] |
| pcb 10 | r2a_rl | 50 | +0.08 [+0.02, +0.16] | 1.003 [0.953, 1.051] |
| pkg 10 | r2a_rl | 50 | +0.12 [+0.02, +0.24] | 0.987 [0.931, 1.047] |

## r2a + 모드 경유 add 점수 (--mode_head): `r2am_rl` vs 모드 경유 점수 없는 부모 `r2a_rl` 대비 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | 방법 | 문제 수 | 성공률 차 (방법 − 기준) [95% CI] | 개수 비 방법/기준 (둘 다 성공) [95% CI] |
|---|---|---|---|---|
| ip 10 | r2am_rl | 50 | +0.00 [+0.00, +0.00] | 0.991 [0.972, 1.004] |
| pcb 10 | r2am_rl | 50 | -0.02 [-0.08, +0.04] | 1.022 [0.971, 1.079] |
| pkg 10 | r2am_rl | 50 | +0.02 [-0.08, +0.12] | 1.023 [0.972, 1.074] |

## 증류 → RL: 같은 단 `*_rl` vs `*_distill` 짝지은 bootstrap 95% CI (같은 문제를 함께 다시 뽑음, 2000회, seed 0)

| 판 | RL | 증류만 | 문제 수 | 성공률 차 (RL − 증류) [95% CI] | 개수 비 RL/증류 (둘 다 성공) [95% CI] |
|---|---|---|---|---|---|
| ip 10 | r0_coord_rl | r0_coord_distill | 50 | +0.04 [+0.00, +0.10] | 0.942 [0.797, 1.107] |
| pcb 10 | r0_coord_rl | r0_coord_distill | 50 | +0.20 [+0.08, +0.32] | 0.673 [0.564, 0.779] |
| pkg 10 | r0_coord_rl | r0_coord_distill | 50 | -0.14 [-0.28, -0.02] | 0.662 [0.574, 0.754] |
| pkg 16 | r0_coord_rl | r0_coord_distill | 25 | -0.08 [-0.32, +0.12] | 0.645 [0.488, 0.794] |
| ip 10 | r1_modal_rl | r1_modal_distill | 50 | -0.04 [-0.10, +0.00] | 0.949 [0.850, 1.052] |
| pcb 10 | r1_modal_rl | r1_modal_distill | 50 | +0.10 [+0.02, +0.18] | 0.788 [0.720, 0.850] |
| pkg 10 | r1_modal_rl | r1_modal_distill | 50 | -0.22 [-0.38, -0.08] | 0.715 [0.659, 0.774] |
| ip 10 | r2_mott_rl | r2_mott_distill | 50 | +0.08 [+0.02, +0.16] | 0.987 [0.974, 0.998] |
| pcb 10 | r2_mott_rl | r2_mott_distill | 50 | +0.10 [-0.02, +0.22] | 1.002 [0.922, 1.080] |
| pkg 10 | r2_mott_rl | r2_mott_distill | 50 | +0.02 [-0.14, +0.16] | 0.942 [0.857, 1.031] |
| ip 10 | r3_loop_rl | r3_loop_distill | 50 | +0.16 [+0.08, +0.26] | 0.992 [0.978, 1.004] |
| pcb 10 | r3_loop_rl | r3_loop_distill | 50 | +0.00 [-0.14, +0.14] | 1.010 [0.926, 1.095] |
| pkg 10 | r3_loop_rl | r3_loop_distill | 50 | +0.08 [-0.04, +0.20] | 0.968 [0.913, 1.024] |

### ip 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 개수 / 종류 인식 greedy (둘 다 성공) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.40 | 10.30 | 1.000 | 2.034 | 2.944 | `runs/2026-10-28/baselines/eval/eval_ip10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_ip10_1__greedy+prune.json` |
| gp_type_aware | 50 (0, 1) | 1.00 | 8.30 | 0.736 | 1.000 | 11.703 | `runs/2026-10-29/baselines_e0plus/eval/eval_ip10_0__gp_type_aware.json`, `runs/2026-10-29/baselines_e0plus/eval/eval_ip10_1__gp_type_aware.json` |
| bm_manoharan_rl | 50 (0, 1) | 0.00 | – | – | – | 0.119 | `runs/2026-10-29/bm_manoharan_rl/eval/eval_ip10_0__bm_manoharan_rl.json`, `runs/2026-10-29/bm_manoharan_rl/eval/eval_ip10_1__bm_manoharan_rl.json` |
| bp_park_rl | 50 (0, 1) | 0.72 | 9.78 | 0.975 | 1.383 | 2.314 | `runs/2026-10-29/bp_park_rl/eval/eval_ip10_0__bp_park_rl.json`, `runs/2026-10-29/bp_park_rl/eval/eval_ip10_1__bp_park_rl.json` |
| modal_rule | 50 (0, 1) | 0.94 | 12.53 | 1.102 | 1.556 | 0.619 | `runs/2026-10-28/baselines/eval/eval_ip10_0__modal_rule.json`, `runs/2026-10-28/baselines/eval/eval_ip10_1__modal_rule.json` |
| r0_coord_distill | 50 (0, 1) | 0.96 | 18.21 | 1.171 | 2.037 | 1.167 | `runs/2026-10-28/r0_coord_distill/eval/eval_ip10_0__r0_coord_distill.json`, `runs/2026-10-28/r0_coord_distill/eval/eval_ip10_1__r0_coord_distill.json` |
| r0_coord_rl | 50 (0, 1) | 1.00 | 11.94 | 1.049 | 1.449 | 1.127 | `runs/2026-10-28/r0_coord_rl/eval/eval_ip10_0__r0_coord_rl.json`, `runs/2026-10-28/r0_coord_rl/eval/eval_ip10_1__r0_coord_rl.json` |
| r0_coord_s1_rl | 50 (0, 1) | 0.96 | 10.73 | 0.968 | 1.292 | 0.595 | `runs/2026-10-29/r0_coord_s1_rl/eval/eval_ip10_0__r0_coord_s1_rl.json`, `runs/2026-10-29/r0_coord_s1_rl/eval/eval_ip10_1__r0_coord_s1_rl.json` |
| r1_modal_distill | 50 (0, 1) | 1.00 | 13.88 | 0.910 | 1.587 | 0.630 | `runs/2026-10-28/r1_modal_distill/eval/eval_ip10_0__r1_modal_distill.json`, `runs/2026-10-28/r1_modal_distill/eval/eval_ip10_1__r1_modal_distill.json` |
| r1_modal_rl | 50 (0, 1) | 0.96 | 10.12 | 0.878 | 1.228 | 0.982 | `runs/2026-10-28/r1_modal_rl/eval/eval_ip10_0__r1_modal_rl.json`, `runs/2026-10-28/r1_modal_rl/eval/eval_ip10_1__r1_modal_rl.json` |
| r2_mott_distill | 50 (0, 1) | 0.92 | 7.98 | 0.736 | 1.023 | 0.586 | `runs/2026-10-28/r2_mott_distill/eval/eval_ip10_0__r2_mott_distill.json`, `runs/2026-10-28/r2_mott_distill/eval/eval_ip10_1__r2_mott_distill.json` |
| r2_mott_rl | 50 (0, 1) | 1.00 | 8.54 | 0.736 | 1.017 | 0.524 | `runs/2026-10-28/r2_mott_rl/eval/eval_ip10_0__r2_mott_rl.json`, `runs/2026-10-28/r2_mott_rl/eval/eval_ip10_1__r2_mott_rl.json` |
| r2a_rl | 50 (0, 1) | 1.00 | 8.70 | 0.736 | 1.029 | 0.353 | `runs/2026-10-29/r2a_rl/eval/eval_ip10_0__r2a_rl.json`, `runs/2026-10-29/r2a_rl/eval/eval_ip10_1__r2a_rl.json` |
| r2am_rl | 50 (0, 1) | 1.00 | 8.50 | 0.736 | 1.013 | 0.325 | `runs/2026-10-29/r2am_rl/eval/eval_ip10_0__r2am_rl.json`, `runs/2026-10-29/r2am_rl/eval/eval_ip10_1__r2am_rl.json` |
| r3_loop_distill | 50 (0, 1) | 0.82 | 6.95 | 0.770 | 1.026 | 1.657 | `runs/2026-10-28/r3_loop_distill/eval/eval_ip10_0__r3_loop_distill.json`, `runs/2026-10-28/r3_loop_distill/eval/eval_ip10_1__r3_loop_distill.json` |
| r3_loop_rl | 50 (0, 1) | 0.98 | 8.39 | 0.736 | 1.013 | 0.574 | `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_1__r3_loop_rl.json` |
| r3_loop_rl@R16 | 50 (0, 1) | 1.00 | 8.44 | 0.736 | 1.009 | 0.619 | `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_0__r3_loop_rl@R16.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_1__r3_loop_rl@R16.json` |
| r3_loop_rl@R2 | 50 (0, 1) | 1.00 | 8.44 | 0.736 | 1.010 | 0.278 | `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_0__r3_loop_rl@R2.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_1__r3_loop_rl@R2.json` |
| r3_loop_rl@R4 | 50 (0, 1) | 1.00 | 8.50 | 0.736 | 1.014 | 0.330 | `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_0__r3_loop_rl@R4.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_ip10_1__r3_loop_rl@R4.json` |
| r3a_rl | 50 (0, 1) | 1.00 | 8.52 | 0.736 | 1.016 | 0.424 | `runs/2026-10-29/r3a_rl/eval/eval_ip10_0__r3a_rl.json`, `runs/2026-10-29/r3a_rl/eval/eval_ip10_1__r3a_rl.json` |

### ip 16×16

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 개수 / 종류 인식 greedy (둘 다 성공) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.56 | 73.93 | 1.000 | – | 82.481 | `runs/2026-10-28/baselines/eval/eval_ip16_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_ip16_1__greedy+prune.json` |

### pcb 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 개수 / 종류 인식 greedy (둘 다 성공) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.90 | 12.02 | 1.000 | 0.341 | 4.838 | `runs/2026-10-28/baselines/eval/eval_pcb10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pcb10_1__greedy+prune.json` |
| gp_type_aware | 50 (0, 1) | 0.66 | 45.33 | 4.834 | 1.000 | 24.761 | `runs/2026-10-29/baselines_e0plus/eval/eval_pcb10_0__gp_type_aware.json`, `runs/2026-10-29/baselines_e0plus/eval/eval_pcb10_1__gp_type_aware.json` |
| bm_manoharan_rl | 50 (0, 1) | 0.00 | – | – | – | 0.237 | `runs/2026-10-29/bm_manoharan_rl/eval/eval_pcb10_0__bm_manoharan_rl.json`, `runs/2026-10-29/bm_manoharan_rl/eval/eval_pcb10_1__bm_manoharan_rl.json` |
| bp_park_rl | 50 (0, 1) | 0.46 | 36.26 | 4.860 | 1.131 | 7.636 | `runs/2026-10-29/bp_park_rl/eval/eval_pcb10_0__bp_park_rl.json`, `runs/2026-10-29/bp_park_rl/eval/eval_pcb10_1__bp_park_rl.json` |
| modal_rule | 50 (0, 1) | 1.00 | 7.14 | 0.841 | 0.208 | 0.505 | `runs/2026-10-28/baselines/eval/eval_pcb10_0__modal_rule.json`, `runs/2026-10-28/baselines/eval/eval_pcb10_1__modal_rule.json` |
| r0_coord_distill | 50 (0, 1) | 0.76 | 15.58 | 1.783 | 0.481 | 2.723 | `runs/2026-10-28/r0_coord_distill/eval/eval_pcb10_0__r0_coord_distill.json`, `runs/2026-10-28/r0_coord_distill/eval/eval_pcb10_1__r0_coord_distill.json` |
| r0_coord_rl | 50 (0, 1) | 0.96 | 6.92 | 0.796 | 0.196 | 2.375 | `runs/2026-10-28/r0_coord_rl/eval/eval_pcb10_0__r0_coord_rl.json`, `runs/2026-10-28/r0_coord_rl/eval/eval_pcb10_1__r0_coord_rl.json` |
| r0_coord_s1_rl | 50 (0, 1) | 0.94 | 7.17 | 0.906 | 0.216 | 3.736 | `runs/2026-10-29/r0_coord_s1_rl/eval/eval_pcb10_0__r0_coord_s1_rl.json`, `runs/2026-10-29/r0_coord_s1_rl/eval/eval_pcb10_1__r0_coord_s1_rl.json` |
| r1_modal_distill | 50 (0, 1) | 0.88 | 8.73 | 1.085 | 0.240 | 1.198 | `runs/2026-10-28/r1_modal_distill/eval/eval_pcb10_0__r1_modal_distill.json`, `runs/2026-10-28/r1_modal_distill/eval/eval_pcb10_1__r1_modal_distill.json` |
| r1_modal_rl | 50 (0, 1) | 0.98 | 6.31 | 0.747 | 0.176 | 0.504 | `runs/2026-10-28/r1_modal_rl/eval/eval_pcb10_0__r1_modal_rl.json`, `runs/2026-10-28/r1_modal_rl/eval/eval_pcb10_1__r1_modal_rl.json` |
| r2_mott_distill | 50 (0, 1) | 0.78 | 7.38 | 0.938 | 0.230 | 1.887 | `runs/2026-10-28/r2_mott_distill/eval/eval_pcb10_0__r2_mott_distill.json`, `runs/2026-10-28/r2_mott_distill/eval/eval_pcb10_1__r2_mott_distill.json` |
| r2_mott_rl | 50 (0, 1) | 0.88 | 6.77 | 0.877 | 0.206 | 0.683 | `runs/2026-10-28/r2_mott_rl/eval/eval_pcb10_0__r2_mott_rl.json`, `runs/2026-10-28/r2_mott_rl/eval/eval_pcb10_1__r2_mott_rl.json` |
| r2a_rl | 50 (0, 1) | 0.96 | 6.88 | 0.819 | 0.203 | 0.391 | `runs/2026-10-29/r2a_rl/eval/eval_pcb10_0__r2a_rl.json`, `runs/2026-10-29/r2a_rl/eval/eval_pcb10_1__r2a_rl.json` |
| r2am_rl | 50 (0, 1) | 0.94 | 6.89 | 0.830 | 0.195 | 0.478 | `runs/2026-10-29/r2am_rl/eval/eval_pcb10_0__r2am_rl.json`, `runs/2026-10-29/r2am_rl/eval/eval_pcb10_1__r2am_rl.json` |
| r3_loop_distill | 50 (0, 1) | 0.84 | 9.19 | 0.864 | 0.243 | 1.898 | `runs/2026-10-28/r3_loop_distill/eval/eval_pcb10_0__r3_loop_distill.json`, `runs/2026-10-28/r3_loop_distill/eval/eval_pcb10_1__r3_loop_distill.json` |
| r3_loop_rl | 50 (0, 1) | 0.84 | 7.40 | 0.845 | 0.223 | 0.920 | `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_1__r3_loop_rl.json` |
| r3_loop_rl@R16 | 50 (0, 1) | 0.78 | 7.87 | 0.887 | 0.264 | 1.669 | `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_0__r3_loop_rl@R16.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_1__r3_loop_rl@R16.json` |
| r3_loop_rl@R2 | 50 (0, 1) | 0.90 | 7.29 | 0.881 | 0.203 | 0.750 | `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_0__r3_loop_rl@R2.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_1__r3_loop_rl@R2.json` |
| r3_loop_rl@R4 | 50 (0, 1) | 0.88 | 7.34 | 0.845 | 0.211 | 0.795 | `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_0__r3_loop_rl@R4.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pcb10_1__r3_loop_rl@R4.json` |
| r3a_rl | 50 (0, 1) | 0.92 | 7.41 | 0.860 | 0.204 | 0.562 | `runs/2026-10-29/r3a_rl/eval/eval_pcb10_0__r3a_rl.json`, `runs/2026-10-29/r3a_rl/eval/eval_pcb10_1__r3a_rl.json` |

### pcb 16×16

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 개수 / 종류 인식 greedy (둘 다 성공) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.92 | 12.63 | 1.000 | – | 61.893 | `runs/2026-10-28/baselines/eval/eval_pcb16_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pcb16_1__greedy+prune.json` |
| r0_coord_distill | 25 (0) | 0.80 | 38.10 | 3.627 | – | 55.917 | `runs/2026-10-28/r0_coord_distill/eval/eval_pcb16_0__r0_coord_distill.json` |

### pkg 10×10

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 개수 / 종류 인식 greedy (둘 다 성공) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.90 | 8.07 | 1.000 | 0.745 | 3.786 | `runs/2026-10-28/baselines/eval/eval_pkg10_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pkg10_1__greedy+prune.json` |
| gp_type_aware | 50 (0, 1) | 0.82 | 12.44 | 1.586 | 1.000 | 9.172 | `runs/2026-10-29/baselines_e0plus/eval/eval_pkg10_0__gp_type_aware.json`, `runs/2026-10-29/baselines_e0plus/eval/eval_pkg10_1__gp_type_aware.json` |
| bm_manoharan_rl | 50 (0, 1) | 0.00 | – | – | – | 0.296 | `runs/2026-10-29/bm_manoharan_rl/eval/eval_pkg10_0__bm_manoharan_rl.json`, `runs/2026-10-29/bm_manoharan_rl/eval/eval_pkg10_1__bm_manoharan_rl.json` |
| bp_park_rl | 50 (0, 1) | 0.16 | 26.38 | 3.392 | 3.040 | 5.519 | `runs/2026-10-29/bp_park_rl/eval/eval_pkg10_0__bp_park_rl.json`, `runs/2026-10-29/bp_park_rl/eval/eval_pkg10_1__bp_park_rl.json` |
| modal_rule | 50 (0, 1) | 0.88 | 6.52 | 0.863 | 0.605 | 2.202 | `runs/2026-10-28/baselines/eval/eval_pkg10_0__modal_rule.json`, `runs/2026-10-28/baselines/eval/eval_pkg10_1__modal_rule.json` |
| r0_coord_distill | 50 (0, 1) | 0.90 | 12.31 | 1.593 | 1.156 | 1.390 | `runs/2026-10-28/r0_coord_distill/eval/eval_pkg10_0__r0_coord_distill.json`, `runs/2026-10-28/r0_coord_distill/eval/eval_pkg10_1__r0_coord_distill.json` |
| r0_coord_rl | 50 (0, 1) | 0.76 | 5.82 | 0.788 | 0.583 | 2.622 | `runs/2026-10-28/r0_coord_rl/eval/eval_pkg10_0__r0_coord_rl.json`, `runs/2026-10-28/r0_coord_rl/eval/eval_pkg10_1__r0_coord_rl.json` |
| r0_coord_s1_rl | 50 (0, 1) | 0.74 | 5.73 | 0.772 | 0.541 | 2.337 | `runs/2026-10-29/r0_coord_s1_rl/eval/eval_pkg10_0__r0_coord_s1_rl.json`, `runs/2026-10-29/r0_coord_s1_rl/eval/eval_pkg10_1__r0_coord_s1_rl.json` |
| r1_modal_distill | 50 (0, 1) | 0.90 | 8.64 | 1.127 | 0.816 | 0.820 | `runs/2026-10-28/r1_modal_distill/eval/eval_pkg10_0__r1_modal_distill.json`, `runs/2026-10-28/r1_modal_distill/eval/eval_pkg10_1__r1_modal_distill.json` |
| r1_modal_rl | 50 (0, 1) | 0.68 | 5.44 | 0.753 | 0.533 | 1.866 | `runs/2026-10-28/r1_modal_rl/eval/eval_pkg10_0__r1_modal_rl.json`, `runs/2026-10-28/r1_modal_rl/eval/eval_pkg10_1__r1_modal_rl.json` |
| r2_mott_distill | 50 (0, 1) | 0.70 | 7.29 | 0.966 | 0.688 | 1.509 | `runs/2026-10-28/r2_mott_distill/eval/eval_pkg10_0__r2_mott_distill.json`, `runs/2026-10-28/r2_mott_distill/eval/eval_pkg10_1__r2_mott_distill.json` |
| r2_mott_rl | 50 (0, 1) | 0.72 | 6.22 | 0.877 | 0.587 | 1.594 | `runs/2026-10-28/r2_mott_rl/eval/eval_pkg10_0__r2_mott_rl.json`, `runs/2026-10-28/r2_mott_rl/eval/eval_pkg10_1__r2_mott_rl.json` |
| r2a_rl | 50 (0, 1) | 0.84 | 6.31 | 0.872 | 0.583 | 0.718 | `runs/2026-10-29/r2a_rl/eval/eval_pkg10_0__r2a_rl.json`, `runs/2026-10-29/r2a_rl/eval/eval_pkg10_1__r2a_rl.json` |
| r2am_rl | 50 (0, 1) | 0.86 | 6.35 | 0.855 | 0.606 | 0.617 | `runs/2026-10-29/r2am_rl/eval/eval_pkg10_0__r2am_rl.json`, `runs/2026-10-29/r2am_rl/eval/eval_pkg10_1__r2am_rl.json` |
| r3_loop_distill | 50 (0, 1) | 0.80 | 7.03 | 0.895 | 0.650 | 1.093 | `runs/2026-10-28/r3_loop_distill/eval/eval_pkg10_0__r3_loop_distill.json`, `runs/2026-10-28/r3_loop_distill/eval/eval_pkg10_1__r3_loop_distill.json` |
| r3_loop_rl | 50 (0, 1) | 0.88 | 6.27 | 0.840 | 0.591 | 1.763 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_0__r3_loop_rl.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl.json` |
| r3_loop_rl@R16 | 50 (0, 1) | 0.78 | 5.97 | 0.833 | 0.574 | 2.320 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_0__r3_loop_rl@R16.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl@R16.json` |
| r3_loop_rl@R2 | 50 (0, 1) | 0.74 | 6.08 | 0.843 | 0.594 | 1.418 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_0__r3_loop_rl@R2.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl@R2.json` |
| r3_loop_rl@R4 | 50 (0, 1) | 0.88 | 6.27 | 0.820 | 0.590 | 2.076 | `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_0__r3_loop_rl@R4.json`, `runs/2026-10-28/r3_loop_rl/eval/eval_pkg10_1__r3_loop_rl@R4.json` |
| r3a_rl | 50 (0, 1) | 0.86 | 6.51 | 0.827 | 0.608 | 0.875 | `runs/2026-10-29/r3a_rl/eval/eval_pkg10_0__r3a_rl.json`, `runs/2026-10-29/r3a_rl/eval/eval_pkg10_1__r3a_rl.json` |

### pkg 16×16

| 방법 | 문제 수 (풀 파일) | 정확 검사 성공률 | 개수 (성공 평균) | 개수 / greedy+prune (둘 다 성공, 같은 파일끼리 짝지음) | 개수 / 종류 인식 greedy (둘 다 성공) | 문제당 시간 (s) | 출처 |
|---|---|---|---|---|---|---|---|
| greedy+prune | 50 (0, 1) | 0.82 | 21.02 | 1.000 | – | 130.854 | `runs/2026-10-28/baselines/eval/eval_pkg16_0__greedy+prune.json`, `runs/2026-10-28/baselines/eval/eval_pkg16_1__greedy+prune.json` |
| r0_coord_distill | 25 (1) | 0.80 | 31.15 | 2.669 | – | 49.804 | `runs/2026-10-28/r0_coord_distill/eval/eval_pkg16_1__r0_coord_distill.json` |
| r0_coord_rl | 25 (1) | 0.72 | 7.94 | 0.611 | – | 18.971 | `runs/2026-10-28/r0_coord_rl/eval/eval_pkg16_1__r0_coord_rl.json` |

## decap 종류 비율 (놓인 decap 중, 정확 검사 성공/실패 문제별; 종류 0 = C가 가장 큰 것, `decap_loop/techs.py`)

| 판 | 방법 | 문제 | 문제 수 | 평균 개수 | 종류 0 | 종류 1 | 종류 2 |
|---|---|---|---|---|---|---|---|
| ip 10 | greedy+prune | 성공 | 20 | 10.3 | 0.46 | 0.05 | 0.50 |
| ip 10 | greedy+prune | 실패 | 30 | 78.6 | 0.07 | 0.02 | 0.90 |
| ip 10 | bm_manoharan_rl | 실패 | 50 | 0.1 | 1.00 | 0.00 | 0.00 |
| ip 10 | bp_park_rl | 성공 | 36 | 9.8 | 0.94 | 0.00 | 0.06 |
| ip 10 | bp_park_rl | 실패 | 14 | 67.6 | 0.26 | 0.00 | 0.74 |
| ip 10 | gp_type_aware | 성공 | 50 | 8.3 | 1.00 | 0.00 | 0.00 |
| ip 10 | modal_rule | 성공 | 47 | 12.5 | 1.00 | 0.00 | 0.00 |
| ip 10 | modal_rule | 실패 | 3 | 25.7 | 1.00 | 0.00 | 0.00 |
| ip 10 | r0_coord_distill | 성공 | 48 | 18.2 | 0.69 | 0.04 | 0.27 |
| ip 10 | r0_coord_distill | 실패 | 2 | 52.0 | 0.48 | 0.01 | 0.51 |
| ip 10 | r0_coord_rl | 성공 | 50 | 11.9 | 0.98 | 0.02 | 0.00 |
| ip 10 | r0_coord_s1_rl | 성공 | 48 | 10.7 | 0.99 | 0.01 | 0.00 |
| ip 10 | r0_coord_s1_rl | 실패 | 2 | 30.0 | 1.00 | 0.00 | 0.00 |
| ip 10 | r1_modal_distill | 성공 | 50 | 13.9 | 0.78 | 0.01 | 0.21 |
| ip 10 | r1_modal_rl | 성공 | 48 | 10.1 | 0.98 | 0.02 | 0.00 |
| ip 10 | r1_modal_rl | 실패 | 2 | 23.0 | 1.00 | 0.00 | 0.00 |
| ip 10 | r2_mott_distill | 성공 | 46 | 8.0 | 0.98 | 0.00 | 0.02 |
| ip 10 | r2_mott_distill | 실패 | 4 | 43.2 | 0.17 | 0.01 | 0.82 |
| ip 10 | r2_mott_rl | 성공 | 50 | 8.5 | 0.97 | 0.00 | 0.03 |
| ip 10 | r2a_rl | 성공 | 50 | 8.7 | 0.97 | 0.00 | 0.03 |
| ip 10 | r2am_rl | 성공 | 50 | 8.5 | 1.00 | 0.00 | 0.00 |
| ip 10 | r3_loop_distill | 성공 | 41 | 7.0 | 1.00 | 0.00 | 0.00 |
| ip 10 | r3_loop_distill | 실패 | 9 | 69.2 | 0.04 | 0.00 | 0.96 |
| ip 10 | r3_loop_rl | 성공 | 49 | 8.4 | 0.99 | 0.00 | 0.00 |
| ip 10 | r3_loop_rl | 실패 | 1 | 13.0 | 0.92 | 0.00 | 0.08 |
| ip 10 | r3_loop_rl@R16 | 성공 | 50 | 8.4 | 0.99 | 0.01 | 0.00 |
| ip 10 | r3_loop_rl@R2 | 성공 | 50 | 8.4 | 1.00 | 0.00 | 0.00 |
| ip 10 | r3_loop_rl@R4 | 성공 | 50 | 8.5 | 1.00 | 0.00 | 0.00 |
| ip 10 | r3a_rl | 성공 | 50 | 8.5 | 1.00 | 0.00 | 0.00 |
| ip 16 | greedy+prune | 성공 | 28 | 73.9 | 0.16 | 0.02 | 0.82 |
| ip 16 | greedy+prune | 실패 | 22 | 204.9 | 0.05 | 0.01 | 0.94 |
| pcb 10 | greedy+prune | 성공 | 45 | 12.0 | 0.40 | 0.13 | 0.47 |
| pcb 10 | greedy+prune | 실패 | 5 | 55.2 | 0.76 | 0.05 | 0.19 |
| pcb 10 | bm_manoharan_rl | 실패 | 50 | 0.4 | 0.00 | 0.00 | 1.00 |
| pcb 10 | bp_park_rl | 성공 | 23 | 36.3 | 0.05 | 0.00 | 0.95 |
| pcb 10 | bp_park_rl | 실패 | 27 | 39.1 | 0.04 | 0.00 | 0.96 |
| pcb 10 | gp_type_aware | 성공 | 33 | 45.3 | 0.00 | 0.94 | 0.06 |
| pcb 10 | gp_type_aware | 실패 | 17 | 42.4 | 0.00 | 0.71 | 0.29 |
| pcb 10 | modal_rule | 성공 | 50 | 7.1 | 0.09 | 0.18 | 0.73 |
| pcb 10 | r0_coord_distill | 성공 | 38 | 15.6 | 0.48 | 0.10 | 0.42 |
| pcb 10 | r0_coord_distill | 실패 | 12 | 60.0 | 0.54 | 0.02 | 0.44 |
| pcb 10 | r0_coord_rl | 성공 | 48 | 6.9 | 0.08 | 0.21 | 0.70 |
| pcb 10 | r0_coord_rl | 실패 | 2 | 45.0 | 0.00 | 0.23 | 0.77 |
| pcb 10 | r0_coord_s1_rl | 성공 | 47 | 7.2 | 0.10 | 0.18 | 0.72 |
| pcb 10 | r0_coord_s1_rl | 실패 | 3 | 82.7 | 0.39 | 0.01 | 0.60 |
| pcb 10 | r1_modal_distill | 성공 | 44 | 8.7 | 0.19 | 0.15 | 0.66 |
| pcb 10 | r1_modal_distill | 실패 | 6 | 50.2 | 0.75 | 0.02 | 0.23 |
| pcb 10 | r1_modal_rl | 성공 | 49 | 6.3 | 0.10 | 0.21 | 0.69 |
| pcb 10 | r1_modal_rl | 실패 | 1 | 10.0 | 0.10 | 0.10 | 0.80 |
| pcb 10 | r2_mott_distill | 성공 | 39 | 7.4 | 0.15 | 0.15 | 0.70 |
| pcb 10 | r2_mott_distill | 실패 | 11 | 32.9 | 0.69 | 0.02 | 0.29 |
| pcb 10 | r2_mott_rl | 성공 | 44 | 6.8 | 0.08 | 0.18 | 0.74 |
| pcb 10 | r2_mott_rl | 실패 | 6 | 9.7 | 0.21 | 0.10 | 0.69 |
| pcb 10 | r2a_rl | 성공 | 48 | 6.9 | 0.09 | 0.17 | 0.74 |
| pcb 10 | r2a_rl | 실패 | 2 | 9.0 | 0.17 | 0.17 | 0.67 |
| pcb 10 | r2am_rl | 성공 | 47 | 6.9 | 0.08 | 0.19 | 0.73 |
| pcb 10 | r2am_rl | 실패 | 3 | 11.0 | 0.21 | 0.03 | 0.76 |
| pcb 10 | r3_loop_distill | 성공 | 42 | 9.2 | 0.24 | 0.12 | 0.65 |
| pcb 10 | r3_loop_distill | 실패 | 8 | 8.8 | 0.07 | 0.17 | 0.76 |
| pcb 10 | r3_loop_rl | 성공 | 42 | 7.4 | 0.05 | 0.22 | 0.73 |
| pcb 10 | r3_loop_rl | 실패 | 8 | 10.1 | 0.07 | 0.38 | 0.54 |
| pcb 10 | r3_loop_rl@R16 | 성공 | 39 | 7.9 | 0.07 | 0.19 | 0.74 |
| pcb 10 | r3_loop_rl@R16 | 실패 | 11 | 12.5 | 0.09 | 0.30 | 0.61 |
| pcb 10 | r3_loop_rl@R2 | 성공 | 45 | 7.3 | 0.07 | 0.20 | 0.73 |
| pcb 10 | r3_loop_rl@R2 | 실패 | 5 | 8.6 | 0.14 | 0.28 | 0.58 |
| pcb 10 | r3_loop_rl@R4 | 성공 | 44 | 7.3 | 0.09 | 0.22 | 0.69 |
| pcb 10 | r3_loop_rl@R4 | 실패 | 6 | 9.5 | 0.05 | 0.21 | 0.74 |
| pcb 10 | r3a_rl | 성공 | 46 | 7.4 | 0.08 | 0.19 | 0.73 |
| pcb 10 | r3a_rl | 실패 | 4 | 9.0 | 0.19 | 0.19 | 0.61 |
| pcb 16 | greedy+prune | 성공 | 46 | 12.6 | 0.29 | 0.15 | 0.56 |
| pcb 16 | greedy+prune | 실패 | 4 | 195.2 | 0.76 | 0.04 | 0.20 |
| pcb 16 | r0_coord_distill | 성공 | 20 | 38.1 | 0.51 | 0.06 | 0.43 |
| pcb 16 | r0_coord_distill | 실패 | 5 | 54.0 | 0.35 | 0.04 | 0.61 |
| pkg 10 | greedy+prune | 성공 | 45 | 8.1 | 0.29 | 0.16 | 0.56 |
| pkg 10 | greedy+prune | 실패 | 5 | 49.2 | 0.09 | 0.04 | 0.87 |
| pkg 10 | bm_manoharan_rl | 실패 | 50 | 0.7 | 0.00 | 0.83 | 0.17 |
| pkg 10 | bp_park_rl | 성공 | 8 | 26.4 | 0.03 | 0.00 | 0.97 |
| pkg 10 | bp_park_rl | 실패 | 42 | 48.7 | 0.00 | 0.00 | 1.00 |
| pkg 10 | gp_type_aware | 성공 | 41 | 12.4 | 0.55 | 0.43 | 0.02 |
| pkg 10 | gp_type_aware | 실패 | 9 | 33.8 | 0.85 | 0.11 | 0.04 |
| pkg 10 | modal_rule | 성공 | 44 | 6.5 | 0.16 | 0.15 | 0.70 |
| pkg 10 | modal_rule | 실패 | 6 | 19.0 | 0.75 | 0.10 | 0.15 |
| pkg 10 | r0_coord_distill | 성공 | 45 | 12.3 | 0.33 | 0.16 | 0.51 |
| pkg 10 | r0_coord_distill | 실패 | 5 | 28.4 | 0.46 | 0.06 | 0.48 |
| pkg 10 | r0_coord_rl | 성공 | 38 | 5.8 | 0.18 | 0.23 | 0.59 |
| pkg 10 | r0_coord_rl | 실패 | 12 | 25.1 | 0.77 | 0.08 | 0.16 |
| pkg 10 | r0_coord_s1_rl | 성공 | 37 | 5.7 | 0.22 | 0.22 | 0.57 |
| pkg 10 | r0_coord_s1_rl | 실패 | 13 | 22.3 | 0.59 | 0.22 | 0.19 |
| pkg 10 | r1_modal_distill | 성공 | 45 | 8.6 | 0.31 | 0.16 | 0.54 |
| pkg 10 | r1_modal_distill | 실패 | 5 | 39.8 | 0.60 | 0.06 | 0.35 |
| pkg 10 | r1_modal_rl | 성공 | 34 | 5.4 | 0.17 | 0.25 | 0.58 |
| pkg 10 | r1_modal_rl | 실패 | 16 | 11.6 | 0.45 | 0.33 | 0.22 |
| pkg 10 | r2_mott_distill | 성공 | 35 | 7.3 | 0.20 | 0.11 | 0.69 |
| pkg 10 | r2_mott_distill | 실패 | 15 | 25.7 | 0.46 | 0.02 | 0.52 |
| pkg 10 | r2_mott_rl | 성공 | 36 | 6.2 | 0.14 | 0.17 | 0.70 |
| pkg 10 | r2_mott_rl | 실패 | 14 | 12.1 | 0.51 | 0.11 | 0.38 |
| pkg 10 | r2a_rl | 성공 | 42 | 6.3 | 0.17 | 0.17 | 0.66 |
| pkg 10 | r2a_rl | 실패 | 8 | 15.2 | 0.66 | 0.07 | 0.27 |
| pkg 10 | r2am_rl | 성공 | 43 | 6.3 | 0.16 | 0.17 | 0.67 |
| pkg 10 | r2am_rl | 실패 | 7 | 15.3 | 0.79 | 0.05 | 0.17 |
| pkg 10 | r3_loop_distill | 성공 | 40 | 7.0 | 0.25 | 0.14 | 0.60 |
| pkg 10 | r3_loop_distill | 실패 | 10 | 18.9 | 0.35 | 0.05 | 0.60 |
| pkg 10 | r3_loop_rl | 성공 | 44 | 6.3 | 0.17 | 0.17 | 0.66 |
| pkg 10 | r3_loop_rl | 실패 | 6 | 18.7 | 0.73 | 0.06 | 0.21 |
| pkg 10 | r3_loop_rl@R16 | 성공 | 39 | 6.0 | 0.17 | 0.17 | 0.66 |
| pkg 10 | r3_loop_rl@R16 | 실패 | 11 | 17.9 | 0.66 | 0.06 | 0.28 |
| pkg 10 | r3_loop_rl@R2 | 성공 | 37 | 6.1 | 0.23 | 0.08 | 0.69 |
| pkg 10 | r3_loop_rl@R2 | 실패 | 13 | 12.8 | 0.61 | 0.04 | 0.36 |
| pkg 10 | r3_loop_rl@R4 | 성공 | 44 | 6.3 | 0.24 | 0.09 | 0.67 |
| pkg 10 | r3_loop_rl@R4 | 실패 | 6 | 28.7 | 0.87 | 0.02 | 0.12 |
| pkg 10 | r3a_rl | 성공 | 43 | 6.5 | 0.14 | 0.18 | 0.68 |
| pkg 10 | r3a_rl | 실패 | 7 | 19.0 | 0.27 | 0.35 | 0.38 |
| pkg 16 | greedy+prune | 성공 | 41 | 21.0 | 0.41 | 0.09 | 0.50 |
| pkg 16 | greedy+prune | 실패 | 9 | 51.7 | 0.11 | 0.06 | 0.83 |
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
| eval_ip10_0 | 1 (20 pF, 2 pH, 0.1 Ω) | 0.12 | 24.67 | 7.444 | 7.444 | 0.40 | 1.00 | 6.432 | `runs/analysis/gp_one_type/eval_ip10_0__greedy+prune@type1.json` |
| eval_ip10_0 | 2 (5 pF, 1 pH, 0.2 Ω) | 0.00 | – | – | – | 0.40 | 1.00 | 6.712 | `runs/analysis/gp_one_type/eval_ip10_0__greedy+prune@type2.json` |
| eval_ip10_1 | 0 (100 pF, 5 pH, 0.05 Ω) | 1.00 | 8.68 | 0.707 | 1.000 | 0.40 | 0.96 | 0.135 | `runs/analysis/gp_one_type/eval_ip10_1__greedy+prune@type0.json` |
| eval_ip10_1 | 1 (20 pF, 2 pH, 0.1 Ω) | 0.24 | 33.67 | 5.351 | 9.224 | 0.40 | 0.96 | 4.317 | `runs/analysis/gp_one_type/eval_ip10_1__greedy+prune@type1.json` |
| eval_ip10_1 | 2 (5 pF, 1 pH, 0.2 Ω) | 0.00 | – | – | – | 0.40 | 0.96 | 5.372 | `runs/analysis/gp_one_type/eval_ip10_1__greedy+prune@type2.json` |
| eval_pcb10_0 | 0 (10000 pF, 100 pH, 0.02 Ω) | 0.04 | 32.00 | 4.571 | 4.571 | 1.00 | 0.84 | 9.110 | `runs/analysis/gp_one_type/eval_pcb10_0__greedy+prune@type0.json` |
| eval_pcb10_0 | 1 (1000 pF, 30 pH, 0.05 Ω) | 0.72 | 48.39 | 5.002 | 6.485 | 1.00 | 0.84 | 9.077 | `runs/analysis/gp_one_type/eval_pcb10_0__greedy+prune@type1.json` |
| eval_pcb10_0 | 2 (100 pF, 10 pH, 0.1 Ω) | 0.00 | – | – | – | 1.00 | 0.84 | 6.620 | `runs/analysis/gp_one_type/eval_pcb10_0__greedy+prune@type2.json` |
| eval_pcb10_1 | 0 (10000 pF, 100 pH, 0.02 Ω) | 0.00 | – | – | – | 0.80 | 0.84 | 10.252 | `runs/analysis/gp_one_type/eval_pcb10_1__greedy+prune@type0.json` |
| eval_pcb10_1 | 1 (1000 pF, 30 pH, 0.05 Ω) | 0.56 | 42.64 | 4.372 | 5.849 | 0.80 | 0.84 | 7.373 | `runs/analysis/gp_one_type/eval_pcb10_1__greedy+prune@type1.json` |
| eval_pcb10_1 | 2 (100 pF, 10 pH, 0.1 Ω) | 0.08 | 41.50 | 4.637 | 5.420 | 0.80 | 0.84 | 7.089 | `runs/analysis/gp_one_type/eval_pcb10_1__greedy+prune@type2.json` |
| eval_pcb16_0 | 0 (10000 pF, 100 pH, 0.02 Ω) | 0.08 | 73.50 | 7.254 | – | 0.96 | – | 217.392 | `runs/analysis/gp_one_type/eval_pcb16_0__greedy+prune@type0.json` |
| eval_pkg10_0 | 0 (1000 pF, 40 pH, 0.03 Ω) | 0.76 | 16.00 | 2.297 | 2.793 | 0.92 | 0.88 | 3.414 | `runs/analysis/gp_one_type/eval_pkg10_0__greedy+prune@type0.json` |
| eval_pkg10_0 | 1 (220 pF, 15 pH, 0.05 Ω) | 0.40 | 8.70 | 1.262 | 1.629 | 0.92 | 0.88 | 1.911 | `runs/analysis/gp_one_type/eval_pkg10_0__greedy+prune@type1.json` |
| eval_pkg10_0 | 2 (47 pF, 8 pH, 0.1 Ω) | 0.08 | 6.00 | 1.333 | 1.300 | 0.92 | 0.88 | 1.977 | `runs/analysis/gp_one_type/eval_pkg10_0__greedy+prune@type2.json` |
| eval_pkg10_1 | 0 (1000 pF, 40 pH, 0.03 Ω) | 0.72 | 16.61 | 1.921 | 2.434 | 0.88 | 0.88 | 3.466 | `runs/analysis/gp_one_type/eval_pkg10_1__greedy+prune@type0.json` |
| eval_pkg10_1 | 1 (220 pF, 15 pH, 0.05 Ω) | 0.56 | 10.50 | 1.210 | 1.492 | 0.88 | 0.88 | 2.771 | `runs/analysis/gp_one_type/eval_pkg10_1__greedy+prune@type1.json` |
| eval_pkg10_1 | 2 (47 pF, 8 pH, 0.1 Ω) | 0.00 | – | – | – | 0.88 | 0.88 | 4.805 | `runs/analysis/gp_one_type/eval_pkg10_1__greedy+prune@type2.json` |

## 종류 인식 greedy: 판 종류마다 맞는 decap 종류 (`scripts/analyze_gp_one_type.py`, `scripts/make_type_aware.py`)

| 판 | 문제 수 | 종류 0만: 성공률 | 종류 1만: 성공률 | 종류 2만: 성공률 | 종류 인식 greedy가 고른 종류 비율 (성공 문제, 0/1/2) |
|---|---|---|---|---|---|
| ip 10 | 50 | 1.00 | 0.18 | 0.00 | 1.00 / 0.00 / 0.00 |
| pcb 10 | 50 | 0.02 | 0.64 | 0.04 | 0.00 / 0.94 / 0.06 |
| pkg 10 | 50 | 0.74 | 0.48 | 0.04 | 0.41 / 0.54 / 0.05 |

단일 종류 g+p로 가장 잘 되는 종류: ip 10 → 종류 0, pcb 10 → 종류 1, pkg 10 → 종류 0. **판 종류마다 다르다** — 규칙 기준선은 판 종류마다 종류를 다시 골라야 하고 (종류 인식 greedy는 그래서 종류 수만큼 다시 돈다), 정책은 모델 하나가 판마다 고른다 (위 "decap 종류 비율" 표).

## 선행 연구 재구현 (재구현 기준, 같은 평가 풀·정확 검사)

### B-Park: Park 2022 / DevFormer식 좌표 입력 attention-model 포인터 정책 (`baselines_ml/park_am.py`)

| 판 | 방법 | 문제 수 | 성공률 | 개수÷greedy+prune | 개수÷종류 인식 greedy | 문제당 시간 (s) |
|---|---|---|---|---|---|---|
| ip 10 | bp_park_rl | 50 | 0.72 | 0.97 | 1.38 | 2.314 |
| pcb 10 | bp_park_rl | 50 | 0.46 | 4.86 | 1.13 | 7.636 |
| pkg 10 | bp_park_rl | 50 | 0.16 | 3.39 | 3.04 | 5.519 |

- 학습 예산: 원 논문은 RL만 — 여기서는 우리와 같은 distill 0.75 h + RL 1.25 h (같은 선생님 해, 같은 학습 풀).
- 행동 공간: 원 논문은 포트 선택(종류 고정) — 여기서는 우리 행동 공간 (칸 × 종류 추가/제거 + 멈춤), 채널마다 포인터 query.
- 보상: 원 논문은 임피던스 점수 — 여기서는 우리 보상 (−개수/N_ref − λ·(실패+위반), λ 라그랑주), 정확 검사 실패 반영.
- 구조·학습: Kool식 encode-once 대신 매 수 다시 인코딩 (상태가 특징에 있음), BatchNorm 대신 LayerNorm, 기준선 교체는 paired t-test 대신 val 최고 갱신 때, 기준선 rollout의 실패는 작업 격자 기준 (정확 검사 안 함), 모방 항·선생님 교체 없음 (`--imit 0`).

### B-Manoharan: Manoharan 2026식 고정 포트 순서 + decap 토큰으로 종류/빈칸 선택 (`baselines_ml/manoharan.py`)

| 판 | 방법 | 문제 수 | 성공률 | 개수÷greedy+prune | 개수÷종류 인식 greedy | 문제당 시간 (s) |
|---|---|---|---|---|---|---|
| ip 10 | bm_manoharan_rl | 50 | 0.00 | – | – | 0.119 |
| pcb 10 | bm_manoharan_rl | 50 | 0.00 | – | – | 0.237 |
| pkg 10 | bm_manoharan_rl | 50 | 0.00 | – | – | 0.296 |

- 학습: 원 논문의 RL 세부 대신 우리 파이프라인 그대로 (distill 0.75 h: 선생님 해를 고정 순서로 다시 걸은 궤적, RL 1.25 h: 그룹 기준선 + 모방 + 선생님 교체).
- 포트 순서: 최악 탐침에서 본 loop L (포트 i 단락, 한 주파수 f0) 오름차순 — f0는 맨판 최악 위반 주파수 (원 논문은 고정 설계 주파수).
- 상태: 고정 특징 주파수 8점의 |Z|/Zt + 전역 블록 MLP와 현재 포트 L 임베딩; 원 논문의 Z 행렬 입력 전체는 아님. 갱신은 우리 env의 rank-1 (Schur/Woodbury).
- 행동: 현재 포트에 종류 또는 빈칸, 제거·종류 변경 없음; 에피소드 길이 = 놓을 수 있는 칸 수 + 1 (학습의 max_steps 64 대신).

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
| runs/2026-10-29/bm_manoharan_distill | manoharan / manoharan | distill | 1456 | 0.77 | val_pcb10_0: –/1.00, val_pkg10_0: –/1.00, val_ip10_0: –/1.00 | `runs/2026-10-29/bm_manoharan_distill/metrics.json` |
| runs/2026-10-29/bm_manoharan_rl | manoharan / manoharan | rl | 321 | 1.27 | val_pcb10_0: –/1.00, val_pkg10_0: 1.50/0.94, val_ip10_0: –/1.00 | `runs/2026-10-29/bm_manoharan_rl/metrics.json` |
| runs/2026-10-29/bp_park_distill | coord / park_am | distill | 2210 | 0.77 | val_pcb10_0: 7.99/0.62, val_pkg10_0: 5.67/0.50, val_ip10_0: 0.75/0.25 | `runs/2026-10-29/bp_park_distill/metrics.json` |
| runs/2026-10-29/bp_park_rl | coord / park_am | rl | 199 | 1.27 | val_pcb10_0: 3.09/0.88, val_pkg10_0: 1.67/0.94, val_ip10_0: 0.65/0.31 | `runs/2026-10-29/bp_park_rl/metrics.json` |
| runs/2026-10-29/lo_ip_r0_distill | coord / grid | distill | 2282 | 0.77 | val_pcb10_0: 2.52/0.50, val_pkg10_0: 1.00/0.81 | `runs/2026-10-29/lo_ip_r0_distill/metrics.json` |
| runs/2026-10-29/lo_ip_r0_rl | coord / grid | rl | 300 | 1.27 | val_pcb10_0: 0.96/0.25, val_pkg10_0: 1.00/0.69 | `runs/2026-10-29/lo_ip_r0_rl/metrics.json` |
| runs/2026-10-29/lo_ip_r1_distill | modal / grid | distill | 2176 | 0.77 | val_pcb10_0: 1.32/0.69, val_pkg10_0: 0.94/0.81 | `runs/2026-10-29/lo_ip_r1_distill/metrics.json` |
| runs/2026-10-29/lo_ip_r1_rl | modal / grid | rl | 343 | 1.27 | val_pcb10_0: 1.21/0.69, val_pkg10_0: 0.94/0.62 | `runs/2026-10-29/lo_ip_r1_rl/metrics.json` |
| runs/2026-10-29/lo_ip_r2_distill | mott / mott | distill | 1621 | 0.77 | val_pcb10_0: 1.14/0.56, val_pkg10_0: 1.08/0.75 | `runs/2026-10-29/lo_ip_r2_distill/metrics.json` |
| runs/2026-10-29/r0_coord_s1_distill | coord / grid | distill | 2215 | 0.77 | val_pcb10_0: 1.97/0.38, val_pkg10_0: 1.20/0.69, val_ip10_0: 0.83/0.19 | `runs/2026-10-29/r0_coord_s1_distill/metrics.json` |
| runs/2026-10-29/r0_coord_s1_rl | coord / grid | rl | 338 | 1.27 | val_pcb10_0: 1.13/0.75, val_pkg10_0: 1.04/0.75, val_ip10_0: 0.78/0.38 | `runs/2026-10-29/r0_coord_s1_rl/metrics.json` |
| runs/2026-10-29/r2a_distill | mott / mott | distill | 1603 | 0.77 | val_pcb10_0: 1.03/0.75, val_pkg10_0: 1.07/0.50, val_ip10_0: 0.69/0.12 | `runs/2026-10-29/r2a_distill/metrics.json` |
| runs/2026-10-29/r2a_rl | mott / mott | rl | 361 | 1.27 | val_pcb10_0: 1.04/0.44, val_pkg10_0: 1.10/0.69, val_ip10_0: 0.69/0.12 | `runs/2026-10-29/r2a_rl/metrics.json` |
| runs/2026-10-29/r2am_distill | mott / mott | distill | 1569 | 0.77 | val_pcb10_0: 0.86/0.50, val_pkg10_0: 0.98/0.56, val_ip10_0: 0.69/0.12 | `runs/2026-10-29/r2am_distill/metrics.json` |
| runs/2026-10-29/r2am_rl | mott / mott | rl | 356 | 1.27 | val_pcb10_0: 1.02/0.56, val_pkg10_0: 0.97/0.50, val_ip10_0: 0.69/0.12 | `runs/2026-10-29/r2am_rl/metrics.json` |
| runs/2026-10-29/r3a_distill | mott / loop | distill | 1477 | 0.77 | val_pcb10_0: 1.14/0.69, val_pkg10_0: 1.07/0.69, val_ip10_0: 0.69/0.25 | `runs/2026-10-29/r3a_distill/metrics.json` |
| runs/2026-10-29/r3a_rl | mott / loop | rl | 346 | 1.27 | val_pcb10_0: 0.99/0.81, val_pkg10_0: 0.97/0.56, val_ip10_0: 0.69/0.12 | `runs/2026-10-29/r3a_rl/metrics.json` |
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

