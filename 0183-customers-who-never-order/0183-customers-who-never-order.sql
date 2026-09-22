# Write your MySQL query statement below
/*SELECT name from Customers
WHERE name not in 
(SELECT c.name
FROM Customers c 
RIGHT JOIN Orders o
ON c.id = o.customerId);
*/


/*SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
*/



SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN
(select customerId from Orders);
