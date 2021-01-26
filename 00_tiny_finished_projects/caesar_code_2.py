# блок функций
def uncoder(lang, mode, shift, text): # функция принимает на входе язык, режим (кодирование, декодирование), шаг сдвига, сам текст)
    rus_abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_ABC = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    eng_abc = 'abcdefghijklmnopqrstuvwxyz'
    eng_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''

    if mode == 'd':
        shift = -shift

    if lang == 'rus':
        a = rus_abc
        A = rus_ABC
        length = 32
    elif lang == 'eng':
        a = eng_abc
        A = eng_ABC
        length = 26

    for char in text:
        if char.isalpha():
            if char.isupper():
                answer += A[(A.find(char) + shift) % length]
                # print(A.find(char), shift, length)
            else:
                answer += a[(a.find(char) + shift) % length]
        else:
            answer += char
    return answer # возвращаем кодированное или декодированное сообщение

# ввод данных и подготовка
text = input('Введитие текст для обработки: ') # получаем строку для обработки
print()

le = [word for word in text.split()] # получаем список слов (со знаками препинания)

# основной цикл
for i in range(len(le)): # основной цикл - берем каждое слово
    shift = 0
    for s in le[i]: # тут считаем число букв в слове
        if s.isalpha():
            shift += 1
    le[i] = uncoder('eng', 'c', shift, le[i]) # запускаем основную функцию для каждого из слов, заменяем результатом исходное слово в списке слов

# блок вывода
print(*le)