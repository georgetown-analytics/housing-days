CREATE TABLE output_csv
AS
SELECT MRIS.*, School.SchoolAvgRank,School.SchoolCount
FROM incr_MRIS_FinalSetup MRIS
LEFT JOIN incr_School1_CountbyZipAvgRank School ON School.Zipcode = MRIS.ZipCode;