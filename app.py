import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Study AI Assistant", page_icon="📚")

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका स्टडी AI अब पूरी तरह तैयार है। अपने प्रोजेक्ट या पढ़ाई से जुड़ा कोई भी सवाल पूछें!")

# अब ऐप खुद आपसे की मांगेगी
user_api_key = st.text_input("अपनी Gemini API Key यहाँ दर्ज करें:", type="password")

if user_api_key:
    try:
        genai.configure(api_key=user_api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        user_query = st.text_input("अपना सवाल यहाँ पूछें:")

        if user_query:
            with st.spinner("AI जवाब सोच रहा है..."):
                response = model.generate_content(user_query)
                st.success("### जवाब:")
                st.write(response.text)
    except Exception as e:
        st.error(f"کوئی غلطی हुई: {e}")
else:
    st.info("💡 कृपया ऊपर दिए गए बॉक्स में अपनी Gemini API Key दर्ज करें ताकि AI काम कर सके।")
