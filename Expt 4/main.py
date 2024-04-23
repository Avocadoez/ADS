import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer

data = pd.read_csv('../Country Quater Wise Visitors.csv')
print(data)
data = data.drop("Country of Nationality", axis="columns")
print(data)

imputer1 = SimpleImputer(missing_values=np.nan, strategy="mean")
output = imputer1.fit(data)
print(output)