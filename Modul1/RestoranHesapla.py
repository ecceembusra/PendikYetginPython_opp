print("=== Restoran Hesabı Hesaplayıcı ===")

yemek_fiyati = float(input("Toplam yemek fiyatı (TL): "))
bahsis_orani = float(input("Bahşiş oranı (%): "))
kisi_sayisi = int(input("Kaç kişi ödeyecek?: "))

bahsis = yemek_fiyati * (bahsis_orani / 100)
toplam_hesap = yemek_fiyati + bahsis
kisi_basi = toplam_hesap / kisi_sayisi

print("\n--- SONUÇ ---")
print(f"Toplam Yemek Fiyatı : {yemek_fiyati} TL")
print(f"Bahşiş Oranı        : %{bahsis_orani}")
print(f"Bahşiş Tutarı       : {bahsis} TL")
print(f"Toplam Hesap        : {toplam_hesap} TL")
print(f"Kişi Başı Tutar     : {kisi_basi:.2f} TL")