# websocket_server.py
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI(title="Voice Agents AI - Day 15 WebSocket Echo")

# Simple test page (optional) so you can test in a browser too.
html = """
<!DOCTYPE html>
<html>
  <head><meta charset="utf-8"><title>WS Echo Test</title></head>
  <body>
    <h1>WebSocket Echo Test</h1>
    <textarea id="messages" cols="60" rows="12" readonly></textarea><br>
    <input id="msg" placeholder="Type a message" />
    <button onclick="send()">Send</button>

    <script>
      const ws = new WebSocket("ws://localhost:8000/ws");
      const box = document.getElementById("messages");
      ws.onopen = () => box.value += "Connected to /ws\\n";
      ws.onmessage = (e) => box.value += "Server: " + e.data + "\\n";
      ws.onclose = () => box.value += "Disconnected\\n";
      function send() {
        const i = document.getElementById("msg");
        ws.send(i.value);
        box.value += "You: " + i.value + "\\n";
        i.value = "";
      }
    </script>
  </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except Exception:
        # Client disconnected or other error; just close gracefully
        await websocket.close()
