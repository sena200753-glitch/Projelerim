



#include <iostream>
using namespace std;

#include <iostream>
using namespace std;

int main() {
    int sayi;


    cout << "bir sayi giriniz: ";
    cin >> sayi;

    if (sayi > 0) {  //Sayı 0'dan büyükse pozitiftir

        cout << "Sayi pozitiftir."; // Pozitif olduğunu ekrana yazdır
    }
    else if (sayi < 0) { //Sayı 0'dan küçükse negatiftir

        cout << "sayi negatiftir"; // Negatif olduğunu ekrana yazdır
    }
    else {  //Sayı ne pozitif ne de negatifse sıfırdır

        cout << "Sayi sıfırdır."; // Sıfır olduğunu ekrana yazdır
    }

    return 0;
}
