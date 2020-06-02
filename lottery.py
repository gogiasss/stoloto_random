from random import sample

lotts = int(input("Введите КОНЕЧНОЕ число в лотерее, например 36 или 45: "))
nums = int(input("Введите сколько цифр отметить (например 5 или 6: "))
count = int(input("Введите количество комбинаций: "))

# Создаем список

numbers = [n for n in range(1,lotts+1)]

# Генерируем количество комбинаций 
for i in range(count):
    combination = sample(numbers, nums)
    print(combination)
    

 
