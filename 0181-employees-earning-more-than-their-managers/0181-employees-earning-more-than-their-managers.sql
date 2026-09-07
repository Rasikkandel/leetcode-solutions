# Write your MySQL query statement below
/*
SELECT o.name as Employee FROM Employee o WHERE o.salary > (SELECT i.salary FROM Employee i WHERE i.id = o.managerId) 
*/

SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;