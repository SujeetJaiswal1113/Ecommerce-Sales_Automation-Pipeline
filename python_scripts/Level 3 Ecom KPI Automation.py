import pandas as pd

# Read Master Dataset
master_df = pd.read_excel("Master_Ecommerce_Report.xlsx")

# Convert Date
master_df["Order_Date"] = pd.to_datetime(master_df["Order_Date"])

# -----------------------------
# BUSINESS KPIs
# -----------------------------

total_orders = len(master_df)

total_revenue = master_df["Total_Amount"].sum()

average_order_value = master_df["Total_Amount"].mean()

average_rating = master_df["Rating"].mean()

total_quantity = master_df["Quantity"].sum()

unique_products = master_df["Product_Name"].nunique()

unique_categories = master_df["Product_Category"].nunique()

unique_cities = master_df["Customer_City"].nunique()

top_product = (
    master_df.groupby("Product_Name")["Total_Amount"]
             .sum()
             .idxmax()
)

top_category = (
    master_df.groupby("Product_Category")["Total_Amount"]
             .sum()
             .idxmax()
)

top_city = (
    master_df.groupby("Customer_City")["Total_Amount"]
             .sum()
             .idxmax()
)

top_payment = (
    master_df["Payment_Method"]
             .mode()[0]
)

highest_order = master_df["Total_Amount"].max()

lowest_order = master_df["Total_Amount"].min()

# -----------------------------
# PRINT KPIs
# -----------------------------

print("\n========== Ecom Sales KPI DASHBOARD ==========\n")

print(f"Total Orders            : {total_orders}")

print(f"Total Revenue           : Rs.{total_revenue:,.2f}")

print(f"Average Order Value     : Rs.{average_order_value:,.2f}")

print(f"Average Rating          : {average_rating:.2f}")

print(f"Total Quantity Sold     : {total_quantity}")

print(f"Unique Products         : {unique_products}")

print(f"Unique Categories       : {unique_categories}")

print(f"Unique Cities           : {unique_cities}")

print(f"Top Revenue Product     : {top_product}")

print(f"Top Revenue Category    : {top_category}")

print(f"Top Revenue City        : {top_city}")

print(f"Most Used Payment Mode  : {top_payment}")

print(f"Highest Order Value     : Rs.{highest_order:,.2f}")

print(f"Lowest Order Value      : Rs.{lowest_order:,.2f}")

print("\n============================================\n")

# -----------------------------
# SAVE KPI REPORT
# -----------------------------

kpi_df = pd.DataFrame({

    "KPI":[
        "Total Orders",
        "Total Revenue",
        "Average Order Value",
        "Average Rating",
        "Total Quantity Sold",
        "Unique Products",
        "Unique Categories",
        "Unique Cities",
        "Top Revenue Product",
        "Top Revenue Category",
        "Top Revenue City",
        "Most Used Payment Mode",
        "Highest Order Value",
        "Lowest Order Value"
    ],

    "Value":[
        total_orders,
        total_revenue,
        average_order_value,
        average_rating,
        total_quantity,
        unique_products,
        unique_categories,
        unique_cities,
        top_product,
        top_category,
        top_city,
        top_payment,
        highest_order,
        lowest_order
    ]

})

kpi_df.to_excel(
    "Ecom_Sales_KPI_Report.xlsx",
    index=False
)

print("Ecom_Sales_KPI_Report Created Successfully")