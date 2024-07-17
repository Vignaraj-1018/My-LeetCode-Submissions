# Write your MySQL query statement below

SELECT a.product_id, b.first_year, a.quantity, a.price
FROM Sales a
JOIN (
    SELECT product_id, MIN(year) as first_year
    FROM Sales
    GROUP BY product_id) b
ON a.product_id = b.product_id AND a.year = b.first_year;