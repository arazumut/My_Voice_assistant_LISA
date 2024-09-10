import pyttsx3

engine = pyttsx3.init()

# Kullanılabilir sesleri listele
voices = engine.getProperty('voices')

for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}, Language: {voice.languages}")
