import pandas as pd

url8 = "C:\\Users\\Пользователь\\Desktop\\Andrii\\MyPython\\ds_salaries.csv"
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(url)
df.to_csv("auto.csv", header=None)
print(df.info)






