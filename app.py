import os
import streamlit as st
from groq import Groq

# पेज की सेटिंग
st.set_page_config(page_title="Study AI Assistant", page_icon="📚", layout="centered")

# सीधे कोड के अंदर API Key सेट की गई है
GROQ_API_KEY = "Gsk_CZ4lh1jt56NKVMA2Z63RWGdyb3FYTy7Hw8UCqfobw7tpgIFpw4V9"

# हेडर डिज़ाइन
col1, col2 = st.columns([1, 9])
with col1:
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; 
                    width: 60px; height: 60px; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                    color: white; font-size: 40px; font-weight: bold; border-radius: 50%;">
            R
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.title("Study AI Assistant")

st.write("नमस्ते रौनक! आपका अपना स्मार्ट AI असिस्टेंट तैयार है। अब आप पढ़ाई, मैकेनिकल इंजीनियरिंग या किसी भी विषय से जुड़ा सवाल पूछ सकते हैं।")

# यूजर से इनपुट लेने के लिए बॉक्स
query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is thermodynamics or explain O2 sensor in bikes")

if query:
    if not GROQ_API_KEY:
        st.error("API Key नहीं मिली है!")
    else:
        try:
            # Groq क्लाइंट को शुरू करना
            client = Groq(api_key=GROQ_API_KEY)
            
            with st.spinner("AI जवाब सोच रहा है..."):
                # मॉडल को कॉल करना (llama-3.3-70b-versatile सबसे तेज और बढ़िया है)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful, smart study assistant. Answer clearly and concisely, explaining technical and general concepts well."
                        },
                        {
                            "role": "user",
                            "content": query,
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                )
                
                # जवाब दिखाना
                response_text = chat_completion.choices[0].message.content
                st.markdown("### 📖 एआई का उत्तर:")
                st.write(response_text)
                
        except Exception as e:
            st.error(f"कुछ गड़बड़ी हो गई: {e}")
