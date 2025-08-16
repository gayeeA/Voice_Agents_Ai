# Day 15: WebSockets

Welcome to Day 15 of the 30 Days of Voice Agents Challenge! 🎉  
We’ve officially reached the halfway mark and introduced **real-time communication** into our app using WebSockets.  

## 🧠 What We Built
- **WebSocket Endpoint**: Added `/ws` to the FastAPI server.  
- **Echo Server**: Any message sent by the client is echoed back by the server.  
- **Postman Test**: Successfully sent and received messages in real-time.  
- **Browser Test Page**: Added a small HTML page to interact with the WebSocket visually.  

This sets the foundation for **streaming responses** from our AI agent in future days, making the conversation feel much more natural and instant.  

## 🛠 Tech Stack

- **Backend**: `FastAPI`, `uvicorn`, `python-dotenv`, `requests`, `jinja2`, `assemblyai`, `google-generativeai`
- **Frontend**: `HTML`, `Bootstrap`, `JavaScript`, `MediaRecorder` API
- **AI APIs**:
  - Murf AI (Text-to-Speech)
  - AssemblyAI (Speech-to-Text)
  - Google Gemini (Large Language Model)

## 🚀 Run the App

1. **Navigate to the project directory:**
   ```bash
   cd day-14/
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt


3. **Create a .env file in the day-14/ directory and add your API keys:**

MURF_API_KEY="your_murf_api_key_here"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
GEMINI_API_KEY="your_gemini_api_key_here"


4. **Run the FastAPI server:**
  ```bash
  uvicorn main:app --reload
  ```
Open your browser and visit http://localhost:8000. 
Grant microphone permissions if prompted.

📂 Project Structure
```bash
day-14/
├── main.py           # Main FastAPI application logic
├── config.py         # API key loading and configuration
├── schemas.py        # Pydantic data schemas
├── services/
│   ├── __init__.py
│   ├── stt.py        # Speech-to-Text service module
│   ├── llm.py        # Language Model service module
│   └── tts.py        # Text-to-Speech service module
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── fallback.mp3
├── requirements.txt
└── .env
```


**Browser Test:** Visit http://localhost:8000 and send a message

**Postman Test:** Connect to ws://localhost:8000/ws, send a message, and see the echo

📂 Project Structure (new additions)
```bash
├── websocket_server.py   # New WebSocket echo server (Day 15)
```



