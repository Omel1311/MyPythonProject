import pandas as pd
import numpy as np
import matplotlib

url8 = "C:\\Users\\Пользователь\\Desktop\\Andrii\\MyPython\\ds_salaries.csv"
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(url)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
df = df.replace('?', np.NAN)

print(df['price'].value_counts())

df['price'] = df['price'].astype(float)
print(df.info())
min = df['price'].min()
max = df['price'].max()
print(min, max)

l = np.linspace(min,max,3).astype(float)
l = list(l)
print(l)
labels = ['low', 'mid', 'high']

pd.cut(x=df['price'], labels=labels, bins=[3, 5555, 55555])
print(df['bins'])

