import pandas as pd

data = {
    'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000]
}

df = pd.DataFrame(data)

vzrMean = df['Возраст'].mean()
vzrMed = df['Возраст'].median()
vzrStd = df['Возраст'].std()

zpMean = df['Зарплата'].mean()
zpMed = df['Зарплата'].median()
zpStd = df['Зарплата'].std()

print(f'Средний возраст - {vzrMean} ;'
      f'\n Медианный возраст - {vzrMed}; '
      f'\n Стандартное отклонение возраста - {vzrStd}')
print(f'Средняя зп - {zpMean} ;\n '
      f'Медианная зп - {zpMed}; \n '
      f'Стандартное отклонение зп - {zpStd}')
