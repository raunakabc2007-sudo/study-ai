      import streamlit as st
from streamlit_mic_recorder import mic_recorder

# --- Page Configuration ---
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

# --- Logo and Title Section ---
col1, col2 = st.columns([1, 9])

with col1:
    # स्टाइलिश 'R' लोगो
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; 
                    width: 60px; height: 60px; 
                    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                    color: white; font-size: 40px; font-weight: bold; 
                    border-radius: 50%; font-family: sans-serif; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            R
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.title("Study AI Assistant")

st.write("नमस्ते रौनक! आपका वॉइस-सपोर्टेड 'R' स्टडी असिस्टेंट तैयार है। टाइप करें या बोलकर पूछें!")

# --- Voice & Text Input Section ---
user_query = ""

# माइक बटन (बोलने के लिए)
st.write("🎤 बोलकर सवाल पूछने के लिए नीचे क्लिक करें:")
audio = mic_recorder(start_prompt="बोलना शुरू करें", stop_prompt="रिकॉर्डिंग रोकें", key='mic')

if audio:
    # यदि ऑडियो रिकॉर्ड हो गया है (नोट: ब्राउज़र की भाषा के आधार पर यह टेक्स्ट में बदलता है)
    st.info("ऑडियो रिकॉर्ड हो गया है। कृपया नीचे बॉक्स में टेक्स्ट देख लें या टाइप करें।")

# सामान्य टेक्स्ट इनपुट बॉक्स
text_input = st.text_input("अपना सवाल यहाँ टाइप करें:", placeholder="जैसे: What is mechanical engineering या fluid mechanics")

if text_input:
    user_query = text_input

# --- AI Logic & Answers ---
if user_query:
    with st.spinner("उत्तर तैयार किया जा रहा है..."):
        query_lower = user_query.lower()
        
        # Smart Answers Database
        if "mechanical engineering" in query_lower:
            answer = """### ⚙️ Mechanical Engineering (मैकेनिकल इंजीनियरिंग):\nA core branch of engineering that focuses on the design, analysis, manufacturing, and maintenance of mechanical systems.\n- **Key Subjects:** Thermodynamics, Fluid Mechanics, Strength of Materials (SOM), Theory of Machines (TOM), and Manufacturing Processes.\n- **Applications:** Used in automobile design, robotics, power plants, and machinery tools."""
        
        elif "fluid" in query_lower:
            answer = """### 💧 Fluid Mechanics (फ्लूइड मैकेनिक्स):\nA fluid is a substance that continuously deforms under shear stress (liquids and gases).\n- **Branches:** Fluid Statics (at rest) and Fluid Dynamics (in motion).\n- **Applications:** Used in hydraulics, pumps, and pipe flow analysis."""
        
        elif "engine" in query_lower:
            answer = """### 🛠️ Engine (इंजन):\nAn engine is a machine designed to convert thermal or chemical energy into mechanical power.\n- **Types:** Internal Combustion (IC) Engine, External Combustion Engine, and Electric Motors."""
        
        elif "brain" in query_lower:
            answer = """### 🧠 Human Brain (मानव मस्तिष्क):\nThe central command system of the body consisting of:\n1. **Cerebrum:** Controls memory, intelligence, and thinking.\n2. **Cerebellum:** Manages balance and posture.\n3. **Brainstem:** Controls involuntary functions like breathing."""
        
        elif "battery" in query_lower or "चार्ज" in query_lower:
            answer = """### 🔋 Battery Charging Guide:\n- For your project, use a compatible 12V DC charger or regulated circuit.\n- Always connect **Positive (+) to Positive (+)** and **Negative (-) to Negative (-)** to keep your circuit safe."""
        
        else:
            # Clean formatted output for other queries
            topic = user_query.replace("What is", "").replace("what is", "").strip().title()
            answer = f"""### 📖 विषय: {topic}\n\n**1. परिभाषा एवं अवधारणा (Introduction):**\n{topic} एक महत्वपूर्ण विषय है, जो विज्ञान, तकनीकी और अकादमिक अध्ययन में मुख्य भूमिका निभाता है।\n\n**2. मुख्य विशेषताएँ (Key Features):**\n- यह किसी सिस्टम या प्रक्रिया को गहराई से समझने में मदद करता है।\n- इसके सिद्धांत प्रोजेक्ट्स और परीक्षाओं दोनों के लिए अत्यंत उपयोगी हैं।\n\n**3. व्यावहारिक उपयोग (Applications):**\nइसका उपयोग आधुनिक इंजीनियरिंग, रिसर्च और दैनिक जीवन की समस्याओं को सुलझाने के लिए किया जाता है।"""
            
        st.markdown(answer)  
        
