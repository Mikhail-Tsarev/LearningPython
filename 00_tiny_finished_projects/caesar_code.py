# функции


def uncoder(lang, mode, shift, text):
    
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
                #print(A.find(char), shift, length)
            else:
                answer += a[(a.find(char) + shift) % length]
        else:
            answer += char
    return answer
    
def is_valid_input(q, a, b):
    ans = input(q)
    if ans not in (a, b):
        print(f'Некорректный ввод! Нужно ввести "{a}" или "{b}"')
        print()
        is_valid_input(q, a, b)
    return ans
            

# основной цикл
while True:
    lang = is_valid_input('Введите язык текста (rus или eng): ', 'rus', 'eng')
    print()
    mode = is_valid_input('Укажиет режим: кодирование (c) или декодирование (d): ', 'c', 'd')
    print()
    shift = int(input('Укажите сдвиг: '))
    print()
    text = input('Введитие текст для обработки: ')
    print()

    print(uncoder(lang, mode, shift, text))
    print()
    ans = input('Еще раз? (нажатие Enter = да, любой символ выход из программы): ')
    if ans == '':
        continue
    else:
        break
