# 🤟 EchoSign – Sign Language Recognition & Text-to-Sign System

EchoSign is an AI-powered accessibility project designed to break communication barriers between sign language users and non-signers.

This repository contains two core Python modules:

- `hand_detect.py` → Detects hand gestures using MediaPipe and OpenCV.
- `text_to_sign.py` → Converts input text into corresponding sign language images.

Built for Hackathon 2026 🚀  
Focus: Accessibility • AI • Real-time Interaction

---

## 📌 Features

### ✋ Hand Gesture Detection (`hand_detect.py`)
- Uses MediaPipe Hands for landmark detection
- Detects gestures like:
  - OK
  - YES
  - NO
  - STOP
  - LOVE
  - L
  - U
  - I
  - F
- Displays detected gesture in real-time on webcam feed
- Built using:
  - OpenCV
  - MediaPipe
  - Python

---

### 🔤 Text to Sign Conversion (`text_to_sign.py`)
- Accepts input text
- Checks if full word sign image exists
- If not found → breaks word into letters
- Returns corresponding sign image paths from `signs/` folder
- Supports:
  - `.jpg`
  - `.jpeg`
- Works as backend API function

