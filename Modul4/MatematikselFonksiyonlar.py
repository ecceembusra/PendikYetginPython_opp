#Matematiksel Fonksiyonlar: Trigonometri, logaritma, istatistik fonksiyonları

import math
from statistics import mean, median, pstdev

def trig_fonksiyonlari():
    aci = float(input("Açıyı (derece) girin: "))
    rad = math.radians(aci)
    print("sin:", math.sin(rad))
    print("cos:", math.cos(rad))
    print("tan:", math.tan(rad))

def log_fonksiyonlari():
    x = float(input("Logaritması alınacak sayıyı girin (>0): "))
    if x <= 0:
        print("Sayı 0'dan büyük olmalı.")
        return
    print("ln(x):", math.log(x))
    print("log10(x):", math.log10(x))

def istatistik_fonksiyonlari():
    sayilar_str = input("Sayıları virgülle ayırarak girin (örn: 1,2,3): ")
    sayilar = [float(s.strip()) for s in sayilar_str.split(",")]

    print("Ortalama:", mean(sayilar))
    print("Medyan:", median(sayilar))
    print("Standart sapma:", pstdev(sayilar))

if __name__ == "__main__":
    print("--- Matematiksel Fonksiyonlar ---")
    print("1) Trigonometri")
    print("2) Logaritma")
    print("3) İstatistik")
    secim = input("Seçiminiz: ")

    if secim == "1":
        trig_fonksiyonlari()
    elif secim == "2":
        log_fonksiyonlari()
    elif secim == "3":
        istatistik_fonksiyonlari()
    else:
        print("Geçersiz seçim.")