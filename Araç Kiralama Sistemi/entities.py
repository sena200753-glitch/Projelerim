from abc import ABC, abstractmethod


class Arac(ABC):
    def __init__(self, plaka, marka, model):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.musait = True  

    @abstractmethod
    def gunluk_ucret(self):
        pass

    def kirala(self):
        if self.musait:
            self.musait = False
            print(f"{self.plaka} plakalı araç kiralandı.")
        else:
            print("Bu araç zaten kiralanmış.")

    def bilgileri_goster(self):
        durum = "Müsait" if self.musait else "Kiralanmış"
        print(f"Plaka: {self.plaka} | Marka: {self.marka} | Model: {self.model} | Durum: {durum}")



class Binek(Arac):
    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 1000



class Ticari(Arac):
    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 1500



class Lux(Arac):
    def __init__(self, plaka, marka, model):
        super().__init__(plaka, marka, model)

    def gunluk_ucret(self):
        return 3000