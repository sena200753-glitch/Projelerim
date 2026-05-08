import oyun_modulu as oyun


def menu():
    oyuncu = input(" Oyuncu adını gir: ")

    while True:
        print("\n MENÜ")
        print("1. Sayı Tahmin")
        print("2. Yazı-Tura")
        print("3. Skorlarım")
        print("4. Çıkış")

        secim = input("Seçim yap: ")

        if secim == "1":
            puan = oyun.sayi_tahmin()
            oyun.skor_kaydet(oyuncu, "Sayı Tahmin", puan)

        elif secim == "2":
            puan = oyun.yazi_tura()
            oyun.skor_kaydet(oyuncu, "Yazı-Tura", puan)

        elif secim == "3":
            oyun.skor_goster()

        elif secim == "4":
            print(" Çıkılıyor...")
            break

        else:
            print(" Geçersiz seçim!")


if __name__ == "__main__":
    menu()