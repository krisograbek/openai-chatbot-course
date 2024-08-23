import streamlit as st
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("My GPT-4o Mini Chatbot 🤖")


if user_prompt := st.chat_input("Your prompt"):
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_prompt}],
        )
        response = completion.choices[0].message.content
        message_placeholder.markdown(response)
