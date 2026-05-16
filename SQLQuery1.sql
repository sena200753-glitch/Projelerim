USE AdventureWorks2022;
GO

SELECT TOP 20*
FROM Purchasing.Vendor;
GO 

SELECT BusinessEntityID, Name, ActiveFlag
FROM Purchasing.Vendor
WHERE ActiveFlag = 1
GO

SELECT Name, PreferredVendorStatus
FROM Purchasing.Vendor
WHERE PreferredVendorStatus = 1
GO

SELECT Name, CreditRating
FROM Purchasing.Vendor 
ORDER BY CreditRating;
GO

SELECT TOP 20*
FROM Purchasing.ProductVendor;
GO

SELECT TOP 20
pv.BusinessEntityID,
pv.ProductID,
pv.StandardPrice,
pv.AverageLeadTime
FROM Purchasing.ProductVendor pv;
GO

SELECT BusinessEntityID, ProductID, AverageLeadTime
FROM Purchasing.ProductVendor
WHERE AverageLeadTime > 20;
GO 

SELECT TOP 20 *
FROM Production.Product;
GO

SELECT TOP 20
P.Name AS UrunAdi,
pv.BusinessEntityID,
pv.StandardPrice,
pv.AverageLeadTime
FROM Purchasing.ProductVendor pv
JOIN Production.Product p
ON pv.ProductID = p.ProductID;
GO

SELECT TOP 10
v.Name AS TedarikciAdi,
p.Name AS UrunAdi
FROM Purchasing.ProductVendor pv
JOIN Purchasing.Vendor v
ON pv.BusinessEntityID = v.BusinessEntityID
JOIN Production.Product p
ON pv.ProductID = pv.ProductID
ORDER BY pv.StandardPrice DESC;
GO