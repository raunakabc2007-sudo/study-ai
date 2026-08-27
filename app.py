import streamlit as st
from groq import Groq

st.set_page_config(page_title="Study AI Assistant", page_icon="📚")

GROQ_API_KEY = "Gsk_CZ4lh1jt56NKVMA2Z63RWGdyb3FYTy7Hw8UCqfobw7tpgIFpw4V9"

st.title("Study AI Assistant")
st.write("नमस्ते रौनक! आपका एआई तैयार है।")

query = st.text_input("अपना सवाल यहाँ पूछें:")

if query:
    try:
        client = Groq(api_key=GROQ_API_KEY)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": query}],
            model="llama-3.3-70b-versatile",
        )
        st.write(chat_completion.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")
