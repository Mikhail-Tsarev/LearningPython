# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

# пригодится формула сочетаний из n элементов по k
from math import factorial

def comb(n, k=2):
    return factorial(n) // (factorial(n - k) * factorial(k))

l = [int(x) for x in input().split()]
count = 0
processed = [] 
for i in l:
    if i not in processed:
        n = l.count(i)
        if n > 1:
            count += comb(n)
            processed.append(i)
        
print(count)
