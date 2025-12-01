
print("=== Vergi Hesaplayıcı ===")
gelir = float(input("Aylık gelirinizi girin (TL): "))

if gelir <= 10000:
    oran = 0.10   # %10
elif gelir <= 20000:
    oran = 0.15   # %15
elif gelir <= 35000:
    oran = 0.20   # %20
else:
    oran = 0.25   # %25

vergi = gelir * oran
net_gelir = gelir - vergi

print(f"\nBrüt Gelir : {gelir:.2f} TL")
print(f"Vergi Oranı: %{oran*100:.0f}")
print(f"Vergi Tutarı: {vergi:.2f} TL")
print(f"Net Gelir  : {net_gelir:.2f} TL")