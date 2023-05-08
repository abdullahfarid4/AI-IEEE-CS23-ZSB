import datetime


def read_solution():
    with open("sudoku_game.txt", 'r') as f:

        # lines where the numbers are
        n = [3, 9, 15, 22, 28, 34, 41, 47, 53]
        user_solve = []

        # enumerate to read only specific lines in file
        for i, line in enumerate(f):
            if i in n:
                x = line.strip().split()
                lst = []
                for k in range(len(x)):
                    # Numbers only exist in odd indexes
                    if k % 2 != 0:
                        lst.append(int(x[k]))
                user_solve.append(lst)

    return user_solve


def generate_file(big_lst: list, file_name):
    x = ' '*9  # BIG SPACE
    x1 = ' '*4  # small space
    n = 0
    with open(file_name, 'w') as f:
        for i in range(57):

            # Lines with File borders and number splitters
            if i in [0, 6, 12, 18, 19, 25, 31, 37, 38, 44, 50, 56]:
                for _ in range(3):
                    f.write(''.join((' ', '-'*9))*3)
                    f.write(' ')
                f.write('\n')

            # Lines with Sudoku Numbers
            elif i in [3, 9, 15, 22, 28, 34, 41, 47, 53]:
                for m in range(9):
                    if m in [3, 6]:
                        f.write("||{}{}{}".format(x1, big_lst[n][m], x1))
                    elif m == 8:
                        f.write("|{}{}{}|".format(x1, big_lst[n][m], x1))
                    else:
                        f.write("|{}{}{}".format(x1, big_lst[n][m], x1))
                f.write('\n')
                n += 1
            # Rest of lines and creates boxes
            else:
                f.write(("|{}|{}|{}|".format(x, x, x))*3)
                f.write('\n')


def start_end_time():
    return datetime.datetime.now()
