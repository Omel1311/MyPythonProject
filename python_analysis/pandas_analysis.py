import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url8 = "C:\\Users\\Пользователь\\Desktop\\Andrii\\MyPython\\ds_salaries.csv"
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(url)
# df.to_csv("auto.csv", header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers

df = df.replace('?', np.NAN)
#pd.set_option('display.max_columns', 10)


print('*'*30)
df['city-mpg'] = 235/df['city-mpg']


#  print(df[['length']].head())
df.rename(columns={'city-mpg':'city-L/100km'}, inplace=True)

df['length'] = (df['length']-df['length'].mean())/df['length'].std()
#  print(df[['length']].head())

df['price'] = df['price'].astype('float')
bins = np.linspace(min(df['price']),max(df['price']),4)
print(bins)

group = ['low','mid', 'high']

df['binning'] = pd.cut(df['price'], bins, labels=group, include_lowest=True )

print(df.head())
print(df.dtypes)




df['price']=df['price'].astype('float')

# print(df['price'].describe())
# z = (13900-13205)/7966
# print('z=', round(z,4))
# sc = 13205/45400
# print('simple_scaling=', sc)
# min_max = ((13205-5118)/(45400-5118))
# print('min_max=', min_max)



# df.plot.scatter(x='length', y='price')
#
# plt.show()

df.plot.hist()
plt.show()




print(pd.get_dummies(df['fuel-type'], dtype=int))
print(df.head())


