# Write your MySQL query statement below
SELECT w1.id as Id 
from Weather w1 
JOIN Weather w2 
ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY) 
WHERE w1.temperature > w2.temperature;