import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# Step 1: Read data into a DataFrame from a JOIN of line_items and products
query = """
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM 
    line_items
JOIN 
    products ON line_items.product_id = products.product_id
"""
df = pd.read_sql_query(query, conn)

# Step 2: Print the first 5 lines
print("\nInitial DataFrame:")
print(df.head())

# Step 3: Add 'total' column (quantity * price)
df['total'] = df['quantity'] * df['price']
print("\nWith 'total' column:")
print(df.head())

# Step 4: Group by product_id
summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

# Rename columns for clarity
summary.columns = ['product_id', 'order_count', 'total_revenue', 'product_name']

# Step 5: Sort by product_name
summary = summary.sort_values(by='product_name')

# Print result
print("\nGrouped and Sorted Summary:")
print(summary.head())

# Step 6: Save to CSV
summary.to_csv("order_summary.csv", index=False)
print("\nSummary saved to order_summary.csv")

# Close the connection
conn.close()
