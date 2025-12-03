#Şifre Oluşturucu --Güvenli rastgele şifre üreten fonksiyonlar
import string
import secrets

def sifre_uret(uzunluk=12, sayi_kullan=True, ozel_karakter=True):
    alfabe = string.ascii_letters  # a-zA-Z
    if sayi_kullan:
        alfabe += string.digits
    if ozel_karakter:
        alfabe += "!@#$%^&*()-_=+?."

    return "".join(secrets.choice(alfabe) for _ in range(uzunluk))

if __name__ == "__main__":
    print("--- Şifre Oluşturucu ---")
    uzunluk = int(input("Şifre uzunluğu: "))
    sayi = input("Rakam kullanılsın mı? (e/h): ").lower() == "e"
    ozel = input("Özel karakter kullanılsın mı? (e/h): ").lower() == "e"

    sifre = sifre_uret(uzunluk, sayi_kullan=sayi, ozel_karakter=ozel)
    print("Oluşturulan şifre:", sifre)