CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT salary FROM(    
         SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) as salary_rank FROM Employee 
       ) as salary_order WHERE salary_rank = n LIMIT 1
  );
END