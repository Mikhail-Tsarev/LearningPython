#Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
#Программа принимает на вход две строки одинаковой длины, на первой строке записаны
#символы исходного алфавита, на второй строке — символы конечного алфавита, после
#чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка,
#которую нужно расшифровать.

in1, in2, in3, in4 = input(), input(), input(), input()
out1, out2 = '', ''

for i in range(len(in3)):
    for j in range(len(in1)):
        if in3[i] == in1[j]:
            out1 += in2[j]
            
for i in range(len(in4)):
    for j in range(len(in2)):
        if in4[i] == in2[j]:
            out2 += in1[j]
            
print(out1)
print(out2)
