import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Имя': ['Анна', 'Борис', 'Виктория', 'Дмитрий', 'Елена', 'Фёдор', 'Галина', 'Иван', 'Ксения', 'Леонид'],
    'Математика': [4, 5, 3, 5, 4, 3, 5, 4, 3, 4],
    'Наука': [5, 4, 3, 5, 3, 4, 5, 4, 3, 3],
    'Английский': [3, 4, 3, 5, 5, 3, 4, 4, 3, 4],
    'История': [4, 3, 4, 4, 5, 4, 4, 3, 4, 3],
    'Искусство': [5, 4, 4, 5, 5, 4, 5, 4, 5, 4],
    'Пол': ['Ж', 'М', 'Ж', 'М', 'Ж', 'М', 'Ж', 'М', 'Ж', 'М'],
    'Возраст': [14, 15, 14, 16, 15, 14, 15, 16, 14, 15]
}

df = pd.DataFrame(data)
column = ['Математика',  'Наука',   'Английский',  'История',  'Искусство']

column_mean = df[column].median()
column_std = df[column].std()

print(column_std)


# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
#
# IQR = Q3_math - Q1_math
#
# downside = Q1_math - 1.5 * IQR
# upside = Q3_math + 1.5 * IQR
#
# df['Математика'].hist()
# plt.show()
#
# print(df.describe())
# print(f'Значение Q1 - {Q1_math}, Значение Q3 -  {Q3_math}, Значение IQR -  {IQR}')