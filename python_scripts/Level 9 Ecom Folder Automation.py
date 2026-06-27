import pandas as pd
import os

# ==========================================
# FOLDER PATH
# ==========================================

folder_path = r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\Automation\indian_ecommerce_sales\Ecommerce_Data"

# ==========================================
# EMPTY LIST
# ==========================================

all_data = []

# ==========================================
# READ EVERY CSV FILE
# ==========================================

for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        file_path = os.path.join(
            folder_path,
            file
        )

        print(f"Reading : {file}")

        df = pd.read_csv(file_path)

        all_data.append(df)

# ==========================================
# MERGE ALL FILES
# ==========================================

master_df = pd.concat(
    all_data,
    ignore_index=True
)

# ==========================================
# CONVERT DATE
# ==========================================

master_df["Order_Date"] = pd.to_datetime(
    master_df["Order_Date"],
    format="%d-%m-%Y"
)

# ==========================================
# BUSINESS SUMMARY
# ==========================================

print()

print("========== FOLDER AUTOMATION ==========")

print()

print("Files Processed :", len(all_data))

print("Total Orders :", len(master_df))

print("Total Revenue : Rs.",
      round(master_df["Total_Amount"].sum(),2))

print("Average Rating :",
      round(master_df["Rating"].mean(),2))

print("Unique Products :",
      master_df["Product_Name"].nunique())

print("Unique Categories :",
      master_df["Product_Category"].nunique())

print("Unique Cities :",
      master_df["Customer_City"].nunique())

print()

print("=======================================")

# ==========================================
# EXPORT REPORT
# ==========================================

master_df.to_excel(

    "Folder_Automation_Report.xlsx",

    index=False

)

print()

print("Folder Automation Completed Successfully")