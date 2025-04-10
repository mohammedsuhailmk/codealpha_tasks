import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 180)
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def run_assistant():
    command = listen_command()

    if 'play' in command:
        song = command.replace('play', '')
        speak('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)

    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').replace('what is', '')
        info = wikipedia.summary(person, 1)
        speak(info)

    elif 'hello' in command:
        speak('Hello! I am your assistant. How can I help you?')

    elif 'bye' in command or 'exit' in command or 'stop' in command:
        speak('Goodbye!')
        exit()

    else:
        speak("I don't know how to do that yet.")

speak("Hi! I am your voice assistant.")
while True:
    run_assistant()
