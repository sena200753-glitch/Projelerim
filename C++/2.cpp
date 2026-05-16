

#include <iostream>
using namespace std;

int main() {
	int arr[] = { 2,4,6,8,10 }; //İçerisinde 5 adet tamsayı bulunan dizi tanımlanır
	int toplam = 0; //toplam değişkeni 0 olarak başlatılır

	for (int i = 0; i < 5; i++) { //Döngü 0'dan başlayarak 5'e kadar çalışır
		if (arr[i] % 4 == 0) { //Dizinin her bir elemanı 4'e bölünür ve kalan 0 ise
			toplam += arr[i]; //toplam değişkenine o elemanın değeri eklenir
		}
	}
	cout << "sonuc " << toplam << endl; // Hesaplanan toplam değeri ekrana yazdırılır
	return 0;


}


