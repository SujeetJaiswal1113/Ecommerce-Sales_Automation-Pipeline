import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# ==========================================================
# DATABASE CONNECTION
# ==========================================================

engine = create_engine(

    "mssql+pyodbc://@DESKTOP-AK7LHRO\\SQLEXPRESS/"
    "ECOMMERCE?"
    "driver=SQL+Server&trusted_connection=yes"

)

print("Connected to SQL Server")

# ==========================================================
# EXTRACT
# ==========================================================

query = """

SELECT *

FROM ecommerce_sales

"""

ecommerce_df = pd.read_sql(query, engine)

print("Data Extracted Successfully")

# ==========================================================
# TRANSFORM
# ==========================================================

print(ecommerce_df["Order_Date"].head())
print(ecommerce_df["Order_Date"].dtype)

ecommerce_df["Order_Date"] = pd.to_datetime(
    ecommerce_df["Order_Date"],
    format="mixed"
)

ecommerce_df["Rank"] = range(
    1,
    len(ecommerce_df)+1
)

ecommerce_df["Order_Year"] = (
    ecommerce_df["Order_Date"].dt.year
)

ecommerce_df["Order_Month"] = (
    ecommerce_df["Order_Date"].dt.month_name()
)

ecommerce_df["Revenue_Category"] = ecommerce_df[
    "Total_Amount"
].apply(

    lambda x:

    "High"

    if x >= 100000

    else "Low"

)

print("Data Transformation Completed")

# ==========================================================
# LOAD
# ==========================================================

report_name = "Final_ETL_Report.xlsx"

with pd.ExcelWriter(report_name) as writer:

    ecommerce_df.to_excel(

        writer,

        sheet_name="Master_Data",

        index=False

    )

print("Excel Report Created")

# ==========================================================
# ETL LOG
# ==========================================================

with open(

    "ETL_Log.txt",

    "a"

) as file:

    file.write(

        f"ETL Success : {datetime.now()}\n"

    )

print("ETL Log Updated")

print()

print("REAL ETL PIPELINE COMPLETED SUCCESSFULLY")