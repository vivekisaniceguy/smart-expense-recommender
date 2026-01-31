import pandas as pd

def load_data(transactions_path, budgets_path):
    transactions = pd.read_csv(transactions_path)
    budgets = pd.read_csv(budgets_path)
    return transactions, budgets