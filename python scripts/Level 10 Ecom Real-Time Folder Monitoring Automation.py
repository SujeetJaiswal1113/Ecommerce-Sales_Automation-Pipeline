import os
import time
import pandas as pd

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ======================================================
# FOLDER TO WATCH
# ======================================================

folder_to_watch = r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\Automation\indian_ecommerce_sales\Ecommerce_Data"

# ======================================================
# AUTOMATION FUNCTION
# ======================================================

def run_automation():

    print("\nStarting Folder Automation...\n")

    all_data = []

    for file in os.listdir(folder_to_watch):

        if file.endswith(".csv"):

            file_path = os.path.join(
                folder_to_watch,
                file
            )

            print(f"Reading : {file}")

            df = pd.read_csv(file_path)

            all_data.append(df)

    if len(all_data) == 0:

        print("No CSV Files Found")

        return

    master_df = pd.concat(
        all_data,
        ignore_index=True
    )

    master_df["Order_Date"] = pd.to_datetime(
        master_df["Order_Date"],
        format="%d-%m-%Y"
    )

    print("\n========== LIVE SUMMARY ==========")

    print("Files Processed :",
          len(all_data))

    print("Total Orders :",
          len(master_df))

    print("Total Revenue : Rs.",
          round(master_df["Total_Amount"].sum(),2))

    print("Average Rating :",
          round(master_df["Rating"].mean(),2))

    print("==================================")

    master_df.to_excel(
        "Live_Folder_Report.xlsx",
        index=False
    )

    print("\nLive Report Updated Successfully\n")


# ======================================================
# WATCHDOG EVENT
# ======================================================

class FolderHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        if event.src_path.endswith(".csv"):

            print("\nNew CSV File Detected")

            print(event.src_path)

            run_automation()


# ======================================================
# START WATCHING
# ======================================================

event_handler = FolderHandler()

observer = Observer()

observer.schedule(
    event_handler,
    folder_to_watch,
    recursive=False
)

observer.start()

print("Watching Folder...")

try:

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()