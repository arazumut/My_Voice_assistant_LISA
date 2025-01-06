import pyttsx3
import speech_recognition as sr
import datetime
import requests
import os
import platform
import webbrowser
import random

#Produced By K. Umut Araz

engine = pyttsx3.init()

# Türkçe sesi seçin
voices = engine.getProperty('voices')
for voice in voices:
    if 'tr' in voice.id or 'Turkish' in voice.name:  # Türkçe bir ses bulun
        engine.setProperty('voice', voice.id)
        break

def konus(metin):
    """Metni sesli olarak okumak için fonksiyon."""
    engine.say(metin)
    engine.runAndWait()

def hesaplama_yap():
    """Kullanıcıdan iki sayı alıp hangi işlemi yapmak istediğini sorar ve sonucu döner."""
    while True:
        konus("Birinci sayıyı söyleyin.")
        sayi1 = ses_al()
        try:
            sayi1 = float(sayi1)
            break
        except ValueError:
            konus("Bu geçerli bir sayı değil. Lütfen tekrar söyleyin.")
    
    while True:
        konus("İkinci sayıyı söyleyin.")
        sayi2 = ses_al()
        try:
            sayi2 = float(sayi2)
            break
        except ValueError:
            konus("Bu geçerli bir sayı değil. Lütfen tekrar söyleyin.")

    while True:
        konus("Hangi işlemi yapmak istiyorsunuz? Toplama, çıkarma, çarpma veya bölme?")
        islem = ses_al()
        if "toplama" in islem:
            sonuc = sayi1 + sayi2
            konus(f"Sonuç {sonuc}")
            break
        elif "çıkarma" in islem:
            sonuc = sayi1 - sayi2
            konus(f"Sonuç {sonuc}")
            break
        elif "çarpma" in islem:
            sonuc = sayi1 * sayi2
            konus(f"Sonuç {sonuc}")
            break
        elif "bölme" in islem:
            if sayi2 == 0:
                konus("Bir sayıyı sıfıra bölemezsiniz. Lütfen yeni bir sayı söyleyin.")
            else:
                sonuc = sayi1 / sayi2
                konus(f"Sonuç {sonuc}")
                break
        else:
            konus("Geçersiz bir işlem söylediniz. Lütfen toplama, çıkarma, çarpma veya bölme işlemlerinden birini söyleyin.")

def ses_al():
    """Mikrofon aracılığıyla sesli komutları almak ve metne dönüştürmek."""
    tanıyıcı = sr.Recognizer()
    with sr.Microphone() as kaynak:
        print("Dinliyorum...")
        tanıyıcı.adjust_for_ambient_noise(kaynak)  # Arka plan gürültüsünü azaltır
        ses = tanıyıcı.listen(kaynak)
        try:
            komut = tanıyıcı.recognize_google(ses, language='tr-TR')  # Türkçe tanıma
            print(f"Siz: {komut}")
            return komut.lower()
        except sr.UnknownValueError:
            konus("Anlayamadım. Lütfen tekrar edin.")
            return ""
        except sr.RequestError:
            konus("Google API'ye bağlanılamadı.")
            return ""

def saat_al():
    """Tarih ve saat bilgisini geri döndürür."""
    simdi = datetime.datetime.now()
    mevcut_saat = simdi.strftime("%H:%M:%S")
    konus(f"Saat şu anda {mevcut_saat}")

def hava_durumu(sehir):
    """Şehrin hava durumu bilgisini alır."""
    api_anahtari = "cfc113e6ed1c17425febb1dbccc2dd40"  # Buraya kendi OpenWeatherMap API anahtarınızı ekleyin
    temel_url = "http://api.openweathermap.org/data/2.5/weather?"
    tam_url = f"{temel_url}q={sehir}&appid={api_anahtari}&units=metric&lang=tr"

    yanit = requests.get(tam_url)
    veri = yanit.json()

    if veri["cod"] != "404":
        ana = veri["main"]
        sicaklik = ana["temp"]
        hava_aciklama = veri["weather"][0]["description"]
        konus(f"{sehir} şehrinde hava {hava_aciklama} ve sıcaklık {sicaklik} derece.")
    else:
        konus("Şehir bulunamadı.")

