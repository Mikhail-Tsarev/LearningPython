# загрузка модулей
import random

# функции

def hello(): # приветствие
    print()
    print('             ************************')
    print('             ***** УГАДАЙ ЧИСЛО *****')
    print('             ************************')
    print()
    print('Угадайте число от 0 до n за минимальное количество попыток!')
    print()
    print('По умолчанию значение n =  100, но Вы можете ввести \nдругое число для задания правой границы диапазона')
    print()


def is_valid_number(n, r_border): # проверка пользовательского ввода
    return n.isdigit() and 0 <= int(n) <= r_border


def stupid_gamer(sg): # реакция на большое число неправильных вводов
    if sg == 3 or sg >= 6:
        print()
        print('****************************')
        print('Да Вы, батенька, туповаты...')
        print('****************************')
    elif sg == 5:
        print()
        print('********************************************')
        print('Может уже все-таки введем нормальное число?!')
        print('********************************************')

        
def max_number(): # запрос правой границы диапазона

    answer = input('Введите целое натуральное число или нажмите Enter: ')
    c = 1
    while True:
        if answer == '':
            return 100
        elif answer.isdigit() and int(answer) > 0:
            return int(answer)          
        else:
            print()
            answer = input('Так нельзя! Введите ЦЕЛОЕ ЧИСЛО > 0 или нажмите Enter: ')
            c += 1
            stupid_gamer(c)
            continue
        
    
def game(): # тело игры
    hello()
    r_border = max_number()
    x_number  = random.randint(1, r_border)
    counter = 1
    c = 0
    # print(x_number)
    while True:
        print()
        answer = input(f'Введите число в диапазоне от 0 до {r_border}: ')
        if not is_valid_number(answer, r_border):
            print(f'Введите целое число в диапазоне от 0 до {r_border}!!!:')
            c += 1
            stupid_gamer(c)
            continue
        answer = int(answer)
        if answer < x_number:
            print('Загаднное число больше Вашего :(')
            print()
            counter +=1
        elif answer > x_number:
            print('Загаднное число меньше Вашего :(')
            print()
            counter += 1
        else:
            if counter == 2:
                s = 'СО'
            else:
                s = 'С'
            print()
            print()
            print('**********************************************************************')
            print(f'ПОЗДРАВЛЯЕМ! ВЫ УГАДАЛИ {s} {counter} РАЗА! ЭТО ДЕЙСТВИТЕЛЬНО {x_number}! :)')
            print('**********************************************************************')
            print()
            break
        
# основной цикл

while True:
    game()
    print('Сыграем еще раз? Нажмите Enter или введите да / yes или нет / no):')
    if input().lower() in ('', 'да', 'д', 'yes', 'y'):
        #os.system('cls')
        continue
    else:
        exit()

