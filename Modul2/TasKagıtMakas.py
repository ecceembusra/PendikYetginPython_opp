import random

print("=== Taş - Kağıt - Makas Oyunu ===")
secenekler = ["tas", "kagit", "makas"]

while True:
    oyuncu = input("\nSeçiminiz (tas/kagit/makas) veya 'q' ile çık: ").lower()

    if oyuncu == "q":
        print("Oyun bitti, görüşürüz! 👋")
        break

    if oyuncu not in secenekler:
        print("Geçersiz seçim!")
        continue

    bilgisayar = random.choice(secenekler)
    print(f"Bilgisayar: {bilgisayar}")

    if oyuncu == bilgisayar:
        print("Berabere!")
    elif (
        (oyuncu == "tas" and bilgisayar == "makas") or
        (oyuncu == "kagit" and bilgisayar == "tas") or
        (oyuncu == "makas" and bilgisayar == "kagit")
    ):
        print("Kazandın!")
    else:
        print("Kaybettin!")