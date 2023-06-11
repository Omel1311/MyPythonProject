import pandas as pd
import numpy as np

url8 = "C:\\Users\\Пользователь\\Desktop\\Andrii\\MyPython\\ds_salaries.csv"
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(url)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
df.replace('?', np.NAN)
print(df.info())

drive_wheels_counts = df['price'].value_counts().to_frame()

drive_wheels_counts.rename(columns={'count': 'value_counts'}, inplace=True)
print(drive_wheels_counts.sort_values(by='value_counts', ascending=True))