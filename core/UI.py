import datetime as dt

def start_ui():
    now = dt.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    
    print("\n==================********************==================")
    if now.hour < 12:
        greeting = "Good Morning!..."
    elif 12 <= now.hour < 18:
        greeting = "Good Afternoon!..."
    else:
        greeting = "Good Evening!..."
        
    print(f"{greeting:>38}")
    print("    Welcome to Employee Database Management System")
    print("==================********************==================")
    print(f"{'Login Time: ' + time_str:>55}\n")
    
    print("    The Instructions for the program are as follows:\n")
    print("1. Add a New Employee")
    print("2. View All the Employee Details")
    print("3. Search for an Employee")
    print("4. Update an Employee Details and Micellaneous")
    print("5. Show Reports and Statistics")
    print("6. Exit the Program\n")

def func_1_ui():
    print("\n-----Select Department-----")
    print("1. IT Dept.")
    print("2. Finance")
    print("3. Sales Dept.")
    print("4. Marketing")
    print("5. Operations")
    print("6. Customer Support")
    print("7. Administration")
    print("8. Legal Dept.")

def func_2_ui():
    print("\n================================ CURRENT EMPLOYEE RECORDS ================================\n")

def func_3_ui():
    print("\n================== SEARCH MENU ==================")
    print("1. Search By Name")
    print("2. Search By Department")
    print("3. Search By Age")
    print("4. Search By Experience")
    print("5. Search By Salary (Range)")
    print("=================================================")

def func_4_ui():
    print("\n================== UPDATE / DELETE EMPLOYEE DETAILS ==================\n")

def func_4_edit_ui():
    print("\nWhat do you want to do?")
    print("1. Edit Employee Details")
    print("2. Delete Employee Record")

def func_4_field_ui():
    print("\nWhich detail do you want to edit?")
    print("1. Name")
    print("2. Department")
    print("3. Age")
    print("4. Position")
    print("5. Experience")
    print("6. Salary")

def print_dataframe(df):
    print("=" * 90)
    print(f"{'Name':<25} {'Department':<18} {'Age':<6} {'Position':<22} {'Exp':<6} {'Salary':<10}")
    print("=" * 90)
    for _, row in df.iterrows():
        print(f"{str(row.iloc[0]):<25} {str(row.iloc[1]):<18} {str(row.iloc[2]):<6} {str(row.iloc[3]):<22} {str(row.iloc[4]):<6} {float(row.iloc[5]):<10.2f}")
    print("=" * 90)

def print_enumerated_dataframe(df):
    print(f"{'S.No':<5} {'Name':<22} {'Department':<16} {'Age':<5} {'Position':<20} {'Exp':<5} {'Salary':<10}")
    print("=" * 88)
    for index, row in df.iterrows():
        print(f"{index + 1:<5} {str(row.iloc[0]):<22} {str(row.iloc[1]):<16} {str(row.iloc[2]):<5} {str(row.iloc[3]):<20} {str(row.iloc[4]):<5} {float(row.iloc[5]):<10.2f}")
    print("=" * 88)

def print_report_ui(stats):
    print("\n==========================================================")
    print("               COMPANY ANALYTICAL REPORT                  ")
    print("==========================================================")
    
    print("\n1. GENERAL OVERVIEW")
    print(f"   • Total Employees      : {stats['total_emp']}")
    print(f"   • Total Monthly Payroll : ₹{stats['total_pay']:,.2f}")
    print(f"   • Average Salary       : ₹{stats['avg_pay']:,.2f}")
    
    print("\n2. DEPARTMENT HEADCOUNT")
    for dept, count in stats['dept_counts'].items():
        print(f"   • {dept:<22} : {count} employee(s)")
        
    print("\n3. AGE EXTREMES")
    print(f"   • Oldest Employee       : {stats['old_name']} ({stats['old_age']} yrs old | {stats['old_dept']})")
    print(f"   • Youngest Employee     : {stats['young_name']} ({stats['young_age']} yrs old | {stats['young_dept']})")
    
    print("\n4. EXPERIENCE EXTREMES")
    print(f"   • Most Experienced      : {stats['exp_name']} ({stats['exp_years']} yrs exp || {stats['exp_dept']})")
    print(f"   • Least Experienced     : {stats['min_exp_name']} ({stats['min_exp_years']} yrs exp || {stats['min_exp_dept']})")
    
    print("\n5. INCOME EXTREMES")
    print(f"   • Highest Paid          : {stats['rich_name']} (₹{stats['rich_sal']:,.2f} || {stats['rich_pos']})")
    print(f"   • Lowest Paid           : {stats['poor_name']} (₹{stats['poor_sal']:,.2f} || {stats['poor_pos']})")
    print("==========================================================\n")