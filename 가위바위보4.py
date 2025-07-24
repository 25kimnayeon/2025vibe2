import streamlit as st
import random

# 🌤️ 하늘색 배경
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/78/70/27/78702706a20ef6c680c92b131ad17418.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            backdrop-filter: blur(2px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🎵 효과음
def play_sound(url):
    st.markdown(
        f"""
        <audio autoplay>
        <source src="{url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# 💖 타이틀 폰트 스타일
def styled_title(text):
    st.markdown(
        f"""
        <h1 style='
            font-family: "Comic Sans MS", cursive, sans-serif;
            font-size: 48px;
            color: #fff3fc;
            text-shadow: 2px 2px #00bfff, -2px -2px #b3e0ff;
            animation: glitter 1.5s infinite alternate;
            text-align: center;
        '>{text}</h1>
        <style>
        @keyframes glitter {{
            0% {{ text-shadow: 0 0 5px #00bfff; }}
            100% {{ text-shadow: 0 0 20px #b3e0ff; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🧠 세션 초기화
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.round = 1
    st.session_state.done = False
    st.session_state.total_win = 0
    st.session_state.total_lose = 0

# 🌟 페이지 설정 + 배경
st.set_page_config(page_title="🌈 하늘빛 가위바위보 🌈", page_icon="☁️", layout="centered")
set_background()
styled_title("☁️ 하늘빛 가위✊ 바위✋ 보✌️ 게임 🌤️")

# 🎀 애니메이션 버튼 스타일
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #a1c4fd, #c2e9fb);
        color: #003366;
        font-size: 22px;
        font-weight: bold;
        border-radius: 40px;
        border: none;
        padding: 15px 35px;
        box-shadow: 0 0 15px #80dfff;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

choices = {"가위 ✌️": "scissors", "바위 ✊": "rock", "보 ✋": "paper"}
result_emoji = {"win": "👏👏👏", "lose": "😢😢😢", "draw": "❓❓❓"}

# 🎮 게임 진행
if not st.session_state.done:
    st.subheader(f"🎮 Round {st.session_state.round} / 3")
    player_choice = st.radio("👇 당신의 선택 👇", list(choices.keys()), horizontal=True)

    if st.button("🌈 승부 보기!"):
        comp_choice = random.choice(list(choices.keys()))
        st.markdown(f"🤖 **컴퓨터의 선택**: {comp_choice}")
        st.markdown(f"🧑 **당신의 선택**: {player_choice}")

        p = choices[player_choice]
        c = choices[comp_choice]

        if p == c:
            st.info(f"무승부! {result_emoji['draw']}")
            play_sound("https://www.fesliyanstudios.com/play-mp3/387")
            st.image("https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif", width=200)
        elif (p == "scissors" and c == "paper") or (p == "rock" and c == "scissors") or (p == "paper" and c == "rock"):
            st.success(f"🎉 이겼어요! {result_emoji['win']}")
            st.session_state.player_wins += 1
            play_sound("https://www.fesliyanstudios.com/play-mp3/438")
            st.image("https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif", width=200)
        else:
            st.error(f"💥 졌어요! {result_emoji['lose']}")
            st.session_state.computer_wins += 1
            play_sound("https://www.fesliyanstudios.com/play-mp3/6678")
            st.image("https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif", width=200)

        st.session_state.round += 1

        if st.session_state.player_wins == 2:
            st.balloons()
            st.markdown("🎊 <h2 style='color: #00bfff;'>✨ 당신이 이겼습니다!! ✨</h2>", unsafe_allow_html=True)
            st.image("https://media.giphy.com/media/111ebonMs90YLu/giphy.gif", width=300)
            st.session_state.total_win += 1
            st.session_state.done = True
        elif st.session_state.computer_wins == 2:
            st.markdown("💀 <h2 style='color: gray;'>😵 당신이 졌습니다...</h2>", unsafe_allow_html=True)
            st.image("https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif", width=300)
            st.session_state.total_lose += 1
            st.session_state.done = True
        elif st.session_state.round > 3:
            if st.session_state.player_wins > st.session_state.computer_wins:
                st.balloons()
                st.markdown("🏆 <h2 style='color: #00ccff;'>3판 종료! 당신이 이겼습니다!</h2>", unsafe_allow_html=True)
                st.session_state.total_win += 1
                st.image("https://media.giphy.com/media/26uf9QPzzlKPvQG5m/giphy.gif", width=300)
            elif st.session_state.player_wins < st.session_state.computer_wins:
                st.markdown("☠️ <h2 style='color: silver;'>3판 종료! 당신이 졌습니다.</h2>", unsafe_allow_html=True)
                st.session_state.total_lose += 1
                st.image("https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif", width=300)
            else:
                st.markdown("🤝 <h2>무승부입니다!</h2>", unsafe_allow_html=True)
                st.image("https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", width=300)
            st.session_state.done = True

# 🧾 결과 및 리셋
if st.session_state.done:
    if st.button("🔁 다시 하기!"):
        st.session_state.round = 1
        st.session_state.player_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.done = False

    st.markdown("---")
    st.markdown("## 🏅 지금까지의 기록")
    st.markdown(f"- ☀️ **총 승리 횟수**: `{st.session_state.total_win}`")
    st.markdown(f"- 🌧️ **총 패배 횟수**: `{st.session_state.total_lose}`")
