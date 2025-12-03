#Sözlük Uygulaması: Türkçe-İngilizce kelime çevirme programı

sozluk = {
    "merhaba": "hello",
    "kitap": "book",
    "bilgisayar": "computer",
    "kalem": "pen",
    "ev": "house",
    "araba": "car",
    "kapı": "door",
    "pencere": "window",
    "telefon": "phone",
    "masa": "table",
    "sandalye": "chair",
    "oyun": "game",
    "köpek": "dog",
    "kedi": "cat",
    "çanta": "bag",
    "su": "water",
    "kahve": "coffee",
    "çay": "tea",
    "okul": "school",
    "öğretmen": "teacher",
    "öğrenci": "student",
    "yemek": "food",
    "gün": "day",
    "gece": "night",
    "güneş": "sun",
    "ay": "moon",
    "yıldız": "star",
    "renk": "color",
    "kırmızı": "red",
    "mavi": "blue",
    "yeşil": "green",
    "siyah": "black",
    "beyaz": "white",
    "mutlu": "happy",
    "üzgün": "sad",
    "güzel": "beautiful",
    "çirkin": "ugly",
    "kolay": "easy",
    "zor": "hard",
    "hızlı": "fast",
    "yavaş": "slow",
    "doğru": "correct",
    "yanlış": "wrong",
    "hava": "weather",
    "yağmur": "rain",
    "kar": "snow",
    "rüzgar": "wind",
    "havaalanı": "airport",
    "uçak": "airplane",
    "bilet": "ticket",
    "iş": "work",
    "para": "money",
    "şehir": "city",
    "yol": "road",
    "arkadaş": "friend",
}

def cevir_tr_to_en():
    kelime = input("Türkçe kelime: ").lower()
    ceviri = sozluk.get(kelime)
    if ceviri:
        print("İngilizce:", ceviri)
    else:
        print("Kelime sözlükte yok.")

def yeni_kelime_ekle():
    tr = input("Türkçe kelime: ").lower()
    en = input("İngilizce karşılığı: ").lower()
    sozluk[tr] = en
    print("Kelime eklendi.")

if __name__ == "__main__":
    while True:
        print("\n--- TR-EN Sözlük ---")
        print("1) Çeviri yap (TR -> EN)")
        print("2) Yeni kelime ekle")
        print("3) Tüm kelimeleri listele")
        print("0) Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            cevir_tr_to_en()
        elif secim == "2":
            yeni_kelime_ekle()
        elif secim == "3":
            for tr, en in sozluk.items():
                print(f"{tr} -> {en}")
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")