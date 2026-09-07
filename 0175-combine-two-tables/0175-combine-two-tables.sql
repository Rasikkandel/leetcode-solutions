# Write your MySQL query statement belowS
SELECT firstName , lastName , city , state FROM PERSON 
LEFT JOIN Address 
ON Person.personId = Address.personId ;