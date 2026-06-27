import pandas as pd

ecommerce_df = pd.read_csv(r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\Automation\indian_ecommerce_sales\indian_ecommerce_sales.csv")

print(ecommerce_df.head())
print(ecommerce_df.shape)
print(ecommerce_df.columns)
ecommerce_df.info()

print("Total Rows =", len(ecommerce_df))

print("Total Revenue =",
      ecommerce_df["Total_Amount"].sum())

print("Unique Products =",
      ecommerce_df["Product_Name"].nunique())

print("Unique Categories =",
      ecommerce_df["Product_Category"].nunique())

ecommerce_df.to_excel(
    "Ecommerce_Report.xlsx",
    index=False
)

print("Report Created Successfully")
