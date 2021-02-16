from random import randint                          #tic-tac-toe
                                                    #ПРИСУТСТВУЮТ НЕДОРАБОТКИ
def print_test_field():                             #ПЕРЕДЕЛАТЬ КОГДА БУДЕТ ВРЕМЯ (ПЕРЕДЕЛАНО! in xox_v2.py)
    print('\n\t 0 | 1 | 2\n\t ' + '-' * 9)
    print('\t 3 | 4 | 5\n\t ' + '-' * 9)
    print('\t 6 | 7 | 8\n\t')

def print_field(arg):
    print('\n\t {} | {} | {}\n\t '.format(arg[0], arg[1], arg[2]) + '-' * 9)
    print('\t {} | {} | {}\n\t '.format(arg[3], arg[4], arg[5]) + '-' * 9)
    print('\t {} | {} | {}\n\t'.format(arg[6], arg[7], arg[8]))

def comparisons(listf, tuplef):  # алгоритм для сравнения победных комбинаций с текущими
    local_list_X = []
    local_list_O = []

    for i in range(len(listf)):
        if listf[i] == 'X':
            local_list_X.append(i)
        elif listf[i] == 'O':
            local_list_O.append(i)

    for item in tuplef:
        local_count_X = 0
        local_count_O = 0
        for initem in item:
            if initem in local_list_X:
                local_count_X += 1
                if local_count_X == 3:
                    return 1
            if initem in local_list_O:
                local_count_O += 1
                if local_count_O == 3:
                    return 2

def comparisons_tie(listf):
    local_count = 0
    for i in listf:
        if i == 'X' or i == 'O':
            local_count += 1
            if local_count == 9:
                return 1

def main_script_X(index):
    field_list[index] = 'X'

def main_script_O(index):
    field_list[index] = 'O'

print('\nНиже указана нумерация клеток игрового поля:')
print_test_field()

vict_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6), )
field_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # главное поле, куда добавляются Х и О

while True:
    turn = input('Хотите начать первым? (y/n): ')
    if turn.lower() == 'y' or turn.lower() == 'n':
        break

if turn.lower() == 'y':
    control_list_1 = []    # в список будут добавляться элементы с Х или О (чтобы избежать повторения)
    
    while True:
        if comparisons(field_list, vict_combs) == 1:
            print('\nВы победили! Поздравляю!')
            print_field(field_list)
            break

        elif comparisons(field_list, vict_combs) == 2:
            print('\nВы проиграли! XD')
            print_field(field_list)
            break

        print_field(field_list)
        hod = int(input('Введите номер ячейки: '))

        while True:
            if hod in control_list_1:
                hod = int(input('Повторите попытку: '))
            else:
                control_list_1.append(hod)
                break

        main_script_X(hod)
        system_turn = randint(0,8)

        while True:
            if system_turn in control_list_1:
                system_turn = randint(0,8)
            else:
                break

        control_list_1.append(system_turn)
        main_script_O(system_turn)

        if comparisons_tie(field_list) == 1:
            print('\nНИЧЬЯ.....')
            print_field(field_list)
            break

if turn.lower() == 'n':   # похож на код сверху, который можно попробовать превратить в функцию, но мне лень...
    control_list_1 = [] 
    
    while True:
        if comparisons(field_list, vict_combs) == 2:
            print('\nВы победили! Поздравляю!')
            print_field(field_list)
            break

        elif comparisons(field_list, vict_combs) == 1:
            print('\nВы проиграли! XD')
            print_field(field_list)
            break

        system_turn = randint(0,8)

        while True:
            if system_turn in control_list_1:
                system_turn = randint(0,8)
            else:
                break

        control_list_1.append(system_turn)
        main_script_X(system_turn)

        print_field(field_list)
        hod = int(input('Введите номер ячейки: '))

        while True:
            if hod in control_list_1:
                hod = int(input('Повторите попытку: '))
            else:
                control_list_1.append(hod)
                break

        main_script_O(hod)

        if comparisons_tie(field_list) == 1:
            print('\nНИЧЬЯ.....')
            print_field(field_list)
            break


