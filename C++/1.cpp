

#include <iostream>
using namespace std;

int main()
{
	int a = 20; // int tamsayı türündedir
	int b = 7; // int tamsayı türündedir
	int c = 3; // int tamsayı türündedir

	float sonuc1 = a / b; // a ve b int türünde olduğu için tamsayı bölme yapılır. 20/7 = 2
	float sonuc2 = (float)a / c; // a float türüne dönüştürülür ve ondalıklı bölme yapılır. O yüzden 20/3 = 6.66667

	cout << sonuc1 << endl; // sonuc1 değişkeninin değeri ekrana yazdırılır
	cout << sonuc2 << endl; // sonuc2 değişkeninin değeri ekrana yazdırılır

}