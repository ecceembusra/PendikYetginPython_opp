print("=== Sınıf Geçme Sistemi ===")

not1 = float(input("1. sınav notu: "))
not2 = float(input("2. sınav notu: "))
not3 = float(input("3. sınav notu: "))

ortalama = (not1 + not2 + not3) / 3

# Harf Notu
if ortalama >= 90:
    harf = "AA"
elif ortalama >= 80:
    harf = "BA"
elif ortalama >= 70:
    harf = "BB"
elif ortalama >= 60:
    harf = "CB"
elif ortalama >= 50:
    harf = "CC"
else:
    harf = "FF"

print(f"\nOrtalama: {ortalama:.2f} → Harf Notu: {harf}")

if ortalama >= 50:
    print("Tebrikler, geçtiniz!")
else:
    print("Maalesef kaldınız.")