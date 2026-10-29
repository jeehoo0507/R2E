# PROPOSALS (에이전트 제안 — 실행 금지, 사람 승인 후 큐로)

## 확인 필요 (서지)
- Manoharan, Wang, Hwang, "RL for Decap Optimization in Postlayout PDNs Using Transformer Architecture", IEEE TSIPI 2026 / Scholars' Mine 3459 — 전문·권호 미확인.
- Park & Sengupta, "Neural Modal Decomposition", arXiv 2609.14402 — 학회 게재 여부 미확인 (설계서에는 NeurIPS 2026 포스터로 적혀 있음).
- Fan et al., "Looped Transformers for Length Generalization", ICLR 2025 — 저자·학회 확인 필요.
- `reports/최종 모델 설계.md`가 인용한 "Kuo 2026" (반복 횟수 랜덤 학습) — 출처 불명.

## 환경 파일 수정이 필요한 문제 (사람 결정)
- `verify._probe_z_exact`의 배치 복소 solve가 이 서버(torch 2.14+cu130, MKL)에서 n ≥ 200 셀·스레드 ≥ 2이면 멈춘다 (`scripts/mkl_repro.py`). 지금은 `decap_loop/safe_verify.py`로 프로세스당 1스레드로 우회. 근본 수정은 `verify.py`에서 `torch.linalg.solve`를 주파수별 루프 또는 `scipy.linalg.lu_solve`로 바꾸는 것.

## 사람 결정이 필요한 것 (QUEUE 한도·평가 세트)
- **16·20칸 eval 풀 생성 시간 (2026-10-28 18:30 측정):** 풀 1개(25문제)를 1스레드로 만드는 시간이 판 변의 ~6제곱으로 늘어남 (풀 json `t_total`: pcb 학습 풀 8칸 ~12 s/문제, 10칸 ~54, 12칸 ~150; eval 10칸 25~104 s/문제). 16칸 6개는 18:20 기준 3시간째 첫 2개가 안 끝남. 이 비율이면 16칸 1개 ~6~9 h → 6개를 2 workers로 ~18~27 h, 20칸 1개 ~30 h 이상 → 6개 ~90 h. 지금 드라이버는 10·16칸 풀이 다 끝나야 E0·단 평가를 시작하므로 10칸 단 평가도 10/29 낮까지 밀린다. 선택지 (에이전트는 QUEUE 한도 4를 지키려고 아무것도 바꾸지 않음):
  (a) CPU 프로세스 한도를 6으로 올려 10칸 평가를 16칸 풀과 동시에 (지금 pod 메모리 ~10~21 GiB / 60, 16칸 풀 worker 하나 3~9 GB),
  (b) 16칸 풀 1개를 멈추고 그 자리에서 10칸 평가 먼저 (멈춘 풀의 진행분은 버려짐),
  (c) 20칸 eval을 파일당 25 → 8문제로 줄이기 (평가 세트 변경이라 사람 승인 필요; 아직 아무 방법도 20칸에서 평가되지 않았으므로 결과를 보고 고르는 문제는 없음).
  - **갱신 (18:55 측정):** 위 추정은 너무 비관적이었음. 실제 `eval_pcb16_0` 9941 s, `eval_pcb16_1` 10392 s (398·416 s/문제, pcb 10칸의 ~7배 → 변 길이의 ~4제곱). 남은 것: pkg16 ×2 (18:00·18:08 시작), ip16 ×2, ip10_1. ip 10칸이 pcb 10칸보다 문제당 ~2배 느려서 ip16이 가장 늦음 → 10·16칸 풀 전체는 10/29 새벽 끝 예상 (계획용 추정, 보고서 숫자 아님). 20칸은 같은 4제곱이면 pcb 풀 1개 ~7 h, 6개 2 workers로 ~1일. (a)(b)(c)는 여전히 사람 결정 사항이지만 급하지는 않음.

- **(d) 기준선 강화: "종류 하나만 쓰는 greedy+prune 중 최선"을 E0에 추가할지 (10/29 02:45).** ip 10칸에서 g+p는 성공 0.40인데, 같은 규칙을 100 pF 종류만 쓰게 하면 50/50 성공·개수가 3단 rl과 같음 (비 1.00~1.03, RESULTS.md "한 종류만" 표, `scripts/analyze_gp_one_type.py`). 지금의 "정책이 ip에서 g+p를 크게 이긴다"는 기준선 규칙의 약점에 기대고 있음. 선택지: (i) 지금 기준선 유지 + 고찰에 이 분석을 적기 (에이전트가 지금 하는 것), (ii) E0에 "종류별 g+p 3번 중 최선(성공 → 개수)"을 새 기준선으로 추가 (10·16칸, 정책 평가는 다시 안 해도 됨 — 같은 풀·같은 검사라 표만 늘어남; 16칸은 1회 수 시간 × 3종류 × 6풀). 평가 세트·검사는 안 바뀜.

