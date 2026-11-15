'''
#1.
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
ev = 0
odd = 0
nine = 0
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        ev = ev + 1
        sum1 = sum1 + i
    elif i % 2 != 0:
        odd = odd + 1
        sum2 = sum2 + i
    if i % 9 == 0:
        nine = nine + 1
        sum3 = sum3 + i

print("Количество четных чисел:", ev)
print("Количество нечетных чисел:", odd)
print("Количество чисел кратных 9:", nine)
print("Среднеее арифметическое четных чисел:", sum1 / ev)
print("Среднеее арифметическое нечетных чисел:", sum2 / odd)
print("Среднеее арифметическое чисел кратных 9:", sum3 / nine)
'''

'''
#2.
l = int(input("Введите длину линии: "))
s = str(input("Введите символ для заполнения линии: "))

for i in range(l):
    print(s)
'''

'''
#3.
a = int(input("Введите число: "))

if a == 7:
    print("Good bye!")
elif a > 0:
    print("Number is positive")
elif a < 0:
    print("Number is negative")
elif a == 0:
    print("Number is equal to zero")
'''

'''
#4.
a = int(input("Введите первое число: "))
if a == 7:
    print("Good bye!")
else:
    b = int(input("Введите второе число: "))
    if b == 7:
        print("Good bye!")
    else:
        c = int(input("Введите третье число: "))
        if c == 7:
            print("Good bye!")
        else:
            print("Сумма чисел:", a + b + c)
            print("Максимальное число:", max(a, b, c))
            print("Минимальное число:", min(a, b, c))
'''
