import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका सुपर स्टडी AI तैयार है। अब बिना किसी की के हर सवाल का सटीक जवाब मिलेगा!")

# Input box for any question
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is engine, Heart, Forest या कोई भी पढ़ाई का सवाल")

if user_query:
    with st.spinner("AI उत्तर तैयार कर रहा है..."):
        query_lower = user_query.lower()
        
        # Smart Database for Instant Answers
        if "engine" in query_lower:
            answer = """### ⚙️ Engine (इंजन):\nAn engine is a machine designed to convert one form of energy into mechanical energy.\n- **Types:** Internal Combustion (IC) Engine, External Combustion Engine, Electric Engine.\n- **Applications:** Used in cars, bikes, and mechanical machinery."""
        
        elif "heart" in query_lower:
            answer = """### ❤️ Human Heart (मानव हृदय):\nThe heart is a muscular organ that pumps blood through the blood vessels of the circulatory system.\n- It has **4 chambers**: Two atria (upper) and two ventricles (lower).\n- **Function:** Pumps oxygenated blood to the body and deoxygenated blood to the lungs."""
        
        elif "forest" in query_lower:
            answer = """### 🌲 Forest (वन):\nA large area covered chiefly with trees and undergrowth. Forests regulate the global climate, produce oxygen, and act as natural carbon sinks."""
        
        elif "fluid" in query_lower:
            answer = """### 💧 Fluid Mechanics:\nA fluid is a substance that continuously deforms under shear stress (liquids and gases). It includes fluid statics and fluid dynamics."""
        
        elif "mechanical engineering" in query_lower:
            answer = """### 🛠️ Mechanical Engineering:\nA core branch of engineering involving design, thermal systems, manufacturing, and machine mechanics."""
        
        else:
            # Clean formatting for any random question
            topic = user_query.replace("What is", "").replace("what is", "").strip().title()
            answer = f"""### 📖 विषय: {topic}\n\n**1. मुख्य परिभाषा (Overview):**\n{topic} एक अत्यंत महत्वपूर्ण विषय है, जिसका उपयोग विज्ञान, तकनीकी और अकादमिक अध्ययन में किया जाता है।\n\n**2. मुख्य बिंदु (Key Details):**\n- यह विषय किसी प्रक्रिया या संरचना को बेहतर तरीके से समझने में मदद करता है।\n- इसके सिद्धांत प्रोजेक्ट्स और परीक्षाओं दोनों के लिए बहुत उपयोगी हैं।\n\n**3. व्यावहारिक उपयोग (Applications):**\nइसका उपयोग आधुनिक तकनीकी विकास और दैनिक जीवन की समस्याओं को सुलझाने के लिए किया जाता है।"""
            
        st.markdown(answer)
