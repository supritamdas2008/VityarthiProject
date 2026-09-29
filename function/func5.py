import pandas as pd
import os
from UI import print_report_ui

def func_5():
    file_path = "data/employees.csv"

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("\nNo database file found!")
        return

    try:
        df = pd.read_csv(file_path, header=None)
    except Exception as e:
        print(f"\nError: {e}")
        return
        
    df.columns = ['Name', 'Dept', 'Age', 'Pos', 'Exp', 'Sal']
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce').fillna(0)
    df['Exp'] = pd.to_numeric(df['Exp'], errors='coerce').fillna(0)
    df['Sal'] = pd.to_numeric(df['Sal'], errors='coerce').fillna(0)

    stats = {
        'total_emp': len(df),
        'total_pay': df['Sal'].sum(),
        'avg_pay': df['Sal'].mean() if not df.empty else 0,
        'dept_counts': df['Dept'].value_counts().to_dict(),
        'old_name': df.loc[df['Age'].idxmax(), 'Name'],
        'old_age': df['Age'].max(),
        'old_dept': df.loc[df['Age'].idxmax(), 'Dept'],
        'young_name': df.loc[df['Age'].idxmin(), 'Name'],
        'young_age': df['Age'].min(),
        'young_dept': df.loc[df['Age'].idxmin(), 'Dept'],
        'exp_name': df.loc[df['Exp'].idxmax(), 'Name'],
        'exp_years': df['Exp'].max(),
        'exp_dept': df.loc[df['Exp'].idxmax(), 'Dept'],
        'min_exp_name': df.loc[df['Exp'].idxmin(), 'Name'],
        'min_exp_years': df['Exp'].min(),
        'min_exp_dept': df.loc[df['Exp'].idxmin(), 'Dept'],
        'rich_name': df.loc[df['Sal'].idxmax(), 'Name'],
        'rich_sal': df['Sal'].max(),
        'rich_pos': df.loc[df['Sal'].idxmax(), 'Pos'],
        'poor_name': df.loc[df['Sal'].idxmin(), 'Name'],
        'poor_sal': df['Sal'].min(),
        'poor_pos': df.loc[df['Sal'].idxmin(), 'Pos']
    }

    print_report_ui(stats)