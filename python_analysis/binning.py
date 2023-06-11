import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.DataFrame({'number': np.random.randint(1, 90, 10)})
lables = ['low', 'mid', 'high']
mean = df['number'].mean()


df['bins'] = pd.cut(x=df['number'], labels=lables, bins=[1,10,40,90])


print(df)

# We can check the frequency of each bin
print(df['bins'].value_counts())


lf = np.linspace(2, 40, num=10).astype(int)
print('line:', lf)

df['number'].plot.hist()
plt.show()