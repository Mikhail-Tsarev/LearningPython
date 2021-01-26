num = [s for s in input('Число для перевода в десятичную систему: ')]
num_sys = int(input('Из какой системы переводим (введите 2 для двоичной): '))
ans = 0


if num_sys == 16: # в случае шестнадцатеричной системы
    for i in range(len(num)):
        num[i] = 10 if num[i] == 'A' else num[i]
        num[i] = 11 if num[i] == 'B' else num[i]
        num[i] = 12 if num[i] == 'C' else num[i]
        num[i] = 13 if num[i] == 'D' else num[i]
        num[i] = 14 if num[i] == 'E' else num[i]
        num[i] = 15 if num[i] == 'F' else num[i]


for i in range(len(num)): # основной цикл обработки
    ans += int(num[i]) * num_sys ** (len(num) -1 - i)

print(ans) # вывод ответа

input()