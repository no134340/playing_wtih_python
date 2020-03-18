"""
Funkcionalnost:
    Crta grafik broj potvrđenih slučajeva i faktor rasta
    (odnos promene broja slučajeva između dva dana),
    po datumu, počevši od 1. prijavljenog slučaja.
    Čuva tabelu sa podacima u .csv (comma separated values) formatu.

    dN(t) = N(t) - N(t-1) - promena broja slučajeva dana t

    faktor_rasta = dN(t) / dN(t - 1)

Izlaz:
    1) serbia_stats.png - slika sa graficima

    2) serbia_confirmed_COVID19_cases.csv - datoteka sa podacima u
    .csv formatu, kolone su datumi, redovi su broj potvrđenih slučajeva
    i faktor rasta

Potrebne biblioteke:
    pandas
    numpy
    matplotlib
    wget

Python verzija: 3.8

Napomena:
    URL sa kojeg se preuzimaju podaci se ažurira na 24h u 23:59 (UTC).
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import wget
import os


matplotlib.rcParams.update({'font.size': 6})
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
data_csv = wget.download(url)
data = pd.read_csv(data_csv)
os.remove(data_csv)
nums = data[data['Country/Region'] == 'Serbia'].index.values
serbia_cases = data.iloc[nums[0], :]
serbia_cases = np.array(serbia_cases[4:], dtype='uint16')
print(serbia_cases)
dates = data.columns[4:]
dates = np.array(dates)[serbia_cases > 0]
serbia_cases = serbia_cases[serbia_cases > 0]

# print(serbia_cases)
diff_by_day = np.append(np.array([0]), np.diff(serbia_cases))
diff_by_day = list(diff_by_day)

fig, axs = plt.subplots(2, figsize=(8, 8), dpi=300)
days = list(range(1, serbia_cases.size + 1))
axs[0].bar(dates, serbia_cases)
axs[0].legend(['slučajeva(potvrđeno) / dan'])
axs[0].set_yticks(np.arange(min(serbia_cases), max(serbia_cases) + 1, 2))
growth = [0]
for i in range(1, len(diff_by_day)):
    if diff_by_day[i - 1] != 0:
        growth.append(diff_by_day[i] / diff_by_day[i - 1])
    else:
        growth.append(0)
axs[1].plot(dates, growth, 'r')
axs[1].legend(['faktor rasta / dan'])
axs[1].set_yticks(np.arange(min(growth), max(growth) + 1, 0.25))
plt.savefig('serbia_stats.png')

tmp = [serbia_cases, growth]
data_serbia = pd.DataFrame(tmp, columns=dates)

serbia_csv = data_serbia.to_csv('serbia_confirmed_COVID19_cases.csv', index=False)
