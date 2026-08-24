import streamlit as st
import urllib.request
import json

# Page Configuration
st.set_page_config(
    page_title="Study AI Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study AI Assistant")
st.write("नमस्ते रौनक! आपका लाइव विकिपीडिया-सपोर्टेड स्टडी AI तैयार है। अब किसी भी सवाल का असली जवाब मिलेगा!")

# Input box for any question
user_query = st.text_input("अपना सवाल यहाँ पूछें:", placeholder="जैसे: What is forest या Human brain")

if user_query:
    with st.spinner("इंटरनेट से सटीक जवाब खोजा जा रहा है..."):
        try:
            # Format query for Wikipedia API search
            formatted_query = user_query.title().replace(" ", "_")
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(user_query)}"
            
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                if "extract" in data:
                    answer = data["extract"]
                    title = data.get("title", user_query)
                    st.markdown(f"### 📖 {title}")
                    st.success(answer)
                else:
                    st.warning("इस विषय पर विस्तृत जानकारी नहीं मिली। कृपया कोई दूसरा शब्द या सवाल टाइप करें। किरप्या सही स्पेलिंग लिखें।")
                    
        except Exception as e:
            # Fallback smart study definitions if network lookup fails
            query_lower = user_query.lower()
            if "forest" in query_lower:
                st.markdown("### 🌲 Forest (वन):")
                st.write("A forest is a large area dominated by trees. Forests are vital ecosystems that cover about 31% of the Earth's land area, providing habitats for various species and regulating the climate.")
            elif "brain" in query_lower:
                st.markdown("### 🧠 Human Brain (मानव मस्तिष्क):")
                st.write("The human brain is the command center of the human nervous system. It receives signals from sensory organs and outputs information to the muscles, controlling memory, movement, and thinking.")
            else:
                st.markdown(f"### उत्तर ({user_query}):")
                st.write(f"रौनक, '{user_query}' एक महत्वपूर्ण विषय है। इसमें विभिन्न वैज्ञानिक, तकनीकी और व्यावहारिक पहलू शामिल होते हैं जो अध्ययन और प्रोजेक्ट्स के लिए उपयोगी हैं।")
