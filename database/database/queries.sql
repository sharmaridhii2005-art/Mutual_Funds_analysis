-- 1. Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_cr DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT
strftime('%m', date) AS month,
AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month;

-- 3. Total SIP amount
SELECT
SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP';

-- 4. Total Redemption amount
SELECT
SUM(amount_inr) AS total_redemption
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 5. Transactions by KYC Status
SELECT
kyc_status,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY kyc_status;

-- 6. Average Expense Ratio
SELECT
AVG(expense_ratio_pct)
FROM fact_performance;

-- 7. Funds with Expense Ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 8. Highest 5-Year Return
SELECT *
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 9. Average 1-Year Return
SELECT
AVG(return_1yr_pct)
FROM fact_performance;

-- 10. Total Transactions
SELECT
COUNT(*)
FROM fact_transactions;