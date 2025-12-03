# Hesap Makinesi (dört işlem+gelişmiş)

import math

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme yapılamaz."
    return a / b

def us_alma(a, b):
    return a ** b

def karekok(a):
    if a < 0:
        return "Hata: Negatif sayının karekökü reel değildir."
    return math.sqrt(a)

def menu():
    print("\n--- Hesap Makinesi ---")
    print("1) Toplama")
    print("2) Çıkarma")
    print("3) Çarpma")
    print("4) Bölme")
    print("5) Üs Alma (a^b)")
    print("6) KareköK")
    print("0) Çıkış")

while True:
    menu()
    secim = input("Seçiminiz: ")

    if secim == "0":
        print("Programdan çıkılıyor...")
        break

    if secim == "6":
        a = float(input("Sayı girin: "))
        print("Sonuç:", karekok(a))
    else:
        a = float(input("Birinci sayıyı girin: "))
        b = float(input("İkinci sayıyı girin: "))

        if secim == "1":
            print("Sonuç:", toplama(a, b))
        elif secim == "2":
            print("Sonuç:", cikarma(a, b))
        elif secim == "3":
            print("Sonuç:", carpma(a, b))
        elif secim == "4":
            print("Sonuç:", bolme(a, b))
        elif secim == "5":
            print("Sonuç:", us_alma(a, b))
        else:
            print("Geçersiz seçim.")