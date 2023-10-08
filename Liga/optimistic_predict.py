import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
# 1. Устанавлииваем оптимальные опции для отображения таблиц
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# 2. считываем информацию с предоставленного Liga360 файла (тестовое задание)
file = 'C:\\Users\\Пользователь\\Desktop\\Проект Тестовое задание 2.xlsx'
df=pd.read_excel(file, sheet_name='Old')

# 3. форматируем и очищаем данные
df.drop(39, axis=0, inplace=True)

# print(df.columns.to_list())
print(df.info())

# 4. получаем общую статистическую информацию из предоставленных данных
# (стандартное отклоненние, min, max, count, среденее и т.д.)
print(df.describe())
print(df.shape)

#  5. в ручном режиме заполняем ячейки таблицы в значении которых уверен на 100% (исходя из
#  данных в таблце о периодах оплаты)

# 6. фиксируем уровень удержания клиентов (предоставленный)
retention_rate_total = 0.96

# 7. расчитываем значение прогнозируемых значний в июле,августе 2023. Поскольку исходя их сусловий задачи следует, что
# 1) данные в таблце расчитаны по-факту (т.е. октябрь 2023)
# 2) клиенты "не новые"
# 3) и они с высокой долей веротяности "успешно" продлевались и в июле, и в августе 2023 года
# 4) то из этого следует, что на них коэфициент удержажания 0,96 с большой долей вероятности
# не распостраняется (т.к. они уже "удержаны") - оптимистический прогоноз.
# 5) поэтому в пустых ячейках за юиль и август 2023 целесообразно устанвить среднеее значение оплаты АО клиента

df['mean'] = df.loc[:, 'Лип.2023':'Сер.2024'].mean(axis=1)
df['Лип.2023'].fillna(df['mean'], inplace=True)
df['Сер.2023'].fillna(df['mean'], inplace=True)

