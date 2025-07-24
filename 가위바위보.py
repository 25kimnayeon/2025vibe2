import streamlit as st
import random

st.set_page_config(page_title="🌟 귀염뽀짝 가위바위보 🌟", page_icon="✊✋✌️", layout="centered")
st.title("🎮✨ 귀염뽀짝 ✨ 가위✊ 바위✋ 보✌️ 게임!")
st.markdown("---")

# 이모지들
choices = {"가위 ✌️": "scissors", "바위 ✊": "rock", "보 ✋": "paper"}
result_emoji = {"win": "👏👏👏", "lose": "😢😢😢", "draw": "❓❓❓"}

# 게임 상태 저장
if "player_wins" not in st.session_state:
    st.session_state.player_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.round = 1
    st.session_state.done = False

# 게임 진행
if not st.session_state.done:
    st.subheader(f"🌈 Round {st.session_state.round} / 3 🌈")
    player_choice = st.radio("👇 당신의 선택을 골라주세요! 👇", list(choices.keys()), horizontal=True)

    if st.button("🎲 승부 보기! 🎲"):
        computer_choice = random.choice(list(choices.keys()))

        st.markdown(f"🤖 컴퓨터의 선택: **{computer_choice}**")
        st.markdown(f"🧑 당신의 선택: **{player_choice}**")

        p = choices[player_choice]
        c = choices[computer_choice]

        if p == c:
            st.info(f"❗ 비겼어요! {result_emoji['draw']}")
        elif (p == "scissors" and c == "paper") or (p == "rock" and c == "scissors") or (p == "paper" and c == "rock"):
            st.success(f"🎉 당신이 이겼어요! {result_emoji['win']}")
            st.session_state.player_wins += 1
        else:
            st.error(f"💥 당신이 졌어요! {result_emoji['lose']}")
            st.session_state.computer_wins += 1

        st.session_state.round += 1

        # 승패 결정
        if st.session_state.player_wins == 2:
            st.balloons()
            st.markdown("🌟🌟 **당신이 이겼습니다!** 🌟🌟")
            st.session_state.done = True
        elif st.session_state.computer_wins == 2:
            st.markdown("💔💔 **당신이 졌습니다!** 💔💔")
            st.session_state.done = True
        elif st.session_state.round > 3:
            if st.session_state.player_wins > st.session_state.computer_wins:
                st.balloons()
                st.markdown("🏆 **3판 종료! 당신이 이겼습니다!** 🏆")
            elif st.session_state.player_wins < st.session_state.computer_wins:
                st.markdown("☁️ **3판 종료! 당신이 졌습니다!** ☁️")
            else:
                st.markdown("🤝 **3판 모두 끝났어요! 무승부입니다.** 🤝")
            st.session_state.done = True

# 리셋 버튼
if st.session_state.done:
    if st.button("🔄 다시 하기"):
        st.session_state.player_wins = 0
        st.session_state.computer_wins = 0
        st.session_state.round = 1
        st.session_state.done = False
