from UI import func_1_ui

def func_1(names, depts, ages, roles, exps, sals):
    while True:
        try:
            count = int(input("How many employees do you want to add? "))
            if count > 0: break
            print("Enter a number greater than 0.\n")
        except ValueError:
            print("Enter a valid number.\n")

    dept_map = {1: "IT Dept.", 2: "Finance", 3: "Sales Dept.", 4: "Marketing", 5: "Operations", 6: "Customer Support", 7: "Administration", 8: "Legal Dept."}

    for i in range(count):
        print(f"\n------------------ Adding Employee {i + 1} of {count} ------------------")
        names.append(input("Enter Employee Name: ").strip())
        
        func_1_ui()
        while True:
            try:
                d_choice = int(input("\nSelect Department (1-8): "))
                if d_choice in dept_map:
                    depts.append(dept_map[d_choice])
                    break
                print("Pick between 1 and 8.")
            except ValueError:
                print("Enter a number.")

        while True:
            try:
                age = int(input("Enter Employee Age (18-60): "))
                if 18 <= age <= 60:
                    ages.append(age)
                    break
                print("Must be between 18 and 60.")
            except ValueError:
                print("Enter a valid number.")

        roles.append(input("Enter Employee Position / Role: ").strip())

        while True:
            try:
                exp = int(input("Enter Work Experience (0-40 years): "))
                if 0 <= exp <= 40:
                    exps.append(exp)
                    break
                print("Must be between 0 and 40.")
            except ValueError:
                print("Enter a valid number.")

        while True:
            try:
                sal = float(input("Enter Employee Salary: "))
                if sal >= 0:
                    sals.append(sal)
                    break
                print("Amount cannot be negative.")
            except ValueError:
                print("Enter a valid amount.")

        print(f"\n--> Employee '{names[-1]}' added successfully!")