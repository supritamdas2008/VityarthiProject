# VityarthiProject
# Employee Database Management System

An all-in-one employee database system built to streamline workforce management. Easily onboard new hires, update existing records, perform multi-criteria searches, and instantly generate detailed analytical reports on company payroll, department headcounts, and employee demographics.

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Terminal & Command Prompt Utilities](#terminal--command-prompt-utilities)

## Features

* **Employee Onboarding:** Add new employees with detailed attributes (Name, Department, Age, Position, Experience, and Salary) with built-in input validation.
* **Centralized Dashboard:** View all current employee records in a clean, tabular format.
* **Advanced Search:** Find specific employees instantly by Name, Department, Age, Experience, or custom Salary ranges.
* **Record Management:** Easily update outdated employee details or delete records from the system using assigned serial numbers.
* **Automated Analytics:** Instantly generate business reports detailing:
  * Total headcount and monthly payroll.
  * Department-wise employee distribution.
  * Extremes in age, experience, and salary metrics.
* **Persistent Storage:** All data is safely and automatically stored in a local `.csv` file format.

## Project Structure

This project uses a modular architecture to separate the user interface, database operations, and core logic for easier maintenance.

```text
├── main.py          # Primary application execution loop and menu routing
├── UI.py            # Centralized UI components, tables, and report layouts
├── database.py      # Persistence module for batch saving to CSV
├── func1.py         # Module: Add new employee records
├── func2.py         # Module: Display all employee records
├── func3.py         # Module: Search database records
├── func4.py         # Module: Edit or delete existing records
├── func5.py         # Module: Generate analytical summary reports
└── data/
    └── employees.csv # Persistent database file (auto-generated)
```

## Prerequisites

To run this project, you will need Python installed on your system along with the Pandas library for data processing.

* Python 3.x
* Pandas

### Install the required Python dependencies:
   ```bash
   pip install pandas
   ```

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/employee-database-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd employee-database-system
   ```

## Usage

Start the application by running the `main.py` file from your terminal or command prompt:

```bash
python main.py
```

Upon launching, you will be greeted by the main menu. Simply enter a number (`1-6`) to navigate through the system:

1. **Add a New Employee:** Prompts you for employee details and saves them.
2. **View All the Employee Details:** Prints a formatted table of all saved records.
3. **Search for an Employee:** Opens the search sub-menu to filter the database.
4. **Update an Employee Details:** Allows editing or deletion of a record based on its Serial Number.
5. **Show Reports and Statistics:** Calculates and displays company-wide metrics.
6. **Exit the Program:** Safely closes the application.

---

## Terminal & Command Prompt Utilities

Here is how you can manage the application terminal window, clear cluttered screens, reset database data, or force exit using Command Prompt or Terminal.

### 1. Clearing the Command Prompt Screen
If your terminal gets messy after running multiple operations:

* **Windows Command Prompt (CMD):**
  ```cmd
  cls
  ```
* **PowerShell / macOS / Linux Terminal:**
  ```bash
  clear
  ```

### 2. Clearing / Resetting All Database Data
If you want to completely erase all saved employee records and reset the system back to a clean state:

* **Windows Command Prompt (CMD):**
  ```cmd
  del data\employees.csv
  ```
* **PowerShell / macOS / Linux Terminal:**
  ```bash
  rm data/employees.csv
  ```
*(Note: The `data/employees.csv` file will automatically be recreated the next time you add a new employee).*

### 3. How to Force Quit / Stop the Application
If the program ever gets stuck or you want to abruptly close it without using menu option 6:

* Press `Ctrl + C` on your keyboard while inside the terminal window.
