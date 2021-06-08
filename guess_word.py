from random import randint

def print_word(*wrd, char=None, lst=[]):
    main_answer = ''
    for i in wrd:
        if (char == i) or (i in lst):
            main_answer += i
        else:
            main_answer += '_'
    return main_answer

def main_game(nm):
    global words_list

    if len(words_list) == 0:
        print('\nВЫ ПОБЕДИЛИ!!!\nВЫ ПОБЕДИЛИ!!!\nВЫ ПОБЕДИЛИ!!!')
        return None

    WORD = words_list[randint(0,len(words_list) - 1)]
    char_list = []
    right_list = []

    print('\nСлово из {} букв: \n'.format(len(WORD)), print_word(*WORD).replace('', ' ').strip())
    l = 10

    while True:
        if l != 0:
            print('\nВведенные символы: ', end='')
            for i in char_list:
                print(i, end=' ')
            char1 = input('\nВведите символ: ')
            if 0 < len(char1) < 2:

                if char1 in WORD:
                    print('\nПравильно!')
                    char_list.append(char1)
                    right_list.append(char1)
                    print(print_word(*WORD, char=char1, lst=right_list).replace('', ' ').strip())

                    if print_word(*WORD, char=char1, lst=right_list) == WORD:
                        print('\nПоздравляю! Ты победил!\nУгадывай новое слово!\n')

                        nm -= 1
                        if nm != -1:
                            words_list.remove(WORD)
                            main_game(nm)
                        else:
                            break
                        break
                else:
                    l -= 1
                    print('\nНеправильно!\nОсталось {} попыток...\n'.format(l))
                    char_list.append(char1)
                    print(print_word(*WORD, lst=right_list).replace('', ' ').strip())
            else:
                print('\nНЕОБХОДИМО ВВЕСТИ СИМВОЛ!!!\nМинус одна попытка.')
                l -= 1
        else:
            print('\nВы проиграли...\nПравильное слово было: {}'.format(WORD))
            break


#ОСНОВНОЙ КОД ПРОГРАММЫ
words_list = [  'python', 
                'visual', 
                'basic', 
                'rust', 
                'ruby',    ]

input('\nИГРА: Угадай слова\nУ тебя 10 попыток на каждое слово\nНажми ENTER чтобы начать...')
main_game(len(words_list))

