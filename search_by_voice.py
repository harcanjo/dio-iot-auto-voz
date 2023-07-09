import speech_recognition as sr
import webbrowser

speech_engine = sr.Recognizer()

with sr.Microphone() as micro:
    print("Gravando...")
    audio = speech_engine.record(micro, duration=5)
    print("Reconhecendo...")
    text = speech_engine.recognize_google(audio, language="pt-BR")
    print(text)

if text == "Abrir Google" or text == "Google":
    webbrowser.open("https://google.com")
else:
    webbrowser.open("https://wikipedia.org")