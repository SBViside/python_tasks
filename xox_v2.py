from random import randint   # TTT V2

class GameField:
    victory_combs = ((1, 2, 3), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
                    (1, 4, 7), (2, 5, 8), (0, 4, 6), (2, 4, 6))  

    FIELD = [' ' for i in range(9)]

    def add_value(self, index, value='X'):
        self.FIELD[index] = value

    def comp_alg(self, value='X'):
        local_count = []
        for i in range(len(self.FIELD)):
            if self.FIELD[i] == value:
                local_count.append(i)
                for l1 in self.victory_combs:
                    k = 0
                    for l2 in l1:
                        if l2 in local_count:
                            k += 1
                            if k == 3:
                                return 1

    def comp_tie(self):
        k = 0
        for i in self.FIELD:
            if i == ' ':
                k += 1
                if k == 0:
                    return 1


    def comparisons(self):                   # ! НАПИСАТЬ МЕТОД ДЛЯ СРАВНЕНИЯ
        if self.comp_alg('X') == 1:
            return 1
        if self.comp_alg('O') == 1:
            return 2
        if self.comp_tie() == 1:
            return 3


    def print_test_field(self):
        print('\n\t\t 0 | 1 | 2\n\t\t ' + '-' * 9)
        print('\t\t 3 | 4 | 5\n\t\t ' + '-' * 9)
        print('\t\t 6 | 7 | 8\n\t\t')

    def print_field(self):
        print('\n\t\t {} | {} | {}\n\t\t '.format(self.FIELD[0], self.FIELD[1], self.FIELD[2]) + '-' * 9)
        print('\t\t {} | {} | {}\n\t\t '.format(self.FIELD[3], self.FIELD[4], self.FIELD[5]) + '-' * 9)
        print('\t\t {} | {} | {}\n\t\t'.format(self.FIELD[6], self.FIELD[7], self.FIELD[8]))

# ЗДЕСЬ НАЧИНАЕТСЯ ТЕЛО ОСНОВНОЙ ПРОГРАММЫ

GField = GameField()

print('\n\t::::::КРЕСТИКИ-НОЛИКИ::::::\nНиже указана нумерация клеток игрового поля:')
GField.print_test_field()

while True:                                                  # ЗДЕСЬ МОЖНО ВЫБРАТЬ ЗА КОГО ИГРАТЬ
    x_or_o = input('Хотите начать первым? (y/n): ')
    if x_or_o == 'y' or x_or_o == 'n':
        break

if x_or_o == 'y':
    check = []
    while True:

        GField.print_field()
        while True:
            turn = int(input('Введите номер ячейки: '))
            if turn not in check:
                break

        check.append(turn)
        GField.add_value(turn, 'X')

        if GField.comparisons() == 1:
            GField.print_field()
            print('\nВы победили! Поздравляю!')
            break
        elif GField.comparisons() == 3:
            GField.print_field()
            print('\nНичья!!!')
            break

        while True:
            comp_turn = randint(0,8)
            if comp_turn not in check:
                break

        check.append(comp_turn)     
        GField.add_value(comp_turn, 'O')

        if GField.comparisons() == 2:
            GField.print_field()
            print('\nВы проиграли...')
            break
        elif GField.comparisons() == 3:
            GField.print_field()
            print('\nНичья!!!')
            break

elif x_or_o == 'n':
    check = []
    while True:
        while True:
            comp_turn = randint(0,8)
            if comp_turn not in check:
                break

        check.append(comp_turn)     
        GField.add_value(comp_turn, 'X')

        if GField.comparisons() == 1:
            GField.print_field()
            print('\nВы проиграли...')
            break
        elif GField.comparisons() == 3:
            GField.print_field()
            print('\nНичья!!!')
            break

        GField.print_field()
        while True:
            turn = int(input('Введите номер ячейки: '))
            if turn not in check:
                break

        check.append(turn)
        GField.add_value(turn, 'O')

        if GField.comparisons() == 2:
            GField.print_field()
            print('\nВы победили! Поздравляю!')
            break
        elif GField.comparisons() == 3:
            GField.print_field()
            print('\nНичья!!!')
            break
