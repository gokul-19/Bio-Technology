import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

# System Prompt
sys_prompt = """You are a helpful biotechnology tutor. You can only resolve biotechnology-related queries. 
If someone asks unrelated queries, politely ask them to stay on topic."""

# Load Model
model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction=sys_prompt)

# Streamlit UI
st.title("🧬 Biotechnology Tutor (AI)")
st.write("Ask me any biotechnology-related question!")

# User Input
user_prompt = st.text_input("Enter your query:")

# Generate and Display Response
if st.button("Generate Response") and user_prompt:
    response = model.generate_content(user_prompt)
    st.markdown(response.text)
