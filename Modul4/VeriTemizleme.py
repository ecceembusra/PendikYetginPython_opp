#Set ile Veri Temizleme: Tekrar eden kayıtları temizleme programı

def tekrar_sil(liste):
    gorulen = set()
    sonuc = []
    for eleman in liste:
        if eleman not in gorulen:
            gorulen.add(eleman)
            sonuc.append(eleman)
    return sonuc

if __name__ == "__main__":
    print("--- Set ile Veri Temizleme ---")
    print("Tekrar eden kayıtları temizler, ilk görülen sıralamayı korur")
    print("*"*90)
    veri_str = input("\nElemanları virgülle ayırarak girin (örn: a,b,c,a,b): ")
    liste = [v.strip() for v in veri_str.split(",")]

    temiz = tekrar_sil(liste)
    print("Temizlenmiş liste:", temiz)