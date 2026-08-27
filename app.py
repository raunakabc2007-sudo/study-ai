import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Study AI Assistant", page_icon="📚")

# आपकी Gemini API Key यहाँ सेट है
GOOGLE_API_KEY = "AQ.Ab8RN6LvOVraZuOALW07gNycPgEa4cuTQBuZE0wMbeCd2giWzQ"

st.title("Study AI Assistant")
st.write("नमस्ते रौनक! आपका एआई पूरी तरह से तैयार है।")

query = st.text_input("अपना सवाल यहाँ पूछें:")

if query:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        with st.spinner("AI सोच रहा है..."):
            response = model.generate_content(query)
            st.markdown("### 📖 उत्तर:")
            st.write(response.text)
            
    except Exception as e:
        st.error(f"Error: {e}")
