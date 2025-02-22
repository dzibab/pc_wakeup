# Wake-on-LAN Web App

A simple FastAPI-based web application to wake up a PC in your local network using Wake-on-LAN (WOL). The app provides a single web page with a button that sends a magic packet to wake up the target PC.

## Features
- Web interface with a single button to wake up a PC
- Uses FastAPI for the backend
- Sends Wake-on-LAN magic packets
- Dockerized for easy deployment

## Prerequisites
1. **Enable Wake-on-LAN (WOL)** on your target PC in BIOS and network adapter settings.
2. Your PC should be connected via **Ethernet** (WOL may not work over Wi-Fi).
3. Install **Docker** and **Docker Compose**.

## Installation & Setup

### 1. Clone the Repository
```sh
git clone git@github.com:dzibab/pc_wakeup.git
cd pc_wakeup
```

### 2. Set Up Environment Variables
Create a `.env` file in the project root and add your PC's MAC address:
```
TARGET_MAC=XX:XX:XX:XX:XX:XX  # Replace with your actual MAC address
```
**Important:** Ensure `.env` is added to `.gitignore` to keep your MAC address private.

### 3. Run with Docker Compose
```sh
docker compose up -d
```
This will build and start the application in a container.

### 4. Access the Web Interface
Open `http://localhost:8000/` in your browser and click the **Wake Up PC** button.

## Development (Without Docker)
If you prefer to run the app directly on your system:

### 1. Install Dependencies
```sh
pip install -r requirements.txt
```

### 2. Run the Application
```sh
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Project Structure
```
pc_wakeup/
│── app.py                 # FastAPI application
│── templates/
│   └── index.html         # Web interface
│── Dockerfile             # Docker container setup
│── docker-compose.yml     # Docker Compose configuration
│── requirements.txt       # Python dependencies
│── .env                   # Environment variables (not committed)
│── .gitignore             # Ignore unnecessary files
```
---
🚀 Happy Waking Up Your PC!

