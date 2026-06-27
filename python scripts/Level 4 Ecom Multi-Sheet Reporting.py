import pandas as pd

# Read Master Dataset
master_df = pd.read_excel("Master_Ecommerce_Report.xlsx")

# Convert Order_Date
master_df["Order_Date"] = pd.to_datetime(master_df["Order_Date"])

# ====================================================
# SHEET 1 : SUMMARY
# ====================================================

summary_df = pd.DataFrame({

    "KPI":[
        "Total Orders",
        "Total Revenue",
        "Average Order Value",
        "Average Rating",
        "Total Quantity Sold",
        "Unique Products",
        "Unique Categories",
        "Unique Cities"
    ],

    "Value":[
        len(master_df),
        master_df["Total_Amount"].sum(),
        master_df["Total_Amount"].mean(),
        master_df["Rating"].mean(),
        master_df["Quantity"].sum(),
        master_df["Product_Name"].nunique(),
        master_df["Product_Category"].nunique(),
        master_df["Customer_City"].nunique()
    ]

})

# ====================================================
# SHEET 2 : PRODUCT REPORT
# ====================================================

product_df = (
    master_df
    .groupby("Product_Name", as_index=False)
    .agg(
        Total_Revenue=("Total_Amount","sum"),
        Total_Orders=("Order_ID","count"),
        Average_Rating=("Rating","mean")
    )
    .sort_values(
        by="Total_Revenue",
        ascending=False
    )
)

# ====================================================
# SHEET 3 : CATEGORY REPORT
# ====================================================

category_df = (
    master_df
    .groupby("Product_Category", as_index=False)
    .agg(
        Total_Revenue=("Total_Amount","sum"),
        Total_Orders=("Order_ID","count")
    )
    .sort_values(
        by="Total_Revenue",
        ascending=False
    )
)

# ====================================================
# SHEET 4 : CITY REPORT
# ====================================================

city_df = (
    master_df
    .groupby("Customer_City", as_index=False)
    .agg(
        Revenue=("Total_Amount","sum"),
        Orders=("Order_ID","count")
    )
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

# ====================================================
# SHEET 5 : PAYMENT REPORT
# ====================================================

payment_df = (
    master_df
    .groupby("Payment_Method", as_index=False)
    .agg(
        Revenue=("Total_Amount","sum"),
        Orders=("Order_ID","count")
    )
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

# ====================================================
# EXPORT TO EXCEL
# ====================================================

file_name = "Ecommerce_Multi_Sheet_Report.xlsx"

with pd.ExcelWriter(file_name) as writer:

    summary_df.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    product_df.to_excel(
        writer,
        sheet_name="Products",
        index=False
    )

    category_df.to_excel(
        writer,
        sheet_name="Categories",
        index=False
    )

    city_df.to_excel(
        writer,
        sheet_name="Cities",
        index=False
    )

    payment_df.to_excel(
        writer,
        sheet_name="Payments",
        index=False
    )

print(f"{file_name} Created Successfully")