import pandas as pd
import os

# Folder containing yearly sales files
folder_path = r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\Automation\indian_ecommerce_sales\Ecommerce_Data"

# Empty list to store DataFrames
all_data = []

# Read every CSV file in the folder
for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        file_path = os.path.join(folder_path, file)

        print(f"Reading : {file}")

        df = pd.read_csv(file_path)

        all_data.append(df)

# Merge all DataFrames
master_df = pd.concat(
    all_data,
    ignore_index=True
)

# Convert Order_Date into Date format
master_df["Order_Date"] = pd.to_datetime(
    master_df["Order_Date"],
    format="%d-%m-%Y"
)

# Basic Analysis
print("\n------------- MASTER DATA SUMMARY -------------")

print("Total Rows :", len(master_df))

print("Total Revenue :",
      master_df["Total_Amount"].sum())

print("Unique Products :",
      master_df["Product_Name"].nunique())

print("Unique Categories :",
      master_df["Product_Category"].nunique())

print("Unique Cities :",
      master_df["Customer_City"].nunique())

print("-----------------------------------------------")

# Export Master Dataset
master_df.to_excel(
    "Master_Ecommerce_Report.xlsx",
    index=False
)

print("\nMaster Report Created Successfully")