import streamlit as st
from groq import Groq

st.set_page_config(page_title="Study AI Assistant", page_icon="📚")

# आपकी नई और सही API Key यहाँ सेट है
GROQ_API_KEY = "Gsk_3XmxCMGR46kXYVpN1CcgWGdyb3FYW33l9QYTIbgLD7gyWtS5gy9u"

st.title("Study AI Assistant")
st.write("नमस्ते रौनक! आपका एआई पूरी तरह से तैयार है।")

query = st.text_input("अपना सवाल यहाँ पूछें:")

if query:
    try:
        client = Groq(api_key=GROQ_API_KEY)
        with st.spinner("AI सोच रहा है..."):
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": query}],
                model="llama-3.3-70b-versatile",
            )
            st.markdown("### 📖 उत्तर:")
            st.write(chat_completion.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")
