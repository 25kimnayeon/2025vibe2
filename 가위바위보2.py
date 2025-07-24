import streamlit as st
import random
import base64

# 🎨 배경 이미지 설정 함수
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🎵 효과음 삽입 함수
def play_sound(sound_url):
    st.markdown(
        f"""
        <audio autoplay>
        <source src="{sound_url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# 🌟 초기 설정
st.set_page_config(page_title="🌈 가위바위보 월드 🌈", page_icon="🎮", layout="centered")
set_background("https://i.pinimg.com/originals/e6/8e/e4/e68ee4b6bb9cb7a15129f27385d02e1e.jpg")  # 💖 귀여운 배경

st.markdown("<h1 style='text-align: center; color: #ff66b2;'>🌟 귀염뽀짝 가위✊ 바위✋ 보✌️ 게임! 🌟</h1>", unsafe_allow_html=True)
st.markdown("---")

# 이모지 선택지
choices = {"가위 ✌️": "scissors", "바위 ✊": "rock", "보 ✋": "paper"}
result_emoji = {"win": "👏👏👏", "lose": "😢😢😢", "draw": "❓❓❓"}

# 세션 상태 초기화
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.round = 1
    st.session_state.done = False

# 진행
if not st.session_state.done:
    st.subheader(f"🧸 Round {st.session_state.round} / 3 🧸")
    player_choice = st.radio("👇 당신의 선택! 👇", list(choices.keys()), horizontal=True)

    if st.button("🎲 승부 보기! 🎲"):
        computer_choice = random.choice(list(choices.keys()))
        st.markdown(f"🤖 **컴퓨터**: {computer_choice}")
        st.markdown(f"🧑 **당신**: {player_choice}")

        p = choices[player_choice]
        c = choices[computer_choice]

        # 결과 판단
        if p == c:
            st.info(f"❗ 비겼어요! {result_emoji['draw']}")
            play_sound("https://www.fesliyanstudios.com/play-mp3/387")  # Neutral 효과음
            st.image("https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif", width=200)  # Draw GIF
        elif (p == "scissors" and c == "paper") or (p == "rock" and c == "scissors") or (p == "paper" and c == "rock"):
            st.success(f"🎉 이겼어요! {result_emoji['win']}")
            st.session_state.player_wins += 1
            play_sound("https://www.fesliyanstudios.com/play-mp3/438")  # Win 효과음
            st.image("https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif", width=200)  # Win GIF
        else:
            st.error(f"💥 졌어요! {result_emoji['lose']}")
            st.session_state.computer_wins += 1
            play_sound("https://www.fesliyanstudios.com/play-mp3/6678")  # Lose 효과음
            st.image("https://media.giphy.com/media/3ohc12ZFtYyPbmwSWs/giphy.gif", width=200)  # Lose GIF

        st.session_state.round += 1

        # 승패 최종 판단
        if st.session_state.player_wins == 2:
            st.balloons()
            st.markdown("🎊🎊 <h2 style='color: #ff66b2;'>당신이 이겼습니다!!</h2> 🎊🎊", unsafe_allow_html=True)
            st.image("https://media.giphy.com/media/111ebonMs90YLu/giphy.gif", width=300)
            st.session_state.done = True
        elif st.session_state.computer_wins == 2:
            st.markdown("💀 <h2 style='color: gray;'>당신이 졌습니다...</h2>", unsafe_allow_html=True)
            st.image("https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif", width=300)
            st.session_state.done = True
        elif st.session_state.round > 3:
            if st.session_state.player_wins > st.session_state.computer_wins:
                st.balloons()
                st.markdown("🏆 <h2 style='color: gold;'>3판 종료! 당신의 승리!</h2>", unsafe_allow_html=True)
                st.image("https://media.giphy.com/media/26uf9QPzzlKPvQG5m/giphy.gif", width=300)
            elif st.session_state.player_wins < st.session_state.computer_wins:
                st.markdown("😵‍💫 <h2 style='color: silver;'>3판 종료! 당신의 패배...</h2>", unsafe_allow_html=True)
                st.image("https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif", width=300)
            else:
                st.markdown("🤝 <h2>무승부입니다!</h2>", unsafe_allow_html=True)
                st.image("https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", width=300)
            st.session_state.done = True

# 🔁 다시 시작
if st.session_state.done:
    if st.button("🔄 다시 하기"):
        st.session_state.player_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.round = 1
        st.session_state.done = False
