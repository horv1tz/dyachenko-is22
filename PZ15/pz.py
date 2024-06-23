"""
Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов
торговой фирмы. Таблица Заказы должна содержать информацию о товарах со
следующей структурой записи: Код товара, Наименование товара, Заказчик
(наименование организации, возможны повторяющиеся значения), Дата заказа, Срок
исполнения (от 1 до 10 дней), Стоимость заказа.
"""
import sqlite3
from datetime import date, timedelta

# Подключение к базе данных
conn = sqlite3.connect('orders.db')
c = conn.cursor()

# Создание таблицы Заказы
c.execute('''CREATE TABLE IF NOT EXISTS Orders
             (OrderID INTEGER PRIMARY KEY AUTOINCREMENT, ProductCode TEXT, ProductName TEXT, Customer TEXT, OrderDate TEXT, DeliveryDate TEXT, OrderCost REAL)''')

# Функция для добавления нового заказа
def add_order(product_code, product_name, customer, order_date, delivery_days, order_cost):
    order_date = date.fromisoformat(order_date)
    delivery_date = order_date + timedelta(days=delivery_days)
    c.execute("INSERT INTO Orders (ProductCode, ProductName, Customer, OrderDate, DeliveryDate, OrderCost) VALUES (?, ?, ?, ?, ?, ?)",
              (product_code, product_name, customer, order_date.isoformat(), delivery_date.isoformat(), order_cost))
    conn.commit()

# Функция для просмотра всех заказов
def view_orders():
    c.execute("SELECT * FROM Orders")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Функция для поиска заказов по критериям
def search_orders(product_code=None, customer=None, order_date=None):
    query = "SELECT * FROM Orders WHERE "
    conditions = []
    if product_code:
        conditions.append(f"ProductCode = '{product_code}'")
    if customer:
        conditions.append(f"Customer = '{customer}'")
    if order_date:
        conditions.append(f"OrderDate = '{order_date}'")
    if conditions:
        query += " AND ".join(conditions)
    else:
        query = "SELECT * FROM Orders"
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)

# Функция для обновления заказа
def update_order(order_id, product_code=None, product_name=None, customer=None, order_date=None, delivery_days=None, order_cost=None):
    updates = []
    if product_code:
        updates.append(f"ProductCode = '{product_code}'")
    if product_name:
        updates.append(f"ProductName = '{product_name}'")
    if customer:
        updates.append(f"Customer = '{customer}'")
    if order_date:
        order_date = date.fromisoformat(order_date)
        updates.append(f"OrderDate = '{order_date.isoformat()}'")
    if delivery_days:
        if not order_date:
            c.execute("SELECT OrderDate FROM Orders WHERE OrderID = ?", (order_id,))
            order_date_str = c.fetchone()[0]
            order_date = date.fromisoformat(order_date_str)
        delivery_date = order_date + timedelta(days=delivery_days)
        updates.append(f"DeliveryDate = '{delivery_date.isoformat()}'")
    if order_cost:
        updates.append(f"OrderCost = {order_cost}")
    update_query = "UPDATE Orders SET " + ", ".join(updates) + f" WHERE OrderID = {order_id}"
    c.execute(update_query)
    conn.commit()

# Функция для удаления заказа
def delete_order(order_id):
    c.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
    conn.commit()

# Примеры использования
add_order('PR001', 'Product 1', 'Company A', '2023-03-27', 5, 100.0)
add_order('PR002', 'Product 2', 'Company B', '2023-03-28', 3, 200.0)
add_order('PR001', 'Product 1', 'Company A', '2023-03-29', 7, 150.0)

print("Все заказы:")
view_orders()

print("\nОбновление заказа с ID 1:")
update_order(1, product_name='Updated Product 1', order_cost=110.0)
view_orders()

print("\nУдаление заказа с ID 2:")
delete_order(2)
view_orders()

# Закрытие соединения с базой данных
conn.close()
