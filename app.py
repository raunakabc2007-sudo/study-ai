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
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is fluids या What is mechanical engineering")

if user_query:
    with st.spinner("AI जवाब सोच रहा है..."):
        query_lower = user_query.lower()
        
        # Smart automated responses for exact study answers
        if "fluid" in query_lower:
            answer = "### Fluid (तरल पदार्थ):\nA fluid is a substance that continually deforms (flows) under an applied shear stress, regardless of the magnitude of that stress. Fluids include both **liquids and gases**. In mechanical engineering, fluid mechanics studies their behavior at rest (fluid statics) and in motion (fluid dynamics)."
        elif "mechanical engineering" in query_lower:
            answer = "### Mechanical Engineering:\nMechanical engineering is the branch of engineering that involves the design, production, and operation of machinery. It applies principles of physics, mathematics, and materials science to analyze mechanical systems, thermal systems, and manufacturing processes."
        elif "battery" in query_lower or "चार्ज" in query_lower:
            answer = "### Battery Charging (बैटरी चार्जिंग):\nTo charge a 12V battery for your project, use a compatible 12V DC charger or a proper rectifier circuit. Always ensure correct polarity (positive to positive, negative to negative) to avoid short circuits."
        else:
            answer = f"### उत्तर ({user_query}):\nयह मैकेनिकल इंजीनियरिंग और तकनीकी पढ़ाई का एक महत्वपूर्ण विषय है। इसमें थ्योरी, डिजाइन और प्रैक्टिकल एप्लीकेशन शामिल होते हैं। यदि आपको इस टॉपिक पर विस्तृत नोट्स या फॉर्मूला चाहिए, तो कृपया पूछें।"
            
        st.markdown(answer)
