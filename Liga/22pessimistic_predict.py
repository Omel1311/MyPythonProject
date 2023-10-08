import pandas as pd

# 1. Устанавлииваем оптимальные опции для отображения таблиц
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# 2. считываем информацию с предоставленного Liga360 файла (тестовое задание)
file = 'C:\\Users\\Пользователь\\Desktop\\Проект Тестовое задание 2.xlsx'
df=pd.read_excel(file, sheet_name='Old')

# 3. форматируем и очищаем данные
df.drop(39, axis=0, inplace=True)

print(df.columns.to_list())
# print(df.info())

# 4. получаем общую статистическую информацию из предоставленных данных
# (стандартное отклоненние, min, max, count, среденее и т.д.)
# print(df.describe())
# print(df.shape)

#  5. в ручном режиме заполняем ячейки таблицы в значении которых уверен на 100% (исходя из
#  данных в таблце о периодах оплаты)

#  6. рассчитываем (фактические данные удержания клиентов в октябре (поскольку исходя из данных таблицы
#  уровень удержания несклько ниже чем 0,96))

column_a_numbers_count = df['Вер.2023'].apply(lambda x: isinstance(x, (int, float))).sum()-1
missing_data_counts_oct = df['Жов.2023'].isnull().sum()
retention_rate_oct_2023 = 1-((missing_data_counts_oct / column_a_numbers_count))

print("Количество действующих АO в колонке 'Вер.2023':", column_a_numbers_count)
print("Количество непродлений в Жов.2023:", missing_data_counts_oct) # рассматривается как признак неудержания клиентов
print("Процент удержания клиентов в Жов.2023:", retention_rate_oct_2023)

# 7. рассчитываем значение прогнозируемых значний в июле и в августе 2023
# с учетом фактического устанволенного уровня удержания коиентов - 76%)
# Вычисляем среднее значение по каждой строке для указанных колонок

df['mean'] = df.loc[:, 'Лип.2023':'Сер.2024'].mean(axis=1)

df['Лип.2023'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Сер.2023'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Лис.2023'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Гру.2023'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Січ.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Лют.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Бер.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Кві.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Тра.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Чер.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Лип.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Сер.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Вер.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Жов.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Лис.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)
df['Гру.2024'].fillna(df['mean'] * retention_rate_oct_2023, inplace=True)


# 8. Удаляем значения клиентов после октября, если отсутсствуют записи об адоненском обслуживании с октября 23 по дек
# 2024 года (очень вероятный признак не удержания клиента)
# Выбираем колонки, которые нужно заполнить
columns_to_fill_zero = ['Лис.2023', 'Гру.2023', 'Січ.2024', 'Лют.2024',
                    'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024', 'Сер.2024', 'Вер.2024', 'Жов.2024',
                    'Лис.2024', 'Гру.2024']

## Создаем маску для строк, где 'Жов.2023' пустое значение или равно 0
has_no_value_oct_2023 = df['Жов.2023'].isnull()| (df['Жов.2023'] == 0)

# Заполняем указанные колонки нулями для строк с пустым значением в 'Жов.2023'
df.loc[has_no_value_oct_2023, columns_to_fill_zero] = 0


# 9. расчитываем полученную сумму и создаем в таблице 2 новые колонки - итоги (3 кв.23/ и весь 2024)
df['2023(III_Qr)'] = df[['Лип.2023', 'Сер.2023', 'Вер.2023']].sum(axis=1)

df['2024'] = df[['Січ.2024', 'Лют.2024', 'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024',
                 'Сер.2024', 'Вер.2024', 'Жов.2024','Лис.2024', 'Гру.2024']].sum(axis=1)

# 10. расчитываем полученную сумму по колонкам и создаем в таблице новую итогувую строку
selected_columns = ['Лип.2023', 'Сер.2023', 'Вер.2023', 'Жов.2023', 'Лис.2023', 'Гру.2023', 'Січ.2024', 'Лют.2024',
                    'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024', 'Сер.2024', 'Вер.2024', 'Жов.2024',
                    'Лис.2024', 'Гру.2024', '2023(III_Qr)', '2024']

sum_values = df[selected_columns].sum()
sum_row = pd.DataFrame([sum_values], columns=selected_columns)
df = df._append(sum_row, ignore_index=True)

# 11. вывод на екран все результатов, проврка и сверка
print(df.head(40))
# print(df.tail())

pesimistic_income = df.iloc[39, 20]
pesimistic_income_rounded = round(pesimistic_income, 2)

pesimistic_income_2024 = df.iloc[39, 21]
pesimistic_income_rounded_2024 = round(pesimistic_income_2024, 2)

print("  ")
print("Итоги расчетов (с учетом удержания клиентов):")
print("Прогнозируемый (ПЕССИМИСТИЧЕСКИЙ) доход компании Liga360 за III квартал 2023 года: ",
      pesimistic_income_rounded, 'грн')

print("Прогнозируемый (ПЕССИМИСТИЧЕСКИЙ) доход компании Liga360 за 2024 год: ",
      pesimistic_income_rounded_2024, 'грн')

# 11. cохраняем результаты
df.to_excel('22df_pessimistic_predict.xlsx', index=False)