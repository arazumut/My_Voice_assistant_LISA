<a href="https://www.python.org" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
    </a> <br>
Sesli asistanım olan Lisa, kullanıcının sesli komutlarını algılayarak çeşitli işlemler yapabiliyor, örneğin hava durumu sorgulama, saat öğrenme, hesaplama yapma, şaka yapma, uygulama açma, not alma, müzik çalma, ve hatta yapay zeka ile sohbet etme gibi işlevler sunuyor.

Kodun Temel İşlevleri:
Sesli Yanıt Verme (Text-to-Speech): pyttsx3 kütüphanesi kullanılarak, asistan kullanıcıya cevap verirken metni sesli okuyor.

speak(text) fonksiyonu, aldığı metni sesli olarak kullanıcının duymasını sağlıyor.
Sesli Komut Alma (Speech Recognition): speech_recognition kütüphanesi kullanarak, mikrofon aracılığıyla kullanıcının söylediği kelimeler metne dönüştürülüyor.



get_audio() fonksiyonu, mikrofonu dinleyerek kullanıcının söylediği kelimeleri algılar ve metne dönüştürür.
Hesaplama Yapma: perform_calculation() fonksiyonu, kullanıcının verdiği iki sayıyı toplama, çıkarma, çarpma veya bölme gibi işlemler yaparak sonucu sesli olarak bildiriyor.

Hava Durumu Bilgisi Alma: get_weather(city) fonksiyonu, OpenWeatherMap API'sini kullanarak belirtilen şehrin hava durumu bilgisini alır ve bunu kullanıcının duyabileceği şekilde sesli olarak söyler.

Tarayıcı Açma ve Uygulama Açma: Tarayıcı açma ve belirli sitelere yönlendirme işlevi sunar (YouTube, LinkedIn, GitHub). Ayrıca open_application(app_name) fonksiyonu ile not defteri veya hesap makinesi gibi uygulamaları açar.

Yapay Zeka ile Sohbet: chat_with_ai() fonksiyonu OpenAI'nin ChatGPT modelini kullanarak kullanıcının sorularına yanıt verir.

Şaka Yapma, Gerçek Söyleme ve Müzik Çalma: Kullanıcı isteğine göre rastgele bir şaka yapabilir, eğlenceli bir bilgi verebilir veya bilgisayarda yüklü olan müzikleri çalabilir.

Not Alma ve Listeleme: Kullanıcı sesli bir not bırakabilir ve bu notlar daha sonra sesli olarak listelenebilir.

Oyun: play_guess_number() fonksiyonu bir sayı tahmin oyunu sunuyor, kullanıcının 1 ile 10 arasında bir sayı tahmin etmesini bekliyor.

Nasıl Çalıştırılır:
Kurulum Gereksinimleri:


pyttsx3, speech_recognition, openai, ve requests gibi kütüphanelerin yüklü olması gerekir. Bunları şu komutla yükleyebilirsiniz:
 

<h1>pip install pyttsx3 speechrecognition openai requests</h1>

API Anahtarları:

OpenWeatherMap'ten hava durumu bilgisi almak için bir API anahtarına ihtiyacınız var. Bu anahtarı get_weather() fonksiyonundaki api_key değişkenine eklemelisiniz.
ChatGPT kullanımı için de OpenAI API anahtarınızı openai.api_key kısmına eklemeniz gerekiyor.
Çalıştırma:

Kodun en altında yer alan if __name__ == "__main__": assistant() satırı, programın çalışmasını başlatıyor.
Bu kodu bir Python dosyası olarak (asistan.py gibi) kaydedip çalıştırabilirsiniz.
Çalıştırdığınızda mikrofonu kullanarak komut vermeye başlayabilirsiniz. Örneğin, "Saat kaç?", "Hava durumu nasıl?", "Hesaplama yap", "Müzik çal" gibi komutlar verebilirsiniz.
Sesli asistan, verilen komutlara göre ilgili işlemi gerçekleştirip size sesli geri bildirim verir.
