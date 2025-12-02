# Multiplication Quiz Programı
#5 adet rastgele çarpma sorusu soran quiz programı

import random

dogru = 0

for i in range(1, 6):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    cevap = int(input(f"{i}. Soru: {a} x {b} = "))

    if cevap == a * b:
        print("<<< Doğru! >>>")
        dogru += 1
    else:
        print(f"*** Yanlış *** \nDoğru cevap: {a*b}")

print("\nToplam doğru sayınız:", dogru)
print("Puanınız:", dogru * 20)