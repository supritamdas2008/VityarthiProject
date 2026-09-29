import pandas as pd
import os
from UI import func_4_ui, func_4_edit_ui, func_4_field_ui, print_enumerated_dataframe

def func_4():
    file_path = "data/employees.csv"
    
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("\nNo database file found!")
        return

    try:
        df = pd.read_csv(file_path, header=None)
    except Exception as e:
        print(f"\nError: {e}"); return

    func_4_ui()
    print_enumerated_dataframe(df)

    try:
        idx = int(input("\nEnter the S.No of the employee: ")) - 1
        if idx < 0 or idx >= len(df):
            print("Invalid S.No!"); return
    except ValueError:
        print("Invalid number!"); return

    emp_name = df.iloc[idx, 0]
    print(f"\nSelected Employee: {emp_name}")
    
    func_4_edit_ui()
    action = input("Enter choice (1-2): ").strip()

    if action == '1':
        func_4_field_ui()
        field = input("Enter choice (1-6): ").strip()
        
        try:
            if field == '1':
                df.iat[idx, 0] = input("Enter new Name: ").strip()
            elif field == '2':
                dept_map = {1: "IT Dept.", 2: "Finance", 3: "Sales Dept.", 4: "Marketing", 5: "Operations", 6: "Customer Support", 7: "Administration", 8: "Legal Dept."}
                d = int(input("Select new Department (1-8): "))
                if d in dept_map: df.iat[idx, 1] = dept_map[d]
                else: print("Invalid choice!"); return
            elif field == '3':
                a = int(input("Enter new Age (18-60): "))
                if 18 <= a <= 60: df.iat[idx, 2] = a
                else: print("Invalid age!"); return
            elif field == '4':
                df.iat[idx, 3] = input("Enter new Position: ").strip()
            elif field == '5':
                e = int(input("Enter new Experience (0-40): "))
                if 0 <= e <= 40: df.iat[idx, 4] = e
                else: print("Invalid experience!"); return
            elif field == '6':
                s = float(input("Enter new Salary: "))
                if s >= 0: df.iat[idx, 5] = s
                else: print("Invalid salary!"); return
            else:
                print("Invalid choice!"); return
                
            df.to_csv(file_path, index=False, header=False)
            print("\n--> Updated successfully!")
        except ValueError:
            print("Invalid entry!")
        except Exception as e:
            print(f"Error: {e}")

    elif action == '2':
        if input(f"Delete '{emp_name}'? (y/n): ").strip().lower() == 'y':
            df = df.drop(idx)
            df.to_csv(file_path, index=False, header=False)
            print("\n--> Deleted successfully!")
        else:
            print("\nDeletion cancelled.")
    else:
        print("Invalid choice!")