def tarayici_ac():
    """Edge tarayıcısını açar."""
    tarayici_yolu = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(tarayici_yolu):
        os.startfile(tarayici_yolu)
    else:
        konus("Edge tarayıcısı bulunamadı.")

def bilgisayari_uyut():
    """Bilgisayarı uyku moduna geçirir."""
    konus("Bilgisayarınızı uyku moduna geçiriyorum.")
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def ses_ayarla():
    """Kullanıcıdan ses seviyesi isteyip sesi ayarlayan fonksiyon."""
    konus("Sesi ne kadar yükselteyim? Yüzde olarak söyleyin.")
    ses_seviyesi = ses_al()
    try:
        seviye = float(ses_seviyesi.replace("%", "").strip()) / 100.0
        if 0 <= seviye <= 1:
            engine.setProperty('volume', seviye)
            konus(f"Ses seviyesi {int(seviye * 100)} olarak ayarlandı.")
        else:
            konus("Lütfen 0 ile 100 arasında bir değer söyleyin.")
    except ValueError:
        konus("Sesi anlamadım, lütfen tekrar edin.")

# Yeni Özellikler:

def youtube_ac():
    """YouTube'u açar."""
    konus("YouTube'u açıyorum.")
    webbrowser.open("https://www.youtube.com")

def linkedin_ac():
    """Linkedin'i açar."""
    konus("Linkedin'i açıyorum.")
    webbrowser.open("https://www.linkedin.com")

def github_ac():
    """Github'ı açar."""
    konus("Github'ı açıyorum.")
    webbrowser.open("https://www.github.com")

def saka_yap():
    """Rastgele bir şaka yapar."""
    sakalar = [
        "Bilgisayar korsanları neden ceket giyer? Çünkü çok fazla verileri vardır!",
        "Matematik kitabı neden üzgündü? Çünkü çok fazla problemi vardı.",
        "Bir mantar neden partide çok popüler? Çünkü o tam bir fungi!"
    ]
    konus(random.choice(sakalar))

def muzik_cal():
    """Bilgisayarda müzik çalar."""
    muzik_klasoru = r"C:\Users\Public\Music"  # Kendi müzik dosya yolunu belirle
    konus("Müziği çalıyorum.")
    sarkilar = os.listdir(muzik_klasoru)
    if sarkilar:
        rastgele_sarki = os.path.join(muzik_klasoru, random.choice(sarkilar))
        os.startfile(rastgele_sarki)
    else:
        konus("Müzik dosyası bulunamadı.")

def haberler_al():
    """Son dakika haberleri getirir."""
    konus("Son dakika haberlerini getiriyorum.")
    webbrowser.open("https://www.bbc.com/news")

def google_ara():
    """Google'da arama yapar."""
    konus("Ne aramak istiyorsunuz?")
    sorgu = ses_al()
    url = f"https://www.google.com/search?q={sorgu}"
    webbrowser.open(url)
    konus(f"{sorgu} için Google'da arama yapıyorum.")

def kod_olustur(gorev):
    """Kullanıcının verdiği göreve göre Python kodu oluşturur."""
    if "toplama" in gorev:
        kod = """
def toplama(a, b):
    return a + b

print(toplama(10, 20))  # Örnek kullanım
"""
        return kod
    elif "çarpma" in gorev:
        kod = """
def carpma(a, b):
    return a * b

print(carpma(10, 20))  # Örnek kullanım
"""
        return kod
    else:
        return "Bu görevi gerçekleştirecek kod bulunamadı."

def kodu_dosyaya_yaz(kod, dosya_adi="uretilen_kod.py"):
    """Üretilen kodu bir dosyaya yazar."""
    with open(dosya_adi, 'w') as dosya:
        dosya.write(kod)
    konus(f"Kod {dosya_adi} dosyasına kaydedildi.")
    print(f"Kod {dosya_adi} dosyasına kaydedildi.")

def asistan():
    konus("Size nasıl yardımcı olabilirim?")
