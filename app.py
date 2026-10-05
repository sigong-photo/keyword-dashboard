import os
import unicodedata
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="네이버 인플루언서 키워드 대시보드",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def find_excel_file():
    files = [f for f in os.listdir(BASE_DIR) if f.endswith('.xlsx')]
    # 1. 파일명에 '네이버'나 '인플루언서'가 포함된 엑셀 파일 우선 탐색
    for f in files:
        normalized = unicodedata.normalize('NFC', f)
        if '네이버' in normalized or '인플루언서' in normalized:
            return os.path.join(BASE_DIR, f)
    # 2. 첫 번째 xlsx 파일
    if files:
        return os.path.join(BASE_DIR, files[0])
    return None

EXCEL_FILE = find_excel_file()

if not EXCEL_FILE or not os.path.exists(EXCEL_FILE):
    st.error("엑셀 파일을 찾을 수 없습니다. keyword 폴더에 .xlsx 파일이 있는지 확인해주세요.")
    st.stop()

@st.cache_data
def load_all_sheets(filepath):
    xl = pd.ExcelFile(filepath)
    sheets = {}
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        # pyarrow 호환성: object 타입 컬럼의 혼합 데이터(문자열+숫자 등)를 문자열로 정규화
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].apply(lambda x: '' if pd.isna(x) else str(x))
        sheets[sheet] = df
    return sheets

with st.spinner("엑셀 데이터를 불러오는 중입니다..."):
    data = load_all_sheets(EXCEL_FILE)

# 사이드바 시트 선택 및 필터
st.sidebar.title("📊 데이터 탐색기")
st.sidebar.caption(f"📁 파일: {os.path.basename(EXCEL_FILE)}")

sheet_list = list(data.keys())
selected_sheet = st.sidebar.selectbox("열람할 시트 선택", sheet_list)
df = data[selected_sheet].copy()

st.title(f"시트: {selected_sheet}")
st.caption(f"전체 행: {len(df):,}개 | 컬럼: {len(df.columns)}개")

# 전역 키워드 검색
search_query = st.text_input("🔍 테이블 내 텍스트 검색", placeholder="검색할 단어를 입력하세요 (예: 전시, 서울, 10월 등)...")
if search_query:
    mask = df.astype(str).apply(lambda row: row.str.contains(search_query, case=False, na=False)).any(axis=1)
    df = df[mask]
    st.info(f"검색 결과: {len(df):,}개 행 필터링됨")

# 컬럼 다중 선택 필터
all_cols = df.columns.tolist()
selected_cols = st.multiselect("표시할 컬럼 선택", all_cols, default=all_cols)

# 데이터 표시 (클릭 정렬, 컬럼 너비 조정 지원)
if selected_cols:
    st.dataframe(
        df[selected_cols],
        width="stretch",
        height=600
    )

    # 필터링 결과 엑셀/CSV 다운로드 기능
    csv = df[selected_cols].to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 현재 필터링된 데이터 CSV 다운로드",
        data=csv,
        file_name=f"{selected_sheet}_filtered.csv",
        mime="text/csv"
    )
else:
    st.warning("표시할 컬럼을 최소 1개 이상 선택해주세요.")
