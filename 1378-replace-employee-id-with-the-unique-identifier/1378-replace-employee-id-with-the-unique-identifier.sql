# Write your MySQL query statement below
SELECT EU.unique_id, EP.name from Employees EP LEFT JOIN EmployeeUNI EU using(id);