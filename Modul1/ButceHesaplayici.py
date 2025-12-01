print("=== Kişisel Bütçe Programı ===")

gelir = float(input("Aylık toplam geliriniz: "))

gider_sayisi = int(input("Kaç farklı gider kalemi gireceksiniz? "))

toplam_gider = 0

for i in range(1, gider_sayisi + 1):
    gider = float(input(f"{i}. gider tutarını girin: "))
    toplam_gider += gider

kalan = gelir - toplam_gider

print("\n--- SONUÇ ---")
print(f"Toplam Gelir : {gelir} TL")
print(f"Toplam Gider : {toplam_gider} TL")
print(f"Kalan Para   : {kalan} TL")

if kalan < 0:
    print("Dikkat! Giderler gelirden fazla. Bütçe açığı var.")
else:
    print("Harika! Bütçen dengeli görünüyor.")