# 8. расчитываем значение прогнозируемых значний в ноябре - декабре 2024 (сентябрь и октябрт уже предоставлен)
# c учетом уровня удержания 96%
df['Лис.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Гру.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Січ.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лют.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Бер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Кві.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Тра.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Чер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лип.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Сер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Вер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Жов.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лис.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Гру.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)

# 9. расчитываем полученную сумму и создаем в таблице 2 новые колонки - итоги
df['2023(III_Qr)'] = df[['Лип.2023', 'Сер.2023', 'Вер.2023']].sum(axis=1)
df['2024'] = df[['Січ.2024', 'Лют.2024', 'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024',
                 'Сер.2024', 'Вер.2024', 'Жов.2024','Лис.2024', 'Гру.2024']].sum(axis=1)

# 10. расчитываем полученную сумму по колонкам и создаем в таблице новую итоговую строку
selected_columns = ['Лип.2023', 'Сер.2023', 'Вер.2023', 'Жов.2023', 'Лис.2023', 'Гру.2023', 'Січ.2024', 'Лют.2024',
                 'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024', 'Сер.2024', '2023(III_Qr)', '2024']

df['2024'] = df[['Лип.2023', 'Сер.2023', 'Вер.2023', 'Жов.2023', 'Лис.2023', 'Гру.2023', 'Січ.2024', 'Лют.2024',
                 'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024', 'Сер.2024']].sum(axis=1)

sum_values = df[selected_columns].sum()
sum_row = pd.DataFrame([sum_values], columns=selected_columns)
df = df._append(sum_row, ignore_index=True)

# 11 вывод на екран все результатов, проврка и сверка
print(df.head())
print(df.tail())

optimistic_income = df.iloc[39, 20]
optimistic_income_rounded = round(optimistic_income, 2)

optimistic_2024 = df.iloc[39, 21]
optimistic_income_rounded_2024 = round(optimistic_2024, 2)

print("  ")
print("Итоги расчетов: ")
print("Прогнозируемый (ОПТИМИСТИЧЕКИЙ) доход компании Liga360 за III квартал 2023 года: ",
      optimistic_income_rounded, 'грн')

print("Прогнозируемый (ОПТИМИСТИЧЕКИЙ) доход компании Liga360 за 2024 год: ",
      optimistic_income_rounded_2024, 'грн')

# 12. cохраняем результаты
df.to_excel('df_optimistic_predict.xlsx', index=False)
#_______________________________________________________________
# Simple Linear Regression

# lm = LinearRegression()

# # X = df[['engine-size']]
# # Y = df['price']
# #
# # lm.fit(X,Y)
# #
# # Yhat=lm.predict(X)
# # print(lm.coef_)
# # print(lm.intercept_)
#
# #_______________________________________________________________
# # Multiple Linear Regression
#
# Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
# # lm.fit(Z, df['price'])
# # print(lm.coef_)
# # print(lm.intercept_)
#
#
# # lm2 = LinearRegression()
# # lm2.fit(df[['normalized-losses' , 'highway-mpg']],df['price'])
# # print(lm2.coef_)
# # print(lm2.intercept_)
#
#
# # # Regression Plot 1
# # width = 12
# # height = 10
# # # plt.figure(figsize=(width, height))
# # # sns.regplot(x="highway-mpg", y="price", data=df)
# # # plt.ylim(0,)
# # # plt.show()
#
#
# # # Regression Plot 2
# # # plt.figure(figsize=(width, height))
# # # sns.regplot(x="peak-rpm", y="price", data=df)
# # # plt.ylim(0,)
# # # plt.show()
#
#
# #_______________________________________________________________
# # #  Verify correlation (corr) | heatmap
#
# # # print('corr', df[["peak-rpm","highway-mpg","price"]].corr())
# # # sns.set (rc = {'figure.figsize':(8, 8)})
# # # dataplot = sns.heatmap(df[["peak-rpm","highway-mpg","price"]].corr(), cmap="YlGnBu", annot=True)
# # # plt.show()
# #
# #______________________________________________________________
# # #  Residual Plot
#
# # # width = 12
# # # height = 10
# # # plt.figure(figsize=(width, height))
# # # sns.residplot(x=df['highway-mpg'],y=df['price'])
# # # plt.show()
#
# #_______________________________________________________________
# #   Multiple Linear Regression | distplot
#
# # Y_hat=lm.predict(Z)
# # plt.figure(figsize=(width, height))
# #
# # ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
# # sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)
# #
# # plt.title('Actual vs Fitted Values for Price')
# # plt.xlabel('Price (in dollars)')
# # plt.ylabel('Proportion of Cars')
# #
# # plt.show()
# # plt.close()
# #
# #_______________________________________________________________
# # # Polynomial Regression
#
# # def PlotPolly(model, independent_variable, dependent_variabble, Name):
# #     x_new = np.linspace(15, 55, 100)
# #     y_new = model(x_new)
# #
# #     plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
# #     plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
# #     ax = plt.gca()
# #     ax.set_facecolor((0.898, 0.898, 0.898))
# #     fig = plt.gcf()
# #     plt.xlabel(Name)
# #     plt.ylabel('Price of Cars')
# #
# #     plt.show()
# #     plt.close()
# #
# #
# # x = df['highway-mpg']
# # y = df['price']
# #
# # f = np.polyfit(x, y, 3)
# # p = np.poly1d(f)
# # print(p)
# #
# # PlotPolly(p, x, y, 'highway-mpg')
#
#
# #_______________________________________________________________
# # Simple Linear Regression
# # The R-square is
#
# X = df[['horsepower']]
# Y = df['price']
# lm.fit(X,Y)
# print('The R-square is: ', lm.score(X, Y))
#
# #_______________________________________________________________
# # Simple Linear Regression
# # predicted value is
#
# Yhat=lm.predict(X)
# print('The output of the first four predicted value is: ', Yhat[0:4])
#
# # Simple Linear Regression
# # mean_squared_error (MSE)
# mse = mean_squared_error(df['price'], Yhat)
# print('The mean square error of price and predicted value is: ', mse)
#
#
# #_______________________________________________________________
# # Multiple Linear Regression¶
# # Let's calculate the R^2:
# # fit the model
# lm.fit(Z, df['price'])
# # Find the R^2
# print('The R-square Multiple Linear Regression¶ is: ', lm.score(Z, df['price']))
#
# #_______________________________________________________________
# # Let's calculate the MSE.
# # Multiple Linear Regression¶
#
# Y_predict_multifit = lm.predict(Z)
# print('The mean square error of price and predicted value using multifit is: ',
#       mean_squared_error(df['price'], Y_predict_multifit))
#
# #_______________________________________________________________
# # Polynomial Fit¶
# # Let's calculate the R^2.
#
# X = df[['horsepower']]
# Y = df['price']
# degree = 2  # Degree of the polynomial
# poly = PolynomialFeatures(degree)
# X_poly = poly.fit_transform(X)
# lm.fit(X_poly, Y)
# y_pred = lm.predict(X_poly)
# r_squared = r2_score(Y, y_pred)
# print('The R-square value is: ', r_squared)

#_______________________________________________________________
# # mean_squared_error Polynomial Fit¶
#
# mean_squared_error = mean_squared_error(df['price'], y_pred)
# print(f'mean_squared_error', {mean_squared_error})
# plt.scatter(X, Y, s=10, label='Actual')
# plt.plot(X, y_pred, color='r', label='Polynomial Fit')
# plt.legend()
# plt.show()
#
# new_input=np.arange(1, 100, 1).reshape(-1, 1)
# lm.fit(X, Y)
# yhat=lm.predict(new_input)
# print(yhat[0:5])
# plt.plot(new_input, yhat)
# plt.show()

"""
Decision Making: Determining a Good Model Fit


<p>Now that we have visualized the different models, and generated the R-squared and MSE values for the fits, how do we determine a good model fit?
<ul>
    <li><i>What is a good R-squared value?</i></li>
</ul>
</p>


<p>When comparing models, <b>the model with the higher R-squared value is a better fit</b> for the data.
<ul>
    <li><i>What is a good MSE?</i></li>
</ul>
</p>

<p>When comparing models, <b>the model with the smallest MSE value is a better fit</b> for the data.</p>

<h4>Let's take a look at the values for the different models.</h4>
<p>Simple Linear Regression: Using Highway-mpg as a Predictor Variable of Price.
<ul>
    <li>R-squared: 0.49659118843391759</li>
    <li>MSE: 3.16 x10^7</li>
</ul>
</p>

<p>Multiple Linear Regression: Using Horsepower, Curb-weight, Engine-size, and Highway-mpg as Predictor Variables of Price.
<ul>
    <li>R-squared: 0.80896354913783497</li>
    <li>MSE: 1.2 x10^7</li>
</ul>
</p>

<p>Polynomial Fit: Using Highway-mpg as a Predictor Variable of Price.
<ul>
    <li>R-squared: 0.6741946663906514</li>
    <li>MSE: 2.05 x 10^7</li>
</ul>
</p>

"""