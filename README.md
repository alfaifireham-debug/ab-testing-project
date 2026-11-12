# A/B Testing Project: New Customer Discount Impact

**سؤال المشروع:** هل يؤدي تقديم خصم 10% للعملاء الجدد إلى زيادة معدل إتمام عمليات الشراء في المتجر؟

## Overview
This project analyzes the impact of offering a 10% welcome discount to first-time visitors on an e-commerce platform. The goal is to determine whether the discount significantly improves the checkout conversion rate compared to the standard pricing experience.

## Experiment Setup
The experiment splits 10,000 new visitors equally into two random groups:
* **Control Group (A):** 5,000 users shown standard product prices (no discount).
* **Treatment Group (B):** 5,000 users offered a 10% discount on their first order.

### Hypotheses
* **Null Hypothesis ($H_0$):** $CR_{treatment} \le CR_{control}$ (The 10% discount does not increase the conversion rate).
* **Alternative Hypothesis ($H_1$):** $CR_{treatment} > CR_{control}$ (The 10% discount increases the conversion rate).
* **Significance Level ($\alpha$):** `0.05`

## Results
Using a one-sided Two-Proportion Z-Test in Python, the simulated experiment produced the following results:

| Group | Total Users | Conversions | Conversion Rate |
| :--- | :---: | :---: | :---: |
| Control (A) | 5,000 | 578 | 11.56% |
| Treatment (B) | 5,000 | 694 | 13.88% |

* **Absolute Lift:** +2.32%
* **Z-statistic:** 3.485
* **P-value:** 0.00025

## Conclusion & Recommendation
Since the p-value (`0.00025`) is well below the `0.05` threshold, we reject the null hypothesis. Offering a 10% discount leads to a statistically significant increase in new customer conversions. 

**Business Recommendation:** Roll out the 10% first-order discount to all new visitors, while monitoring profit margins and considering a minimum order threshold if needed.

## Files
* `ab_test_analysis.py`: Python script for data simulation, conversion calculation, and Z-test execution.
