import streamlit as st
from google import genai
# Get API Key
api_key = st.secrets["GEMINI_API_KEY"]

# Create Gemini Client
client = genai.Client(api_key=api_key)

# Page Configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

h1 {
    color: white;
    text-align: center;
}

.stMarkdown p {
    color: white;
    font-size: 18px;
}

.stTextArea textarea {
    border-radius: 12px;
    border: 2px solid white;
    font-size: 16px;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

.response-box {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 Gemini AI Chatbot")
st.write("Ask Gemini anything!")

# User Input
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence"
)

# Generate Response
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Response Generated!")

        st.markdown(
            f"""
            <div class="response-box">
                {response.text}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a prompt.")



