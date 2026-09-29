import pandas as pd
import os
from UI import func_2_ui, print_dataframe

def func_2():
    func_2_ui()
    file_path = "data/employees.csv"

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("No database file found! Add employees first.")
        return

    try:
        df = pd.read_csv(file_path, header=None)
        print_dataframe(df)
        print(f"Total Employees Found: {len(df)}")
    except Exception as e:
        print(f"Error reading records: {e}")