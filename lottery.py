from random import sample

numbers = []
lotts = int(input("Введите КОНЕЧНОЕ число в лотерее, например 36 или 45: "))
nums = int(input("Введите сколько цифр отметить (например 5 или 6: "))
count = int(input("Введите количество комбинаций: "))


for i in range(lotts+1):
    numbers.append(i)
    
numbers.remove(0) #удаляем 0
     
def lottery():
    print(sample(numbers,nums))
 
for i in range(count):
    print(lottery())
