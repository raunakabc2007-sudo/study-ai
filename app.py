
import streamlit as st

st.set_page_config(page_title="Study AI Assistant", page_icon="📚")

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका स्टडी AI ऐप सफलतापूर्वक लाइव हो चुका है।")

# सवाल पूछने का बॉक्स
user_query = st.text_input("अपना सवाल यहाँ पूछें:")

if user_query:
    st.success(f"आपने पूछा: {user_query}")
    st.info("यह आपका अपना स्टडी AI ऐप है। आप यहाँ अपने प्रोजेक्ट या पढ़ाई से जुड़े सवाल पूछ सकते हैं!")
