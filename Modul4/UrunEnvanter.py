#Ürün Envanter Sistemi: Dictionary ile ürün ekleme, stok güncelleme, arama

envanter = {}  # {urun_kodu: {"ad": ..., "stok": ..., "fiyat": ...}}

def urun_ekle():
    kod = input("Ürün kodu: ")
    ad = input("Ürün adı: ")
    stok = int(input("Stok miktarı: "))
    fiyat = float(input("Birim fiyat: "))

    envanter[kod] = {"ad": ad, "stok": stok, "fiyat": fiyat}
    print("Ürün eklendi.")

def stok_guncelle():
    kod = input("Güncellenecek ürün kodu: ")
    if kod not in envanter:
        print("Ürün bulunamadı.")
        return
    yeni_stok = int(input("Yeni stok miktarı: "))
    envanter[kod]["stok"] = yeni_stok
    print("Stok güncellendi.")

def urun_ara():
    kod = input("Aranacak ürün kodu: ")
    urun = envanter.get(kod)
    if not urun:
        print("Ürün bulunamadı.")
        return
    print(f"Kod: {kod} | Ad: {urun['ad']} | Stok: {urun['stok']} | Fiyat: {urun['fiyat']} TL")

def menu():
    print("\n--- Ürün Envanter Sistemi ---")
    print("1) Ürün ekle")
    print("2) Stok güncelle")
    print("3) Ürün ara")
    print("4) Tüm ürünleri listele")
    print("0) Çıkış")

if __name__ == "__main__":
    while True:
        menu()
        secim = input("Seçiminiz: ")

        if secim == "1":
            urun_ekle()
        elif secim == "2":
            stok_guncelle()
        elif secim == "3":
            urun_ara()
        elif secim == "4":
            for kod, u in envanter.items():
                print(f"{kod} -> {u}")
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")