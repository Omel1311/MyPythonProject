import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

file = 'C:\\Users\\Пользователь\\Downloads\\Car_Sales_Kaggle_DV0130EN_Lab2_Start.xlsx'

df = pd.read_excel(file, sheet_name='Histogram Chart')


print(df.head())

print(df.describe(include='all'))

print(df.sample(n=9))

print(df.isnull().sum())
# sns.regplot(x='A',y='B', data=df)
# plt.show()
# lables = 'low', 'mid', 'high'
# sum_col = df ['col1'] + df['col2']
# df['col3'] = sum_col - sum_col.mean()/sum_col.std()
#
#
# df['bins'] = df['col1']

# sns.residplot(x='A',y='B', data=df)
# plt.show()

# df.plot.hist()
# plt.show()

print(df.nunique())
print(df.index)
print(df.columns)
nl = df.nlargest(5, 'Price')
l = df.iloc[:10, 2:5].copy()

l.