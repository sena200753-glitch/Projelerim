
#include <iostream>
using namespace std;

int main()
{
	int sayi = 3; // sayi değişkeni 3 olarak tanımlanır
	for (int i = 0; i < 4; i++) { // i değişkeni 0'dan başlayarak 4'e kadar döngü oluşturur
		cout << "i=" << i << ", sonuc=" << (sayi + i * 2) << endl; // Her döngüde i'nin değeri ve (sayi + i * 2) ifadesinin sonucu ekrana yazdırılır
	}

}

