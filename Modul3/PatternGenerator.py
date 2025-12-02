# Pattern Generator
# Kullanıcının seçtiği deseni çizen program

tip=input("Hangi şekil/sembol olsun?")
n = int(input("Kaç satır olsun? "))

print(f"\n {tip} Sembolü Deseni:")

for i in range(1, n + 1):
    print(tip * i)