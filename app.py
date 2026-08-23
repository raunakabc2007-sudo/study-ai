import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Study AI Assistant", page_icon="📚")

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका स्टडी AI अब पूरी तरह तैयार है। अपने प्रोजेक्ट या पढ़ाई से जुड़ा कोई भी सवाल पूछें!")

# आपकी Gemini API Key
GOOGLE_API_KEY = "AQ.Ab8RN6LJ9r5qvY-t3Se_e5kqGKxlgvj3RIH1dl0DnkOaR4UziQ"

if not GOOGLE_API_KEY:
    st.warning("⚠️ कृपया अपनी Gemini API Key दर्ज करें।")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # सही और काम करने वाला मॉडल
    model = genai.GenerativeModel('gemini-1.5-flash')

    # सवाल पूछने का बॉक्स
    user_query = st.text_input("अपना सवाल यहाँ पूछें:")

    if user_query:
        with st.spinner("AI जवाब सोच रहा है..."):
            try:
                response = model.generate_content(user_query)
                st.success("### जवाब:")
                st.write(response.text)
            except Exception as e:
                st.error(f"کوئی غلطی हुई: {e}")
