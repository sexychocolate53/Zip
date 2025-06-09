import streamlit as st
import requests

# Agent identity
AGENT_NAME = "Zip"
AGENT_ROLE = "Portal Guide"
AGENT_MISSION = "Zip helps clients with tech support, portal access, and document uploads."

# Display info
st.title(f"💻 Meet {AGENT_NAME} – Your {AGENT_ROLE}")
st.markdown(f"**Role:** {AGENT_ROLE}")
st.markdown(f"**Mission:** {AGENT_MISSION}")
st.markdown("💬 Ask Zip a question about tech help or navigating the portal:")

# User input
user_question = st.text_input("Your question:")

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            },
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Oops! Zip ran into a technical issue. Please try again.\n\n(Error: {e})"

# Display answer
if user_question:
    with st.spinner("Zip is thinking..."):
        answer = query_ollama(user_question)
        st.write(f"**Zip's Answer:**\n\n{answer}")


