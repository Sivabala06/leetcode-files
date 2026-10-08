-- # Write your MySQL query statement below
-- select name   As Customers
-- from Customers c
-- where not exists 
-- (select 1 from Orders o
-- where o.customerId = c.id );

SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId 
    FROM Orders
);
