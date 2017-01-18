CREATE TABLE incr_MRIS1_CountSales
AS
SELECT MRIS.Address As Address, count(MRIS.Address) As SalesHistCount, max(MRIS.CloseDate) As MaxCloseDt
FROM Source_MRIS MRIS
GROUP BY MRIS.Address;