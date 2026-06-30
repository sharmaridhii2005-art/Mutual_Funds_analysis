import pandas as pd

# Read the NAV History dataset
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort by AMFI code and date
nav = nav.sort_values(by=["amfi_code", "date"])

# Forward-fill missing NAV values within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
nav = nav.drop_duplicates()

# Keep only valid NAV values (greater than 0)
nav = nav[nav["nav"] > 0]

# Save the cleaned dataset
nav.to_csv("data/processed/02_nav_history.csv", index=False)

# Display results
print("✅ NAV History cleaned successfully!")
print("Total rows:", len(nav))
print("\nData Types:")
print(nav.dtypes)
print("\nFirst 5 rows:")
print(nav.head())
