import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("sales.csv.xlsx")
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
total_sales=df["AMOUNT"].sum()
average_sales=df["AMOUNT"].mean()
max_sale = df.loc[df["AMOUNT"].idxmax()]
min_sale= df.loc[df["AMOUNT"].idxmin()]
print("\nSales statistics")
print("Total sales:",total_sales)
print("Average sales:",average_sales)
print("Highest selling Product:",max_sale["PRODUCT"],"-",max_sale["AMOUNT"])
print("Lowest selling product:",min_sale["PRODUCT"],"-",min_sale["AMOUNT"])

plt.bar(df["PRODUCT"], df["AMOUNT"])
plt.title("product sales")
plt.xlabel("Product")
plt.ylabel("Amount")

plt.savefig("sales_chart.png")
print("\nchart saved as sales_chart.png")