import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
scorecard = pd.read_csv("data/processed/fund_scorecard.csv")

# Merge datasets
funds = pd.merge(
    fund_master,
    scorecard,
    on="amfi_code",
    suffixes=("_master", "_score")
)

# Ask user for risk category
risk = input("Enter Risk Category (Low / Moderate / High / Very High): ")

# Filter by risk category
recommend = funds[
    funds["risk_category"].str.lower() == risk.lower()
]

# Sort by Sharpe Ratio
recommend = recommend.sort_values(
    by="sharpe_ratio",
    ascending=False
)

# Choose the correct column names
scheme_col = "scheme_name_master" if "scheme_name_master" in recommend.columns else "scheme_name"
fund_col = "fund_house_master" if "fund_house_master" in recommend.columns else "fund_house"

print("\nTop 3 Recommended Funds\n")

print(
    recommend[
        [
            scheme_col,
            fund_col,
            "risk_category",
            "sharpe_ratio"
        ]
    ].head(3)
)