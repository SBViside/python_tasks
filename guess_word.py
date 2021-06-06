from random import randint

def print_word(*wrd, char=None, lst=[]):
    main_answer = ''
    for i in wrd:
        if (char == i) or (i in lst):
            main_answer += i
        else:
            main_answer += '_'
    return main_answer

words_list = [  'python', 
                'computer', 
                'desktop', 
                'laptop', 
                'keyboard', 
                'mouse', 
                'internet', 
                'touchpad', 
                'windows', 
                'linux',    ]

WORD = words_list[randint(0,len(words_list))]

right_list = []

input('\nИГРА: Угадай слова\nУ тебя 10 попыток на каждое слово\nНажми ENTER чтобы начать...')

k = len(words_list)

def main_game(nm):

    global right_list
    global WORD
    global words_list

    print('\nСлово из {} букв: \n'.format(len(WORD)), print_word(*WORD).replace('', ' ').strip())

    l = 10

    while True:
        if l != 0:
            char1 = input('\nВведите символ: ')

            if 0 < len(char1) < 2:

                if char1 in WORD:
                    print('\nПравильно!')

                    right_list.append(char1)
                    print(print_word(*WORD, char=char1, lst=right_list).replace('', ' ').strip())

                    if print_word(*WORD, char=char1, lst=right_list) == WORD:
                        print('\nПоздравляю! Ты победил!\nУгадывай новое слово!\n')
                        words_list.remove(WORD)
                        WORD = words_list[randint(0,len(words_list) - 1)]
                        right_list = []
                        nm -= 1
                        if nm != -1:
                            main_game(nm)
                        else:
                            break
                        break

                else:
                    l -= 1
                    print('\nНеправильно!\nОсталось {} попыток...\n'.format(l))
                    print(print_word(*WORD, lst=right_list).replace('', ' ').strip())
            else:
                print('\nНЕОБХОДИМО ВВЕСТИ СИМВОЛ!!!\nМинус одна попытка.')
                l -= 1
        else:
            print('\nВы проиграли...\nПравильное слово было: {}'.format(WORD))
            break

main_game(k)

