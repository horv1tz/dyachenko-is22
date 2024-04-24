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
    order_date = order_date
    delivery_date = order_date + timedelta(days=delivery_days)
    c.execute("INSERT INTO Orders (ProductCode, ProductName, Customer, OrderDate, DeliveryDate, OrderCost) VALUES (?, ?, ?, ?, ?, ?)",
              (product_code, product_name, customer, order_date, delivery_date, order_cost))
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

# Примеры использования
add_order('PR001', 'Product 1', 'Company A', date(2023, 3, 27), 5, 100.0)
add_order('PR002', 'Product 2', 'Company B', date(2023, 3, 28), 3, 200.0)
add_order('PR001', 'Product 1', 'Company A', date(2023, 3, 29), 7, 150.0)

print("Все заказы:")
view_orders()

print("\nЗаказы для 'Company A':")
search_orders(customer='Company A')

print("\nЗаказы с кодом 'PR001':")
search_orders(product_code='PR001')

# Закрытие соединения с базой данных
conn.close()