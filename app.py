import streamlit as st
import pandas as pd

from backend.data_loader import load_data
from backend.feature_engineering import compute_monthly_overspend
from backend.similarity import build_user_matrix, compute_similarity
from backend.recommender import generate_recommendations

st.set_page_config(
    page_title="SpendSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

transactions, budgets = load_data(
    "data/transactions.csv",
    "data/budgets.csv"
)

data = compute_monthly_overspend(transactions, budgets)

st.sidebar.title("SpendSense")
st.sidebar.caption("Smart Expense Behavioral Recommender")

user_ids = sorted(data.user_id.unique())
user_id = st.sidebar.selectbox("Select User", user_ids)

month = st.sidebar.selectbox(
    "Select Month",
    [1, 2],
    index=0
)

st.title("Financial Health Dashboard")
st.caption("Personalized insights based on spending behavior")

user_month_data = data[
    (data.user_id == user_id) &
    (data.month == month)
]

total_spend = int(user_month_data.amount.sum())
overspend_count = int((user_month_data.overspend > 1).sum())
avg_overspend = round(user_month_data.overspend.mean(), 2)

c1, c2, c3 = st.columns(3)
c1.metric("Total Spend", f"₹{total_spend}")
c2.metric("Overspent Categories", overspend_count)
c3.metric("Average Overspend Ratio", avg_overspend)

st.divider()

st.subheader("Category-wise Spending")

chart_data = (
    user_month_data[["category", "amount"]]
    .groupby("category")
    .sum()
)

st.bar_chart(chart_data)

st.divider()

st.subheader("Personalized Recommendations")

if month == 1:
    st.info("Recommendations will be available after observing one full month.")
else:
    user_matrix_m1 = build_user_matrix(data, month=1)
    user_matrix_m2 = build_user_matrix(data, month=2)

    similarity_df = compute_similarity(user_matrix_m1)

    recs = generate_recommendations(
        user_id,
        user_matrix_m1,
        user_matrix_m2,
        similarity_df,
        budgets
    )

    if not recs:
        st.success("No significant overspending detected.")
    else:
        for r in recs:
            st.markdown(
                f"""
                **Reduce {r['category'].title()} Spending**
                - Suggested reduction: ₹{r['reduce_amount']}
                - Overspend ratio: {r['overspend_ratio']}×
                - Similar users success rate: {r['success_rate']}%
                """
            )
            st.divider()
