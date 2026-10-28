# PROGRESS (갱신 2026-10-28 06:35 UTC, 라운드 1, 첫날)

- 돌고 있는 것: `scripts/build_pools.py` → `runs/pool_v1/` (48 파일: 학습 8/10/12칸 ×3종류 ×3, 검증 10칸 ×3, 평가 10/16/20칸 ×3종류 ×50문제; 14 프로세스, 06:04 시작, 20×20 평가 파일이 가장 느림 ≈ 40~60분 예상).
- 끝난 것: 환경 확인(sanity·smoke 통과) / `decap_loop/techs.py` 세 종류 / `safe_verify.py`(MKL 멈춤 우회) / 1단 `--feat modal`(`modal_env.py`, 단위 검사 통과) / 3단 `loop_model.py`(단위 검사 통과) / 3단계 방법론(증류→RL+expert iteration) `train.py` / `scripts/make_teacher.py`, `eval_policy.py`, `collect_results.py`, `run_rung.py` / 전체 파이프라인 스모크 `scripts/smoke_pipeline.py` 통과(로그 `agent/logs/smoke_pipeline.log`).
- 다음 4시간: 풀 완료 → `make_teacher.py`(g+p→LS, 정확 검사) → E0 기준선(g+p, LS) 평가 → 0단(coord)·1단(modal) `run_rung.py` 동시 시작(증류 0.75h + RL 1.25h) → 2단(mott).
- 결정: 1단 = 0단 좌표 입력 + 공진 참여 포트 특징 + 정확한 1수 효과 (좌표 유지) — 사다리가 "한 단씩 쌓기"라 한 번에 하나만 바꾸기 위해. 좌표를 뺀 `modal_only`는 ablation으로 코드만 둠.
- 결정: 모든 CPU 정확 검사는 프로세스당 torch 1스레드 — 이 서버의 MKL이 n≥200·스레드≥2 배치 복소 solve에서 멈춤(`scripts/mkl_repro.py`). 환경 파일은 수정하지 않음(PROPOSALS.md).
- 결정: 2단은 기존 `model.py`의 `MoTT` 그대로 사용(재구현 안 함). 검사 대역은 세 종류 모두 기본값. 학습 설정은 `run_mott.sh` COMMON(d128·4층·8heads·B16·M8·lr3e-4)을 전 단 공통.
- 결정: IP 종류 난이도 EASY(0.2~0.5), PCB/PKG HARD(0.02~0.2) — probe에서 IP HARD는 greedy가 10칸 25%, 16칸 0% 성공(`agent/logs/probe_techs.log`).
