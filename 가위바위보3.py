import streamlit as st
import random

# 🎨 움직이는 배경 + 블러 효과 설정
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDY5N2ZsdGJzZTY5bHRqbm81cWExenZ4MXQ0aGh0djQ0Mm1rZXM2OCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/RvzF2Cdt42fi4/giphy.gif");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            backdrop-filter: blur(4px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🎵 효과음 삽입
def play_sound(url):
    st.markdown(
        f"""
        <audio autoplay>
        <source src="{url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# 💖 타이틀 폰트 스타일 설정
def styled_title(text):
    st.markdown(
        f"""
        <h1 style='
            font-family: "Comic Sans MS", cursive, sans-serif;
            font-size: 48px;
            color: #fff3fc;
            text-shadow: 2px 2px #ff69b4, -2px -2px #ffd1f7;
            animation: glitter 1.5s infinite alternate;
            text-align: center;
        '>{text}</h1>
        <style>
        @keyframes glitter {{
            0% {{ text-shadow: 0 0 5px #ff69b4, 0 0 10px #ffd1f7; }}
            100% {{ text-shadow: 0 0 15px #ff69b4, 0 0 25px #ffd1f7; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🧠 초기 세션 값
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.round = 1
    st.session_state.done = False
    st.session_state.total_win = 0
    st.session_state.total_lose = 0

# 🖼️ 앱 설정 + 배경 적용
st.set_page_config(page_title="🎀 가위바위보 월드 🎀", page_icon="🌸", layout="centered")
set_background()

# 🌟 타이틀 출력
styled_title("🌈 귀염뽀짝 가위✊ 바위✋ 보✌️ 월드!")

st.markdown("---")

choices = {"가위 ✌️": "scissors", "바위 ✊": "rock", "보 ✋": "paper"}
result_emoji = {"win": "👏👏👏", "lose": "😢😢😢", "draw": "❓❓❓"}

if not st.session_state.done:
    st.subheader(f"🎮 Round {st.session_state.round} / 3 🎮")
    player_choice = st.radio("👇 당신의 선택을 골라주세요 👇", list(choices.keys()), horizontal=True)

    if st.button("⚔️ 승부!"):
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
            st.markdown("🎊 <h2 style='color: #ff66b2;'>✨ 당신이 이겼습니다!! ✨</h2>", unsafe_allow_html=True)
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
                st.markdown("🏆 <h2 style='color: gold;'>3판 종료! 당신이 이겼습니다!</h2>", unsafe_allow_html=True)
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

# 🔄 다시하기 + 🏅 랭킹 표시
if st.session_state.done:
    if st.button("🔁 다시 하기!"):
        st.session_state.round = 1
        st.session_state.player_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.done = False

    st.markdown("---")
    st.markdown("## 🏅 지금까지의 기록")
    st.markdown(f"- 🧡 **승리 횟수**: `{st.session_state.total_win}`")
    st.markdown(f"- 💙 **패배 횟수**: `{st.session_state.total_lose}`")
