# main.py - Entry point for the Expense Tracker

from expense_tracker import ExpenseTracker  # Import our tracker module

def main():
    tracker = ExpenseTracker()  # Create an instance of ExpenseTracker

    while True:
        # Display menu
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Remove Expense")
        print("4. Exit")
        
        # Get user's choice
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            # Add a new expense
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (optional, leave blank for today): ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, date if date else None, description)

        elif choice == "2":
            # List all expenses
            tracker.list_expenses()

        elif choice == "3":
            # Remove an expense
            tracker.list_expenses()
            index = int(input("Enter the number of the expense to remove: ")) - 1
            tracker.remove_expense(index)

        elif choice == "4":
            # Exit the program
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()