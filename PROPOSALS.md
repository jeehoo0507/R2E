# PROPOSALS (에이전트 제안 — 실행 금지, 사람 승인 후 큐로)

## 확인 필요 (서지)
- Manoharan, Wang, Hwang, "RL for Decap Optimization in Postlayout PDNs Using Transformer Architecture", IEEE TSIPI 2026 / Scholars' Mine 3459 — 전문·권호 미확인.
- Park & Sengupta, "Neural Modal Decomposition", arXiv 2609.14402 — 학회 게재 여부 미확인 (설계서에는 NeurIPS 2026 포스터로 적혀 있음).
- Fan et al., "Looped Transformers for Length Generalization", ICLR 2025 — 저자·학회 확인 필요.
- `reports/최종 모델 설계.md`가 인용한 "Kuo 2026" (반복 횟수 랜덤 학습) — 출처 불명.

## 환경 파일 수정이 필요한 문제 (사람 결정)
- `verify._probe_z_exact`의 배치 복소 solve가 이 서버(torch 2.14+cu130, MKL)에서 n ≥ 200 셀·스레드 ≥ 2이면 멈춘다 (`scripts/mkl_repro.py`). 지금은 `decap_loop/safe_verify.py`로 프로세스당 1스레드로 우회. 근본 수정은 `verify.py`에서 `torch.linalg.solve`를 주파수별 루프 또는 `scipy.linalg.lu_solve`로 바꾸는 것.

## 해보고 싶은 것 (오늘은 안 함)
- 선생님 LS를 cutting-plane 안에서 실행 (`make_teacher.py`가 지금은 g+p용으로 인증된 격자에서 LS 1회 → LS 해의 정확 검사 통과율 0.00~0.81, 선생님이 대부분 g+p로 떨어짐; `agent/logs/make_teacher.log`). eval의 `local_search`처럼 격자를 키우며 재실행하면 "LS 선생님"이 실제로 LS가 된다. 오늘 0·1·2단은 지금 선생님으로 같은 조건이라 비교는 유효; 바꾸면 사다리 전체 재학습 필요.
- 1단 modal 특징에 잔여 인덕턴스(rational fit의 s·e 항) 추가 — 데이터 분석에서 전이는 되지만 약함(AUC 0.60→0.65)이라 첫날은 생략.
- `--feat modal_only`(좌표 제거) ablation — "좌표가 해로운가"를 분리해서 보는 비교. 코드는 있음.
- 종류별 검사 대역(PCB 10 MHz~5 GHz, IP 200 MHz~20 GHz) — 지금은 셋 다 기본 대역. 대역을 바꾸면 PCB 10칸 공진이 대역 밖으로 나가므로 보류.
