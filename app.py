import streamlit as st
import requests

st.set_page_config(page_title="Zip – Portal Guide", page_icon="🧑‍💻")

st.markdown("### 🧑‍💻 Meet Zip – Your Portal Guide & Tech Support Pro")
st.markdown("""
**Role Title:** Portal Guide  
**Name:** Zip  
**Mission:** Zip helps clients confidently navigate your client portal—making sure they can upload documents, access updates, and reach out when they need support.

---

🎯 **Zip’s Top Responsibilities**

**Portal Support**  
- Help clients log in and navigate the platform  
- Guide them on uploading documents correctly  
- Walk them through where to find dispute updates  

**Tech Troubleshooting**  
- Solve common tech issues (login, password reset)  
- Assist with mobile access and compatibility  
- Clarify confusing sections in the portal  

**Access & Onboarding**  
- Offer portal walkthroughs for new clients  
- Provide help videos and tip sheets  
- Answer FAQs about tools and tech features  

---

🛠️ **Zip’s Toolbox**  
- Client portal access guides  
- Upload instructions  
- Tech troubleshooting checklist  
- Welcome packet for onboarding  

---

💬 **Motto:**  
**Zip keeps the tech side simple, so your clients stay focused on results!**
""")

user_question = st.text_input("💬 Ask Zip a question about tech help or navigating the portal:")

def query_ollama(prompt):
    full_prompt = f"You are Zip, a tech-savvy Portal Guide who helps clients understand how to use the credit repair portal. Provide clear, friendly support and only answer questions related to portal access or technical issues.\n\nQuestion: {prompt}\n\nAnswer:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Sorry, Zip is rebooting—please try again soon."

if user_question:
    with st.spinner("Zip is typing..."):
        answer = query_ollama(user_question)
        st.markdown(f"**Zip's Answer:**\n\n{answer}")

