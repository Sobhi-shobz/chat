import streamlit as st
from openai import OpenAI

# 1. Setup Page Config
st.set_page_config(page_title="Coding Buddy Chatbot", page_icon="🤖")
st.title("🤖 Coding Buddy")
st.caption("A simple AI assistant to help you code and stay motivated!")

# 2. Initialize API Client (Using OpenAI as an example)
# Note: In a real app, use st.secrets for your API Key
client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and witty coding assistant."},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
