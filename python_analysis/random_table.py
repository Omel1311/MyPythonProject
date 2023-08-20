import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(np.random.randint(0,100,size=(40, 4)), columns=list('ABCD'))


print(df.head())
df.to_excel('random.xlsx')
print(df.describe(include='all'))
print(df.tail(10))
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

df.plot.hist()
plt.show()


