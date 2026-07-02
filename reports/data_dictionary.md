# Data Dictionary

## 02_nav_history.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique mutual fund code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## 08_investor_transactions.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| transaction_id | Integer | Unique transaction ID |
| amfi_code | Integer | Mutual fund code |
| transaction_date | Date | Transaction date |
| transaction_type | Text | SIP, Lumpsum or Redemption |
| amount_inr | Float | Transaction amount |
| kyc_status | Text | KYC verification status |

## 07_scheme_performance.csv

| Column | Data Type | Description |



|--------|-----------|-------------|
| amfi_code | Integer | Mutual fund code |
| return_1yr_pct | Float | 1-year return (%) |
| return_3yr_pct | Float | 3-year return (%) |
| return_5yr_pct | Float | 5-year return (%) |
| expense_ratio_pct | Float | Expense ratio (%) |