Python script na vytvorenie jednoduchej, nekompletnej databazy pre eshop. Vyuzite na vysvetlenie zakladnych select-ov a join-ov.

## Jednoduché selecty

```
SELECT * FROM users;
```

```
SELECT * FROM products;
```

```
SELECT * FROM orders;
```

```
SELECT * FROM order_products;
```

Selectni iba meno z produktov:

```
SELECT name FROM products;
```

Alias pre názov tabuľky:

```
SELECT p.name FROM products p;
```

Funkcia `SUM()`:

```
SELECT SUM(p.price) FROM products p;
```

Alias stĺpca:

```
SELECT SUM(p.price) AS "cena vsetkych produktov" FROM products p;
```

Funkcia `COUNT()`:

```
SELECT COUNT(*) AS pocet_produktov FROM products;
```

Funkcia `AVG()`:

```
SELECT AVG(p.price) AS "priemerna cena produktu" FROM products p;
```

Operácie v selecte:

```
SELECT p.price + p.id FROM products p;
```

```
SELECT p.price - p.id FROM products p;
```

```
SELECT p.price * p.id FROM products p;
```

```
SELECT p.price % p.id FROM products p;
```

## Filtrovanie

`WHERE`:

```
SELECT * FROM users
WHERE id=1;
```

`IN`:

```
SELECT * FROM users
WHERE id IN (1, 2, 5);
```

```
SELECT * FROM users
WHERE first_name IN ('John', 'Marco');
```

Reťazec:

```
SELECT * FROM users
WHERE first_name='John';
```

`LIKE`:

```
SELECT * FROM users
WHERE first_name LIKE '%o%';
```

```
SELECT * FROM users
WHERE first_name LIKE 'M%';
```

```
SELECT * FROM users
WHERE first_name LIKE '%o';
```

Väčší, menší, iný:

```
SELECT * FROM users
WHERE id > 2;
```

```
SELECT * FROM users
WHERE id < 2;
```

```
SELECT * FROM users
WHERE id <= 2;
```

```
SELECT * FROM users
WHERE id <> 2;
```

```
SELECT * FROM users
WHERE id != 2;
```

Konkrétny príklad:

```
SELECT p.name FROM products p
WHERE p.price > 2000;
```

Selectni všetky produkty s cenou väčšou ako je priemerná cena všetkých produktov:

```
SELECT p.name, p.price FROM products p
WHERE p.price > (
  SELECT AVG(price) FROM products
);
```

Zoradené zostupne:

```
SELECT p.name, p.price FROM products p
WHERE p.price > (
  SELECT AVG(price) FROM products
)
ORDER BY p.price DESC;
```

Zoradené vzostupne:

```
SELECT p.name, p.price FROM products p WHERE p.price > (
  SELECT AVG(price) FROM products
)
ORDER BY p.price ASC;
```

## Joiny

Skrátený (implicitný) inner join:

```
SELECT o.id AS order_id, u.first_name FROM orders o, users u
WHERE u.id=o.user_id;
```

Inner join:

```
SELECT o.id AS order_id, u.first_name FROM orders o
INNER JOIN users u ON u.id=o.user_id;
```

Left join:

```
SELECT o.id AS order_id, u.first_name FROM orders o
LEFT JOIN users u ON u.id=o.user_id;
```

Right join:

```
SELECT o.id AS order_id, u.first_name FROM orders o
RIGHT JOIN users u ON u.id=o.user_id;
```

Left join (ale v podstate right join predšlej query):

```
SELECT o.id AS order_id, u.first_name FROM users u
LEFT JOIN orders o ON o.user_id=u.id;
```

Dvojtý left join na many-to-many vzťah:

```
SELECT o.id AS order_id, p.id AS product_id, p.name FROM orders o
LEFT JOIN order_products op ON op.order_id=o.id
LEFT JOIN products p ON p.id=op.product_id;
```

Ako predošla query, ale right join na produkty:

```
SELECT o.id AS order_id, p.id AS product_id, p.name FROM orders o
LEFT JOIN order_products op ON op.order_id=o.id
RIGHT JOIN products p ON p.id=op.product_id;
```

Ako predošla query, ale full outer join na produkty:

```
SELECT o.id AS order_id, p.id AS product_id, p.name FROM orders o
LEFT JOIN order_products op ON op.order_id=o.id
FULL OUTER JOIN products p ON p.id=op.product_id;
```

Dvojtý full outer join:

```
SELECT o.id AS order_id, p.id AS product_id, p.name FROM orders o
FULL OUTER JOIN order_products ON op.order_id=o.id
FULL OUTER JOIN products p ON p.id=op.product_id;
```

Skrátený dvojtý inner join:

```
SELECT o.id AS order_id, p.id AS product_id, p.name, p.price FROM orders o, products p, order_products op
WHERE o.id=op.order_id AND p.id=op.product_id;
```

Selectni pocet produktov, cenu a priemernu cenu objednavky:

```
SELECT
  o.id AS order_id,
  COUNT(p.price) AS number_of_products,
  SUM(p.price) order_sum,
  AVG(p.price) AS avg_price
FROM orders o, products p, order_products op
WHERE o.id=op.order_id
  AND p.id=op.product_id
GROUP BY o.id;
```
