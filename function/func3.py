import pandas as pd
import os
from UI import func_3_ui, print_dataframe

def func_3():
    file_path = "data/employees.csv"

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("\nNo database file found!")
        return

    try:
        df = pd.read_csv(file_path, header=None)
        df[2] = pd.to_numeric(df[2], errors='coerce')
        df[4] = pd.to_numeric(df[4], errors='coerce')
        df[5] = pd.to_numeric(df[5], errors='coerce')
    except Exception as e:
        print(f"\nError opening database: {e}")
        return

    func_3_ui()
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice == '1':
        val = input("Enter Name: ").strip().lower()
        result = df[df[0].astype(str).str.lower().str.contains(val)]
    elif choice == '2':
        val = input("Enter Department: ").strip().lower()
        result = df[df[1].astype(str).str.lower().str.contains(val)]
    elif choice == '3':
        try:
            val = int(input("Enter Age: "))
            result = df[df[2] == val]
        except ValueError:
            print("Invalid age."); return
    elif choice == '4':
        try:
            val = int(input("Enter Experience: "))
            result = df[df[4] == val]
        except ValueError:
            print("Invalid experience."); return
    elif choice == '5':
        try:
            min_s = float(input("Enter Min Salary: "))
            max_s = float(input("Enter Max Salary: "))
            result = df[(df[5] >= min_s) & (df[5] <= max_s)]
        except ValueError:
            print("Invalid salary."); return
    else:
        print("Invalid choice!")
        return

    if result.empty:
        print("\n--> No matching employees found.")
    else:
        print_dataframe(result)
        print(f"Total Matches Found: {len(result)}")