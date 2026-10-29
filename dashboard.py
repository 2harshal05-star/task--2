
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_excel("data/cleaned_dataset.xlsx")
Path("dashboard").mkdir(exist_ok=True)

# Calculate key metrics
total_sales = df["Total_Sales"].sum()
total_orders = len(df)
average_sale = df["Total_Sales"].mean()
total_quantity = df["Quantity"].sum()

print("========== DASHBOARD SUMMARY ==========")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Records: {total_orders:,}")
print(f"Average Sale per Record: ₹{average_sale:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")

# Prepare category sales
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(
    ascending=False
)

# Prepare monthly sales
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)
monthly_sales.index = monthly_sales.index.astype(str)

# Create dashboard figure
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

category_sales.plot(
    kind="bar", ax=axes[0], title="Sales by Category"
)
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Total Sales")
axes[0].tick_params(axis="x", rotation=45)

monthly_sales.plot(
    kind="line", marker="o", ax=axes[1], title="Monthly Sales Trend"
)
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Total Sales")
axes[1].tick_params(axis="x", rotation=45)

fig.suptitle("Sales Analytics Dashboard", fontsize=16)
fig.tight_layout()
fig.savefig("dashboard/sales_dashboard.png", dpi=150)
plt.close(fig)

print("\nDashboard saved to dashboard/sales_dashboard.png")
