import sqlite3
import pandas as pd

#convert dataset to sqlite database
df = pd.read_csv('data/product_data.csv')
conn = sqlite3.connect('data/product_data.db')
df.to_sql('inventory', conn, if_exists='replace', index=False)
print("database created successfully!")

# Query 1 - See first 10 products
query1 = "SELECT * FROM inventory LIMIT 10"
result1 = pd.read_sql_query(query1, conn)
print("\n=== FIRST 10 PRODUCTS ===")
print(result1)

query2 = """
select product_name, category, warehouse, expiry_date
FROM inventory
Where expiry_date <= date('now', '+30 days')
order by expiry_date ASC
LIMIT 10"""
result_2 = pd.read_sql_query(query2, conn)
print("\n=== products expiring within 30 days ===")
print(result_2)

query3 = """
select warehouse,
count(*)as total_products,
sum(stock_quantity)as total_stock,
avg(stock_quantity)as avg_stock
from inventory
group by warehouse
order by total_products desc
"""
result_3 = pd.read_sql_query(query3, conn)
print("\n=== warehouse stock summary ===")
print(result_3)