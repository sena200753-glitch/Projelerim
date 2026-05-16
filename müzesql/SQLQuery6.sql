CREATE TABLE restorasyon( 

restorasyon_id INT PRIMARY KEY IDENTITY(1,1), 

eser_id INT, 

uzman_id INT, 

baslangic_tarihi DATE, 

durum VARCHAR(30), 

maliyet INT 

); 