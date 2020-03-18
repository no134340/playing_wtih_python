import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('time_series_19-covid-Confirmed.csv')
data.drop(range(1, 31))
nums = data.iloc[:, 26:]
print(nums)
sum_by_day = nums.sum(axis=0)
diff_by_day = sum_by_day.diff()
sum_by_day = list(sum_by_day)
diff_by_day = list(diff_by_day)
print(diff_by_day)
plt.plot(sum_by_day)
plt.show()
growth = []
for i in range(1, len(diff_by_day)):
    growth.append(diff_by_day[i]/diff_by_day[i-1])
print(growth)
