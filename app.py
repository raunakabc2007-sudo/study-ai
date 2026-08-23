import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study AI Assistant")
st.write(f"नमस्ते रौनक! आपका स्टडी AI अब पूरी तरह तैयार है। अपने प्रोजेक्ट या पढ़ाई से जुड़ा कोई भी सवाल पूछें!")

# Automatic model configuration using Streamlit Secrets or default setup
try:
    # Try using Streamlit secrets if available, or environment
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")
    else:
        # Fallback initialization 
        genai.configure()
        model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.info("AI मॉडल कनेक्ट हो रहा है...")

# Input box for user question
st.markdown("### अपना सवाल यहाँ पूछें:")
user_query = st.text_input("", placeholder="जैसे: What is mechanical engineering या बैटरी कैसे चार्ज करें?")

if user_query:
    with st.spinner("AI जवाब सोच रहा है..."):
        try:
            response = model.generate_content(user_query)
            st.markdown("### उत्तर:")
            st.write(response.text)
        except Exception as e:
            st.error(f"त्रुटि हुई: {e}")
