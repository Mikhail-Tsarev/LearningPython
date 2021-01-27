##Программа должна считывать одну строку со стандартного ввода и выводить
##для каждого уникального слова в этой строке число его повторений
##(без учёта регистра) в формате "слово количество" (см. пример вывода).
##Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно
##выводиться только один раз.

s = input().lower().split() # преобразовываем строку на входе в список, приведя все к нижнему регистру и разделив по пробелу
dict = {}
for x in s: # помещаем каждый элемент списка в словарь в качестве ключа
    if x not in dict: # проверяем есть ли такой ключ, если нет,создаем, присваиваем стартовое значение 
        dict[x] = 1
    else:             # если ключ есть, увеличиваем значение элемента на 1
        dict[x] +=1 
for el in dict: # вывод словаря в требуемом формате
    print(el, dict[el])
