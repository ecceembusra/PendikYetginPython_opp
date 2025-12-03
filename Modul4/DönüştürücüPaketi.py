#Dönüştürücü Paketi: Birim dönüştürme fonksiyonları (sıcaklık, uzunluk, ağırlık)

def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_mile(km):
    return km * 0.621371

def mile_to_km(mile):
    return mile / 0.621371

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def menu():
    print("\n--- Dönüştürücü Paketi ---")
    print("1) Sıcaklık: C -> F")
    print("2) Sıcaklık: F -> C")
    print("3) Uzunluk: Km -> Mil")
    print("4) Uzunluk: Mil -> Km")
    print("5) Ağırlık: Kg -> Libre")
    print("6) Ağırlık: Libre -> Kg")
    print("0) Çıkış")

if __name__ == "__main__":
    while True:
        menu()
        secim = input("Seçiminiz: ")

        if secim == "0":
            break

        deger = float(input("Dönüştürülecek değeri girin: "))

        if secim == "1":
            print("Sonuç:", c_to_f(deger), "F")
        elif secim == "2":
            print("Sonuç:", f_to_c(deger), "C")
        elif secim == "3":
            print("Sonuç:", km_to_mile(deger), "mil")
        elif secim == "4":
            print("Sonuç:", mile_to_km(deger), "km")
        elif secim == "5":
            print("Sonuç:", kg_to_lb(deger), "lb")
        elif secim == "6":
            print("Sonuç:", lb_to_kg(deger), "kg")
        else:
            print("Geçersiz seçim.")