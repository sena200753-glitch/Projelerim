#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct Oda {
    int odaNo; 
    int ucret;
};

struct Musteri {
    int musteriNo;
    string ad;
    string soyad;
    string tc;
};

void odaEkle() { 
    Oda o;
    ofstream file("odalar.txt", ios::app); // Dosyayı yazmak ve dosya varsa içeriğini silmeden yeni verileri dosyaya ekler.

    cout << "Oda No: ";
    cin >> o.odaNo;
    cout << "Ucret: ";
    cin >> o.ucret;

    file << o.odaNo << " " << o.ucret << endl;
    file.close();

    cout << "Oda eklendi.\n";
}

void odalariListele() {
    ifstream file("odalar.txt");c // Dosyadan veri okumak için kullanılır.
    Oda o;

    cout << "\nOdalar:\n";
    while (file >> o.odaNo >> o.ucret) {
        cout << "Oda No: " << o.odaNo << " Ucret: " << o.ucret << endl;
    }
    file.close(); // Dosya ile ilgili işlemler tamamlandıktan sonra dosyanın güvenli şekilde kapatılması için kullanılmıştır.
}

void musteriEkle() {
    Musteri m;
    ofstream file("musteriler.txt", ios::app);

    cout << "Musteri No: ";
    cin >> m.musteriNo;
    cout << "Ad: ";
    cin >> m.ad;
    cout << "Soyad: ";
    cin >> m.soyad;
    cout << "TC: ";
    cin >> m.tc;

    file << m.musteriNo << " " << m.ad << " " << m.soyad << " " << m.tc << endl;
    file.close();

    cout << "Musteri eklendi.\n";
}

void odaKaydiYap() {
    int odaNo, musteriNo;
    ofstream file("kayitlar.txt", ios::app);

    cout << "Oda No: ";
    cin >> odaNo;
    cout << "Musteri No: ";
    cin >> musteriNo;

    file << odaNo << " " << musteriNo << endl;
    file.close();

    cout << "Oda kaydi yapildi.\n";
}

void hataliSecim() {
    cout << "\nHatali Secim\n";
    cout << "Devam etmek icin tiklayiniz...\n";
    cin.ignore();
    cin.get();
}

int main() {
    int secim, altSecim;

    do {    //Programın sürekli çalışmasını sağlamk için do-while döngüsü kullanılmıştır.
        system("cls");
        cout << "Otel Islemleri\n";
        cout << "----------------\n";
        cout << "1- Oda Islemleri\n";
        cout << "2- Musteri Islemleri\n";
        cout << "3- Oda Kayit Islemleri\n";
        cout << "99- Cikis\n";
        cout << "Seciminiz: ";
        cin >> secim;

        switch (secim) {  //Kullanıcının ana menüde yaptığı seçime göre hangi işlemin yapılcacağını belirlemek için switch-case kullanılmıştır.
        case 1:
            system("cls");
            cout << "Oda Islemleri\n";
            cout << "----------------\n";
            cout << "1- Oda Ekle\n";
            cout << "2- Odalari Listele\n";
            cout << "99- Ust Menu\n";
            cout << "Seciminiz: ";
            cin >> altSecim;

            if (altSecim == 1) odaEkle(); // Alt menüde yapılan seçime göre seçilenin çalıştırılması için if-else kullanılmıştır.
            else if (altSecim == 2) odalariListele();
            else if (altSecim != 99) hataliSecim(); // Menüde tanımlı olmayan bir değer girildiğinde kullanıcıya hata mesajı gösterir
            break;

        case 2:
            system("cls");
            musteriEkle();
            break;

        case 3:
            system("cls");
            odaKaydiYap();
            break;

        case 99:
            cout << "Cikis yapiliyor...\n";
            break;

        default:
            hataliSecim();
        }

    } while (secim != 99);

    return 0;
}
