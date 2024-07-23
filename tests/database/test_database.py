import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()
    

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)
    

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Individual part of the project:


# Get all data from the customers column
@pytest.mark.database
def test_sellect_all_data():
    db = Database()
    all = db.get_sellect_all_data()

    print(all)
    

# Get data on the number of customers from a certain country
@pytest.mark.database
def test_check_country_user():
    db = Database()
    country = db.get_country_user("Ukraine")

    # Checking that the list is not empty
    assert len(country) > 0, "Список користувачів з країни Ukraine порожній"

    # Checking the first record
    assert country[0][0] == "Ukraine"

    # If more records are expected, you can check them as well, but only if you are sure they exist
    if len(country) > 1:
        assert country[1][0] == "Ukraine"
    print(len(country))


# Checking the increase in value of all values ​​in the "quantity by 5" column
@pytest.mark.database
def test_product_update():
    db = Database()
    # Checking the initial values:
    initial_qnt = db.select_update_qnt()
    print("Початкові значення:", initial_qnt)
    db.update_product_qnt()
    # Validation of values ​​after update
    updated_qnt = db.select_update_qnt()
    # Checking that the values ​​have increased by 5
    print("Значення після оновлення:", updated_qnt)
    for initial, updated in zip(initial_qnt, updated_qnt):
        assert (
            updated[1] == initial[1] + 5
        ), f"Помилка:{initial} \
            не збільшилась на 5"
    assert updated_qnt


# This test adds several products,
# and then checks whether the added products are available in the database
@pytest.mark.database
def test_insert_many_products():
    db = Database()
    products = [
        (5, "цукерки", "з горіхами", 25),
        (6, "торт", "Київський", 10),
        (7, "шоколад", "чорний", 20),
    ]

    db.insert_many_products(products)
    result = db.select_update_qnt()
    assert any(product[1] == 25 for product in result if product[0] == 5)
    assert any(product[1] == 10 for product in result if product[0] == 6)
    assert any(product[1] == 20 for product in result if product[0] == 7)
    print(result)


# A test that checks the left-hand union of two tables\
# Customers Orders
@pytest.mark.database
def test_left_join_orders():
    db = Database()
    orders = db.get_left_join_orders()
    print("Замовлення", orders)
    assert orders
