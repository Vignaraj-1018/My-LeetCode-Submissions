# Write your MySQL query statement below

SELECT p1.product_id,
COALESCE(
    (SELECT p2.new_price
    FROM Products p2
    WHERE p2.product_id = p1.product_id AND p2.change_date <= '2019-08-16'
    ORDER BY p2.change_date DESC
    LIMIT 1),
    10) as price
FROM (SELECT DISTINCT product_id FROM Products) as p1;