import pandas as pd
import os

def save_lists_to_csv(names, depts, ages, roles, exps, sals):
    file_path = "data/employees.csv"
    os.makedirs("data", exist_ok=True)
    
    df = pd.DataFrame({
        0: names, 1: depts, 2: ages, 3: roles, 4: exps, 5: sals
    })
    
    df.to_csv(file_path, mode='a', header=False, index=False)
    print("\n--> Data saved successfully!")
    
    names.clear()
    depts.clear()
    ages.clear()
    roles.clear()
    exps.clear()
    sals.clear()