# PROGRESS (갱신 2026-10-29 04:58 UTC, 라운드 37)

**지금 (04:58):** GPU r3a **RL** it 275 (3514 s, oom 0, gpu peak 17.2 GB) · CPU 4 = 학습 certify 2 + 10칸 종류 2 g+p (5/6 끝, 남은 것 ip10_1) + side16_gp 16칸 g+p 1 worker. GPU 큐: r3a → r2a → bp_park → bm_manoharan → 사다리 0~3단 seed 1·2 (8개). pod 16.3 GiB, oom_kill 0.

## 라운드 37 (04:57~ UTC)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 16.3 GiB / 60, oom_kill 0. r3a RL it 275 (`runs/2026-10-29/r3a_rl/log.txt`).
- **종류 2 g+p ip10_0·pkg10_1 끝 → E0+ 기록 5/6** (`collect_results.py`, RESULTS 재생성; `runs/2026-10-29/baselines_e0plus/eval/`):
  - **ip 10 (25문제, 파일 0)**: E0+ 성공 1.00, 개수 7.92 (모두 종류 0) vs g+p 0.40 → E0+/g+p 개수 비 0.765. 정책 vs E0+: 성공률 차 모두 +0.00, **개수 비 0단 1.437 [1.260, 1.628] · 1단 1.206 [1.112, 1.304] · 2단 1.019 [0.979, 1.064] · 3단 1.026 [0.997, 1.072]** → ip에서는 E0+가 강한 기준선이고, 2·3단만 E0+와 같은 개수 (CI가 1 포함), 0·1단은 더 많이 씀. 사다리 효과가 E0+ 기준으로는 ip에서 보임 (g+p 기준으로는 안 보였던 것). 정책이 E0+를 넘지는 못함 — 그대로 보고.
  - **pkg 10 (50문제, 파일 0·1)**: E0+ 성공 0.82, 개수 12.44, E0+/g+p 개수 비 1.586 [1.372, 1.836]. 정책 vs E0+: 개수 비 0.53~0.59, 성공률 차 −0.14~+0.06 (모두 CI 0 포함).
  - "판 종류마다 맞는 decap 종류" 표: 단일 종류 최선 ip → 0 (1.00), pcb → 1 (0.64), pkg → 0 (0.74), pkg는 E0+가 고른 종류가 0·1 섞임 (0.41 / 0.54).
- 결정: 새 실험·코드 변경 없음 (CPU 4칸 꽉 참; 남은 판단은 r3a RL `done:` ~05:15 → 10칸 평가, ip10_1 종류 2 → E0+ 6/6).
- 다음 라운드: r3a 10칸 평가 기록 → ablation 표 (r3a vs r3) + E0+ 대비 판정 → RESULTS 재생성. ip10_1 종류 2 끝나면 ip E0+ 50문제로.

## 라운드 36 (04:45~ UTC, 라운드 35 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 15.9 GiB / 60, oom_kill 0. r3a RL it 225 (train_pcb10_2 cert-bad 5, OOM 0, grid capped 51). E0+ 기록 3/6 그대로 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~35와 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음 (남은 종류 2: ip10_0·ip10_1·pkg10_1 → E0+ 6/6).

