SELECT eser.eser_adi, uzman.ad_soyad, restorasyon.durum
FROM restorasyon
INNER JOIN eser ON restorasyon.eser_id = eser.eser_id	
INNER JOIN uzman ON restorasyon.uzman_id = uzman.uzman_id;