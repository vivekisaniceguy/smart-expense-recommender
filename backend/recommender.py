import pandas as pd

def generate_recommendations(
    user_id,
    user_matrix_m1,
    user_matrix_m2,
    similarity_df,
    budgets,
    top_k=5
):
    similar_users = (
        similarity_df[user_id]
        .drop(user_id)
        .sort_values(ascending=False)
        .head(top_k)
        .index
    )

    improvement = user_matrix_m1 - user_matrix_m2

    avg_improve = improvement.loc[similar_users].mean()
    success_rate = (improvement.loc[similar_users] > 0).mean()

    user_overspend = user_matrix_m1.loc[user_id]
    scores = {}

    for category in user_overspend.index:
        if user_overspend[category] > 1 and avg_improve[category] > 0:
            scores[category] = (
                user_overspend[category]
                * avg_improve[category]
                * success_rate[category]
            )

    ranked = pd.Series(scores).sort_values(ascending=False)

    recommendations = []

    for category in ranked.index:
        budget = budgets[
            (budgets.user_id == user_id) &
            (budgets.category == category)
        ]["budget"].values[0]

        reduce_amount = int((user_overspend[category] - 1) * budget)

        recommendations.append({
            "category": category,
            "reduce_amount": reduce_amount,
            "overspend_ratio": round(user_overspend[category], 2),
            "success_rate": int(success_rate[category] * 100)
        })

    return recommendations
