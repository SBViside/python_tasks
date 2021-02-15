from random import randint

class GameField:
	victory_combs = ((1, 2, 3), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
					(1, 4, 7), (2, 5, 8), (0, 4, 6), (2, 4, 6))  

	FIELD = [' ' for i in range(8)]

	print_field(self):
		print('\n\t {} | {} | {}\n\t '.format(arg[0], arg[1], arg[2]) + '-' * 9)
    	print('\t {} | {} | {}\n\t '.format(arg[3], arg[4], arg[5]) + '-' * 9)
    	print('\t {} | {} | {}\n\t'.format(arg[6], arg[7], arg[8]))



"""
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
"""