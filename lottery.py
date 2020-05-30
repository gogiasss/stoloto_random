from random import sample

numbers = []

# Выбрать диапазон чисел, например от 1 до 45, но
# ставим на единицу больше т.к. последнее число не включается
# в список
for i in range(1,46):
    numbers.append(i)
    
# Сколько цифр нужно отметить в поле
def lottery():
    print(sample(numbers,6))

# Количество комбинаций
for i in range(3):
    print(lottery())


