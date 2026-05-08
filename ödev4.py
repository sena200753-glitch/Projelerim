#Sena Aydın
#300125029

karakterler = [
    {"isim": "Aragorn", "sinif": "savasci", "seviye": 15, "hp": 220, "altin": 500},
    {"isim": "Gandalf", "sinif": "buyucu", "seviye": 20, "hp": 140, "altin": 300},
    {"isim": "Legolas", "sinif": "okcu", "seviye": 12, "hp": 160, "altin": 550},
    {"isim": "Gimli", "sinif": "savasci", "seviye": 10, "hp": 200, "altin": 600},
    {"isim": "Thranduil", "sinif": "okcu", "seviye": 14, "hp": 175, "altin": 900},
    {"isim": "Saruman", "sinif": "buyucu", "seviye": 18, "hp": 130, "altin": 800}
]


okcu_mu = lambda k: k["sinif"] == "okcu"
guclu_mu = lambda k: k["seviye"] > 10 and k["hp"] > 150


okcular = list(filter(okcu_mu, karakterler))
gucluler = list(filter(guclu_mu, karakterler))


print("\n=== OKÇULAR ===")
for k in okcular:
    print(f"- {k['isim']} (Seviye: {k['seviye']}, HP: {k['hp']})")

print("\n=== GÜÇLÜ KARAKTERLER ===")
for k in gucluler:
    print(f"- {k['isim']} (Seviye: {k['seviye']}, HP: {k['hp']})")


seviye_15_ustu = [k["isim"] for k in karakterler if k["seviye"] > 15]

print("\n=== SEVİYE 15 ÜSTÜ ===")
for isim in seviye_15_ustu:
    print(f"- {isim}")


etiketli_liste = [
    (k["isim"], "Zengin" if k["altin"] > 500 else "Fakir")
    for k in karakterler
]

print("\n=== EKONOMİ DURUMU ===")
for isim, etiket in etiketli_liste:
    print(f"- {isim}: {etiket}")