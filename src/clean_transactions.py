import pandas as pd

# Read the dataset
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Flag rows where any return value is missing after conversion
anomalies = performance[
    performance[return_columns].isnull().any(axis=1)
]

print("Anomalies found:", len(anomalies))

# Keep only expense ratios between 0.1% and 2.5%
performance = performance[
    (performance["expense_ratio_pct"] >= 0.1) &
    (performance["expense_ratio_pct"] <= 2.5)
]

# Save cleaned dataset
performance.to_csv(
    "data/processed/07_scheme_performance.csv",
    index=False
)

print("✅ Scheme Performance cleaned successfully!")
print("Total rows:", len(performance))