- **(e) 외부 데이터 검증 (QUEUE 10/29 03:30 B) — 포기 (10/29 03:40, ~15분 사용).** `github.com/ai4co/devformer` (v1.0.1) shallow clone → `/home/coder/ext_devformer/` (저장소 밖, 코드는 실행 안 함; `.npy`만 `allow_pickle=False`로 읽음, `scripts/ext_devformer_inspect.py`). 확인한 것:
  1. 데이터 = **고정 Z 행렬 하나** `10x10_pkg_chip.npy` [201 주파수 × 100 × 100] complex (100 MHz~20 GHz 표, 대칭), 문제 100개 (`test.npz`)는 탐침 1개 + keep-out mask만 다름. **목표 임피던스 없음** (보상 = 정해진 K개로 Σ(|Z0|−|Z|)·1e9/f).
  2. **공개 체크포인트가 저장소에 없음** (README의 `data/dpp/pretrained/CSE_2000_epoch-50.pt`는 Google Drive zip; 쓰려면 그 저장소 코드와 pickle `torch.load`를 실행해야 함).
  3. decap = **한 종류, R+C만** (0.1436 Ω, 0.1 nF, ESL 0 → SRF 없음), 그리고 시뮬레이터가 `np.abs(decap)` (실수)를 decap 임피던스로 씀 → 우리 물리(복소 R+L+C)와 다름.
  - 안 맞는 이유: (i) 우리 성공 판정은 `verify.py` 700점 정확 검사 (격자 Laplacian으로 임의 f에서 Y(f)를 다시 풂) — 201점 표 Z에서는 돌릴 수 없음 → 새 판정이 필요하고 그건 규칙 2 밖. (ii) 정책 입력 차원이 T=3 종류에 묶여 있음 (`sim.feat_dim`, techs.py "All kinds keep T = 3") → 종류 1개 판은 가짜 종류 채우기 필요. (iii) ESL 0이면 `--fc_bias`의 log SRF가 정의되지 않음. (iv) 목표 Zt를 우리가 정해야 함 (Manoharan 4.2절은 0.5 Ω).
  - 사람이 원하면 필요한 것: 표 Z 어댑터 (bank를 201점 Z에서 직접) + 201점 판정 (보고서에 "DevFormer 판정 기준"으로 따로 표기) + Zt 선택 + 종류 패딩 규칙 + Drive 체크포인트 다운로드·실행 허가. 2일 이상 걸릴 것으로 보고, 마감(11/8 동결) 안에서 사다리·아키텍처 실험보다 뒤.

## 2일차 아키텍처 개선 — 노벨티 2줄 메모 (QUEUE 10/29 03:45, 판정은 사람)
- **(a) `--fc_bias` (r3a 10/29 03:10, 이어서 r2a):** 가장 가까운 선행: MatNet 2021 (두 집합 사이 행렬을 attention 편향으로), Manoharan 2026 (decap ESL·ESR·C 토큰). / 다른 점: 편향이 **공진 모드 k와 decap 종류 t 사이의 주파수 궁합** −|log f_k − log SRF_t|/τ_h이고 모드는 매 수 갱신되는 loaded 판의 피크 → 종류 선택을 규칙 없이 공진 상태에 연결.
- (b)는 QUEUE 03:15 수정으로 삭제 (이미 MoTT add head [u, c, u⊙c]에 있음).
- B-Park (`baselines_ml/park_am.py`)는 기준선이라 노벨티 아님.

## 해보고 싶은 것 (오늘은 안 함)
- 선생님 LS를 cutting-plane 안에서 실행 (`make_teacher.py`가 지금은 g+p용으로 인증된 격자에서 LS 1회 → LS 해의 정확 검사 통과율 0.00~0.81, 선생님이 대부분 g+p로 떨어짐; `agent/logs/make_teacher.log`). eval의 `local_search`처럼 격자를 키우며 재실행하면 "LS 선생님"이 실제로 LS가 된다. 오늘 0·1·2단은 지금 선생님으로 같은 조건이라 비교는 유효; 바꾸면 사다리 전체 재학습 필요.
- 1단 modal 특징에 잔여 인덕턴스(rational fit의 s·e 항) 추가 — 데이터 분석에서 전이는 되지만 약함(AUC 0.60→0.65)이라 첫날은 생략.
- `--feat modal_only`(좌표 제거) ablation — "좌표가 해로운가"를 분리해서 보는 비교. 코드는 있음.
- 종류별 검사 대역(PCB 10 MHz~5 GHz, IP 200 MHz~20 GHz) — 지금은 셋 다 기본 대역. 대역을 바꾸면 PCB 10칸 공진이 대역 밖으로 나가므로 보류.
