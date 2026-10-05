# 📊 네이버 인플루언서 공연·전시·예술 키워드 대시보드

네이버 인플루언서 공식 참여 키워드 1,486개 및 10월 추천 TOP 100, 7,430개 롱테일 상세 키워드 후보를 실시간으로 검색하고 분석할 수 있는 웹 애플리케이션입니다.

🔗 **웹 바로가기 (배포 주소)**: [https://sigong-photo.github.io/keyword-dashboard/](https://sigong-photo.github.io/keyword-dashboard/)

![Platform](https://img.shields.io/badge/Platform-Web%20%2F%20GitHub%20Pages-blue)
![Data](https://img.shields.io/badge/Keywords-1%2C486%2B-orange)
![Sheets](https://img.shields.io/badge/Sheets-10-success)

---

## ✨ 주요 기능

- **10개 분석 시트 전체 지원**:
  - `지금TOP100`: 10월 우선 작성 추천 키워드 및 상세 검색어 후보
  - `전체키워드`: 공연·전시·예술 전체 참여 키워드 목록
  - `키워드분석`: 기본 기획점수, 10월 작성점수, 콘텐츠 방향, 주의사항
  - `상세키워드추천`: 7,430개 롱테일 확장 키워드 후보
  - `월별캘린더`: 1월 ~ 12월 시즌별 작성 로드맵 및 작성 단계
  - `월별점수`, `키워드복사용`, `일정출처`, `분석안내`, `수집정보`
- **고속 실시간 검색 & 정렬**:
  - 키워드, ID, 카테고리 등 전체 텍스트 실시간 필터링
  - 컬럼별 클릭 오름차순/내림차순 정렬 및 페이지네이션
  - 보고 싶은 컬럼만 켜고 끄는 열 선택 필터
- **1-클릭 키워드 복사 & CSV 내보내기**:
  - 키워드 클릭 시 클립보드로 즉시 복사
  - 현재 필터링된 결과 그대로 UTF-8 BOM 인코딩 엑셀용 CSV 다운로드
- **서버리스 동작**:
  - GitHub Pages를 통한 100% 클라이언트 사이드 고속 로딩
  - 모바일, 태블릿, PC 완벽 반응형 인터페이스

---

## 💻 로컬 실행 방법

브라우저에서 `index.html`을 바로 열거나 로컬 웹 서버로 실행할 수 있습니다:

```bash
cd keyword
python3 -m http.server 8000
```
브라우저에서 `http://localhost:8000` 접속
