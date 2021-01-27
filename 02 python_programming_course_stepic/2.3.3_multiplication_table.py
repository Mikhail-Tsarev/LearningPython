##Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd,
##каждое в своей строке. Программа должна вывести фрагмент таблицы умножения
##для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d]

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for y in range(c, d + 1):
    print('\t', end='')
    print(y, end='\t')
print()
for i in range(a, b+1):
    print(i, end='')
    for j in range(c, d+1):
        print('\t', end='')
        print(i*j, end='')
    print()
