import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


# system = st.text_input("System:", "You are a helpful assistant.")
prompt = st.text_input("Your Prompt:")

if st.button("Generate Response"):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # {"role": "user", "content": system},
            {"role": "user", "content": prompt},
        ],
    )
    response = completion.choices[0].message.content
    st.write(response)
