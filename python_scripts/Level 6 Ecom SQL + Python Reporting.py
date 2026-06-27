import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# DATABASE CONNECTION
# ==========================================

engine = create_engine(
    "mssql+pyodbc://@DESKTOP-AK7LHRO\\SQLEXPRESS/ECOMMERCE?driver=SQL+Server&trusted_connection=yes"
)

# ==========================================
# QUERY 1 : TOP 10 PRODUCTS
# ==========================================

product_query = """

SELECT TOP 10

Product_Name,

SUM(Total_Amount) AS Total_Revenue,

SUM(Quantity) AS Total_Quantity

FROM ecommerce_sales

GROUP BY Product_Name

ORDER BY Total_Revenue DESC

"""

# ==========================================
# QUERY 2 : CATEGORY REPORT
# ==========================================

category_query = """

SELECT

Product_Category,

SUM(Total_Amount) AS Total_Revenue,

COUNT(Order_ID) AS Total_Orders

FROM ecommerce_sales

GROUP BY Product_Category

ORDER BY Total_Revenue DESC

"""

# ==========================================
# QUERY 3 : CITY REPORT
# ==========================================

city_query = """

SELECT

Customer_City,

SUM(Total_Amount) AS Total_Revenue,

COUNT(Order_ID) AS Total_Orders

FROM ecommerce_sales

GROUP BY Customer_City

ORDER BY Total_Revenue DESC

"""

# ==========================================
# QUERY 4 : PAYMENT REPORT
# ==========================================

payment_query = """

SELECT

Payment_Method,

SUM(Total_Amount) AS Total_Revenue,

COUNT(Order_ID) AS Total_Orders

FROM ecommerce_sales

GROUP BY Payment_Method

ORDER BY Total_Revenue DESC

"""

# ==========================================
# READ SQL DATA
# ==========================================

product_df = pd.read_sql(
    product_query,
    engine
)

category_df = pd.read_sql(
    category_query,
    engine
)

city_df = pd.read_sql(
    city_query,
    engine
)

payment_df = pd.read_sql(
    payment_query,
    engine
)

# ==========================================
# EXPORT TO EXCEL
# ==========================================

file_name = "Ecommerce_SQL_Report.xlsx"

with pd.ExcelWriter(file_name) as writer:

    product_df.to_excel(
        writer,
        sheet_name="Top Products",
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

print()

print("SQL Automation Completed Successfully")

print()

print(file_name)