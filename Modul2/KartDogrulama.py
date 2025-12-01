print("=== Kredi Kartı Doğrulama ===")
kart_no = input("Kredi kartı numarasını boşluksuz girin: ")

#rakamlardan oluşma test
if not kart_no.isdigit():
    print("Kart numarası sadece rakamlardan oluşmalıdır!")
else:
    # Luhn algoritması
    ters_rakamlar = kart_no[::-1]      
    toplam = 0

    for i, rakam in enumerate(ters_rakamlar):
        n = int(rakam)

        # Her ikinci haneyi (1,3,5... index) 2 ile çarp
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9  # 12 -> 1+2 = 3 yerine 12-9=3

        toplam += n

    if toplam % 10 == 0:
        print("Kart numarası GEÇERLİ ")
    else:
        print("Kart numarası GEÇERSİZ ")