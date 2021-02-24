from random import randint   # TTT V2

class GameField:
    victory_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
                    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  
    FIELD = [' ' for i in range(9)]

    def add_value(self, index, value='X'):
        self.FIELD[index] = value

    def comp_alg(self, value='X'):
        local_count = []
        for i in range(len(self.FIELD)):
            if self.FIELD[i] == value:
                local_count.append(i)

        for item in self.victory_combs:
            k = 0
            for i in item:
                if i in local_count:
                    k += 1
                    if k == 3:
                        return 1

    def comp_tie(self):
        k = 0
        for i in self.FIELD:
            if i == 'X' or i == 'O':
                k += 1
                if k == 9:
                    return 1

    def comparisons(self):
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

GField = GameField()

print('\n\t::::::КРЕСТИКИ-НОЛИКИ::::::\nНиже указана нумерация клеток игрового поля:')
GField.print_test_field()

while True:                                                  # ЗДЕСЬ МОЖНО ВЫБРАТЬ ЗА КОГО ИГРАТЬ
    x_or_o = input('Хотите начать первым? (y/n): ')
    if x_or_o == 'y' or x_or_o == 'n':
        break

def your_turn(class_field):
    class_field.print_field()
    while True:
        try:
            turn = int(input('Введите номер ячейки: '))
            if (turn not in check) and (turn <= 8 and turn >= 0):
                break
        except Exception:
            print('Неверное значение!')

    check.append(turn)
    class_field.add_value(turn, 'X')

    if class_field.comparisons() == 1:
        class_field.print_field()
        print('Вы победили! Поздравляю!\n')
        raise KeyError
    elif class_field.comparisons() == 3:
        class_field.print_field()
        print('Ничья!!!\n')
        raise KeyError

def mach_turn(class_field):
    while True:
        comp_turn = randint(0,8)
        if comp_turn not in check:
            break

    check.append(comp_turn)     
    class_field.add_value(comp_turn, 'O')

    if class_field.comparisons() == 2:
        class_field.print_field()
        print('Вы проиграли...\n')
        raise KeyError
    elif class_field.comparisons() == 3:
        class_field.print_field()
        print('Ничья!!!\n')
        raise KeyError

if x_or_o == 'y':
    check = []
    try:
        while True:
            your_turn(GField)
            mach_turn(GField)
    except KeyError:
        pass

elif x_or_o == 'n':
    check = []
    try:
        while True:
            mach_turn(GField)
            your_turn(GField)
    except KeyError:
        pass
