# Prime Number Range Programı
#İki sayı arasındaki tüm asal sayıları bulan program

baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))

print("\nAsal sayılar:")

for sayi in range(baslangic, bitis + 1):
    if sayi > 1:
        asal = True
        for i in range(2, int(sayi ** 0.5) + 1):
            if sayi % i == 0:
                asal = False
                break
        if asal:
            print(sayi, end=" ")