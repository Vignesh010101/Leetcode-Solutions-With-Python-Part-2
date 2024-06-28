/* Write your PL/SQL query statement below */
with abc as 
(
    SELECT product_id, year,  quantity, price, 
    RANK() OVER (PARTITION BY product_id ORDER BY year) AS rank
    FROM sales
    )
select a.product_id , a.year as first_year , a.quantity , a.price 
from abc  a
where a.rank = 1;
