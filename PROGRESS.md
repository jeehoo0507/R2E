# PROGRESS (갱신 2026-10-28 05:45 UTC, 라운드 1, 첫날)

- 환경: RTX A5000 24GB ×1, 16 CPU, torch 2.14 cu130. `sanity_check.py` 통과, `smoke_mott.py --device cuda` 통과 (로그 `agent/logs/`).
- 돌고 있는 것: `scripts/probe_techs.py` (세 종류 × 난이도 × 크기에서 greedy+prune 성공률·개수 점검 → 난이도 확정용).
- 끝난 것: `decap_loop/techs.py` (PCB/PKG/IP 세 종류 PDNConfig, 환경 파일 미수정).
- 다음 4시간: 문제 은행(학습 8/10/12칸 ×3종류, 평가 10/16/20칸 ×3종류 ×50문제, 검증 10칸 ×3종류 ×16) 병렬 생성 → E0 기준선(greedy+prune, LS) → `--feat modal`(1단) 구현 → 0단·1단 2h 학습 동시 시작.
- 결정: 2단은 `decap_loop/model.py`의 기존 `MoTT`를 그대로 쓴다 (새 `mott.py`를 만들지 않음) — 이미 설계서 §3과 같은 구조가 구현·스모크 통과 상태라 재구현은 낭비.
- 결정: 검사 대역은 세 종류 모두 기본값(10 MHz~20 GHz)으로 둔다 — 기존 설정 유지; 대역을 바꾸면 PCB 10칸 판의 공진이 대역 밖으로 나가 모달 특징이 비게 됨.
- 결정: 학습 설정은 `run_mott.sh`의 COMMON(d128, 4층, 8 heads, B16, M8, lr 3e-4)을 사다리 전 단에 동일 적용 — 기존 설정 유지.
