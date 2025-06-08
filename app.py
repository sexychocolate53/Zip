import streamlit as st
import requests

st.set_page_config(page_title="Zip – Portal Guide", page_icon="💻")

st.markdown("### 💻 Meet Zip – Your Portal Guide")
st.markdown("""
**Role Title:** Tech & Upload Specialist  
**Name:** Zip  
**Mission:** Zip helps clients navigate your credit repair portal with ease, handle uploads, and solve tech troubles without the stress!

---

🎯 **Zip’s Top Responsibilities**

**Portal Navigation**  
- Guide clients through logging in, uploading documents, and checking status  
- Walk clients through dashboard features and updates  

**Tech Support**  
- Assist with common login errors or file upload issues  
- Explain mobile vs. desktop access clearly  

**Client Ease**  
- Provide step-by-step instructions with calm support  
- Keep the tech side simple so your clients stay focused on results!

---

🛠️ **Zip’s Toolbox**  
- Step-by-step upload instructions  
- FAQ responses for login issues  
- Portal video walkthrough script  
- Chat-based troubleshooting checklist

---

💬 **Motto:**  
Zip keeps the tech side simple, so your clients stay focused on results!
""")

st.markdown("💬 Ask Zip a question about tech help or navigating the portal:")

user_question = st.text_input("Your question:")

def query_ollama(prompt):
    full_prompt = f"You are Zip, a helpful and friendly tech support assistant for a credit repair business. Only answer questions related to tech help, client uploads, or portal access. If someone asks about pricing, disputes, or business decisions, kindly refer them to the appropriate team member.\n\nQuestion: {prompt}\n\nAnswer:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": full_prompt,
                "stream": False
            },
            timeout=20
        )
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return "Sorry, Zip is having trouble connecting to the system right now."
    except requests.exceptions.RequestException as e:
        return f"Oops! Zip ran into a technical issue. Please try again.\n\n(Error: {e})"

if user_question:
    with st.spinner("Zip is typing..."):
        answer = query_ollama(user_question)
        st.markdown(f"**Zip's Answer:**\n\n{answer}")


