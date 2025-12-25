import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

if not os.path.exists("charts"):
    os.makedirs("charts")

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Product A": np.random.randint(15000, 55000, 12),
    "Product B": np.random.randint(18000, 65000, 12),
    "Product C": np.random.randint(10000, 45000, 12)
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)
print("Dataset created: sales_data.csv\n")

print("==== SALES DATA ====")
print(df.head(12))
print("----------------------\n")

df["Total Sales"] = df["Product A"] + df["Product B"] + df["Product C"]

total_sales = df["Total Sales"].sum()
best_month = df.loc[df["Total Sales"].idxmax(), "Month"]
worst_month = df.loc[df["Total Sales"].idxmin(), "Month"]

print(f"Total Annual Sales: ₹{total_sales}")
print(f"Best Month: {best_month}")
print(f"Worst Month: {worst_month}\n")

product_totals = {
    "Product A": df["Product A"].sum(),
    "Product B": df["Product B"].sum(),
    "Product C": df["Product C"].sum()
}

best_product = max(product_totals, key=product_totals.get)
print(f"Best Performing Product: {best_product}\n")

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="Month", y="Total Sales", marker="o")
plt.title("Monthly Total Sales Trend")
plt.savefig("charts/monthly_sales_trend.png")
plt.show()

plt.figure(figsize=(10,6))
df.plot(x="Month", y=["Product A","Product B","Product C"], marker="o")
plt.title("Product Sales Comparison")
plt.savefig("charts/product_comparison.png")
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(x=list(product_totals.keys()), y=list(product_totals.values()))
plt.title("Total Sales per Product (Year)")
plt.savefig("charts/product_totals.png")
plt.show()

print("Charts saved inside /charts folder.")
