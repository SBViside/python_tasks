from random import randint   # TTT V2

class GameField:
    victory_combs = ((1, 2, 3), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
                    (1, 4, 7), (2, 5, 8), (0, 4, 6), (2, 4, 6))  

    FIELD = [' ' for i in range(9)]

    def add_value(self, index, value='X'):
        self.FIELD[index] = value

    def comparisons(self):
        pass                       # ! НАПИСАТЬ МЕТОД ДЛЯ СРАВНЕНИЯ

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

while True:
    x_or_o = input('Хотите начать первым? (y/n): ')
    if x_or_o == 'y' or x_or_o == 'n':
        break

GField.print_field()