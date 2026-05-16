



#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()

{
	int n; // Matrisin satir sayisi
	int matris[10][10]; // Maksimum 10x10 boyutunda matris


	system("cls");   // Ekrani temizleme komutu 

	printf("::: Matris Islemleri :::\n"); // Başlık yazdırma
	printf("Matrisin satir sayisini giriniz (1-10 arasinda): "); // Kullanıcıdan matris boyutunu alma
	scanf_s("%d", &n); // Kullanıcıdan matris boyutunu alma

	for (int i = 0; i < n; i++) // Matris elemanlarini kullanicidan alma
	{
		for (int j = 0; j < n; j++) // İç içe döngü ile matris elemanlarını alma
		{
			printf("[%d,%d]=", i + 1, j + 1); // Matris elemaninin konumunu gösterme
			scanf_s("%d", &matris[i][j]);  // Matris elemanini kullanicidan alma
		}
	}


	printf("\n"); // Yeni satır ekleme
	for (int i = 0; i < n; i++) // Matris elemanlarini ekrana yazdirma
	{
		for (int j = 0; j < n; j++) // İç içe döngü ile matris elemanlarını yazdırma
		{
			printf("%d ", matris[i][j]); // Matris elemanini ekrana yazdirma
		}
		printf("\n"); // Satir sonu
	}

	return 0;
}