# expense_tracker.py

from expense import Expense  # Importing the Expense class

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date, description=""):
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        print(f"Added: {expense}")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. {expense}")

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid index.")