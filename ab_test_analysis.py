import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Set seed for reproducibility
np.random.seed(10)

# Sample size for each group
n_control = 5000
n_treatment = 5000

# Simulate conversion data (1 = purchased, 0 = did not purchase)
# Baseline conversion rate ~11.5%, Treatment group ~13.8%
control_data = np.random.binomial(1, 0.115, n_control)
treatment_data = np.random.binomial(1, 0.138, n_treatment)

# Create a DataFrame
df = pd.DataFrame({
    'group': ['control'] * n_control + ['treatment'] * n_treatment,
    'converted': np.concatenate([control_data, treatment_data])
})

# Calculate conversion rates
summary = df.groupby('group')['converted'].agg(['count', 'sum', 'mean'])
summary.columns = ['Total Users', 'Conversions', 'Conversion Rate']
print(summary)
print("-" * 40)

# Two-proportion Z-test
conversions = [summary.loc['treatment', 'Conversions'], summary.loc['control', 'Conversions']]
samples = [summary.loc['treatment', 'Total Users'], summary.loc['control', 'Total Users']]

z_stat, p_val = proportions_ztest(conversions, samples, alternative='larger')

print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_val:.5f}")

# Check significance at alpha = 0.05
if p_val < 0.05:
    print("Result: Statistically significant. Reject the null hypothesis.")
else:
    print("Result: Not statistically significant. Fail to reject the null hypothesis.")
