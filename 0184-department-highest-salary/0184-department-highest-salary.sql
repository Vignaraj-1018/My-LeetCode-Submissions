# Write your MySQL query statement below

SELECT d.name AS Department, e.name AS Employee, e.salary
FROM Department d
JOIN Employee e
ON e.departmentId=d.id
WHERE
    (departmentId, salary) IN (
        SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId
    );