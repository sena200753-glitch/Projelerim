


#include <iostream>
using namespace std;

int main() {
    const int ogrenciSayisi = 5;
    float vize, kisaSinav, final;
    float ortalama[ogrenciSayisi];
    float sinifOrt = 0;
    int enBasarili = 0;

    for (int i = 0; i < ogrenciSayisi; i++) {  // Her öğrenci için notları al
        cout << i + 1 << ". ogrencinin notlarini giriniz:" << endl; // Öğrenci numarasını 1'den başlat

        cout << "Vize:"; // Vize notunu al
        cin >> vize;

        cout << "Kisa Sinav: "; // Kısa sınav notunu al
        cin >> kisaSinav;

        cout << "Final: "; // Final notunu al
        cin >> final;

        ortalama[i] = vize * 0.30 + kisaSinav * 0.10 + final * 0.60; // Ortalamayı hesapla
        sinifOrt += ortalama[i]; // Sınıf ortalamasına ekle

        if (ortalama[i] > ortalama[enBasarili]) { // En başarılı öğrenciyi bul
            enBasarili = i; // En başarılı öğrencinin indeksini güncelle
        }

        cout << "Ogrencinin agirlikli ortalamasi: " << ortalama[i] << endl << endl; // Öğrencinin ağırlıklı ortalamasını yazdır
    }

    sinifOrt /= ogrenciSayisi;

    cout << "Sinif ortalamasi: " << sinifOrt << endl;
    cout << "En basarili ogrenci: " << enBasarili + 1 << ". ogrenci" << endl;


    return 0;
}