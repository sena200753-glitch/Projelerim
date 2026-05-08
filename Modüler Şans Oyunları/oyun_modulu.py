import random
import csv
import os


def sayi_tahmin():
    print("\n Sayı Tahmin Oyununa Hoş Geldin!")
    hedef = random.randint(1, 100)
    hak = 7

    while hak > 0:
        try:
            tahmin = int(input(f"Tahminin (Kalan hak: {hak}): "))

            if tahmin == hedef:
                print(" Doğru bildin! +50 puan")
                return 50
            elif tahmin < hedef:
                print("Daha büyük!")
            else:
                print("Daha küçük!")

            hak -= 1

        except ValueError:
            print(" Lütfen sayı gir!")

    print(f" Bilemedin! Doğru sayı: {hedef}")
    return 0


def yazi_tura():
    print("\n Yazı-Tura Oyununa Hoş Geldin!")
    secim = input("Yazı mı Tura mı? (y/t): ").lower()

    if secim not in ["y", "t"]:
        print(" Geçersiz seçim!")
        return 0

    sonuc = random.choice(["y", "t"])

    if secim == sonuc:
        print("Kazandın! +20 puan")
        return 20
    else:
        print("Kaybettin!")
        return 0




DOSYA_ADI = "skorlar.csv"


def skor_kaydet(oyuncu, oyun, puan):
    dosya_var = os.path.exists(DOSYA_ADI)

    with open(DOSYA_ADI, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not dosya_var:
            writer.writerow(["Oyuncu", "Oyun", "Puan"])

        writer.writerow([oyuncu, oyun, puan])


def skor_goster():
    print("\n SKORLAR:")

    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))

    except FileNotFoundError:
        print("Henüz skor dosyası yok. (Oluşturuluyor...)")
        with open(DOSYA_ADI, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Oyuncu", "Oyun", "Puan"])