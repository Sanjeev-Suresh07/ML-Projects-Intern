# Business Brief: 2025 Sales Trend and Customer Analysis

**Data note:** This analysis uses **generated (simulated) data**, not real customer data. It is a made-up order table of 2,000 orders from 300 customers across 2025, with amounts assumed to be in rupees (INR). Findings describe this simulated data only.

## Context
A manager wants to know which months and product categories earn the most, who the best customers are, and what to do next. The analysis covers 2,000 orders worth about 2.40 million INR in total, with an average order value of about 1,202 INR. The full working is in the notebook `03_sales_analysis.ipynb`.

## Key findings
1. **Monthly revenue stayed in a narrow band.** It ranged from 179,784 INR (August, the worst month) to 232,027 INR (February, the best). February was 20.0% above January, and August was 18.9% below July.
2. **Fashion earns the most.** Fashion brings 35.5% of revenue, followed by Electronics (30.1%), Home (19.3%) and Books (15.1%). Fashion leads in 9 of 12 months.
3. **Category ranking comes from order count, not order size.** Average order value is similar in every category (about 1,164 to 1,220 INR).
4. **Revenue is spread widely across customers.** The top 10% of customers (30 of 300) bring only 18.9% of revenue, and the top 20% bring 33.9%. The 80/20 idea does not hold here. The biggest single customer accounts for 0.75% of revenue.

## Recommendations
1. **Run a broad loyalty offer, not a VIP-only one.** The top 10% bring only 18.9% of revenue, so a top-customer programme reaches a small slice. With 6.7 orders per customer on average, a repeat-purchase offer open to all 300 customers is a better target.
2. **Focus stock and marketing on Fashion and Electronics.** Together they bring 65.6% of revenue. Growing Books (298 orders) and Home (381 orders) means getting more orders, for example through bundles with the top two categories.
3. **Plan a promotion for the slow late-summer period.** August was the weakest month, and Home was especially low that month (19,291 INR). A targeted August offer could lift the dip.

## Next steps
- Repeat this analysis on **real, multi-year sales data**. The ups and downs here reflect chance in the simulated data, so seasonality should be confirmed before acting on recommendation 3.
- Test the loyalty offer on a small group of customers first and compare repeat-purchase rates with a group that did not receive it.
- Track orders per customer over time to see whether any customers are drifting away, which would support a true churn analysis.
