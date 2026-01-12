import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech to text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Sun rahi hoon...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="en-in")
        print("Tumne kaha:", command)
        return command.lower()
    except:
        return ""

# Wish user
def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning, main Mira hoon")
    elif hour < 18:
        speak("Good afternoon, main Mira hoon")
    else:
        speak("Good evening, main Mira hoon")

wish()

# Main loop
while True:
    command = listen()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Abhi time hai {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Aaj ki date hai {date}")

    elif "open youtube" in command:
        speak("YouTube khol rahi hoon")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Google khol rahi hoon")
        webbrowser.open("https://google.com")

    elif "open chrome" in command:
        speak("Chrome open kar rahi hoon")
        os.system("google-chrome")

    elif "hello Mira" in command:
        speak("Hello, main Myra hoon. Batao kya madad chahiye")

    elif "exit" in command or "bye" in command:
        speak("Goodbye, milte hain")
        break