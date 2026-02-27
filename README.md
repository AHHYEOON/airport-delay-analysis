# 전국 공항 기상 지연 데이터 대시보드 (Data Dashboard)

## 프로젝트 소개
공공데이터를 활용하여 전국 공항별 기상 지연 횟수를 분석하고, 이를 한눈에 볼 수 있도록 시각화한 웹 대시보드입니다.
로컬 환경의 CSV 데이터를 SQLite 데이터베이스로 구축하고, Streamlit을 활용해 클라우드 환경에 배포하는 전체 데이터 파이프라인을 직접 구현했습니다.

**배포 링크:** [https://airport-delay-analysis-wasdezrffwi3n39ksxcx3g.streamlit.app/]

## 기술 스택 (Tech Stack)
* **Language:** Python
* **Data Processing:** Pandas
* **Database:** SQLite3
* **Web/Visualization:** Streamlit, Altair
* **Deployment:** Streamlit Community Cloud

## 시스템 아키텍처 및 파이프라인
1. **데이터 전처리:** 'airport_delay_clean.csv' 파일 정제 및 그룹화 로직 구현 ('groupby', 'sort_values')
2. **DB 적재:** Pandas DataFrame을 내장 데이터베이스인 SQLite3('airport_data.db')로 이관하여 데이터 영속성 확보
3. **대시보드 시각화:** 파이썬 환경에서 SQL 쿼리('SELECT')를 호출하여 데이터를 추출하고, Streamlit을 통해 막대그래프 및 데이터프레임 시각화
4. **클라우드 배포:** GitHub와 Streamlit Cloud을 연동하여 CI/CD 및 글로벌 웹 배포

## 트러블슈팅
클라우드 배포 과정에서 발생한 심각한 **의존성 충돌(Dependency Hell)** 문제들을 디버깅하고 해결했습니다.

**1. Python 버전 호환성 문제 (`imghdr` ModuleNotFoundError)**
* **문제:** Streamlit Cloud의 기본 환경이 Python 3.13으로 업데이트되면서, 기존에 사용되던 내장 모듈인 `imghdr`이 삭제되어 앱이 크래시 됨.
* **해결:** 배포 환경의 Advanced Settings에서 Python 버전을 안정적인 `3.12`로 명시적으로 다운그레이드하여 호환성 문제 해결.

**2. PyArrow & NumPy 2.0 엔진 충돌 (`LargeUtf8` Error)**
* **문제:** 최신 PyArrow의 `LargeUtf8` 스키마를 구버전 Streamlit이 인식하지 못해 데이터프레임 렌더링에 실패함. 
* **해결:** `requirements.txt`에서 하위 패키지(altair, numpy 등)의 버전을 개별적으로 내리는 대신, **`streamlit>=1.32.0`**으로 상위 프레임워크 자체를 최신 버전으로 강제 업그레이드하는 정면 돌파 방식을 선택하여 깔끔하게 의존성 트리 충돌을 해결함

## 실행 방법 (Local Run)
```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. 대시보드 실행
streamlit run day3_dashboard.py