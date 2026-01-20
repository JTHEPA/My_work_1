import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv(
    'expenses.csv',
    on_bad_lines='warn',
)
 
def add_expense():
    date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food/Transport/Utilities/etc): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    new_expense = pd.DataFrame([[date, category, description, amount]],
                               columns=['Date', 'Category', 'Description', 'Amount'])
    new_expense.to_csv('expenses.csv', mode='a', header=False, index=False)
    print("\n Expense added successfully!\n")