CREATE TABLE incr_School1_CountbyZipAvgRank
AS
SELECT School.Zip As Zipcode, count(School.School) As SchoolCount, avg(School.SchoolDiggerStarRating) As SchoolAvgRank
FROM Source_SchoolDigger School
GROUP BY School.Zip;