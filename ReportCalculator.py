import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generating Mock Data using random 
np.random.seed(42)

days = 31
mock_data = {
    "Day": np.arange(1, days + 1),
    "Screen Time Reduction": np.random.choice([0, 0.5, 1], days),  # 0: Increased, 0.5: Same, 1: Reduced
    "Fitness Completed": np.random.choice([0, 1], days),  # 0: Skipped, 1: Completed
    "Mood Score": np.random.choice([0, 0.5, 1], days),  # 0: Sad, 0.5: Neutral, 1: Happy
    "Mental Health Completed": np.random.choice([0, 1], days),  # 0: Skipped, 1: Completed
}


df = pd.DataFrame(mock_data)

# Calculate Daily Success Score (DSS)
df["DSS"] = df[["Screen Time Reduction", "Fitness Completed", "Mood Score", "Mental Health Completed"]].mean(axis=1)


df["7-Day Rolling DSS"] = df["DSS"].rolling(window=7, min_periods=1).mean()


df["Weekly Improvement"] = df["7-Day Rolling DSS"].diff(periods=7).fillna(0)


global_avg_dss = 0.6
df["Success Score (%)"] = (df["DSS"].mean() / global_avg_dss) * 100




overall_success = df["DSS"].mean() * 100


weekly_avg = df.groupby((df.index // 7))["DSS"].mean()
best_week = weekly_avg.idxmax() + 1  # Week number (1-based index)
worst_week = weekly_avg.idxmin() + 1  # Week number (1-based index)


mood_distribution = df["Mood Score"].value_counts(normalize=True) * 100
happiest_days = (df["Mood Score"] == 1).sum()
saddest_days = (df["Mood Score"] == 0).sum()


fitness_completion_rate = df["Fitness Completed"].mean() * 100

# Create a summary report
insights = {
    "Overall Success Score": f"{overall_success:.2f}%",
    "Best Week": f"Week {best_week}",
    "Worst Week": f"Week {worst_week}",
    "Happiest Days": happiest_days,
    "Saddest Days": saddest_days,
    "Fitness Completion Rate": f"{fitness_completion_rate:.2f}%",
}

# starting the plotting here

plt.figure(figsize=(12, 6))


plt.subplot(2, 2, 1)
plt.plot(df["Day"], df["DSS"], marker="o", linestyle="-", label="DSS")
plt.axhline(y=df["DSS"].mean(), color="r", linestyle="--", label="Avg DSS")
plt.xlabel("Day")
plt.ylabel("DSS Score")
plt.title("Daily Success Score Over Time")
plt.legend()


plt.subplot(2, 2, 2)
mood_distribution.plot(kind="bar", color=["red", "orange", "green"])
plt.xlabel("Mood (0=Sad, 0.5=Neutral, 1=Happy)")
plt.ylabel("Percentage")
plt.title("Mood Distribution")

# 3️⃣ Weekly DSS Comparison
plt.subplot(2, 2, 3)
plt.bar(weekly_avg.index + 1, weekly_avg, color="blue", alpha=0.7)
plt.xlabel("Week")
plt.ylabel("Average DSS")
plt.title("Weekly Success Score")


plt.subplot(2, 2, 4)
plt.pie(
    [fitness_completion_rate, 100 - fitness_completion_rate],
    labels=["Completed", "Missed"],
    autopct="%1.1f%%",
    colors=["green", "gray"],
    startangle=90,
)
plt.title("Fitness Completion Rate")

plt.tight_layout()
plt.show()



insights_df = pd.DataFrame(list(insights.items()), columns=["Metric", "Value"])

import ace_tools as tools
tools.display_dataframe_to_user(name="Monthly Insights", dataframe=insights_df)
