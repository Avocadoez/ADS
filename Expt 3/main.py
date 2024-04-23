import numpy as np
import pandas as pd
import math

data = pd.read_csv('../Country Wise Gender.csv')
custom = data[['2014 Male', '2015 Male']]


x = custom['2014 Male']
y = custom['2015 Male']

x_mean = x.mean()
y_mean = y.mean()

custom['dx'] = x - x_mean
custom['dy'] = y - y_mean

custom['dx_squared'] = custom['dx']**2
custom['dy_squared'] = custom['dy']**2

custom['dxdy'] = (x - x_mean) * (y - y_mean)

print(custom)

numerator = custom['dxdy'].sum()
denominator = math.sqrt(custom['dx_squared'].sum() * custom['dy_squared'].sum())
r = numerator/denominator

print("Correlation: ", end='')
print(r)
if 0.3 < r < 0.75:
    print('It is Moderately positively Correlated!')
elif 0.75 <= r < 1:
    print('It is Highly positively Correlated!')
elif r >= 1:
    print('It is perfect positively Correlated!')
elif -0.3 < r < -0.75:
    print('It is Moderately negatively Correlated!')
elif -0.75 <= r < -0.1:
    print('It is Highly negatively Correlated!')
elif r <= -1:
    print('It is perfect negatively Correlated!')
else:
    print('It is not that correlated')
