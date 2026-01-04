import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def create_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass


def add_expense():
    category = input("Enter category (Food/Travel/Bills/Study): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!\n")


def view_expenses():
    print("\n--- All Expenses ---")
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.\n")


def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                total += float(row[2])
        print(f"\n💰 Total Expense: ₹{total}\n")
    except FileNotFoundError:
        print("No data available.\n")


def menu():
    create_file()
    while True:
        print("==== Smart Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


menu()
