# Smart Expense Recommender

Smart Expense Recommender is a fintech-style application that analyzes user transaction data and provides personalized, explainable spending behavior recommendations using recommender system concepts.

Instead of recommending products, the system recommends **actionable financial behavior changes** based on how similar users improved their spending habits.

---

## Features

- Aggregates raw transaction logs into monthly spending profiles  
- Models user behavior using overspend ratios  
- Applies user-based collaborative filtering with cosine similarity  
- Learns from peer behavior improvements over time  
- Generates ranked, explainable spending recommendations  
- Interactive dashboard built with Streamlit  

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  

---

## Project Structure

smart-expense-recommender/
│
├── data/
│ ├── transactions.csv
│ └── budgets.csv
│
├── backend/
│ ├── data_loader.py
│ ├── feature_engineering.py
│ ├── similarity.py
│ └── recommender.py
│
├── app.py
├── requirements.txt
└── README.md

---

## How It Works

1. User spending is tracked for one full month  
2. Monthly category-wise spending is aggregated  
3. Overspend ratios are computed to normalize behavior  
4. Similar users are identified using cosine similarity  
5. Spending behaviors that improved for similar users are analyzed  
6. Personalized, ranked recommendations are generated with explanations  

---

## Running the Application

### 1. Install dependencies
```bash
pip install -r requirements.txt
streamlit run app.py
Reduce Shopping Spending
Suggested reduction: ₹1800
Overspend ratio: 1.6×
Similar users success rate: 72%
---

## Evaluation Approach

Traditional accuracy metrics are not suitable for this problem.
The system is evaluated using:

Reduction in overspend ratio

Month-over-month spending improvement

Recommendation adoption rate

Overall budget adherence



