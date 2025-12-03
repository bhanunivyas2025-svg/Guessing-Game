import streamlit as st
import random

st.title("🎯 Number Guessing Game")
st.write("Guess the number between **1 and 100**!")

# Initialize the secret number in session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = ""

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if guess < st.session_state.secret_number:
        st.session_state.message = "⬆️ Too low! Try again."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "⬇️ Too high! Try again."
    else:
        st.session_state.message = "🎉 Correct! You guessed the number!"

st.write(st.session_state.message)

if st.button("New Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.message = "New game started! Guess again."
