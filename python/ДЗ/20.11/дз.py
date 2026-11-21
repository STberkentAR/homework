#1.
'''
try:
    user_input = input("Введите число: ")
    number = int(user_input)
    print("Квадрат числа:", number * number)
except ValueError:
    print("Введите целое число.")
'''

#2.
'''
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    
    result = num1 / num2
    print("Результат:", result)

except ValueError:
    print("Нужно ввести два целых числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
'''

#3.
'''
dow = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

try:
    day_input = input("Введите номер дня недели: ")
    day_num = int(day_input)
    
    if day_num < 1 or day_num > 7:
        raise IndexError
    
    print(dow[day_num - 1])
    
except ValueError:
    print("Введите номер дня")
except IndexError:
    print("Нет такого дня")
finally:
    print("Проверка завершена")
'''