# Write your MySQL query statement below
SELECT Department, Employee, Salary FROM 
(
    SELECT d.name as Department, e.name as Employee, e.salary as Salary, DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee e
    JOIN Department d
    ON d.id = e.departmentId
) as _rank
WHERE salary_rank <= 3
ORDER BY Salary DESC, Department, Employee;