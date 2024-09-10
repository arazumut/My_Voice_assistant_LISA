import pyttsx3

engine = pyttsx3.init()

# Türkçe sesi seçin
voices = engine.getProperty('voices')
for voice in voices:
    if 'tr' in voice.id or 'Turkish' in voice.name:  # Türkçe bir ses bulun
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Merhaba, size nasıl yardımcı olabilirim?")
