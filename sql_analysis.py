
import pandas as pd
import sqlite3
from pathlib import Path

# Load the cleaned dataset
df = pd.read_excel("data/cleaned_dataset.xlsx")

# Create a database file
Path("sql").mkdir(exist_ok=True)
connection = sqlite3.connect("sql/sales.db")

# Import the dataset into SQLite
df.to_sql("orders", connection, if_exists="replace", index=False)

print("Dataset successfully loaded into SQLite!")

# 1. Total sales
print("\n1. TOTAL SALES")
print(pd.read_sql_query("""
SELECT ROUND(SUM(Total_Sales), 2) AS total_sales
FROM orders;
""", connection))

# 2. Sales by category
print("\n2. SALES BY CATEGORY")
print(pd.read_sql_query("""
SELECT Category, ROUND(SUM(Total_Sales), 2) AS total_sales
FROM orders
GROUP BY Category
ORDER BY total_sales DESC;
""", connection))

# 3. Sales by city
print("\n3. SALES BY CITY")
print(pd.read_sql_query("""
SELECT City, ROUND(SUM(Total_Sales), 2) AS total_sales
FROM orders
GROUP BY City
ORDER BY total_sales DESC;
""", connection))

# 4. Top 5 products by sales
print("\n4. TOP 5 PRODUCTS BY SALES")
print(pd.read_sql_query("""
SELECT Product, ROUND(SUM(Total_Sales), 2) AS total_sales
FROM orders
GROUP BY Product
ORDER BY total_sales DESC
LIMIT 5;
""", connection))

# 5. Total quantity sold by product
print("\n5. QUANTITY SOLD BY PRODUCT")
print(pd.read_sql_query("""
SELECT Product, SUM(Quantity) AS total_quantity
FROM orders
GROUP BY Product
ORDER BY total_quantity DESC;
""", connection))

# 6. Average customer age by gender
print("\n6. AVERAGE CUSTOMER AGE BY GENDER")
print(pd.read_sql_query("""
SELECT Gender, ROUND(AVG(Age), 2) AS average_age
FROM orders
GROUP BY Gender;
""", connection))

connection.close()
print("\nSQL analysis completed!")
