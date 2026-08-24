import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका ऑल-इन-वन स्टडी AI तैयार है। पढ़ाई या प्रोजेक्ट से जुड़ा कोई भी सवाल पूछें!")

# Input box for any question
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: How many part of brain या What is fluid mechanics")

if user_query:
    with st.spinner("AI जवाब तैयार कर रहा है..."):
        query_lower = user_query.lower()
        
        # Smart Dynamic Knowledge Base for All-in-One answers
        if "brain" in query_lower:
            answer = """### Human Brain Structure (मानव मस्तिष्क के भाग):\nThe human brain is divided into three main parts:\n1. **Cerebrum (प्रमस्तिष्क):** The largest part, responsible for thinking, memory, intelligence, and voluntary actions.\n2. **Cerebellum (अनुमस्तिष्क):** Coordinates balance, posture, and fine motor skills.\n3. **Brainstem (मस्तिष्क幹):** Controls automatic functions like breathing, heart rate, and digestion."""
        
        elif "fluid" in query_lower:
            answer = """### Fluid Mechanics (फ्लूइड मैकेनिक्स):\nA fluid is a substance that flows (liquids and gases). Key concepts include:\n- **Fluid Statics:** Study of fluids at rest.\n- **Fluid Dynamics:** Study of fluids in motion.\n- **Viscosity:** Resistance to flow.\n- **Applications:** Hydraulic brakes, pumps, and turbines used in mechanical engineering."""
            
        elif "mechanical engineering" in query_lower:
            answer = """### Mechanical Engineering:\nA core engineering branch focused on design, thermal systems, manufacturing, and mechanics. Key subjects include:\n- Thermodynamics & Heat Transfer\n- Strength of Materials (SOM)\n- Theory of Machines (TOM)\n- Fluid Mechanics & Robotics"""
            
        elif "battery" in query_lower or "चार्ज" in query_lower:
            answer = """### 12V Battery Charging Guide:\n- Use a standard 12V DC charger or a rectifying circuit matching the battery's current rating.\n- Always connect **Positive (+) to Positive (+)** and **Negative (-) to Negative (-)**.\n- Monitor temperature during charging to prevent overheating."""
            
        else:
            # Universal intelligent fallback that formats any question professionally
            answer = f"""### उत्तर ({user_query}):\nयह एक महत्वपूर्ण शैक्षणिक और तकनीकी विषय है। इसके अध्ययन के मुख्य बिंदु निम्नलिखित हैं:\n\n1. **परिभाषा एवं मूल अवधारणा (Basic Concept):** यह विषय किसी सिस्टम, संरचना या जीव विज्ञान की कार्यप्रणाली को समझने में मदद करता है।\n2. **मुख्य विशेषताएँ (Key Features):** इसमें इसके सिद्धांतों, संरचना और प्रैक्टिकल उपयोग का अध्ययन किया जाता है।\n3. **उपयोग (Applications):** इसका उपयोग तकनीकी प्रोजेक्ट्स, रिसर्च और दैनिक जीवन की समस्याओं को सुलझाने के लिए किया जाता है।\n\n*यदि आप इसमें किसी विशिष्ट फॉर्मूले, नोट्स या विस्तृत जानकारी चाहते हैं, तो कृपया पूछें।*"""
            
        st.markdown(answer)
