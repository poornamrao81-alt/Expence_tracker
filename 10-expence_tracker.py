expenses = []

print("===== PERSONAL EXPENSE TRACKER =====")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n----- YOUR EXPENSES -----")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['category']} - ₹{expense['amount']}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\nTotal Expense: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")