


#include <iostream>
using namespace std;

int main()
{
    int sifre = 2901;  
    int girilen;
	int hak = 3;       // Kullanıcının 3 hakkı var

	while (hak > 0) // Hakkı olduğu sürece döngü devam eder
    {
        cout << "Sifreyi giriniz: ";
        cin >> girilen;

        if (girilen == sifre) 
        {
            cout << "Giris basarili" << endl;
            break; // Doğruysa döngüden çık
        }
        else
        {
			hak--; // Hakkı bir azalt

            if (hak == 0) 
            {
				cout << "Hesap kilitlendi" << endl; // Hakkı kalmadıysa hesap kilitlenir
            }
            else
            {
				cout << "Yanlis sifre. Kalan hak: " << hak << endl; // Yanlışsa kalan hakkı gösterir
            }
        }
    }

    return 0;
}
