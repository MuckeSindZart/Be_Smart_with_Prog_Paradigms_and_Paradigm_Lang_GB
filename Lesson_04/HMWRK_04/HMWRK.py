import numpy as np
import matplotlib.pyplot as plt



# Создаем массив из 50 случайных целых чисел от 0 до 10
var1 = np.random.randint(0, 10, 50)
print(var1)

# Создаем положительно коррелированный массив с некоторым случайным шумом
var2 = var1 + np.random.randint(0, 10, 50)
print(var2)

# Рассчитываем корреляцию между двумя массивами
correlation_matrix = np.corrcoef(var1, var2)
print(f'Корреляция: {correlation_matrix[0, 1]:.2f}')