def meter_to_feet(meter):
    return meter * 3.28084

def feet_to_meter(feet):
    return feet / 3.28084

def kg_to_pound(kg):
    return kg * 2.20462

def pound_to_kg(pound):
    return pound / 2.20462

while True:
    print("*****************************")
    print("--- Basit Dönüştürücü ---")
    print("*****************************")
    print("1) Metre  -> Feet")
    print("2) Feet   -> Metre")
    print("3) Kilogram -> Pound")
    print("4) Pound    -> Kilogram")
    print("0) Çıkış")

    secim = input("Seçiminizi girin: ")

    if secim == "0":
        print("Programdan çıkılıyor...")
        break

    # Sayı girişi al
    deger = float(input("Dönüştürülecek değeri girin: "))

    if secim == "1":
        sonuc = meter_to_feet(deger)
        print(f"{deger} metre = {sonuc:.2f} feet")
    elif secim == "2":
        sonuc = feet_to_meter(deger)
        print(f"{deger} feet = {sonuc:.2f} metre")
    elif secim == "3":
        sonuc = kg_to_pound(deger)
        print(f"{deger} kg = {sonuc:.2f} pound")
    elif secim == "4":
        sonuc = pound_to_kg(deger)
        print(f"{deger} pound = {sonuc:.2f} kg")
    else:
        print("Geçersiz seçim! Lütfen 0-4 arasında bir değer girin.")