# expense.py - This file will define the Expense class.

from datetime import datetime  # We’ll use this to handle dates

class Expense:
    def __init__(self, amount, category, date=None, description=""):
        # Initialize the class attributes for each expense
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()  # If no date is given, use the current date
        self.description = description

    def get_summary(self):
        # Returns a string summarizing the expense
        return f"{self.date.strftime('%Y-%m-%d')}: {self.category} - ${self.amount} ({self.description})"
    
    def update_amount(self, new_amount):
        # Updates the amount for the expense
        if new_amount >= 0:
            self.amount = new_amount
        else:
            print("Amount cannot be negative")

    def update_category(self, new_category):
        # Updates the category for the expense
        self.category = new_category