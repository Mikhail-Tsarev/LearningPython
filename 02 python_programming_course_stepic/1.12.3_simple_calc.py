##Напишите простой калькулятор, который считывает с пользовательского ввода
##три строки: первое число, второе число и операцию, после чего применяет
##операцию к введённым числам ("первое число" "операция" "второе число")
##и выводит результат на экран.
##
##Поддерживаемые операции: +, -, /, *, mod, pow, div, где
##mod — это взятие остатка от деления,
##pow — возведение в степень,
##div — целочисленное деление.


a = float(input())
b = float(input())
r = input()

if (r == '/' or r == 'mod' or r == 'div') and b == 0:
    print('Деление на 0!')
elif r == '+':
    print(a + b)
elif r == "-":
    print(a - b)
elif r == "/":
    print(a / b)
elif r == "*":
    print(a * b)
elif r == "pow":
    print(a ** b)
elif r == "mod":
    print(a % b)
elif r == "div":
    print(a // b)
else:
    print('Неверный оператор')
