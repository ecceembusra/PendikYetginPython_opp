# Advanced Number Guess Game
"""
Min–max ipucu + puan sistemi
	•	1–100 arası sayı tutulur
	•	Her yanlışta min–max aralığı daraltılır
	•	100 üzerinden puan düşer
"""

import random

sayi = random.randint(1, 100)
puan = 100
hak = 7

min_sayi = 1
max_sayi = 100

print("1-100 arasında bir sayı tuttum. Bakalım bulabilecek misin!")

while hak > 0:
    print(f"\nTahmin aralığın: {min_sayi} - {max_sayi}")
    tahmin = int(input("Tahmininiz: "))

    if tahmin == sayi:
        print("\nTebrikler! Doğru bildiniz!")
        print("Puanınız:", puan)
        break
    else:
        hak -= 1
        puan -= 15

        if tahmin > sayi:
            print("Daha küçük bir sayı deneyin.")
            max_sayi = tahmin - 1
        else:
            print("Daha büyük bir sayı deneyin.")
            min_sayi = tahmin + 1

if hak == 0:
    print("\nKaybettiniz!...")
    print("Tutulan sayı:", sayi)
    print("Puanınız: 0")