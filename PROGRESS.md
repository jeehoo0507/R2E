# PROGRESS (갱신 2026-10-28 12:25 UTC, 라운드 2)

- 사고: 06:41경 서버 재시작으로 라운드 1의 풀 생성이 죽음 (48개 중 eval_pcb10_0/1, eval_pkg10_0 3개만 완성; 3개 g+p 인증 0.92/0.76/0.88). 라운드 1 종료 기록 없음.
- 돌고 있는 것 (모두 `scripts/bg.py`로 세션 분리 → 라운드가 끝나도 계속): ① 풀 재생성 `agent/logs/build_pools_v1_r2.log` (train·val 30개 먼저, 그다음 eval 15개; 기존 파일은 건너뜀) ② 드라이버 `scripts/pipeline_day1.py` → `agent/logs/pipeline_day1.log`: train/val 완료 대기 → 선생님(LS) → 0단 coord·1단 modal 동시 학습(증류 0.75h + RL 1.25h) → eval 풀 대기 → E0(g+p, LS, modal 규칙) → 0·1단 인증 평가 → 2단 mott → `collect_results.py`.
- 끝난 것: 라운드 1 코드 전부(스모크 통과, `agent/logs/smoke_pipeline.log`). 아직 보고 가능한 숫자 없음.
- 다음 라운드: `pipeline_day1.log`·`make_teacher.log` 확인, 선생님 통계(LS/g+p) 기록, 학습 로그(`runs/2026-10-28/r*_*/log.txt`) 중간 val 기록, eval 풀이 끝나면 E0 결과 RESULTS.md.
- 결정: 백그라운드 작업은 `scripts/bg.py`(python `start_new_session`)로 띄움 — 허용 도구에 nohup/setsid가 없고, 라운드 1처럼 세션과 함께 죽으면 안 되기 때문.
- 결정: 풀은 train·val 먼저, eval 나중 — 학습이 eval 20×20(가장 느림)을 기다리지 않게. 풀 내용·시드는 그대로라 재현성 불변.
- 결정: 0·1단은 같은 시간 예산으로 GPU 동시 학습(같은 모델 크기·인자, `CERTIFY_WORKERS=6` 동일), 반복 수는 로그에서 확인해 기록. 2단은 GPU 경쟁을 피하려 0·1단 뒤에.
- 결정 (라운드 1에서 유지): 1단 = 좌표 + modal 특징, 정확 검사는 프로세스당 1스레드, 2단은 기존 `MoTT`, IP 난이도 EASY / PCB·PKG HARD.
