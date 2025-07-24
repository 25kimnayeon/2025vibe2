import streamlit as st
import random

st.set_page_config(page_title="💭 아무말 이상형 월드컵", page_icon="🏆", layout="wide")

st.markdown("""
    <style>
        .title-text {
            text-align: center;
            font-size: 48px;
            color: hotpink;
            font-weight: bold;
        }
        .subtitle-text {
            text-align: center;
            font-size: 24px;
            color: #888;
        }
        .emoji-box {
            font-size: 80px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-text'>💥 아무말 이상형 월드컵 💥</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>당신의 아무말 취향은 무엇인가요? 🤯🔥💫</div>", unsafe_allow_html=True)
st.markdown("---")

# 아무말 후보 리스트
candidates = [
    "🌶️ 매운 고추를 입에 문 고양이",
    "🍕 피자 위에서 춤추는 고라니",
    "🦖 복싱하는 공룡",
    "🍞 식빵을 베개 삼은 하마",
    "🚀 달로 출근하는 직장인",
    "🐙 문어가 만든 초코케이크",
    "🦄 무지개 토하는 유니콘",
    "🛸 외계인과 카드게임 하는 펭귄",
    "🐸 논문 쓰는 개구리",
    "🧃 종이컵에 담긴 우주",
    "🌪️ 바람과 탱고 추는 판다",
    "🪐 우주선에 낀 고슴도치",
    "🍣 스시가 되고 싶은 치타",
    "🌈 색연필로 그린 세계",
    "🎮 플레이스테이션 조종하는 오징어",
    "🍿 팝콘 대신 튀긴 구름"
]

# 초기 세팅
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.pool = candidates.copy()
    random.shuffle(st.session_state.pool)
    st.session_state.winners = []

# 라운드 안내
st.markdown(f"<h3 style='text-align:center;'>✨ {len(st.session_state.pool)//2}강 대결! ✨</h3>", unsafe_allow_html=True)

# 대진 구성
if len(st.session_state.pool) >= 2:
    col1, col2 = st.columns(2)
    left = st.session_state.pool.pop()
    right = st.session_state.pool.pop()

    with col1:
        st.markdown(f"<div class='emoji-box'>{left}</div>", unsafe_allow_html=True)
        if st.button(f"✅ 이거 선택!", key=left):
            st.session_state.winners.append(left)
            st.rerun()

    with col2:
        st.markdown(f"<div class='emoji-box'>{right}</div>", unsafe_allow_html=True)
        if st.button(f"✅ 이거 선택!", key=right):
            st.session_state.winners.append(right)
            st.rerun()
else:
    if len(st.session_state.winners) == 1:
        st.markdown("""
            <h2 style='text-align: center; color: gold;'>🏆 당신의 아무말 월드컵 최종 우승자는... 🥁</h2>
        """, unsafe_allow_html=True)
        st.markdown(f"<div class='emoji-box'>{st.session_state.winners[0]}</div>", unsafe_allow_html=True)
        st.success("✨ 아무말 챔피언! 대환장 취향 인정합니다 ✨")
        st.balloons()
        if st.button("🔁 다시 하기"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    else:
        # 다음 라운드로 이동
        st.session_state.pool = st.session_state.winners.copy()
        st.session_state.winners = []
        st.session_state.round += 1
        random.shuffle(st.session_state.pool)
        st.rerun()
