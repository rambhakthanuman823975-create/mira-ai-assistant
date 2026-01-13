# 🤖 Mira AI Assistant

A **Jarvis‑style offline AI voice assistant** built in **Python**, designed to work on Windows.
Mira can listen, speak, respond romantically like a human, and control your system using voice commands.

---

## ✨ Features

* 🎤 **Voice Recognition** (Speech-to-Text)
* 🔊 **Text-to-Speech (TTS)** with female voice
* 🧠 **Offline Command Processing** (no internet required)
* 💻 **Windows System Control**

  * Open Settings
  * Open Applications
  * Shutdown / Restart / Sleep
* 💬 **Romantic & Human‑like Replies**
* 🧾 **Memory System (basic)**
* ⚡ **Always Listening Mode** (Jarvis‑style)

---

## 🛠️ Technologies Used

* Python 3.11
* `speech_recognition`
* `pyttsx3`
* `pyaudio`
* `os` / `subprocess`
* Windows SAPI5 Voice Engine

---

## 📂 Project Structure

```
mira-ai-assistant/
│
├── myra.py          # Basic assistant logic
├── myra_pro.py      # Advanced assistant with system commands
├── README.md        # Project documentation
```

---

## ▶️ How to Run

### 1️⃣ Install Python 3.11

Download from: [https://www.python.org](https://www.python.org)

### 2️⃣ Install Required Libraries

```bash
pip install speechrecognition pyttsx3 pyaudio
```

> ⚠️ If `pyaudio` fails on Windows, install using a wheel file.

---

### 3️⃣ Run Mira

```bash
python myra_pro.py
```

Mira will say:

> **"Hello, I am Mira. Online and listening."**

---

## 🗣️ Example Voice Commands

* "Open settings"
* "Open YouTube"
* "Shutdown system"
* "Restart computer"
* "Can you hear me?"
* "Bye Mira"

---

## 🧠 Future Upgrades (Planned)

* AI Brain (ChatGPT‑style responses)
* GUI with Jarvis animation
* Wake word detection ("Hey Mira")
* Long‑term memory
* Mobile & Web version

---

## 👨‍💻 Developer

**Ram Bhakt Hanuman**
GitHub: [https://github.com/rambhakthanuman823975-create](https://github.com/rambhakthanuman823975-create)

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🛠️ Contribute

---

❤️ *Mira is not just a program, she listens.*
