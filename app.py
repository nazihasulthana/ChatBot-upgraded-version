import streamlit as st
import random

greetings = ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"]
how_are_you = ["I'm fine!", "Doing great!", "All good!", "Awesome!"]
thanks = ["You're welcome!", "No problem!", "Anytime!"]

st.title("🤖 My Chatbot")

user = st.text_input("You:")

if user:
    user = user.lower().strip()

    if user in ["hi", "hey","hello","hyy","hy"]:
        st.write("🤖", random.choice(greetings))

    elif "how are you" in user:
        st.write("🤖", random.choice(how_are_you))

    elif "thank" in user:
        st.write("🤖", random.choice(thanks))

    elif user in ["bye", "exit", "quit"]:
        st.write("🤖 Goodbye! 👋")

    else:
        st.write("🤖 I don't understand 🤔")