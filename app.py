import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from wakeonlan import send_magic_packet
from dotenv import load_dotenv


load_dotenv()
TARGET_MAC = os.getenv("TARGET_MAC")


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = Path("templates/index.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@app.post("/wake")
async def wake():
    if TARGET_MAC:
        send_magic_packet(TARGET_MAC)
        return {"status": "Magic Packet Sent"}
    return {"error": "TARGET_MAC not set"}
