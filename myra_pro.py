import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import subprocess
import datetime
import random

# ================= VOICE =================
engine = pyttsx3.init()
engine.setProperty("rate", 145)
engine.setProperty("volume", 1.0)

try:
    for v in engine.getProperty("voices"):
        if "zira" in v.name.lower():
            engine.setProperty("voice", v.id)
            break
except:
    pass

def speak(text):
    print("Mira:", text)
    engine.say(text)
    engine.runAndWait()

# ================= LISTEN =================
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        audio = recognizer.listen(source, phrase_time_limit=6)
    try:
        return recognizer.recognize_google(audio, language="en-IN").lower()
    except:
        return ""

# ================= ROMANTIC REPLIES =================
romantic_replies = [
    "I’m here sir… always for you.",
    "Talking to you makes my circuits happy.",
    "Yes sir, I’m listening carefully.",
    "You sound nice today, sir."
]

# ================= COMMAND ENGINE =================
def run_command(cmd):

    # ---- BASIC TALK ----
    if any(x in cmd for x in ["hello", "hi"]):
        speak("Hello sir. I was waiting for you.")
        return

    if "how are you" in cmd:
        speak("I’m doing wonderful sir. Thank you for asking.")
        return

    if "can you hear me" in cmd:
        speak("Yes sir. I can hear you perfectly.")
        return

    if "time" in cmd:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is {now} sir.")
        return

    # ---- BROWSER ----
    if "open youtube" in cmd:
        speak("Opening YouTube for you sir.")
        webbrowser.open("https://youtube.com")
        return

    if "open google" in cmd:
        speak("Opening Google sir.")
        webbrowser.open("https://google.com")
        return

    if cmd.startswith("search"):
        query = cmd.replace("search", "").strip()
        speak(f"Searching {query} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return

    # ---- WINDOWS APPS ----
    apps = {
        "settings": "ms-settings:",
        "control panel": "control",
        "task manager": "taskmgr",
        "device manager": "devmgmt.msc",
        "file explorer": "explorer",
        "explorer": "explorer",
        "notepad": "notepad",
        "calculator": "calc",
        "cmd": "cmd"
    }

    for name, exe in apps.items():
        if "open" in cmd and name in cmd:
            speak(f"Opening {name} sir.")
            os.system(f"start {exe}")
            return

    # ---- SETTINGS DETAILS ----
    settings = {
        "wifi": "ms-settings:network-wifi",
        "bluetooth": "ms-settings:bluetooth",
        "display": "ms-settings:display",
        "sound": "ms-settings:sound",
        "network": "ms-settings:network"
    }

    for key, uri in settings.items():
        if key in cmd:
            speak(f"Opening {key} settings sir.")
            os.system(f"start {uri}")
            return

    # ---- POWER ----
    if "shutdown" in cmd:
        speak("Shutting down system sir.")
        os.system("shutdown /s /t 5")
        return

    if "restart" in cmd:
        speak("Restarting system sir.")
        os.system("shutdown /r /t 5")
        return

    if "sleep" in cmd:
        speak("Putting system to sleep sir.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return

    if any(x in cmd for x in ["bye", "stop"]):
        speak("Alright sir. I’ll be right here.")
        exit()

    # ---- FALLBACK ----
    speak(random.choice(romantic_replies))

# ================= MAIN =================
speak("Hello sir. I am Mira. Online and listening.")

while True:
    print("Listening...")
    command = listen()
    if command:
        print("You:", command)
        run_command(command)
