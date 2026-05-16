#Veri analizi ve görselleştirme için kullanılan kütüphaneler
import pandas as pd
import matplotlib.pyplot as plt


class DataPreprocessor:
    def __init__(self, dosya_yolu): #Sınıf oluşturulurken çalışır, veri dosyasını yükler
        self.__veri = pd.read_csv(dosya_yolu)  #CSV dosyasını okuyup DataFrame olarak saklar

    # Veri setinin genel özetini ekrana yazdırır
    def veri_ozeti(self):
        print("İlk 5 Satır:") #Veri setinin ilk 5 satırını gösterir (veriyi tanımak için)
        print(self.__veri.head())

        print("\nVeri Seti Bilgisi:") #Sütunlar, veri tipleri ve null değer bilgisi verir
        self.__veri.info()

        print("\nSayısal Özet:") #Sayısal sütunların ortalama, min, max gibi istatistiklerini gösterir
        print(self.__veri.describe())

    def eksik_veri_kontrolu(self): #Eksik verileri kontrol eder
        print("Eksik Veri Sayıları:")
        print(self.__veri.isnull().sum()) #Her sütunda kaç tane boş değer olduğunu gösterir

    def eksikleri_doldur(self, strateji='mean'):   # Eksik verileri belirlenen stratejiye göre doldurur
        for sutun in self.__veri.columns:
            if self.__veri[sutun].isnull().sum() > 0:  # Sütunda eksik veri varsa işlem yapar

                #Sayısal sütunlar için işlemler
                if pd.api.types.is_numeric_dtype(self.__veri[sutun]):
                    if strateji == 'mean':
                        deger = self.__veri[sutun].mean()  # Ortalama ile doldurma
                    elif strateji == 'median':
                        deger = self.__veri[sutun].median() # Medyan ile doldurma
                    else:
                        deger = self.__veri[sutun].mean() # Varsayılan olarak ortalama kullanılır

                # Metinsel sütunlar
                else:
                    deger = self.__veri[sutun].mode()[0]

                self.__veri[sutun].fillna(deger, inplace=True)  # Eksik değerleri seçilen değer ile doldurur

        print("Eksik veriler dolduruldu.")

    def sutun_sil(self, sutun_adi):   # Veri setinden istenen bir sütunu siler
        if sutun_adi in self.__veri.columns:
            self.__veri.drop(columns=[sutun_adi], inplace=True)
            print(f"{sutun_adi} sütunu silindi.")
        else:
            print(f"{sutun_adi} sütunu bulunamadı.")

    def dagilim_ciz(self, sutun_adi):  # Belirli bir sütunun dağılımını grafikle gösterir
        if sutun_adi in self.__veri.columns: # Sütun var mı kontrol edilir
            plt.figure(figsize=(10, 5))

            if self.__veri[sutun_adi].dtype == 'object': # Eğer sütun metinse bar grafiği çizilir
                self.__veri[sutun_adi].value_counts().head(10).plot(kind='bar')
                plt.xticks(rotation=45)
            else:
                self.__veri[sutun_adi].plot(kind='hist', bins=20) # Sayısal veriler için histogram çizilir

            plt.title(f"{sutun_adi} Dağılımı")
            plt.xlabel(sutun_adi)
            plt.ylabel("Frekans")
            plt.show()
        else:
            print(f"{sutun_adi} sütunu bulunamadı.")

    def veriyi_kaydet(self, dosya_adi):  # Düzenlenmiş veri setini CSV dosyası olarak kaydeder
        self.__veri.to_csv(dosya_adi, index=False)  # DataFrame'i CSV dosyasına yazar
        print(f"Veri {dosya_adi} dosyasına kaydedildi.")