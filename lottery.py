from random import sample

numbers = []
nums = 6 # сколько цифр надо отметить в игровом поле
count = 3 # количество комбинаций

# Выбрать диапазон чисел, например от 1 до 45
# (необходимо выбрать число на 1 больше, 
# так как последнее не включается в список

for i in range(1,46):
    numbers.append(i)
     
def lottery():
    print(sample(numbers,nums))
 
for i in range(count):
    print(lottery())
