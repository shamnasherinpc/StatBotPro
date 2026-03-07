import pandas as pd
import matplotlib.pyplot as plt

def run_safe_analysis(file_path):

    df = pd.read_excel(file_path)

    print("\nDataset Info:")
    print(df.info())

    total_sales = df["AMOUNT"].sum()
    average_sales = df["AMOUNT"].mean()

    max_sale = df.loc[df["AMOUNT"].idxmax()]
    min_sale = df.loc[df["AMOUNT"].idxmin()]

    print("\nSales statistics")
    print("Total sales:", total_sales)
    print("Average sales:", average_sales)
    print("Highest selling Product:", max_sale["PRODUCT"], "-", max_sale["AMOUNT"])
    print("Lowest selling product:", min_sale["PRODUCT"], "-", min_sale["AMOUNT"])

    plt.bar(df["PRODUCT"], df["AMOUNT"])
    plt.title("Product Sales")
    plt.xlabel("Product")
    plt.ylabel("Amount")

    plt.savefig("sales_chart.png")

    print("\nChart saved as sales_chart.png")