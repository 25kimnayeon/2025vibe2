import streamlit as st
import random

# 🌈 배경: 하늘 + 무지개 + 별
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/f2/62/8a/f2628a3c718f8ac7b3e0c25bb13c3147.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            backdrop-filter: blur(2px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🎵 효과음 재생
def play_sound(url):
    st.markdown(
        f"""
        <audio autoplay>
        <source src="{url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# ✨ 타이틀 폰트
def styled_title(text):
    st.markdown(
        f"""
        <h1 style='
            font-family: "Comic Sans MS", cursive, sans-serif;
            font-size: 50px;
            color: #fff;
            text-shadow: 3px 3px #ff69b4, -2px -2px #b3e0ff;
            animation: glitter 1.5s infinite alternate;
            text-align: center;
        '>{text}</h1>
        <style>
        @keyframes glitter {{
            0% {{ text-shadow: 0 0 8px #ffccff; }}
            100% {{ text-shadow: 0 0 20px #99e6ff; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🎀 캐릭터 GIF 매핑
character_gifs = {
    "가위 ✌️": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDY0djRhd2d3OTY5Z21jdmw3ZzI1dzJ6NzhlMm1rMm1ubnM5ajNlcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jQqU9ytT5Oa8xPIFWz/giphy.gif",
    "바위 ✊": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDFqcnhrMXRxNm51a3B6YmhrZzdkN3F5NmVxYzN0cnhjZ2lzd3NmbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Zv3WwMRe5bM3k/giphy.gif",
    "보 ✋": "https://media.giphy.com/media/l1J9sN9qx5b3j0LZ6/giphy.gif"
}

# 🧠 세션 초기화
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.round = 1
    st.session_state.done = False
    st.session_state.total_win = 0
    st.session_state.total_lose = 0

# 🌟 페이지 설정 + 배경
st.set_page_config(page_title="가위바위보 게임!!!!!", page_icon="🎯", layout="centered")
set_background()
styled_title("💥 가위바위보 게임!!!!! 💥")

# ✨ 애니메이션 버튼 스타일
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #b3e0ff, #ffccff);
        color: #003366;
        font-size: 22px;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        padding: 14px 40px;
        box-shadow: 0 0 15px #fff9f9;
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
result_emojis = {
    "win": random.choice(["🏆", "🎉", "🦄", "👏", "🌈"]),
    "lose": random.choice(["😢", "😭", "💀", "👻", "☁️"]),
    "draw": random.choice(["😐", "😶", "🤔", "❓", "🔄"])
}

if not st.session_state.done:
    st.subheader(f"✨ Round {st.session_state.round} / 3 ✨")
    player_choice = st.radio("🎈 당신의 선택 🎈", list(choices.keys()), horizontal=True)

    if st.button("🌟 가위바위보!! 🌟"):
        comp_choice = random.choice(list(choices.keys()))
        st.markdown(f"🤖 **컴퓨터**: {comp_choice}")
        st.image(character_gifs[comp_choice], width=200)

        st.markdown(f"🧑 **당신**: {player_choice}")
        st.image(character_gifs[player_choice], width=200)

        p = choices[player_choice]
        c = choices[comp_choice]

        if p == c:
            st.info(f"무승부! {result_emojis['draw']}")
            play_sound("https://www.fesliyanstudios.com/play-mp3/387")
        elif (p == "scissors" and c == "paper") or (p == "rock" and c == "scissors") or (p == "paper" and c == "rock"):
            st.success(f"이겼어요! {result_emojis['win']}")
            st.session_state.player_wins += 1
            play_sound("https://www.fesliyanstudios.com/play-mp3/438")
        else:
            st.error(f"졌어요... {result_emojis['lose']}")
            st.session_state.computer_wins += 1
            play_sound("https://www.fesliyanstudios.com/play-mp3/6678")

        st.session_state.round += 1

        if st.session_state.player_wins == 2:
            st.balloons()
            st.markdown("🎊 <h2 style='color: #00bfff;'>✨ 당신이 이겼습니다!! ✨</h2>", unsafe_allow_html=True)
            st.session_state.total_win += 1
            st.session_state.done = True
        elif st.session_state.computer_wins == 2:
            st.markdown("💀 <h2 style='color: gray;'>😵 당신이 졌습니다...</h2>", unsafe_allow_html=True)
            st.session_state.total_lose += 1
            st.session_state.done = True
        elif st.session_state.round > 3:
            if st.session_state.player_wins > st.session_state.computer_wins:
                st.balloons()
                st.markdown("🏆 <h2 style='color: #00ccff;'>3판 종료! 당신이 이겼습니다!</h2>", unsafe_allow_html=True)
                st.session_state.total_win += 1
            elif st.session_state.player_wins < st.session_state.computer_wins:
                st.markdown("☠️ <h2 style='color: silver;'>3판 종료! 당신이 졌습니다.</h2>", unsafe_allow_html=True)
                st.session_state.total_lose += 1
            else:
                st.markdown("🤝 <h2>무승부입니다!</h2>", unsafe_allow_html=True)
            st.session_state.done = True

# 🔁 다시 시작 + 기록
if st.session_state.done:
    if st.button("🔄 다시 하기!"):
        st.session_state.round = 1
        st.session_state.player_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.done = False

    st.markdown("---")
    st.markdown("## 🏅 지금까지의 랭킹 기록")
    st.markdown(f"- 🏆 총 승리: `{st.session_state.total_win}`")
    st.markdown(f"- 💔 총 패배: `{st.session_state.total_lose}`")
