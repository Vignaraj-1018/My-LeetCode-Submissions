# Write your MySQL query statement below
SELECT id, SUM(count) AS num
FROM (
    SELECT requester_id as id, COUNT(*) as count
    FROM RequestAccepted
    GROUP BY requester_id
UNION ALL
    SELECT accepter_id as id, COUNT(*) as count
    FROM RequestAccepted
    GROUP BY accepter_id
) as f
GROUP BY id
ORDER BY num DESC
LIMIT 1;