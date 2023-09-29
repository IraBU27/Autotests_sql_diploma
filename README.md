# Autotests_sql_diploma
SQL-запросы:
```sh
SELECT c.login, COUNT(o.track) AS "countOrder"
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id=o."courierId"
WHERE o."inDelivery"=true
GROUP BY c.login;
```
```sh
SELECT id,
 CASE 
   WHEN finished = true THEN '2'
   WHEN cancelled = true THEN '-1'
   WHEN "inDelivery" = true THEN '1'
   ELSE '0'
 END AS status 
FROM "Orders";
```
