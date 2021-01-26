# модули
from random import choice
from random import shuffle

#функции

def hello(): # приветствие
    print()
    print('             *************************')
    print('             *** ИГРА УГАДАЙ СЛОВО ***')
    print('             *************************')
    print()
    print('ТЕМА СЕГОДНЯШНЕЙ ИГРЫ - ЖИВОТНЫЕ!')
    print()

def get_word(list_of_words):
    shuffle(list_of_words)
    return choice(list_of_words) 

def check_input(q, l, r):
    ans = input(q)
    if ans.lower() in l[0]:
        return r[0]
    elif ans.lower() in l[1]:
        return r[1]
    else:
        print('Неверный ввод')
        print()
        return check_input(q, l, r)
        
def game():
    
    hello()
    lives = check_input('Выбери уровень сложности? Легко / Сложно (введи "л" или "с"): ', [('л', 'легко', 'easy'), ('с', 'c', 'сложно')], [10, 5])
    word = get_word(animals).upper()
    ans_string = ['-' for _ in range(len(word))]
    wrong_attempts = []
    
    print('Осталось жизней:', lives)

    while lives > 0:
        print('*' * len(word) * 2)
        print(*ans_string, sep=' ')
        print('*' * len(word) * 2)
    
        if ''.join(ans_string) == word:
            print(f'УРА!!! Вы отгадали слово! Это действительно {word}!')
            print()
            break
        print()
    
        ans = input('Введите букву или слово целиком: ').upper()
        if ans == word:
            print()
            print(f'УРА!!! Вы отгадали слово! Это действительно {word}!')
            break
        elif len(ans) == 1 and ans in wrong_attempts:
            lives -= 1
            print('Мы уже пытались это делать и оно не сработало... \nЗачем же наступать на те же грабли? 0_o')
            print()
            print(f'Осталось жизнней: {lives}')
            print()
        
        elif len(ans) == 1 and ans in word:
            for i in range(len(word)):
                if word[i] == ans:
                    ans_string[i] = ans
            print()
        
        elif len(ans) == len(word):
            lives -= 1
            print(f'Не-а! Осталось жизнней: {lives}')
        
        elif len(ans) > 1:
            print('Можно вводить только 1 букву или все слово!')
        
        elif len(ans) == 1 and ans not in wrong_attempts:
            lives -= 1
            print(f'Не-а! Осталось жизнней: {lives}')
            print()
            wrong_attempts.append(ans)
      
        if lives == 0 :
            print(f'Вы проиграили! А слово-то было простое - {word}!!!')
            break




# список слов
animals = ['Жираф', 'Слон', 'Носорог', 'Зебра', 'Лошадь', 'Корова',
            'Бизон', 'Антилопа', 'Коза', 'Свинья', 'Тигр',
            'Кошка', 'Лев', 'Обезьяна', 'Носуха', 'Кролик', 'Крот',
            'Питон', 'Удав', 'Морж', 'Пингвин', 'Саламандра',
            'Крокодил', 'Шакал', 'Волк', 'Буйвол', 'Як',
            'Бегемот', 'Енот', 'Скунс', 'Медведь', 'Рысь', 'Росомаха',
            'Косуля', 'Гепард', 'Барс', 'Шимпанзе', 'Черепаха',
            'Морж', 'Скат', 'Тюлень', 'Сурикат', 'Лемур', 'Мышь',
            'Крыса', 'Кенгуру', 'Панда', 'Игуана', 'Варан', 'Павиан',
            'Павлин', 'Муравьед', 'Альпака', 'Утконос', 'Горностай', 'Журавль',
            'Броненосец', 'Трубкозуб']


# тело игры

while True:
    game()
    print()
    q = input('Eще раз? (Enter == да, любой символ - выход): ')
    if q:
        break


