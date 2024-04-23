import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
df = pd.read_csv("../TCS__EQNSENSE__MINUTE.csv")

# Assuming the dataset already contains the necessary columns: timestamp, open, high, low, close, volume

# Define population size and sample size
population_size = 30
sample_size = 20
alpha = 0.05  # Default value for alpha

# Calculate population mean and deviation from the first population_size entries
population_mean = df['open'].head(population_size).mean()
population_deviation = df['open'].head(population_size).std()

# Calculate sample mean from the first sample_size rows
sample_mean = df['open'].head(sample_size).mean()

# Define hypotheses for two-tailed test
H0_two_tailed = "Null Hypothesis: The sample mean is equal to the population mean (μ)"
H1_two_tailed = "Alternative Hypothesis: The sample mean is not equal to the population mean (μ)"

# Calculate t-score for two-tailed test
t_score_two_tailed = (sample_mean - population_mean) / (population_deviation / np.sqrt(sample_size))

# Look up critical t-value for two-tailed test
critical_t_value_two_tailed = stats.t.ppf(1 - alpha/2, df=sample_size-1)  # For two-tailed test

# Compare t-score with critical t-value for two-tailed test
if abs(t_score_two_tailed) < critical_t_value_two_tailed:
    decision_two_tailed = "Reject H0"
else:
    decision_two_tailed = "Accept H0"

# Calculate p-value for two-tailed test
p_value_two_tailed = 2 * (1 - stats.t.cdf(abs(t_score_two_tailed), df=sample_size-1))  # Two-tailed test

# Define hypotheses for one-tailed test
H0_one_tailed = "Null Hypothesis: The sample mean is less than or equal to the population mean (μ)"
H1_one_tailed = "Alternative Hypothesis: The sample mean is greater than the population mean (μ)"

# Calculate t-score for one-tailed test
t_score_one_tailed = (sample_mean - population_mean) / (population_deviation / np.sqrt(sample_size))

# Look up critical t-value for one-tailed test
critical_t_value_one_tailed = stats.t.ppf(1 - alpha, df=sample_size-1)  # For one-tailed test

# Compare t-score with critical t-value for one-tailed test
if t_score_one_tailed > critical_t_value_one_tailed:
    decision_one_tailed = "Reject H0"
else:
    decision_one_tailed = "Accept H0"

# Calculate p-value for one-tailed test
p_value_one_tailed = 1 - stats.t.cdf(t_score_one_tailed, df=sample_size-1)  # One-tailed test

# Print results for two-tailed test
print("Two-Tailed Test:")
print("Population Mean (μ):", population_mean)
print("Population Size (N):", population_size)
print("Sample Size (n):", sample_size)
print("Population Deviation (σ):", population_deviation)
print("Alpha (level of significance):", alpha)
print("Sample Mean:", sample_mean)
print("\nHypotheses:")
print(H0_two_tailed)
print(H1_two_tailed)
print("\nT-score:", t_score_two_tailed)
print("Critical T-value (two-tailed):", critical_t_value_two_tailed)
print("Decision based on T-test:", decision_two_tailed)
print("P-value:", p_value_two_tailed)

# Print results for one-tailed test
print("\nOne-Tailed Test:")
print("Population Mean (μ):", population_mean)
print("Population Size (N):", population_size)
print("Sample Size (n):", sample_size)
print("Population Deviation (σ):", population_deviation)
print("Alpha (level of significance):", alpha)
print("Sample Mean:", sample_mean)
print("\nHypotheses:")
print(H0_one_tailed)
print(H1_one_tailed)
print("\nT-score:", t_score_one_tailed)
print("Critical T-value (one-tailed):", critical_t_value_one_tailed)
print("Decision based on T-test:", decision_one_tailed)
print("P-value:", p_value_one_tailed)