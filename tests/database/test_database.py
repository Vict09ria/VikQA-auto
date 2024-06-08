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


# Індивідуальна частина


@pytest.mark.database  # Отримання всіх даних з колонки customers
def test_select_all_data():
    db = Database()
    all = db.get_sellect_all_data()

    print(all)


@pytest.mark.database  # Перевірка країни покупців.
# Отримання даних про кількість замовників з певної країни
def test_check_country_user():
    db = Database()
    country = db.get_country_user("Ukraine")

    # Перевірка, що список не порожній
    assert len(country) > 0, "Список користувачів з країни Ukraine порожній"

    # Перевірка першого запису
    assert country[0][0] == "Ukraine"

    # Якщо очікується більше записів, можна перевірити і їх, але тільки якщо впевнені, що вони існують
    if len(country) > 1:
        assert country[1][0] == "Ukraine"
    print(len(country))
