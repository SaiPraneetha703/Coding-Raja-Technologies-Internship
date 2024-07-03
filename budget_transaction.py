import json
import os
from datetime import datetime

TRANSACTIONS_FILE = 'transactions.json'

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        """Loads transactions from a JSON file if it exists."""
        if os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, 'r') as file:
                self.transactions = json.load(file)

    def save_transactions(self):
        """Saves the current list of transactions to a JSON file."""
        with open(TRANSACTIONS_FILE, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, category, date, transaction_type):
        """Adds a new transaction to the list."""
        transaction = {
            'amount': amount,
            'category': category,
            'date': date,
            'type': transaction_type  # 'income' or 'expense'
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def calculate_budget(self):
        """Calculates the remaining budget by deducting expenses from income."""
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return income - expenses

    def analyze_expenses(self):
        """Provides insights by categorizing expenses and displaying spending trends."""
        expense_analysis = {}
        for t in self.transactions:
            if t['type'] == 'expense':
                category = t['category']
                if category not in expense_analysis:
                    expense_analysis[category] = 0
                expense_analysis[category] += t['amount']
        return expense_analysis

    def list_transactions(self):
        """Lists all transactions with their details."""
        for i, t in enumerate(self.transactions):
            print(f"ID: {i} | Amount: {t['amount']} | Category: {t['category']} | Date: {t['date']} | Type: {t['type']}")

def main():
    budget_tracker = BudgetTracker()
    
    while True:
        print("\nBudget Tracker Application")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. List Transactions")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
                budget_tracker.add_transaction(amount, category, date, 'income')
                print("Income added.")
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
                budget_tracker.add_transaction(amount, category, date, 'expense')
                print("Expense added.")
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        
        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining budget: {remaining_budget}")
        
        elif choice == '4':
            expenses = budget_tracker.analyze_expenses()
            print("Expense Analysis by Category:")
            for category, amount in expenses.items():
                print(f"Category: {category}, Amount Spent: {amount}")
        
        elif choice == '5':
            budget_tracker.list_transactions()
        
        elif choice == '6':
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

