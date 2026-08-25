         import streamlit as st
import google.generativeai as genai
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",  # Default favicon
    layout="centered"
)

# --- Logo and Title Section ---
# यह कोड आपके टाइटल के बगल में 'R' लोगो और 'Study AI Assistant' टेक्स्ट को एक साथ दिखाता है
col1, col2 = st.columns([1, 9])

with col1:
    # यहाँ 'R' का स्टाइलिश लोगो दिखाया गया है
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
    # यह आपका मुख्य टाइटल और वेलकम मैसेज है
    st.title("Study AI Assistant")

st.write("नमस्ते रौनक! आपका पर्सनलाइज़्ड 'R' AI पूरी तरह एक्टिव है। अपने मैकेनिकल इंजीनियरिंग या प्रोजेक्ट से जुड़ा सवाल पूछें!")

# --- AI Setup with Streamlit Secrets ---
try:
    # 1. API Key को Streamlit Secrets से सुरक्षित रूप से लें
    # (यह की आपके Streamlit डैशबोर्ड के Secrets बॉक्स में होनी चाहिए)
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # 2. Gemini Model को सेट करें (Gemini 1.5 Flash सबसे तेज़ है)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
except Exception as e:
    st.error(f"API Key लोड करने में समस्या आई। कृपया Streamlit Secrets में 'GEMINI_API_KEY' सही तरह से सेव करें। एरर: {e}")
    st.stop() # की न मिलने पर ऐप आगे नहीं चलेगी

# --- User Input and AI Processing ---
# इनपुट बॉक्स
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is fluid dynamics या Explain Bernoulli's principle")

if user_query:
    with st.spinner("रौनक का 'R' AI जवाब सोच रहा है..."):
        try:
            # 3. AI को सवाल भेजना और जवाब पाना
            response = model.generate_content(user_query)
            
            # 4. AI के जवाब को स्क्रीन पर दिखाना
            st.markdown("### उत्तर:")
            st.success(response.text)
            
        except Exception as e:
            st.error(f"जवाब जनरेट करते समय एक एरर आया: {e}")
            st.info("यह अक्सर API Key की लिमिट खत्म होने या नेटवर्क की समस्या के कारण होता है।")   
