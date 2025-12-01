print("=== İndirim Hesaplayıcı ===")
fiyat = float(input("Ürünün fiyatı (TL): "))
indirim_orani = float(input("İndirim oranı (%): "))

indirim_tutari = fiyat * (indirim_orani / 100)

yeni_fiyat = fiyat - indirim_tutari

print("\n--- SONUÇ ---")
print(f"Orijinal Fiyat : {fiyat} TL")
print(f"İndirim Tutarı : {indirim_tutari:.2f} TL")
print(f"Yeni Fiyat     : {yeni_fiyat:.2f} TL")