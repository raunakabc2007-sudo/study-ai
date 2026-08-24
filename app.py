import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका स्टडी AI अब पूरी तरह तैयार है। अपने प्रोजेक्ट या पढ़ाई से जुड़ा कोई भी सवाल पूछें!")

# API Key Configuration
# We will use Streamlit Secrets or prompt safely
api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    # Sidebar input for API Key if not in secrets
    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # User input
        user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is mechanical engineering")
        
        if user_query:
            with st.spinner("AI जवाब सोच रहा है..."):
                response = model.generate_content(user_query)
                st.markdown("### उत्तर:")
                st.write(response.text)
    except Exception as e:
        st.error(f"त्रुटि हुई: {e}")
else:
    st.warning("कृपया बाईं तरफ के मेनू (Sidebar) में अपनी Gemini API Key दर्ज करें ताकि AI काम कर सके।")
    
