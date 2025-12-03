#E-Ticaret Sepeti: Ürün ekleme, çıkarma, toplam fiyat hesaplama

sepet = []  # her eleman: {"ad": ..., "fiyat": ..., "adet": ...}

def urun_ekle():
    ad = input("Ürün adı: ")
    fiyat = float(input("Birim fiyat: "))
    adet = int(input("Adet: "))
    sepet.append({"ad": ad, "fiyat": fiyat, "adet": adet})
    print("Ürün sepete eklendi.")

def urun_cikar():
    ad = input("Sepetten çıkarılacak ürün adı: ")
    for urun in sepet:
        if urun["ad"].lower() == ad.lower():
            sepet.remove(urun)
            print("Ürün sepetten çıkarıldı.")
            return
    print("Ürün sepette bulunamadı.")

def toplam_tutar():
    toplam = sum(urun["fiyat"] * urun["adet"] for urun in sepet)
    print("Toplam tutar:", toplam, "TL")

def sepet_goruntule():
    if not sepet:
        print("Sepet boş.")
        return
    for urun in sepet:
        print(f"{urun['ad']} - {urun['adet']} adet - {urun['fiyat']} TL")

if __name__ == "__main__":
    while True:
        print("\n--- E-Ticaret Sepeti ---")
        print("1) Ürün ekle")
        print("2) Ürün çıkar")
        print("3) Sepeti görüntüle")
        print("4) Toplam fiyatı hesapla")
        print("0) Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            urun_ekle()
        elif secim == "2":
            urun_cikar()
        elif secim == "3":
            sepet_goruntule()
        elif secim == "4":
            toplam_tutar()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")