CREATE TABLE gonderi( 
    gonderi_id INT PRIMARY KEY IDENTITY(1,1), 
    musteri_id INT, 
    gonderi_turu VARCHAR(50), 
    ucret INT, 
    cikis_tarihi DATE,
    FOREIGN KEY (musteri_id) REFERENCES musteri(musteri_id)
    );