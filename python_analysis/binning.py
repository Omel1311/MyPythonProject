import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.DataFrame({'number': np.random.randint(1, 100, 10)})
lables = ['low', 'mid', 'high']
min = df['number'].min()
max = df['number'].max()

lf = np.linspace(min, max, num=4).astype(int)
df['bins'] = pd.cut(x=df['number'], labels=lables, bins=[lf[0],lf[1],lf[2],lf[3]])


print(df)

# We can check the frequency of each bin
print(df['bins'].value_counts())


lf = np.linspace(min, max, num=4).astype(int)
print('line:', lf)

df['number'].plot.hist()
plt.show()