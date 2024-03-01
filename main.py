import psycopg2

conn = psycopg2.connect(dbname="message", user="iamratnikov", password="vr2609")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE orders (id SERIAL PRIMARY KEY, ord_no INTEGER, purch_amt INTEGER,"
#                " ord_date VARCHAR(50), customer_id INTEGER, salesman_id INTEGER)")
# orders = [(70001, 150.5, "2012-10-05", 3005, 5002),
#           (70009, 270.65, "2012-09-10", 3001, 5005),
#           (70002, 65.26, "2012-10-05", 3002, 5001),
#           (70004, 110.5, "2012-08-17", 3009, 5003),
#           (70007, 948.5, "2012-09-10", 3005, 5002),
#           (70005, 2400.6, "2012-07-27", 3007, 5001),
#           (70008, 5760, "2012-09-10", 3002, 5001),
#           (70010, 1983.43, "2012-10-10", 3004, 5006),
#           (70003, 2480.4, "2012-10-10", 3009, 5003),
#           (70012, 250.45, "2012-06-27", 3008, 5002),
#           (70011, 75.29, "2012-08-17", 3003, 5007),
#           (70013, 3045.6, "2012-04-25", 3002, 5001)]
# cursor.executemany("INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, "
#                    "salesman_id) VALUES (%s, %s, %s, %s, %s)", orders)
# conn.commit()
"""
1)Напечатайте номер заказа, дату заказа и количество для каждого заказа,
Который продал продавец под номером: 5002
"""
cursor.execute("SELECT * FROM orders WHERE salesman_id=5002 ")
for i in cursor.fetchall():
    print(f"{i[1]} - {i[3]} - {i[2]}- {i[5]}")
print("----------------------------------")
'''
3)Напечатайте по порядку данные о дате заказа, id продавца, номер заказа,
количество
'''
cursor.execute("SELECT * FROM orders")
for i in cursor.fetchall():
    print(f"{i[3]} - {i[5]} - {i[1]}- {i[2]}")
# cursor.execute("DROP TABLE orders")
# conn.commit()
cursor.close()
conn.close()
