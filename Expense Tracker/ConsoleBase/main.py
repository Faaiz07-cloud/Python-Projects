import os
import json

data_file = "expenses.json"

# load expenses
def load_expenses():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    else:
        return []

# save expenses
def save_expenses(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

# add expenses
def add_expense(expenses):
    print("\n>>>>> Add new expense <<<<<")
    date = input("Enter the date: YYYY-MM-DD ")
    categories = [
        'Food & Dining',
        'Transport',
        'Housing',
        'Entertainment',
        'Health',
        'Shopping',
        'Education',
        'Travel',
        'Savings & Investments',
        'Donations & Gifts',
        'Other'
    ]
    print("\nCategories:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")
    user_category = (input("Enter your choice: "))
    description = input("Enter your description: ")
    amount = int(input("Enter your amount: "))
    payment_method = input("Enter your payment method: Cash/Card/Wallet ")
    user_id = len(expenses) + 1
    expense_dict = {
        "ID": user_id,
        "Date": date,
        "Category": user_category,
        "Description": description,
        "Amount": amount,
        "Payment_method": payment_method,
    }
    expenses.append(expense_dict)
    print("\n>>>>>> New Expense added! <<<<<<")

# view expenses
def view_expenses(expenses):
    if not expenses:
        print("\n>>>>>> No expenses! <<<<<<")
    else:
        print("\nExpenses List:")
        for exp in expenses:
            print(f"ID: {exp['ID']}")
            print(f"Date: {exp['Date']}")
            print(f"Category: {exp['Category']}")
            print(f"Description: {exp['Description']}")
            print(f"Amount: {exp['Amount']}")
            print(f"Payment Method: {exp['Payment_method']}")
            print("---------------------------------------")

# total expenses
def total_expenses(expenses):
    if not expenses:
        print("\n>>>>>> No expenses! <<<<<<")
    else:
        total = sum(exp["Amount"] for exp in expenses)
        print(f"\nTotal Expenses: {total}")
# menu
def main():
     expenses =  load_expenses()
     while True:
         print("\n>>>>>> Expense Tracker <<<<<<")
         print("1. Add Expense")
         print("2. View Expenses")
         print("3. Total Expenses")
         print("4. Exit")
         try:
               choice = int(input("\nEnter your choice: "))
               if choice == 1:
                      add_expense(expenses)
               elif choice == 2:
                      view_expenses(expenses)
               elif choice == 3:
                      total_expenses(expenses)
               elif choice == 4:
                      save_expenses(expenses)
                      print("\nExpenses saved! Bye.\n")
                      break
               else:
                      print("\nInvalid choice!")
         except ValueError:
                      print("\nInvalid Input!")

try:
    if __name__ == '__main__':
          main()
except KeyboardInterrupt:
    print("\nBye.\n")


