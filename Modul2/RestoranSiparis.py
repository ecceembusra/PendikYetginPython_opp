print("=== Restoran Sipariş Sistemi ===")

menu = {
    1: ("Pizza", 120),
    2: ("Hamburger", 90),
    3: ("Makarna", 75),
    4: ("Salata", 60),
    5: ("İçecek", 25)
}

toplam = 0

while True:
    print("\n--- MENÜ ---")
    for no, (isim, fiyat) in menu.items():
        print(f"{no}) {isim} - {fiyat} TL")
    print("0) Siparişi Bitir")

    secim = int(input("Seçiminiz: "))

    if secim == 0:
        break

    if secim not in menu:
        print("Geçersiz seçim!")
        continue

    adet = int(input("Kaç adet istiyorsunuz? "))

    urun_adi, fiyat = menu[secim]
    ara_tutar = fiyat * adet
    toplam += ara_tutar

    print(f"{adet} adet {urun_adi} eklendi. Ara toplam: {ara_tutar} TL")

print(f"\nÖdenecek Toplam Tutar: {toplam} TL")
print("Afiyet olsun!")