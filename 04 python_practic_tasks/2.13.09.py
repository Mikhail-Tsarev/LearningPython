##Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
##Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def foo(r1, s1, r2, s2):
    if (r1 + s1) == (r2 + s2) or (r1 - s1) == (r2 - s2) or r1 == r2 or s1 == s2:
        return True
    
l = []   
flag = False

for i in range(8):
    f = list(map(int, input().split()))
    l.append(f)
    
for i in range(7):
    for j in range(i+1, 8):
        if foo(*l[i], *l[j]):
            flag = True
    if flag:
        print('YES')
        break
else:
    print('NO')
