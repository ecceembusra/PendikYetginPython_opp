from datetime import datetime

print("=== Yaşadığın Gün Hesaplayıcı ===")

dogum_tarihi_str = input("Doğum tarihinizi (GG-AA-YYYY formatında) giriniz: ")

dogum_tarihi = datetime.strptime(dogum_tarihi_str, "%d-%m-%Y")

bugun = datetime.now()

yasadigin_gun = (bugun - dogum_tarihi).days
print("-------------------------------------------------------")
print(f"Bugüne kadar toplam {yasadigin_gun} gün yaşadınız")