## 라운드 35 (04:42~ UTC, 라운드 34 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 16.6 GiB / 60, oom_kill 0. E0+ 기록 3/6 그대로 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- r3a RL it 200 val (16문제, 보고서용 아님): pcb 1.124/fail 0.62 · pkg 1.000/0.88 · ip 0.691/0.12 → it 100 (score 1.678, best 유지)보다 나쁨. 같은 시점 r3 RL: pcb 0.990/0.75 · pkg 0.964/0.56 · ip 0.691/0.19 — r3도 best가 it 100이었음 → 두 run 모두 RL 후반에 val이 나빠지는 같은 모양, 평가는 best ckpt로 하므로 조건 동일.
- 결정: 새 실험·코드 변경 없음 (라운드 23~34와 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음 (남은 종류 2: ip10_0·ip10_1·pkg10_1 → E0+ 6/6).

## 라운드 34 (04:39~ UTC)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 22.3 GiB / 60, oom_kill 0. r3a RL 마지막 줄 it 175 그대로 (resume ckpt it 192 저장).
- **종류 2 g+p pcb10_1·pkg10_0 끝 → E0+ 기록 3/6** (`collect_results.py` → `make_type_aware.py`, RESULTS 재생성):
  - pcb 10 (50문제, 파일 0·1): E0+ 성공 0.66, 개수 45.3 vs g+p 0.90 / 12.0 → 개수 비 E0+/g+p 4.83 [3.85, 5.84]. 정책 vs E0+ 개수 비 0.18~0.22, 성공률 차 +0.18~+0.32.
  - pkg 10 (25문제, 파일 0만): E0+ 성공 0.84, 개수 12.9 vs g+p 0.90 → 개수 비 1.83 [1.46, 2.28], 성공률 차 −0.08 [−0.24, +0.08]. 정책 vs E0+ 개수 비 0.51~0.56, 성공률 차 −0.04~+0.04 (CI 0 포함).
  - 종류 2만: pcb10_1 0.08, pkg10_0 0.08. 단일 종류로 가장 잘 되는 종류: **pcb → 1, pkg → 0 (ip → 0)** → RESULTS에 "판 종류마다 다르다" 문장이 자동으로 나옴 (QUEUE 03:15 4번 대비 문장).
  - 해석: pcb·pkg 모두 "종류 하나 고정" E0+는 g+p보다 약함 (종류를 섞어야 하는 판). ip에서만 E0+가 강할 것으로 예상 (종류 0만 50/50) — ip 종류 2 끝나면 확인. PROPOSALS (d') 그대로 (사람 결정).
- 결정: 새 실험·코드 변경 없음 (CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음 (남은 종류 2: ip10_0·ip10_1·pkg10_1 → E0+ 6/6).

## 라운드 33 (04:37~ UTC, 라운드 32 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 16.8 GiB / 60, oom_kill 0. r3a RL it 175 (train_pcb10_0 cert-bad 2, OOM 0, gpu peak 16.4 GB). E0+ 기록 1/6 그대로 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~32와 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음.

## 라운드 32 (04:34~ UTC, 라운드 31 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 17.2 GiB / 60, oom_kill 0. r3a RL 마지막 줄 it 150 그대로, E0+ 기록 1/6 그대로 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~31과 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음.

## 라운드 31 (04:32~ UTC, 라운드 30 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개 (load 4.1), pod 17.3 GiB / 60, oom_kill 0. r3a RL it 150 (train_pcb12_1 cert-bad 3, OOM 0, grid capped 15; val은 it 100이 마지막). 종류 2 기록 1/6 그대로 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~30과 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음.

## 라운드 30 (04:29~ UTC, 라운드 29 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개, pod 17.1 GiB / 60, oom_kill 0. r3a RL 마지막 줄 it 125 그대로. 종류 2 기록 1/6 그대로 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~29와 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음.

## 라운드 29 (04:26~ UTC, 라운드 28 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개, pod 15.6 GiB / 60, oom_kill 0. r3a RL it 125 (train_pcb12_1 cert-bad 9, OOM 0; val은 it 100이 마지막: score 1.678).
- 새로 끝난 실험 없음 (E0+ 기록 1/6 그대로) → RESULTS 재생성 없음. 선행 연구 재구현 절·각 표 아래 차이 한 줄은 `collect_results.py`에 이미 있음 확인 (bp_park·bm_manoharan 기록이 생기면 자동 표시).
- 결정: 새 실험·코드 변경 없음 (라운드 23~27과 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음.

## 라운드 28 (04:21~ UTC)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, pod 15.8 GiB / 60, oom_kill 0.
- **종류 2 g+p pcb10_0 끝 → 첫 E0+ 기록** (`runs/2026-10-29/baselines_e0plus/eval/eval_pcb10_0__gp_type_aware.json`, 25문제): 종류 0·1·2만 성공률 0.04 / 0.72 / 0.00 → E0+ 성공 0.72, 개수 48.4 (모두 종류 1). **g+p (0.90) 보다 성공률 낮고, 둘 다 성공한 문제 개수 비 E0+/g+p 5.00 [3.79, 6.30]** — pcb에서는 종류를 섞어야 하므로 "종류 하나 고정"은 강한 기준선이 아님. 정책 vs E0+ 개수 비 (pcb10_0, 25문제) 0.17~0.22는 이 약점 때문. RESULTS 재생성.
- 결정: E0+ 정의 (QUEUE 03:15 4번)는 그대로 두고, g+p 대비·E0+ 대비를 둘 다 계속 보고 → "{g+p, E0+} 중 문제마다 최선"을 정식 기준으로 할지는 PROPOSALS (d')에 (사람 결정; 기준선을 바꾸는 일이라 에이전트가 정하지 않음).
- `collect_results.py` 수정 2개 (CPU 거의 안 씀): (1) **같은 단 편향 없는 버전 대비 짝지은 bootstrap CI 표** 추가 (`ABLATIONS`: r3a_rl vs r3_loop_rl, r2a_rl vs r2_mott_rl; QUEUE 03:15 3번 판정 기준) — 기록이 생기면 자동 표시, r2_mott_rl vs r3_loop_rl로 표 모양 확인. (2) "판 종류마다 맞는 decap 종류" 표가 종류 0·1(50문제)과 종류 2(25문제)를 섞어 계산하던 것을 **세 종류가 모두 끝난 풀 파일만** 쓰게 고침, 판 종류가 하나뿐이면 "같다/다르다" 문장을 내지 않음.
- 다음 라운드: 라운드 22와 같음 (r3a RL `done:` ~05:15 → r3a 10칸 평가 → 새 ablation 표·E0+ 대비로 판정).

## 라운드 27 (04:18~ UTC, 라운드 26 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개 (certify 2 + 종류 2 g+p + 16칸 g+p 1 worker RSS 9.1 GB), pod 16.5 GiB / 60, oom_kill 0.
- r3a RL it 100 (1254 s, OOM 0, gpu peak 14.6 GB, grid capped 5): val (보고서용 아님, 16문제) pcb 1.121/fail 0.44 · pkg 0.972/0.56 · ip 0.691/0.12, score 1.678 (new best). 같은 시점 r3 RL: pcb 0.991/0.44 · pkg 0.979/0.62 · ip 0.691/0.12, score 1.679 → 거의 같음; 판정은 10칸 eval 뒤 (`runs/2026-10-29/r3a_rl/log.txt`).
- 종류 2 g+p 기록 아직 0/6 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~26과 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤).
- 다음 라운드: 라운드 22와 같음.

## 라운드 26 (04:15~ UTC, 라운드 25 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개 (certify 2 + 종류 2 g+p pcb10_0 + 16칸 g+p 1 worker RSS 9.2 GB), pod 15.1 GiB / 60, oom_kill 0. r3a RL it 75 (gpu peak 14.4 GB, r3 RL의 같은 시점 14.6 GB와 비슷). 종류 2 기록은 아직 0/6 → 새로 끝난 실험 없음, RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23~25와 같은 이유).
- 다음 라운드: 라운드 22와 같음.

## 라운드 25 (04:12~ UTC, 라운드 24 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개, oom_kill 0.
- **10칸 종류 1만 쓰는 g+p 6파일 끝** (`runs/analysis/gp_one_type/*@type1.json`, 각 25문제; 성공률 / 성공 문제 평균 개수): ip10_0 0.12 / 24.7 · ip10_1 0.24 / 33.7 · pcb10_0 0.72 / 48.4 · pcb10_1 0.56 / 42.6 · pkg10_0 0.40 / 8.7 · pkg10_1 0.56 / 10.5. (종류 0: ip 1.00, pcb 0.04·0.00, pkg 0.76·…) → 판 종류마다 맞는 decap 종류가 다르다는 QUEUE 4번 대비가 종류 1에서도 보임. E0+ 표는 종류 2 끝(~05:30) 뒤 `make_type_aware.py`로.
- 결정: 새 실험·코드 변경 없음 (CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤). RESULTS 재생성은 E0+가 완성되는 종류 2 뒤에 한 번에 (지금 종류 1은 분석 기록이라 요약표 행이 바뀌지 않음).
- 다음 라운드: 라운드 22와 같음.

## 라운드 24 (04:10~ UTC, 라운드 23 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, CPU 바쁜 것 4개 (certify 2 + 종류 g+p ip10_1 종류 1 + 16칸 g+p 1 worker RSS 9.2 GB), pod 14.5 GiB / 60, oom_kill 0. r3a RL it 50 (603 s, OOM 0). 새로 끝난 실험 없음 → RESULTS 재생성 없음.
- 결정: 새 실험·코드 변경 없음 (라운드 23과 같은 이유: CPU 4칸 꽉 참, 다음 판단은 r3a RL `done:` ~05:15 뒤). DAILY는 01:50 작성 → 다음은 10/30 01:50 무렵.
- 다음 라운드: 라운드 22와 같음.

## 라운드 23 (04:07~ UTC, 라운드 22 직후라 짧음)
- 상태 정상: `ensure_running.py` → day2 드라이버·side16_gp 살아 있음, 프로세스 목록에 CPU 바쁜 것 4개 (certify 2 + 종류 g+p 1 + 16칸 g+p 1), oom_kill 0. 새로 끝난 실험 없음 → RESULTS 재생성 없음.
- `analyze_gp_one_type.py`가 `--skip_existing`를 받는 것 확인 (드라이버 CPU 줄의 e0plus 항목이 같은 인자를 씀; side10_base.log의 argparse 오류는 수정 전 흔적).
- 결정: 새 실험·코드 변경 없음 — CPU 4칸이 차 있고, 다음 판단(r3a 10칸 평가, E0+ 열)은 ~05:15 이후 기록이 있어야 가능.
- 다음 라운드: 라운드 22와 같음 (r3a RL `done:` → r3a 10칸 평가 → 종류 2 끝 → `make_type_aware.py` → r3 대비·E0+ 대비 판정).

## 라운드 22 (04:03~ UTC)
- 상태 정상 (드라이버·side16_gp·종류 루프 살아 있음, oom_kill 0). 새로 끝난 실험 없음 → RESULTS 재생성 없음.
- 후보 (c) 검산 루프 코드 확인: 1수 깊이 Woodbury 검산(모든 add/remove의 정확한 V−V′·최악 여유)은 이미 1~3단 입력 + logit prior에 있음 → PROPOSALS 2일차 메모 (c). 새것이 되려면 여러 수 초안 + 모드 재추출이어야 함.
- 결정: (c)는 (a) r3a·r2a 판정 뒤로 미룸 — 한 번에 하나만 바꾸기 규칙, GPU 큐 ~20 h, CPU 4칸이 다 차서 smoke test도 못 돌림.
- 다음 라운드: r3a RL `done:` (~05:15) → 드라이버의 r3a 10칸 평가 → 종류 2 끝 (~05:30) → `make_type_aware.py`로 E0+ 열 채우기 → r3 대비·E0+ 대비 판정.

## 라운드 21 (03:24~ UTC)
- 상태 정상: day2 드라이버·side16_gp 살아 있음, oom_kill 0. side10_base.log의 `--skip_existing` argparse 오류는 이전 체인의 흔적이고, 지금 루프(pid 117899, 종류 0→1→2)는 정상 진행.
- **r3a distill 끝** (03:56): 1477 iter / 0.77 h, best iter 800 (val score 1.858), gpu peak 12.1 GB, OOM 0 (`runs/2026-10-29/r3a_distill/log.txt`). 같은 예산의 r3 distill은 1500 iter, best iter 1400 score 1.743 — val 16문제라 잡음 큼, 판정은 10칸 eval 뒤 (보고서용 아님). r3a RL 03:57 시작 → 끝 ~05:15 예상, 그다음 드라이버가 r3a 10칸 평가 (CPU 줄 최우선).
- **QUEUE B (외부 데이터) 포기, ~15분** → PROPOSALS (e). DevFormer 공개 데이터는 고정 Z 행렬 하나(201점 표, 100 포트, 문제 100개 = 탐침 + keep-out), decap 한 종류 R+C (ESL 0 → SRF 없음), 목표 임피던스 없음, 체크포인트는 저장소에 없음(Google Drive). 우리 판정 `verify.py` 700점 검사(격자 Laplacian으로 임의 f 재계산)를 표 Z에 적용할 수 없고, 정책 입력이 T=3 종류에 묶여 있음.
- 결정: 외부 데이터 어댑터를 만들지 않음 — 새 판정 기준이 필요해 규칙 2 밖이고, QUEUE가 "형식이 안 맞으면 포기"를 허용. 필요한 것 목록은 PROPOSALS (e)에 (사람 결정).
- 다음 라운드: r3a RL 진행·OOM·`done:` → r3a 10칸 평가 기록 → 종류별 g+p 1·2 끝 (~05:30) → E0+ 표 → r3 대비·E0+ 대비 판정 → RESULTS 재생성.

## 라운드 20 (02:59~ UTC) — QUEUE 2일차 지시 + 03:15 수정 반영
- **지금 도는 것:** GPU `r3a` = 3단 loop + `--fc_bias` (QUEUE 03:15 3번: `dec_from_mode`에만 편향 −|log f_k − log SRF_t|/τ_h, τ head마다 학습, init 1 decade; 나머지·COMMON·seed·distill 0.75 h + RL 1.25 h는 r3와 같음), 03:10 시작 (`runs/2026-10-29/r3a_distill/log.txt`). 큐: r3a → r2a (2단 + 같은 편향) → bp_park. CPU: ip16_1 풀 (11.9 h째) + 10칸 종류 하나 g+p (종류 0→1→2, `agent/logs/side10_base.log`) + 학습 certify 2 = 4.
- **새 드라이버 `scripts/pipeline_day2.py`** (`agent/logs/pipeline_day2.log`): `agent/day2_queue.json`을 매 단계 다시 읽음 → GPU 줄 학습 하나씩 (CERTIFY_WORKERS=2), CPU 줄 1 worker: 끝난 학습의 10칸 평가 → "cpu" 항목 순서 (E0+ 10칸 → 16칸을 풀 파일 하나씩: E0+ 종류 0·1·2 + rl 사다리 4단 → 1일차 남은 10칸 r3@R·distill). `ensure_running.py`는 day2 드라이버 + side16_gp (+ 16칸 풀 파일이 없으면 build_pools 1 worker).
- 결정: **1일차 드라이버·side_evals 멈춤** (03:02) — 학습에 certify 2칸이 필요하고 한도는 4. 버린 진행분: r0 rl 16칸 job ~20분, r3 @R4 10칸 job 수 분 (같은 명령이 day2 큐에 있음).
- 결정: **CERTIFY_WORKERS 2 유지** (QUEUE는 2 또는 1 허용) — 1로 하면 같은 시간 예산의 RL iter 수가 r3·r2와 달라져 "편향 하나만 바꾼" 비교가 흐려짐. 대신 16칸 평가는 풀 생성이 끝나 그 칸이 비면 (side16_gp: 16칸 g+p → modal_rule) 그리고 E0+ 10칸이 끝나면 (CPU 줄) 1 worker로 이어짐.
- 결정: 03:04에 시작한 `a2_fc` (2단 + 편향 + 모드←decap 역방향 attention 추가 = 두 가지 변경)는 QUEUE 03:15 수정과 달라 6분 만에 멈춤 → `runs/2026-10-29/a2_fc*_killed_031014_spec_changed`. 역방향 코드는 지움.
- **E0+ 종류 인식 greedy (정식):** `scripts/make_type_aware.py` (종류별 g+p 기록에서 문제마다 성공 해 중 최소 개수, 셋 다 실패면 실패, 시간은 종류 합) → 보통 eval 기록 `runs/2026-10-29/baselines_e0plus/eval/`. `collect_results.py`가 먼저 실행; 요약표·종류별 표에 "개수÷종류 인식 greedy" 열, 새 표 "판 종류마다 맞는 decap 종류" + 숫자에서 자동 생성되는 한 문장 (QUEUE 4번). 10칸 종류 1·2 기록이 끝나면 자동으로 채워짐 (/tmp 가짜 기록으로 선택 규칙·표 확인).
- **B-Park 구현** (`baselines_ml/park_am.py`, `train.py --model park_am --baseline rollout --imit 0`): 좌표 입력 transformer 인코더 + 문맥 glimpse + C·tanh 포인터 (채널마다 query), RL = frozen copy greedy rollout 기준선. CPU smoke 통과. RESULTS "선행 연구 재구현" 절 + 원 논문과 다른 점 4줄 (기록이 생기면 표시). QUEUE대로 r3a 결과 뒤에 학습 (큐 3번째).
- **B-Manoharan 구현** (`baselines_ml/manoharan.py`, `--model manoharan`): 포트 순서 = 최악 탐침에서 본 loop L (포트 단락, 맨판 최악 위반 주파수 f0 한 점) 오름차순, 행동 = 현재 포트에 종류 또는 빈칸, 상태 = 고정 특징 주파수 |Z|/Zt MLP + 포트 L 임베딩, decap 토큰 + 빈칸 토큰 attention 점수, 갱신은 env rank-1. 선생님 해를 고정 순서로 다시 걷는 궤적으로 distill. 확인: val ip10_0·pcb10_0 32문제에서 고정 순서 재생이 선생님 개수와 같게 성공 (1.00, 개수 비 1.000), CPU 학습 smoke (distill·rl 3 iter) rc 0. 원 논문과 다른 점 4줄은 RESULTS "선행 연구 재구현" 절에 (기록이 생기면 표시).
- **짝지은 bootstrap 95% CI** (`collect_results.py`, 2000회, seed 0): 종류 인식 greedy 대비 + g+p 대비 성공률 차·개수 비. 예: g+p 대비 ip10 3단 rl 성공률 +0.58 [+0.44, +0.70], 개수 비 0.736 [0.578, 0.887]; pcb10 3단 rl −0.06 [−0.20, +0.08], 0.845 [0.738, 0.949].
- 결정: 사다리 seed 1·2 학습 8개를 GPU 큐 끝에 미리 넣음 (QUEUE 3번; GPU가 놀지 않게). 최종 후보 seed는 r3a/r2a 판정 뒤 추가.
- 다음 라운드: r3a distill `done:` → RL 진행·OOM → r3a 10칸 평가 (CPU 줄 최우선, ~05:30 이후 시작 예상) → 10칸 종류별 g+p 끝 (~05:30) → 종류 인식 greedy 표 확인 → r3 대비·종류 인식 greedy 대비 판정 → RESULTS.

## 라운드 19 (02:22~ UTC)
- 상태 정상: 드라이버 살아 있음 (16칸 r0 rl 평가 1 worker, RSS ~10 GB, 첫 기록 아직), side_evals 0단 rl 10칸 4/6, ip16_1 풀 3.3 h째, pod mem 21 GiB / 60, oom_kill 0.
- **ip g+p 실패 원인 확인 (기록된 occ, 학습 없음)** — `scripts/analyze_ip_swap.py` → `runs/analysis/ip_swap.json`: g+p 실패 30문제에서 **위치는 그대로 두고 모든 decap을 종류 0 (100 pF)으로 바꾸면 30/30 통과** (최악 중앙값 0.42 Zt), 종류 1·2로 바꾸면 0/30 (1.66, 4.57). 3단 rl 해(29개)도 모두 종류 1로 바꾸면 0/29, 종류 2로 0/29. → 실패는 위치가 아니라 **종류 선택** 때문. g+p 기록은 cutting-plane 0 round → g+p가 자기 작업 격자에서도 불가능으로 끝남 (격자 문제 아님).
- **g+p를 종류 0만 쓰게 하면** (`scripts/analyze_gp_one_type.py`, 같은 탐욕 규칙에 `only` 제한, 같은 cutting-plane·정확 검사; 분석용) ip10 50/50 성공, 개수 7.92 / 8.68 — **3단 rl과 같은 문제에서 개수 비 rl/종류0 = 1.03, 1.00**, 시간 0.44 / 0.14 s/문제. 즉 ip에서 "정책이 g+p보다 성공률이 높다"(0.98 vs 0.40)는 **g+p 기준선의 종류 선택 규칙(지금 최악점을 가장 많이 낮추는 소자)이 약해서**이고, 종류만 고정한 단순 규칙이 정책과 같은 수준. 보고서 주장 범위에 직접 영향 → 그림 2·3 해석에 반드시 적을 것.
- 결정: 이 단일 종류 g+p는 **분석용으로만** 기록 (`runs/analysis/`, RESULTS 별도 표) — 보고 기준선을 바꾸는 것(예: "종류별 g+p 중 최선"을 E0에 추가)은 사람 결정 → PROPOSALS (d). 지금은 pcb·pkg 10칸에도 종류 0·1·2 각각 돌려 ip만의 현상인지 확인 중 (`agent/logs/side10_base.log`, 1 process; pcb10_0 종류 0만으로 0.04 성공). 이어서 같은 칸에서 10칸 modal_rule·LS 기준선 평가 (드라이버 E0 순서에 있던 것, 같은 명령·같은 기록 파일).
- **10칸 rl 사다리 4단 모두 끝** (각 50문제, 성공률 / 개수÷g+p): ip 0단 1.00/1.05 · 1단 0.96/0.88 · 2단 1.00/0.74 · 3단 0.98/0.74; pcb 0.96/0.80 · 0.98/0.75 · 0.88/0.88 · 0.84/0.84; pkg 0.76/0.79 · 0.68/0.75 · 0.72/0.88 · 0.88/0.84. 성공률에 단조 추세 없음; ip 개수만 0→2단에서 줄어듦 (1.05 → 0.74). 0단도 ip 1.00 → ip의 높은 성공률은 사다리 구조와 무관 (위 종류 선택 분석과 맞음). side_evals는 3단 @R2/4/16 10칸 진행 중.
- **16칸 첫 rl 기록** (r0 rl `eval_pkg16_1`, 2202 s / 25문제, 성공 0.72, 개수 7.94, 18.97 s/문제): **`peak_rss_mb` 23087 — chunk 5로도 ~22 GB 그대로**. 정점은 정책 rollout이 아니라 job 안 다른 곳 (16칸 F 390 격자의 25문제 bank/격자 추가 쪽으로 추정, 확인 안 함; certify는 문제마다 256 MB 조각이라 아님). ps로는 대부분 ~10 GB, 정점은 잠깐.
- 결정: **W16 = 1 유지** — 23 GB × 2 + 풀/side 칸이면 45 GiB 한도를 넘을 수 있음 (QUEUE). 16칸 rl job ~37~95 min → rl 4단 × 6풀 ~1일 (계획용).
- 결정: 4번째 CPU 칸은 위 분석·10칸 기준선에 씀 (풀 1 + 드라이버 1 + side_evals 1 + 이것 1 = 4). 처음에 10칸 LS를 띄웠다가 분석 스크립트가 5번째가 되지 않도록 2분 만에 멈추고 한 줄(같은 칸)로 합침.

## 라운드 18 (02:03~ UTC)
- 상태 정상: 드라이버 살아 있음 (16칸 r0 rl 평가, 1 worker, chunk 5, 02:00 시작), pod mem 17 GiB / 60, oom_kill 0. side_evals: **1단 rl 10칸 끝** (02:04) → 0단 rl 10칸 중. side16_gp는 ip16_1 풀 대기.
- 10칸 rl 사다리 (RESULTS.md 재생성, 각 50문제, 성공률 / 개수÷g+p): 1단 ip 0.96/0.88 · pcb 0.98/0.75 · pkg 0.68/0.75, 2단 1.00/0.74 · 0.88/0.88 · 0.72/0.88, 3단 0.98/0.74 · 0.84/0.84 · 0.88/0.84. **단이 올라갈수록 좋아지는 단조 추세는 아님** (pkg 성공률만 1→3단 증가, pcb는 감소) — 0단·distill 기록 뒤 그림 3에서 판단.
- **그림 1 초안** `reports/fig1_board_draft_r3rl_side10.png` (3단 rl, 10칸 `_0` 파일 세 종류, `--pick median` = 성공 문제 중 개수 중앙값: pcb #4 7개 0.985, pkg #11 5개 0.793, ip #13 8개 0.990). `fig_board.py` 수정: 종류마다 decap 라이브러리가 달라 범례를 행마다 (전에는 PCB 값만 보여 pkg·ip 행이 틀린 값), 행 제목에 문제 번호·방법, 실패면 "(fails)", `--title`.
- **고찰 그림** `reports/fig_ip_gp_fail_ip10_0_13.png`: 같은 ip10_0 #13에서 g+p 74개 (대부분 5 pF) → 정확 검사 최악 1.703 Zt (실패), 3단 rl 100 pF 8개 → 0.990. 두 해 모두 맨판의 ~3.3 GHz 공진은 누르지만 ~1.2 GHz에 반공진 피크가 생김; g+p는 이 피크가 1.70, 정책은 0.99. 즉 g+p의 실패는 "판을 다 채워도 못 누르는 새 피크"이고, 원인(종류 선택 순서 vs 반공진 감쇠)은 아직 미확인 — 단정하지 않음.
- **ip g+p 실패 30문제 전체** (`scripts/analyze_ip_gp_fail.py` → `runs/analysis/ip_gp_fail.json`, RESULTS.md 새 표): g+p 최악점은 **30/30 모두 맨판 최악 공진보다 낮은 주파수** (비 중앙값 0.36, 0.28~0.45; 최악 중앙값 1.83 Zt) = decap이 만든 새 반공진. 같은 문제를 통과한 3단 rl(29개)과 **총 정전용량은 비슷** (g+p/정책 중앙값 0.95) → "용량 부족"이 아니라 구성(5 pF 다수 vs 100 pF 소수)의 차이. 정책 해도 최악점이 같은 대역(0.4~1.8 GHz)에 0.90~1.00으로 붙어 있는 경우가 많음 (겨우 통과). 감쇠(ESR)·배치 위치 중 무엇이 피크 높이를 정하는지는 아직 미확인.
- 결정: 그림은 기록된 occ로만 다시 계산 (학습·평가 조건 변경 없음, 10칸 100셀 1스레드 수 초). 그림 1 최종본은 16칸 기록이 생기면 같은 스크립트로.
- 02:19: 16칸 r0 rl 평가 worker (chunk 5) 18분째 RSS 9.4 GB, pod 19.5 GiB, 첫 기록 아직 없음 (16칸 정책 job ~1.4 h → ~03:30 예상). W16은 기록의 `peak_rss_mb`를 보고 정함 (그대로 1).
- 다음 라운드: r0 rl 16칸 첫 기록 `peak_rss_mb` < ~14 GB이면 `pipeline_day1.py`의 `W16 = 2` + 드라이버 재시작 (ATTACH) → side_evals 0단 rl 10칸 → RESULTS 재생성 (10칸 rl 사다리 4단 완성) → ip16_1 풀 완성·side16_gp 시작 확인 → 그림 3 10칸 초안 (`fig_results.py`).

## 라운드 17 (01:22~ UTC, 10/29 첫 라운드 → DAILY.md 작성)
- 상태 정상: 드라이버 살아 있음, pod mem 31 → 38.7 GiB / 60 (16칸 평가 worker 둘 10.3~11.0 GB), oom_kill 0. GPU 비어 있음.
- **10칸 3단 rl 평가 끝** (side_evals, 6 파일 150문제): 성공률 / 개수÷g+p — ip 0.98 / 0.74, pcb 0.84 / 0.84, pkg 0.88 / 0.84 (g+p: 0.40 / 0.90 / 0.90). ip에서 g+p 실패 30문제는 판 100칸 중 60~99개를 채우고도 실패 (최악 |Z| 1.2~3.6 Zt), 3단 rl은 그중 29개를 3~26개로 통과. 시간/문제 rl 0.44~3.09 s vs g+p 2.2~4.9 s (`runs/2026-10-28/r3_loop_rl/eval/`, `.../baselines/eval/`). 이어서 2단 rl 10칸 평가 중.
- **`collect_results.py` 버그 수정**: (종류, 크기)마다 방법 기록 하나만 남아 `_0` 파일이 `_1`로 덮였고 (표가 25문제), 한 방법이 `_0`만, g+p가 `_1`만 있으면 **다른 문제끼리** 개수 비를 짝지을 수 있었음. 이제 파일들을 합치고 짝은 같은 파일 안에서만, 표에 문제 수 표시. (g+p pcb10 성공률 0.80 → 0.90 = 두 파일 평균.)
- **드라이버 순서 변경** (01:36 재시작, r0 distill 평가·풀 생성 ATTACH): 16칸 정책 평가 1개가 75분 넘게 기록 0 → 단 평가는 16칸 풀만, **rl 4단 먼저 → distill → 3단 @R** (10칸은 side_evals가 함). 이전 드라이버의 2-worker 평가가 살아 있으면 끝날 때까지 기다림 (한도 4 유지). mock 실행으로 순서 확인.
- **`scripts/side16_gp.py`** (01:36 시작, `agent/logs/side16_gp.log`): 풀 생성(ip16_1, 마지막 1 worker)이 끝나면 그 칸에서 16칸 g+p → modal_rule, 1 worker. 이유: g+p는 개수 비의 기준인데 드라이버 순서로는 16칸 g+p가 하루 넘게 뒤에 있었음.
- 결정: 순서만 바꿈, 실험 조건 그대로 (같은 eval_policy·풀·rounds·1스레드). 돌던 r0 distill 16칸 평가는 75분 진행분을 버리지 않으려고 그대로 둠 (끝까지 ~수 시간).
- DAILY.md 첫 작성 (10/29).
- **ip에서 g+p가 실패하는 이유 (기록된 occ, 학습 없음)**: `collect_results.py`에 decap 종류 비율 표 추가. ip 10칸 g+p 실패 30문제는 평균 78.6개, 그중 0.90이 종류 2 (5 pF / 1 pH / 0.2 Ω, ESL 가장 작음); 3단 rl 성공 49문제는 평균 8.4개, 0.99가 종류 0 (100 pF / 5 pH). 탐욕 규칙이 지금 최악 주파수를 가장 많이 낮추는 ESL 최소 소자를 계속 고르다 판을 채움 → 보고서 고찰 후보 (RESULTS.md "decap 종류 비율").
- 2단 rl 10칸 첫 기록: pkg10_1 성공 0.60 (3단 0.88, g+p 0.88).
- **첫 16칸 정책 기록** (01:47): r0 distill `eval_pcb16_0` 5183 s / 25문제, 성공 0.80, 개수 38.1 (풀 생성 때 g+p 10.8), 마지막 라운드 방법 시간 55.9 s/문제 (1스레드). 계획용: 16칸 정책 job 1개 ~1.4 h → 드라이버의 16칸 단 평가 (8단계 × 6풀 + @R 3 × 6풀) 2 workers로 ~2일. 마감(11/8) 안이지만 20칸은 그 뒤 → 20칸 범위는 사람 결정 (PROPOSALS (c)).
- r0 distill 16칸 두 번째 기록: `eval_pkg16_1` 5703 s, 성공 0.80, 개수 31.15.
- **메모리 사고 (OOM 직전)**: 01:48 pod mem **51.6 GiB / 60** (anon 55 GB). 16칸 정책 평가 worker가 job 하나 안에서 ~10 → **22 GB**까지 커짐 (25문제를 한 rollout에), 둘이 동시에 정점이면 44 GB + 풀 생성 6 GB + side 3 GB. 조치: 드라이버 정지 → r0 distill 평가 정지 (기록 2개 저장 직후, 새 job 둘은 ~8분·1분 진행분 버림) → `eval_policy.py` 수정: (1) `--inst_chunk N` (정책 greedy rollout을 N문제씩), (2) `Pool(maxtasksperchild=1)` (job마다 새 프로세스 → 정점 메모리가 다음 job에 남지 않음), (3) 기록에 `peak_rss_mb`, `inst_chunk`. **동치 확인**: 3단 rl `eval_pkg10_1`을 chunk 5로 다시 → ok·count·worst·occ·rounds·F 모두 기존 기록과 같음 (`runs/chunk_equiv/equiv_check/`, peak 4.5 GB). 드라이버 02:00 재시작: 16칸 단 평가 `--inst_chunk 5`, **1 worker** (`W16`). 02:01 pod mem 10.4 GiB.
- 결정: 16칸 정책 평가는 1 worker로 시작 — chunk 5의 16칸 정점은 아직 모름. 첫 기록의 `peak_rss_mb`가 ~14 GB 아래면 다음 라운드에 `W16 = 2`. 그동안 CPU 칸은 3개만 씀 (드라이버 1 + side_evals 1 + 풀 생성/side16_gp 1).
- **관찰: 시간 측정이 부하에 따라 흔들림** — 같은 정책·같은 풀·같은 해인데 문제당 3.09 s (01:17, CPU 4개 바쁨) vs 1.23 s (01:57). 그림 2의 시간은 지금 기록(평가 중 다른 프로세스와 같이 돈 것)을 그대로 쓰면 안 됨 → 평가가 끝난 뒤 조용한 상태에서 같은 조건으로 따로 시간만 재는 단계가 필요 (계획에 추가, 실험 조건 변경 아님).
- 다음 라운드: r0 rl 16칸 첫 기록의 `peak_rss_mb` → W16 2로 올릴지 결정 → side_evals 2·1·0단 rl 10칸 기록 → RESULTS 재생성 → 첫 16칸 정책 기록 시간·ip16_1 풀 완성·side16_gp 시작 확인 → ip g+p 실패 원인 분석 (기록된 occ, 학습 없음) → 그림 1 초안.

## 라운드 16 (23:30~01:20 UTC)
- 상태 정상: 드라이버 살아 있음, pod mem 13.4 → 26.3 GiB / 60, oom_kill 0.
- **r3 (3단 loop) RL 끝** (00:19): 352 iter / 1.27 h, best iter 100 (val score 1.679), cuda_oom_skipped 0, chunk 2, gpu peak 17.1 GB, 선생님 교체 296, λ 1.42, grid capped 151 step (`runs/2026-10-28/r3_loop_rl/metrics.json`). 최종 val (보고서용 아님): pcb 0.99/fail 0.81, pkg 1.00/0.50, ip 0.69/0.19 → best는 iter 100. **사다리 0~3단 학습 모두 끝** (모두 distill 0.75 h + RL 1.25 h, 같은 인자).
- RL best val score (낮을수록 좋음, val 16문제라 잡음 큼, 보고서용 아님): 0단 1.999 → 1단 1.737 → 2단 1.691 → 3단 1.679.
- eval 풀: `eval_ip16_0` 9187 s, `eval_ip10_1` 305 s 완성. 남은 것 `eval_ip16_1` 하나 (worker 1개).
- 드라이버 early evals 시작 (00:20): r0 distill부터 이미 만든 풀 11개, 2 workers. 16칸 정책 평가 1개가 30분 넘게 걸림 (00:49에 아직 기록 0) → 드라이버 순서(정책마다 16칸 먼저)로는 10칸 사다리 표가 오래 비어 있음.
- **4번째 CPU 칸 사용** (`scripts/side_evals.py`, 00:40~, `agent/logs/side_evals.log`): 10칸 eval 6개에 greedy+prune → 0~3단 rl → 3단 @R2/4/16 → 0~3단 distill 순서, 1 worker. 같은 `eval_policy.py`·같은 기록 파일이라 드라이버는 이미 있는 기록을 건너뜀. 첫 기록: `eval_pkg10_1` greedy+prune 513 s (ok 0.88).
- 결정: 4번째 칸은 평가에만 씀 (풀 1 + 드라이버 평가 2 + side 1 = 4, QUEUE 한도 그대로; 20칸 풀 생성이 시작되면 side는 멈춤). 실험 조건은 안 바꿈. GPU는 비어 있지만 학습에 필요한 CPU 검사 칸(2개)이 없어 새 학습은 안 띄움. 정책 평가는 CPU 1스레드 그대로 (그림 2 시간 비교 조건 "같은 계산기").
- 01:17 side: 10칸 greedy+prune 6개 끝 (2168 s, `runs/2026-10-28/baselines/eval/`; 정확 검사 ok pcb 1.00·0.80 / pkg 0.92·0.88 / ip 0.40·0.40 — ip는 cutting-plane 0 round, 풀 생성 때 g+p ok와 같음). 이어서 3단 rl 10칸 평가 중. pod mem 최고 35.2 GiB (16칸 평가 worker 둘이 커짐), oom_kill 0.
- 드라이버 16칸 정책 평가 (r0 distill): 01:20에 60분째 기록 0 → 16칸은 정책 1개 × 풀 6개가 몇 시간 단위. 11개 정책이면 16칸 단 평가만 하루 이상일 수 있음 (계획용 관찰, 숫자는 첫 기록 뒤 다시 계산).
- 다음 라운드: 첫 16칸 정책 평가 시간 기록 → 그걸로 16칸 남은 시간 계산, 너무 길면 16칸은 rl 4개 먼저 (distill·@R은 뒤로) 순서만 바꾸는 것 검토 → 10칸 사다리 RESULTS.md → 05:30 무렵 첫 DAILY.md.

## 라운드 15 (23:25 UTC~, 라운드 14 직후라 짧음)
- 상태 정상: 드라이버 살아 있음, pod mem 11.7 GiB / 60, oom_kill 0. GPU 18.6 GB (r3 RL).
- r3 (3단 loop) RL iter 100: OOM 0, gpu peak 14.7 GB, grid capped 7, resume.pt iter 93. iter 100 val (보고서용 아님): pcb 0.99/fail 0.44, pkg 0.98/0.62, ip 0.69/0.12, val score 1.679 (new best; 0~2단 RL best 1.999 / 1.737 / 1.691보다 낮음, val 16문제라 잡음 큼) (`runs/2026-10-28/r3_loop_rl/log.txt`).
- **드라이버 CPU 줄 수정** (`scripts/pipeline_day1.py`): r3 RL이 끝나면 (~00:25) GPU 줄의 certify 2개가 비는데, 옛 순서는 ip16 ×2·ip10_1 풀이 다 끝날 때(~05시 예상)까지 아무 평가도 안 해서 CPU 2칸이 ~4.5 h 놀았음. 이제 풀 생성은 별도 스레드로 두고, **모든 단 학습이 끝나면 이미 만든 eval 풀 9개**(pcb·pkg 10/16 각 2, ip10_0)에서 단 평가 (r0~r3 distill·rl, r3 @R2/4/16) → E0 gp/modal_rule을 먼저 돌림. 평가 기록은 파일이 있으면 건너뛰므로 뒤의 원래 순서는 남은 풀만 채움. 동시 CPU 프로세스는 풀 2 + 평가 2 = 4 (QUEUE 한도 그대로). `eval_policy.py --sets`는 쉼표로 여러 glob 허용. mock 실행으로 순서 확인, 드라이버 23:27 재시작 (풀 생성·r3 학습 ATTACH, 끊김 없음).
- 결정: 평가 순서만 앞당김 — 실험 조건(풀·검사·rounds·workers)은 그대로라 보수적 변경. 풀 파일은 .json이 써진 것만 (build_pools가 .pkl 다음에 씀) 골라 반쯤 쓴 풀을 읽지 않음.
- 관찰 (계획용, 보고서 숫자 아님): eval 풀 생성 시간(cutting-plane 안 g+p, 16칸 2.8~5.1 h/풀)으로 보면 16칸 E0 gp·LS는 풀마다 몇 시간씩 걸림 → 16칸 E0 전체가 10/29 하루 이상 걸릴 수 있음. 정책 평가는 롤아웃이 싸서 훨씬 빠를 것 (val 48문제가 학습 중 수십 초) → 단 평가를 E0보다 먼저 둔 이유.
- 다음 라운드: r3 RL `done:`(~00:25)·`cuda_oom_skipped` → 드라이버 로그에 `early evals while pools build` 시작 확인 → 첫 단 평가 기록 → RESULTS.md 평가 표 → 10/29 05:30 무렵 첫 DAILY.md.

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
