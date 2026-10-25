
import streamlit as st
from google import genai

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

    print("Sending a short test request...")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Reply with only: Hello Mahdi!",
        config={"http_options": {"timeout": 20000}},
    )

    print("Response:", response.text)

except Exception as e:
    print("ERROR:", type(e).__name__, str(e))
