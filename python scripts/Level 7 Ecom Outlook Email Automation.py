import win32com.client
import os

# ==========================================
# CREATE OUTLOOK APPLICATION
# ==========================================

outlook = win32com.client.Dispatch(
    "Outlook.Application"
)

mail = outlook.CreateItem(0)

# ==========================================
# RECEIVER DETAILS
# ==========================================

mail.To = "sujeetgjaiswal@gmail.com"

mail.Subject = "E-Commerce Sales Automation Report"

mail.Body = """

Hello,

Please find attached the latest
E-Commerce Sales Report
generated automatically using Python.

Regards,

Python Automation

"""

# ==========================================
# ATTACH REPORT
# ==========================================

report_path = r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\Automation\indian_ecommerce_sales\Ecommerce_SQL_Report.xlsx"

if os.path.exists(report_path):

    mail.Attachments.Add(report_path)

    print("Attachment Added")

else:

    print("Report Not Found")

# ==========================================
# SEND EMAIL
# ==========================================

mail.Send()

print()

print("Email Sent Successfully")

print()

print("Automation Completed")