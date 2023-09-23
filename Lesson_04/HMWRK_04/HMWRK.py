import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

# Создаем массив из 50 случайных целых чисел от 0 до 10
var1 = np.random.randint(0, 10, 50)

# Создаем положительно коррелированный массив с некоторым случайным шумом
var2 = var1 + np.random.normal(0, 10, 50)

# Рассчитываем корреляцию между двумя массивами
correlation_matrix = np.corrcoef(var1, var2)
correlation = correlation_matrix[0, 1]

# Создаем график
plt.scatter(var1, var2, label=f'Корреляция: {correlation:.2f}', color='b')
plt.xlabel('Var1')
plt.ylabel('Var2')
plt.title('Диаграмма рассеяния и корреляция Пирсона')

# Добавляем легенду
plt.legend()

# Сохраняем график в файл
plt.savefig('correlation_plot.png')

# Показываем график на экране (необязательно)
plt.show()