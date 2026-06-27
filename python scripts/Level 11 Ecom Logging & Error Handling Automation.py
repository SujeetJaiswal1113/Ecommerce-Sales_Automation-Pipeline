import pandas as pd
import logging

# ==========================================
# LOG FILE CONFIGURATION
# ==========================================

logging.basicConfig(
    filename="Ecommerce_Automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:

    logging.info("Automation Started")

    # Read Dataset
    ecommerce_df = pd.read_csv(
        "indian_ecommerce_sales.csv"
    )

    logging.info("Data Read Successfully")

    # Business KPIs
    total_orders = len(ecommerce_df)

    total_revenue = ecommerce_df["Total_Amount"].sum()

    average_rating = ecommerce_df["Rating"].mean()

    print("Total Orders :", total_orders)

    print("Total Revenue :", round(total_revenue, 2))

    print("Average Rating :", round(average_rating, 2))

    logging.info("Business KPI Calculated Successfully")

    # Export Report
    ecommerce_df.to_excel(
        "Logging_Report.xlsx",
        index=False
    )

    logging.info("Excel Report Created Successfully")

    print("\nAutomation Completed Successfully")

except Exception as e:

    logging.error(f"Error Occurred : {e}")

    print("Automation Failed")

finally:

    logging.info("Automation Finished")