import pandas as pd

def compute_monthly_overspend(transactions, budgets):
    monthly = (
        transactions
        .groupby(["user_id", "month", "category"])["amount"]
        .sum()
        .reset_index()
    )

    data = monthly.merge(
        budgets,
        on=["user_id", "category"],
        how="left"
    )

    data["overspend"] = data["amount"] / data["budget"]
    data.head()
    return data
