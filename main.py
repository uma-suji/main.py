import streamlit as st
import random

st.title("Guess The Number")
st.write("I will think of a number between range of 1-100. Try to guess it correctly within less attempts.")

if 'computer_guess' not in st.session_state:
     st.session_state.computer_guess = random.randint(1, 100)
     st.write(st.session_state.computer_guess)  

def guess():
    user_guess = st.number_input("Enter your guess: ")

    if user_guess < st.session_state.computer_guess:
        st.write("Guess higher!")
    elif user_guess > st.session_state.computer_guess:
        st.write("Guess lower!")
    else:
        st.success("Congratulations! You guessed the number correctly .")

guess()