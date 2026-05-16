


#include <iostream>
using namespace std;

int main()
{
    // 1'den 10'a kadar çarpım tablosu

    for (int i = 1; i <= 10; i++) // Dış döngü: 1'den 10'a kadar sayılar
    {
        for (int j = 1; j <= 10; j++) // İç döngü: 1'den 10'a kadar sayılar
        {
            cout << i << " x " << j << " = " << i * j << endl; // Çarpım işlemi ve sonucu ekrana yazdırılır
        }

        cout << endl;
    }

    return 0;
}

