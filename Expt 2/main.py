import pandas as pd
from statistics import variance
from statistics import stdev

data = pd.read_csv('../Country Wise Gender.csv')[0: 10]
# df = pd.DataFrame(data)

# mean meadian mode
print('\nComputation of Central Tendency')
print("\nMean of the Country Wise Gender Dataset")
print(data.mean())
print("\n********************************************************************")
print("\nMedian of the Country Wise Gender Dataset")
print(data.median())
print("\n********************************************************************")
print("\nMode of the Country Wise Gender Dataset")
print(data.mode())

print("\n********************************************************************")

print('\nComputation of Dispersion')
# range
print("\nRange: ")
range1 = data['2020 Male'].max() - data['2019 Male'].min()
range2 = data['2020 Female'].max() - data['2020 Male'].min()
print("Range of 2019: " + str(range1))
print("Range of 2020: " + str(range2))

print("\n********************************************************************")

# variance
print("\nVariance: ")
variance1 = variance(data['2019 Male'])
variance2 = variance(data['2020 Male'])
print("Variance of 2019: " + str(variance1))
print("Variance of 2020: " + str(variance2))

print("\n********************************************************************")

# standard deviation
print("\nStandard Deviation: ")
std1 = stdev(data['2019 Male'])
std2 = stdev(data['2020 Male'])
print("Standard Deviation of 2019: " + str(std1))
print("Standard Deviation of 2020: " + str(std2))

print("\n********************************************************************")

print('\nSkewness of Dataset')
#skewness
skew1 = data['2020 Male'].skew()
skew2 = data['2020 Female'].skew()
print("Skewness of 2019: " + str(skew1))
print("Skewness of 2020: " + str(skew2))

