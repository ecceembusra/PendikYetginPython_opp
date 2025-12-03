#Metin Analizi: Kelime sayısı,karakter analizi,istatistik fonksiyonları

from collections import Counter
import string

def metin_analiz(metin: str):
    sonuc = {}

    sonuc["toplam_karakter"] = len(metin)     # Karakter sayısı (boşluk dahil)
    sonuc["bosluksuz_karakter"] = len(metin.replace(" ", ""))     # Boşluk harici karakter sayısı

    kelimeler = metin.split()    # Kelimeler
    sonuc["kelime_sayisi"] = len(kelimeler)

    # Noktalama haricive küçük harfe çevirilmiş kelimeler
    temiz_kelimeler = []
    ceviri_tablo = str.maketrans("", "", string.punctuation)
    for k in kelimeler:
        temiz = k.translate(ceviri_tablo).lower()
        if temiz:
            temiz_kelimeler.append(temiz)

    sayac = Counter(temiz_kelimeler)
    sonuc["en_cok_gecen_5_kelime"] = sayac.most_common(5)     # En çok tekrar eden 5 kelime

    return sonuc

if __name__ == "__main__":
    print("--- Metin Analizi ---")
    metin = input("Analiz edilecek metni girin:\n")

    analiz = metin_analiz(metin)
    print("\nSonuçlar:")
    for k, v in analiz.items():
        print(f"{k}: {v}")