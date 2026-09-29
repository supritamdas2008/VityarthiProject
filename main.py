from UI import start_ui
from database import save_lists_to_csv
from func1 import func_1
from func2 import func_2
from func3 import func_3
from func4 import func_4
from func5 import func_5

names, depts, ages, roles, exps, sals = [], [], [], [], [], []

def main():
    while True:
        start_ui()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            func_1(names, depts, ages, roles, exps, sals)
            save_lists_to_csv(names, depts, ages, roles, exps, sals)
            input("\nPress Enter to return...")
        elif choice == '2':
            func_2()
            input("\nPress Enter to return...")
        elif choice == '3':
            func_3()
            input("\nPress Enter to return...")
        elif choice == '4':
            func_4()
            input("\nPress Enter to return...")
        elif choice == '5':
            func_5()
            input("\nPress Enter to return...")
        elif choice == '6':
            print("\nExiting program.")
            break
        else:
            print("\nInvalid option.")
            input("Press Enter to try again...")

main()