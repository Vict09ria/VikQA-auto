import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\Victoria\\VikQA-auto" + r"\\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode,country FROM customers \
            WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id  = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description,\
              quantity)\
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
                FROM orders \
                    JOIN customers ON orders.customer_id = customers.id \
                        JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Індивідуальна частина проекту:

    # Отримати всі дані з таблиці customers
    def get_sellect_all_data(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Отримати дані про наявність користувачів з певної країни
    def get_country_user(self, country):
        query = "SELECT country FROM customers WHERE country = ?"
        self.cursor.execute(query, (country,))
        record = self.cursor.fetchall()
        return record

    # Збільшити всі значення в колонці "кількість на 5"
    def update_product_qnt(self):
        query = "UPDATE products SET quantity = quantity + 5"
        self.cursor.execute(query)
        self.connection.commit()

    # Отримати дані про зміни в таблиці продукти

    def select_update_qnt(self):
        query = "SELECT  id, quantity FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Метод,який додає нові товари до бази данних
    def insert_many_products(self, products):
        query = "INSERT OR REPLACE INTO products (id, name, description,quantity)\
              VALUES (?, ?, ?, ?)"
        self.cursor.executemany(query, products)
        self.connection.commit()

    # Метод,який повертає всі записи з cutomers таблиці \
    # та відповідні записи з orders таблиці
    def get_left_join_orders(self):
        query = "SELECT orders.id,customers.name FROM customers \
                LEFT JOIN orders ON orders.customer_id = customers.id\
                    ORDER BY customers.name"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
