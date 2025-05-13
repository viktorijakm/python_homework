import sqlite3

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = 1")


# --- Task 1 ---
# SQL query to find total price per order
query = """
SELECT 
  o.order_id, 
  SUM(li.quantity * p.price) AS total_price
FROM 
  orders o
JOIN 
  line_items li ON o.order_id = li.order_id
JOIN 
  products p ON li.product_id = p.product_id
GROUP BY 
  o.order_id
ORDER BY 
  o.order_id
LIMIT 5;
"""

# Execute the query and fetch results
cursor.execute(query)
results = cursor.fetchall()

# Print the results
print("Order ID | Total Price")
print("----------------------")
for row in results:
    print(f"{row[0]:>8} | ${row[1]:.2f}")


# --- Task 2 --
print("\nCustomer Name | Average Total Price")
print("-------------------------------------")

query2 = """
SELECT 
  c.customer_name,
  AVG(order_totals.total_price) AS average_total_price
FROM 
  customers c
LEFT JOIN (
  SELECT 
    o.customer_id AS customer_id_b,
    SUM(p.price * li.quantity) AS total_price
  FROM 
    orders o
  JOIN 
    line_items li ON o.order_id = li.order_id
  JOIN 
    products p ON li.product_id = p.product_id
  GROUP BY 
    o.order_id
) AS order_totals
ON c.customer_id = order_totals.customer_id_b
GROUP BY 
  c.customer_id;
"""

cursor.execute(query2)
rows = cursor.fetchall()
for row in rows:
    customer_name, avg_price = row
    if avg_price is not None:
        print(f"{customer_name:<20} | ${avg_price:.2f}")
    else:
        print(f"{customer_name:<20} | $0.00")



# --- Task 3 --

print("\nLine Items for New Order:")
print("----------------------------")

# Begin transaction
conn.execute("BEGIN")

# Get IDs
cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
customer_id = cursor.fetchone()[0]

cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name= 'Harris'")
employee_id = cursor.fetchone()[0]

cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
product_ids = [row[0] for row in cursor.fetchall()]

# Insert order and get order_id
cursor.execute("""
    INSERT INTO orders (customer_id, employee_id, date)
    VALUES (?, ?, DATE('now'))
    RETURNING order_id
""", (customer_id, employee_id))
order_id = cursor.fetchone()[0]

# Insert line items (10 of each product)
for product_id in product_ids:
    cursor.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, 10)
    """, (order_id, product_id))

# Commit transaction
conn.commit()

# Verify insertion
cursor.execute("""
SELECT 
    li.line_item_id, 
    li.quantity, 
    p.product_name
FROM 
    line_items li
JOIN 
    products p ON li.product_id = p.product_id
WHERE 
    li.order_id = ?
""", (order_id,))

rows = cursor.fetchall()
for line_item_id, quantity, product_name in rows:
    print(f"{line_item_id:<15} | {quantity:<8} | {product_name}")



# --- Task 4 --

print("\nEmployees with More Than 5 Orders:")
print("--------------------------------------")

query4 = """
SELECT 
  e.employee_id,
  e.first_name,
  e.last_name,
  COUNT(o.order_id) AS order_count
FROM 
  employees e
JOIN 
  orders o ON e.employee_id = o.employee_id
GROUP BY 
  e.employee_id
HAVING 
  COUNT(o.order_id) > 5;
"""

cursor.execute(query4)
rows = cursor.fetchall()
for row in rows:
    employee_id, first_name, last_name, order_count = row
    print(f"{employee_id:<5} | {first_name:<15} | {last_name:<15} | {order_count:<5}")




# Close connection
conn.close()