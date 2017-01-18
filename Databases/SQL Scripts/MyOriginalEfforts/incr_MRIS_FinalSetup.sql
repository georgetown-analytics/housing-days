CREATE TABLE incr_MRIS_FinalSetuptest
AS
SELECT MRIS.*, (((MRIS.ClosePrice - MRIS.ListPrice)*1.0)/MRIS.ListPrice) AS PriceDiffFactor, MRISCnt.SalesHistCount, Dates2.TrueDate AS PostDateTrue, Dates1.TrueDate As CloseDtTrue, Dates1.ComboMYr As CloseDtMonthYear, MRIS.ZipCode || Dates1.ComboMYr As ZipMYrLookup
FROM Source_MRIS MRIS
LEFT JOIN Lookup_CSVDateVal Dates1 ON Dates1.DateVal = MRIS.CloseDate
LEFT JOIN Lookup_CSVDateVal Dates2 ON Dates2.DateVal = (MRIS.CloseDate - MRIS.DOMP)
LEFT JOIN incr_MRIS1_CountSales MRISCnt ON MRISCnt.Address = MRIS.Address;	