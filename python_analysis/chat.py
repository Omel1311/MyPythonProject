# Создаем пустой список для хранения зарплат сотрудников
salaries = []

# Запросим у пользователя количество сотрудников
num_employees = int(input("Введите количество сотрудников: "))

# Вводим зарплаты сотрудников и добавляем их в список


for i in range(num_employees):
    salary = float(input(f"Введите зарплату для сотрудника {i+1}: "))
    salaries.append(salary)

# Расчет средней зарплаты
average_salary = sum(salaries) / num_employees

# Нахождение максимальной зарплаты
max_salary = max(salaries)

# Вывод результатов анализа
print(f"Средняя зарплата на предприятии: {average_salary:.2f}")
print(f"Максимальная зарплата на предприятии: {max_salary:.2f}")
