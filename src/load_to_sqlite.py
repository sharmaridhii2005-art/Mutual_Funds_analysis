import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///database/bluestock_mf.db")

# Read cleaned CSV files
nav = pd.read_csv("data/processed/02_nav_history.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions.csv")
performance = pd.read_csv("data/processed/07_scheme_performance.csv")

# Load into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

# Verify row counts
print("NAV rows:", len(nav))
print("Transaction rows:", len(transactions))
print("Performance rows:", len(performance))

print("\n✅ Database created successfully!")