import streamlit as st
import random
import base64

# 페이지 설정
st.set_page_config(page_title="숫자 맞히기 게임!!!!!", page_icon="🔮", layout="centered")

# 배경 이미지 세팅
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        bg_img = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""<style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
            font-family: 'Comic Sans MS', cursive;
        }}
        .title-font {{
            font-size:40px !important;
            font-weight:bold;
            color: #ff69b4;
            text-shadow: 2px 2px 4px #000000;
        }}
        .emoji {{
            font-size: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 오디오 재생
def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# 🎨 테마 선택
theme = st.sidebar.selectbox("🎨 테마를 선택하세요!", ["🎀 공주", "🧙 마법사"])
if theme == "🎀 공주":
    set_background("img/princess.png")
    emoji_set = ["👑", "🌸", "🎀", "💖", "🧁"]
    primary_color = "#ffb6c1"
elif theme == "🧙 마법사":
    set_background("img/wizard.png")
    emoji_set = ["🧙‍♂️", "✨", "🔮", "🪄", "📜"]
    primary_color = "#b39ddb"

# 🔥 난이도 선택
difficulty = st.sidebar.radio("💥 난이도를 선택하세요!", ["🍼 쉬움", "😬 보통", "🔥 어려움"])
if difficulty == "🍼 쉬움":
    max_num, max_tries = 50, 10
elif difficulty == "😬 보통":
    max_num, max_tries = 100, 7
else:
    max_num, max_tries = 200, 5

# 상태 초기화
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, max_num)
    st.session_state.tries = 0
    st.session_state.game_over = False

# 제목
st.markdown(f"<h1 class='title-font'>{random.choice(emoji_set)} 숫자 맞히기 게임!!!!! {random.choice(emoji_set)}</h1>", unsafe_allow_html=True)
st.markdown(f"📌 1부터 {max_num}까지의 숫자 중 하나를 맞혀보세요!")
st.markdown(f"🧮 기회: {max_tries}번")

# 숫자 입력
if not st.session_state.game_over:
    guess = st.number_input("🔢 숫자를 입력하세요!", min_value=1, max_value=max_num, step=1, key="guess")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ 맞혀보기"):
            st.session_state.tries += 1

            if guess == st.session_state.target:
                play_audio("audio/correct.mp3")
                st.success(f"{random.choice(emoji_set)} 정답입니다! 축하해요! {random.choice(emoji_set)}")
                st.balloons()
                st.session_state.game_over = True
            elif guess < st.session_state.target:
                play_audio("audio/wrong.mp3")
                st.warning("🔽 너무 작아요!")
            else:
                play_audio("audio/wrong.mp3")
                st.warning("🔼 너무 커요!")

            if st.session_state.tries >= max_tries and not st.session_state.game_over:
                st.error(f"💣 기회를 모두 사용했어요! 정답은 {st.session_state.target}였어요.")
                st.session_state.game_over = True

    with col2:
        if st.button("🔄 다시 시작"):
            st.session_state.target = random.randint(1, max_num)
            st.session_state.tries = 0
            st.session_state.game_over = False
            play_audio("audio/start.mp3")
            st.experimental_rerun()

# 남은 기회
if not st.session_state.game_over:
    st.markdown(f"💫 남은 기회: **{max_tries - st.session_state.tries}번**")

st.markdown("---")
st.markdown("🌈 게임을 즐겨주셔서 감사합니다! 더 많은 테마도 기대해주세요! 💖")
