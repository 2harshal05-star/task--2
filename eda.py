
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the cleaned dataset
file_path = Path("data/cleaned_dataset.xlsx")
df = pd.read_excel(file_path)

# Display basic information
print("========== DATASET OVERVIEW ==========")
print("Dataset shape:", df.shape)

print("\n========== FIRST 5 ROWS ==========")
print(df.head().to_string(index=False))

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe(include="all").to_string())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== SALES BY CATEGORY ==========")
print(
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY CITY ==========")
print(
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== TOP 5 PRODUCTS BY SALES ==========")
print(
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Create charts folder
Path("charts").mkdir(exist_ok=True)

# Chart 1: Sales by category
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(
    ascending=False
)
category_sales.plot(kind="bar", title="Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.close()

# Chart 2: Sales by city
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(
    ascending=False
)
city_sales.plot(kind="bar", title="Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/sales_by_city.png")
plt.close()

print("\nEDA completed. Charts saved in the charts folder.")