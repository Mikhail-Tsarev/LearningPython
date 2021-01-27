##Выведите таблицу размером n x n, заполненную числами от 1 до n^2 по спирали,
##выходящей из левого верхнего угла и закрученной по часовой стрелке

n = int(input())
a = [[0 for i in range(n)] for i in range(n)]
x = 0
y = n - 1
k = 1
while x < y:
    for i in range(x, y):
        a[x][i] = k
        a[i][y] = k + y - x
        a[y][-1 - i] = k + 2 * (y - x)
        a[-1 - i][x] = k + 3 * (y - x)
        k += 1
    k = a[-1 - i][x] + 1
    x += 1
    y -= 1
if n % 2 != 0:
    a[x][y] = k
for x in a:
    print(*x)
