from entities import Binek, Ticari, Lux


araclar = [
    Binek("34ABC123", "Toyota", "Corolla"),
    Ticari("34DEF456", "Ford", "Transit"),
    Lux("34GHI789", "BMW", "5 Serisi"),
    Binek("34JKL321", "Honda", "Civic")
]


def kiralanabilir_araclari_listele():
    print("\n Müsait Araçlar ")
    for arac in araclar:
        if arac.musait:
            arac.bilgileri_goster()


def arac_kirala():
    plaka = input("Kiralamak istediğiniz aracın plakasını girin: ")

    for arac in araclar:
        if arac.plaka == plaka:
            arac.kirala()
            return

    print("Araç bulunamadı!")


def toplam_gelir_hesapla():
    toplam = 0

    for arac in araclar:
        if not arac.musait: 
            toplam += arac.gunluk_ucret()

    print(f"Toplam günlük gelir: {toplam} TL")


def menu():
    while True:
        print("\n ARAÇ KİRALAMA SİSTEMİ ")
        print("1. Kiralanabilir araçları listele")
        print("2. Araç kirala")
        print("3. Toplam günlük gelir hesapla")
        print("4. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            kiralanabilir_araclari_listele()
        elif secim == "2":
            arac_kirala()
        elif secim == "3":
            toplam_gelir_hesapla()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    menu()