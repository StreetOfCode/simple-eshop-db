import psycopg2

CREATE_USERS_TABLE_QUERY = """
    CREATE TABLE users (
        id integer not null primary key,
        first_name text,
        last_name text
    )
"""

ADD_USERS_QUERY = """
    INSERT INTO users VALUES(1, 'John', 'Doe');
    INSERT INTO users VALUES(2, 'Marco', 'Polo');
    INSERT INTO users VALUES(3, 'Chris', 'Colombus');
    INSERT INTO users VALUES(4, 'Bruce', 'Lee');
    INSERT INTO users VALUES(5, 'Jackie', 'Chan');
"""

CREATE_ORDERS_TABLE_QUERY = """
    CREATE TABLE orders (
        id integer primary key,
        user_id integer references users(id),
        created_at timestamp
    )
"""

ADD_ORDERS_QUERY = """
    INSERT INTO orders VALUES(1, 1, date('now'));
    INSERT INTO orders VALUES(2, 1, date('now'));
    INSERT INTO orders VALUES(3, 1, date('now'));
    INSERT INTO orders VALUES(4, 1, date('now'));
    INSERT INTO orders VALUES(5, 2, date('now'));
"""

CREATE_PRODUCTS_TABLE_QUERY = """
    CREATE TABLE products (
        id integer not null primary key,
        name text,
        description text,
        price decimal
    )
"""

ADD_PRODUCTS_QUERY = """
    INSERT INTO products VALUES(1, 'Macbook Pro 13', 'The ideal...', 3000);
    INSERT INTO products VALUES(2, 'Macbook Pro 16', 'The larger ideal...', 4000);
    INSERT INTO products VALUES(3, 'Dell XPS 13', 'The ideal windows...', 2000);
    INSERT INTO products VALUES(4, 'Dell XPS 15', 'The larger ideal windows...', 2500);
    INSERT INTO products VALUES(5, 'Lenovo ThinkPad T14', 'The ideal vacuumlabs...', 1500);
"""

CREATE_ORDER_PRODUCTS_TABLE_QUERY = """
    CREATE TABLE order_products (
        id integer not null primary key,
        order_id integer references orders(id), 
        product_id integer references products(id)
    )
"""

ADD_ORDER_PRODUCTS_QUERY = """
    INSERT INTO order_products VALUES(1, 1, 1);
    INSERT INTO order_products VALUES(2, 1, 2);
    INSERT INTO order_products VALUES(3, 1, 3);
    INSERT INTO order_products VALUES(4, 1, 4);
    INSERT INTO order_products VALUES(5, 1, 5);

    INSERT INTO order_products VALUES(6, 2, 2);
    INSERT INTO order_products VALUES(7, 2, 3);
    INSERT INTO order_products VALUES(8, 2, 5);
    
    INSERT INTO order_products VALUES(9, 3, 1);
    INSERT INTO order_products VALUES(10, 3, 1);
    
    INSERT INTO order_products VALUES(11, 4, 3);
    INSERT INTO order_products VALUES(12, 4, 3);

    INSERT INTO order_products VALUES(13, 5, 2);
"""


def connect_to_db():
    db = psycopg2.connect(
        "host='localhost' dbname='eshop' user='[FILL_IN_USER]' password='[FILL_IN_PASSWORD]'"
    )
    cursor = db.cursor()
    return (db, cursor)


def create_eshop_db():
    (db, cursor) = connect_to_db()

    cursor.execute(CREATE_USERS_TABLE_QUERY)
    cursor.execute(CREATE_ORDERS_TABLE_QUERY)
    cursor.execute(CREATE_PRODUCTS_TABLE_QUERY)
    cursor.execute(CREATE_ORDER_PRODUCTS_TABLE_QUERY)

    cursor.execute(ADD_USERS_QUERY)
    cursor.execute(ADD_ORDERS_QUERY)
    cursor.execute(ADD_PRODUCTS_QUERY)
    cursor.execute(ADD_ORDER_PRODUCTS_QUERY)

    db.commit()

    return (db, cursor)


(db, cursor) = create_eshop_db()
db.close()
