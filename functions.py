def speak(text):
    """Metni sesli olarak okumak için fonksiyon."""
    engine.say(text)
    engine.runAndWait()

def perform_calculation():
    """Kullanıcıdan iki sayı alıp hangi işlemi yapmak istediğini sorar ve sonucu döner."""
    
    while True:

    #Produced By K. Umut Araz
        speak("Birinci sayıyı söyleyin.")
        num1 = get_audio()

        try:
            num1 = float(num1)
            break
        except ValueError:
            speak("Bu geçerli bir sayı değil. Lütfen tekrar söyleyin.")

    
    
    while True:
        speak("İkinci sayıyı söyleyin.")
        num2 = get_audio()

        try:
            num2 = float(num2)
            break
        except ValueError:
            speak("Bu geçerli bir sayı değil. Lütfen tekrar söyleyin.")

    while True:
        speak("Hangi işlemi yapmak istiyorsunuz? Toplama, çıkarma, çarpma veya bölme?")
        operation = get_audio()

        if "toplama" in operation:
            result = num1 + num2
            
            speak(f"Sonuç {result}")
            break
        elif "çıkarma" in operation:
            result = num1 - num2
            speak(f"Sonuç {result}")
            break
        elif "çarpma" in operation:
            result = num1 * num2
            speak(f"Sonuç {result}")
            break
        elif "bölme" in operation:
            if num2 == 0:
                speak("Bir sayıyı sıfıra bölemezsiniz. Lütfen yeni bir sayı söyleyin.")
            else:
                result = num1 / num2
                speak(f"Sonuç {result}")
                break
        else:
            speak("Geçersiz bir işlem söylediniz. Lütfen toplama, çıkarma, çarpma veya bölme işlemlerinden birini söyleyin.")

def get_audio()
    """Mikrofon aracılığıyla sesli komutları almak ve metne dönüştürmek."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        recognizer.adjust_for_ambient_noise(source)  # Arka plan gürültüsünü azaltır
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='tr-TR')  # Türkçe tanıma
            print(f"Siz: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Anlayamadım. Lütfen tekrar edin.")
            return ""
        except sr.RequestError:
            speak("Google API'ye bağlanılamadı.")
            return ""

def get_time():
    """Tarih ve saat bilgisini geri döndürür."""
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"Saat şu anda {current_time}")

def get_weather(city):
    """Şehrin hava durumu bilgisini alır."""
    api_key = "cfc113e6ed1c17425febb1dbccc2dd40"  # Buraya kendi OpenWeatherMap API anahtarınızı ekleyin
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric&lang=tr"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        weather_desc = data["weather"][0]["description"]
        speak(f"{city} şehrinde hava {weather_desc} ve sıcaklık {temperature} derece.")
    else:
        speak("Şehir bulunamadı.")

def open_browser():
    """Edge tarayıcısını açar."""
    browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    if os.path.exists(browser_path):
        os.startfile(browser_path)
    else:
        speak("Edge tarayıcısı bulunamadı.")

        

def sleep_computer():
    """Bilgisayarı uyku moduna geçirir."""
    speak("Bilgisayarınızı uyku moduna geçiriyorum.")
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def adjust_volume():
    """Kullanıcıdan ses seviyesi isteyip sesi ayarlayan fonksiyon."""
    speak("Sesi ne kadar yükselteyim? Yüzde olarak söyleyin.")
    volume_input = get_audio()


    try:
        volume = float(volume_input.replace("%", "").strip()) / 100.0
        
        if 0 <= volume <= 1:
            engine.setProperty('volume', volume)
            speak(f"Ses seviyesi {int(volume * 100)} olarak ayarlandı.")
        else:
            speak("Lütfen 0 ile 100 arasında bir değer söyleyin.")
    
    except ValueError:
        speak("Sesi anlamadım, lütfen tekrar edin.")

# Yeni Özellikler:

def open_youtube():
    """YouTube'u açar."""
    speak("YouTube'u açıyorum.")
    webbrowser.open("https://www.youtube.com")

def open_linkedin():
    """Linkedin'i açar."""
    speak("Linkedin'i açıyorum.")
    webbrowser.open("https://www.linkedin.com")

def open_github():
    """Github'ı açar."""
    speak("Github'ı açıyorum.")
    webbrowser.open("https://www.github.com")       

def tell_joke():
    """Rastgele bir şaka yapar."""
    jokes = [
        "Bilgisayar korsanları neden ceket giyer? Çünkü çok fazla verileri vardır!",
        "Matematik kitabı neden üzgündü? Çünkü çok fazla problemi vardı.",
        "Bir mantar neden partide çok popüler? Çünkü o tam bir fungi!"
    ]
    speak(random.choice(jokes))

def play_music():
    """Bilgisayarda müzik çalar."""
    music_folder = r"C:\Users\Public\Music"  # Kendi müzik dosya yolunu belirle
    speak("Müziği çalıyorum.")
    songs = os.listdir(music_folder)
    if songs:
        random_song = os.path.join(music_folder, random.choice(songs))
        os.startfile(random_song)
    else:
        speak("Müzik dosyası bulunamadı.")

def get_news():
    """Son dakika haberleri getirir."""
    speak("Son dakika haberlerini getiriyorum.")
    webbrowser.open("https://www.bbc.com/news")

def search_google():
    """Google'da arama yapar."""
    speak("Ne aramak istiyorsunuz?")
    query = get_audio()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"{query} için Google'da arama yapıyorum.")

def generate_code(task):
    """Kullanıcının verdiği göreve göre Python kodu oluşturur."""
    if "toplama" in task:
        code = """
def toplama(a, b):
    return a + b

print(toplama(10, 20))  # Örnek kullanım
"""
        return code
    elif "çarpma" in task:
        code = """
def carpma(a, b):
    return a * b

print(carpma(10, 20))  # Örnek kullanım
"""
        return code
    else:
        return "Bu görevi gerçekleştirecek kod bulunamadı."

def write_code_to_file(code, filename="generated_code.py"):
    """Üretilen kodu bir dosyaya yazar."""
    with open(filename, 'w') as file:
        file.write(code)
    speak(f"Kod {filename} dosyasına kaydedildi.")
    print(f"Kod {filename} dosyasına kaydedildi.")

def assistant():
    speak("Size nasıl yardımcı olabilirim?")
