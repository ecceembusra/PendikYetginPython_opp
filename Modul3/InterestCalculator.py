# Compound Interest Calculator
# Bileşik faiz hesaplayan program (Yıl yıl gösterilir)

ana_para = float(input("Ana para: "))
oran = float(input("Faiz oranı (%): ")) / 100
yil = int(input("Kaç yıl hesaplanacak? "))

print("\nYıl Yıl Bileşik Faiz Tablosu:\n")

for i in range(1, yil + 1):
    ana_para = ana_para * (1 + oran)
    print(f"{i}. yıl sonunda toplam para: {ana_para:.2f} TL")