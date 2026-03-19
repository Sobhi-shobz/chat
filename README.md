🤖 AI Chatbot: The Coding Buddy
A sleek, responsive web-based chatbot designed to help developers debug code, learn new concepts, and stay motivated during long coding sessions.

🚀 Quick Start (Local Setup)
Follow these steps to get the chatbot running on your machine:

Clone the Repository

git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name


Create a Virtual Environment (Recommended)

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Create a Virtual Environment (Recommended)

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

set Up API Keys

Create a .env file in the root directory.

Add your API key: OPENAI_API_KEY=your_key_here


Run the App

Bash
streamlit run app.py

Technical Approach
For this project, I implemented a Generative AI API approach using the following stack:

Frontend: Streamlit for a rapid, Python-native web interface.

Brain: [OpenAI GPT-3.5/4] (or Groq/Llama) via API for natural language processing.

Memory: Utilized Streamlit's session_state to maintain conversation context, allowing the bot to "remember" previous parts of the chat.

What makes this unique?
Unlike standard bots, this "Coding Buddy" is programmed with a specific System Prompt that prioritizes concise code snippets and uses a witty, encouraging tone to reduce developer burnout.


Challenges & Solutions
1. The "Memory" Problem
Challenge: Every time the user sent a message, the Streamlit app would rerun, causing the chat history to wipe clean.

Solution: I implemented st.session_state to store a list of messages. This ensures the history persists across reruns and is sent back to the API so the AI understands the context.

2. API Security
Challenge: I initially realized that pushing my API key to GitHub would be a major security risk.

Solution: I moved the sensitive credentials into a .env file and added that file to .gitignore. I also added a check in the code to warn the user if the key is missing.

3. UI/UX Flow
Challenge: The chat felt "static" while waiting for the AI to process a long answer.

Solution: I used st.write_stream to display the AI's response word-by-word (streaming), making the interaction feel more like a real-time conversation.
