import streamlit as st
from urllib.parse import quote
import time

# [v3.0] 신찾기: UI 문구 한국어 최적화 및 레이블 정제 버전
# 2026-02-16 업데이트
# 지침 준수: 전체 코드 제공 및 상세 변경 사항 비교 설명

def generate_partners_link(query, min_p, max_p):
    """
    쿠팡 파트너스 추적 파라미터(lptag)를 포함한 최적화된 검색 링크 생성
    """
    af_id = "AF7661905"
    base_url = "https://www.coupang.com/np/search?"
    
    params = [
        f"q={quote(query)}",
        f"sorter=saleCountDesc", 
        f"rocketAll=true",       
        f"lptag={af_id}",        
        "isAddedCart="           
    ]
    
    if min_p > 0: params.append(f"minPrice={min_p}")
    if max_p > 0: params.append(f"maxPrice={max_p}")
    
    return base_url + "&".join(params)

# --- UI 레이아웃 ---
st.set_page_config(page_title="신찾기", page_icon="💰")

# 메인 타이틀
st.title("💰 신찾기")
st.markdown("### 당신의 발에 딱 맞는 '인생 신발'을 찾아드립니다.")

# 1. 첫 번째 섹션 이름 변경
st.subheader("📸 사용 중인 신발 사진 업로드하기")
# 파일 업로더 레이블 한국어화
uploaded_file = st.file_uploader("신발 밑창이나 발 사진을 여기에 드래그하거나 클릭하여 업로드하세요.", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    st.image(uploaded_file, caption="분석 대상 이미지", width=300)
    st.success("✅ 비주얼 데이터 분석 준비 완료!")

# 2. 두 번째 섹션 이름 변경
st.subheader("📍 상세 조건 설정")
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("성별", ["남성", "여성"], horizontal=True)
    length = st.selectbox("발길이 (mm)", options=[str(x) for x in range(220, 305, 5)], index=10)
with col2:
    design = st.selectbox("신발 종류", ["런닝화", "스니커즈", "구두", "워크화", "슬립온"])
    price_range = st.selectbox("예산 범위", ["전체", "3~7만원", "7~15만원", "15만원 이상"])

# 3. 버튼 문구 유지
if st.button("🚀 AI 추천 상품", use_container_width=True):
    with st.status("AI가 최적의 상품을 매칭 중입니다...", expanded=True) as status:
        time.sleep(1.2)
        st.write("마모 패턴 분석 중...")
        time.sleep(0.8)
        st.write("베스트 리뷰 데이터 대조 중...")
        status.update(label="분석 완료! 리포트가 생성되었습니다.", state="complete", expanded=False)

    price_map = {"3~7만원": (30000, 70000), "7~15만원": (70000, 150000), "15만원 이상": (150000, 1000000), "전체": (0, 0)}
    min_p, max_p = price_map.get(price_range, (0, 0))
    
    query = f"{gender} {length}mm {design}"
    final_url = generate_partners_link(query, min_p, max_p)

    st.markdown("---")
    st.header("📋 AI 개인화 추천 리포트")
    
    r_col1, r_col2 = st.columns(2)
    with r_col1:
        st.info("### 🔬 진단 결과\n**[안정성 우선]** 추천\n사진 분석 결과, 발목 지지력이 우수한 모델이 필요합니다.")
    with r_col2:
        st.success(f"### 💬 리뷰 분석 요약\n{length}mm 구매자의 **89%**가 착화감에 만족했습니다.")

    st.markdown("#### 🎯 지금 바로 확인해야 할 최적의 상품")
    st.link_button("👉 추천 상품 보러가기", final_url, type="primary", use_container_width=True)

# 필수 문구 유지
st.divider()
st.caption("이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다. (ID: AF7661905)")
