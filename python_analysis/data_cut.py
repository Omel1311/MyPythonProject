import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'col1': [np.random.randint(1,100,100)],
    'col2': [np.random.randint(1,100, 100)]
}

df = pd.DataFrame(data)
print(df.head())

# lables = 'low', 'mid', 'high'
# sum_col = df ['col1'] + df['col2']
# df['col3'] = sum_col - sum_col.mean()/sum_col.std()
#
#
# df['bins'] = df['col1']