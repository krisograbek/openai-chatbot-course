import streamlit as st
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("My GPT-4o Mini Chatbot 🤖")

# step 1 keep messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 1 show messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"

if user_prompt := st.chat_input("Your prompt"):
    # step 1 Save user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # step 0: display user prompt
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        completion = client.chat.completions.create(
            model=st.session_state.model,
            # step 2: pass the entire
            messages=[
                {"role": msg["role"], "content": msg["content"]}
                for msg in st.session_state.messages
            ],
        )
        response = completion.choices[0].message.content
        message_placeholder.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})