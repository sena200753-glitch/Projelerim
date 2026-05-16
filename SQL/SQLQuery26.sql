CREATE TABLE teslimat( 
    teslimat_id INT PRIMARY KEY IDENTITY(1,1), 
    gonderi_id INT, 
    kurye_id INT, 
    teslim_durumu VARCHAR(20), 
    teslim_tarihi DATE,
    );