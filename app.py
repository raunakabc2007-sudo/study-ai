     import streamlit as st

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

st.write("नमस्ते रौनक! आपका बिना की वाला 'R' स्टडी असिस्टेंट तैयार है। अपने पढ़ाई या प्रोजेक्ट से जुड़ा सवाल पूछें!")

# --- Input Box ---
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is fluid mechanics, Engine या Brain")

if user_query:
    with st.spinner("उत्तर तैयार किया जा रहा है..."):
        query_lower = user_query.lower()
        
        # Smart Answers Database
        if "fluid" in query_lower:
            answer = """### 💧 Fluid Mechanics (फ्लूइड मैकेनिक्स):\nA fluid is a substance that continuously deforms (flows) under shear stress (liquids and gases).\n- **Branches:** Fluid Statics (at rest) and Fluid Dynamics (in motion).\n- **Applications:** Used in hydraulics, pumps, and pipe flow analysis in mechanical engineering."""
        
        elif "engine" in query_lower:
            answer = """### ⚙️ Engine (इंजन):\nAn engine converts thermal or chemical energy into mechanical power.\n- **Types:** Internal Combustion (IC) Engine, External Combustion Engine, Electric Motors.\n- **Components:** Cylinder, piston, crankshaft, and valves."""
        
        elif "brain" in query_lower:
            answer = """### 🧠 Human Brain (मानव मस्तिष्क):\nThe control center of the nervous system consisting of:\n1. **Cerebrum:** Controls memory and intelligence.\n2. **Cerebellum:** Controls balance and coordination.\n3. **Brainstem:** Controls involuntary functions like breathing."""
        
        elif "battery" in query_lower or "चार्ज" in query_lower:
            answer = """### 🔋 Battery Charging Guide:\n- For a 12V battery project, use a compatible DC charger or regulated rectifier.\n- Always maintain correct polarity (**Positive to Positive, Negative to Negative**) to prevent short circuits."""
        
        elif "mechanical engineering" in query_lower:
            answer = """### 🛠️ Mechanical Engineering:\nA core engineering discipline focused on designing, manufacturing, and maintaining mechanical systems, thermal power, and machine tools."""
        
        else:
            # Clean automated formatting for any other question
            topic = user_query.replace("What is", "").replace("what is", "").strip().title()
            answer = f"""### 📖 विषय: {topic}\n\n**1. मुख्य परिभाषा (Introduction):**\n{topic} एक महत्वपूर्ण शैक्षणिक और तकनीकी विषय है, जिसका उपयोग प्रोजेक्ट्स और परीक्षाओं में किया जाता है।\n\n**2. मुख्य बिंदु (Key Characteristics):**\n- यह विषय किसी सिस्टम या प्रक्रिया की कार्यप्रणाली को गहराई से समझने में मदद करता है।\n- इसके सिद्धांत व्यावहारिक विज्ञान और इंजीनियरिंग में अत्यधिक उपयोगी हैं।\n\n**3. उपयोग (Applications):**\nइसका उपयोग आधुनिक तकनीकी विकास और समस्याओं के समाधान के लिए किया जाता है।"""
            
        st.markdown(answer)    
