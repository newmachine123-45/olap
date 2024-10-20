-- Certainly! Below are simple SQL queries that illustrate how to perform the OLAP operations using a hypothetical sales database with a table named sales_data. The relevant columns might include region, product, sales_amount, date, etc.
-- slice
SELECT *
FROM sales_data
WHERE region = 'North';
-- dice
SELECT *
FROM sales_data
WHERE product IN ('Product A', 'Product B')
  AND region IN ('North', 'South');
-- drill down
SELECT YEAR(date) AS year, QUARTER(date) AS quarter, SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY YEAR(date), QUARTER(date)
ORDER BY year, quarter;
-- drill up
SELECT YEAR(date) AS year, SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY YEAR(date)
ORDER BY year;
-- pivot rotate
SELECT product,
       SUM(CASE WHEN region = 'North' THEN sales_amount ELSE 0 END) AS North_Sales,
       SUM(CASE WHEN region = 'South' THEN sales_amount ELSE 0 END) AS South_Sales
FROM sales_data
GROUP BY product;
-- aggregation
SELECT SUM(sales_amount) AS total_sales
FROM sales_data;
