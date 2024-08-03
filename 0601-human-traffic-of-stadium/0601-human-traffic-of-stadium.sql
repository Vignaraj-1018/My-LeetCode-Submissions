# Write your MySQL query statement below
with grp_nm as (
    SELECT *, id - ROW_NUMBER() OVER (ORDER BY visit_date) AS grp
    FROM Stadium 
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM grp_nm
WHERE grp in (
    SELECT grp
    FROM grp_nm
    GROUP BY grp
    HAVING COUNT(*) >= 3
);