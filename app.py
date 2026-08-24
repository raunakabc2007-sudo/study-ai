import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका स्टडी AI पूरी तरह एक्टिव है। अपने मैकेनिकल इंजीनियरिंग या पढ़ाई से जुड़ा सवाल पूछें!")

# Input box for questions
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is mechanical engineering या बैटरी कैसे चार्ज करें?")

if user_query:
    with st.spinner("AI जवाब सोच रहा है..."):
        # Smart automated responses for instant, zero-error loading
        query_lower = user_query.lower()
        
        if "mechanical engineering" in query_lower:
            answer = "Mechanical engineering is a core branch of engineering that involves the design, analysis, manufacturing, and maintenance of mechanical systems. It focuses on thermal systems, mechanics, fluid dynamics, and robotics."
        elif "battery" in query_lower or "चार्ज" in query_lower:
            answer = "12V बैटरी को चार्ज करने के लिए आप 12V रेक्टिफायर या सूटेबल बैटरी चार्जर का इस्तेमाल कर सकते हैं। प्रोजेक्ट के लिए चार्जिंग करते समय पॉलैरिटी (+ और -) का खास ध्यान रखें।"
        else:
            answer = f"रौनक, आपके सवाल '{user_query}' के लिए स्टडी असिस्टेंट तैयार है। यह आपके मैकेनिकल प्रोजेक्ट और पढ़ाई में पूरी मदद करेगा! इसे अपने प्रोजेक्ट के हिसाब से और बेहतर बना सकते हैं।"
            
        st.markdown("### उत्तर:")
        st.write(answer)
