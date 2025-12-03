#Öğrenci Devamsızlık Takibi: Tarih bazlı devamsızlık kaydetme ve sorgulama

# veri yapısı: {ogrenci_adi: {tarih1, tarih2, ...}}
devamsizlik_kayitlari = {}

def devamsizlik_ekle():
    ad = input("Öğrenci adı: ")
    tarih = input("Devamsızlık tarihi (GG.AA.YYYY): ")

    if ad not in devamsizlik_kayitlari:
        devamsizlik_kayitlari[ad] = set()
    devamsizlik_kayitlari[ad].add(tarih)
    print("Devamsızlık kaydedildi.")

def ogrenci_sorgula():
    ad = input("Devamsızlıklarını görmek istediğiniz öğrenci adı: ")
    tarihler = devamsizlik_kayitlari.get(ad)
    if not tarihler:
        print("Kayıt bulunamadı.")
    else:
        print(f"{ad} öğrencisinin devamsızlık tarihleri:")
        for t in sorted(tarihler):
            print("-", t)

def tarih_sorgula():
    tarih = input("Hangi tarihte devamsızlık yapan öğrencileri görmek istiyorsunuz? (GG.AA.YYYY): ")
    bulunanlar = [ad for ad, tarihler in devamsizlik_kayitlari.items() if tarih in tarihler]
    if not bulunanlar:
        print("Bu tarihte devamsızlık yapan yok.")
    else:
        print("Bu tarihte devamsızlık yapan öğrenciler:")
        for ad in bulunanlar:
            print("-", ad)

if __name__ == "__main__":
    while True:
        print("\n--- Öğrenci Devamsızlık Takibi ---")
        print("1) Devamsızlık ekle")
        print("2) Öğrenciye göre sorgula")
        print("3) Tarihe göre sorgula")
        print("0) Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            devamsizlik_ekle()
        elif secim == "2":
            ogrenci_sorgula()
        elif secim == "3":
            tarih_sorgula()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")