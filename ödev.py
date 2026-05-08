ad = input("Adinizi girin: ")
soyad = input("Soyadinizi girin: ")
yas = int(input("Yasinizi girin: "))
sehir = input("Yasadiğiniz şehir: ")
meslek = input("Mesleğiniz: ")

bes_yil_sonra_yas = yas + 5
harf_sayisi = len(ad + soyad)   

print(f"Ad Soyad : {ad} {soyad}")
print(f"Yaş      : {yas}")
print(f"Şehir    : {sehir}")
print(f"Meslek   : {meslek}")

print(f"5 yil sonraki yasiniz: {bes_yil_sonra_yas}")
print(f"Ad ve soyad toplam harf sayisi: {harf_sayisi}") 
