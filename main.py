
import pandas as pd
import matplotlib.pyplot as plt


df =pd.read_excel("data/sales_ex.xlsx")
print(df.head())
print(df.columns)
print(df.info())

print(df.isnull().sum())

df["Quantity"].fillna(df["Quantity"].mean(),inplace=True)
df["Price"].fillna(df["Price"].mean(),inplace=True)

print(df.isnull().sum())

print(df.duplicated().sum())

df["Sales"] = df["Quantity"] * df["Price"]

# ---- Dashboard ----
plt.figure(figsize=(12, 5))

# 🔹 ADD DASHBOARD TITLE (HERE ✅)
plt.suptitle("Agneyra | Sales Performance Dashboard",
             fontsize=16, fontweight="bold")


# 🔹 BAR CHART – Sales by Product
plt.subplot(1, 2, 1)
product_sales = df.groupby("Product")["Sales"].sum()
product_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)

# 🔹 PIE CHART – Sales Share by Product
plt.subplot(1, 2, 2)
product_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Sales Distribution")
plt.ylabel("")  # remove y-label

# Show dashboard
plt.tight_layout()
plt.show()

