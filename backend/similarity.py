import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_user_matrix(data, month):
    month_data = data[data["month"] == month]

    user_matrix = (
        month_data
        .pivot(index="user_id", columns="category", values="overspend")
        .fillna(1.0)
    )
    return user_matrix

def compute_similarity(user_matrix):
    sim = cosine_similarity(user_matrix)
    return pd.DataFrame(
        sim,
        index=user_matrix.index,
        columns=user_matrix.index
    )
