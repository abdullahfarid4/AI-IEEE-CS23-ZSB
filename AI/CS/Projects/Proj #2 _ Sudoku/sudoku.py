import random as rd
import file_operations

board = [[0 for _ in range(9)] for _ in range(9)]


def add_nums(i, j, matrix):
    # this function adds random number in a box
    lst_1_to_9 = list(range(1, 10))

    for y in range(3 * i, 3 * i + 3):
        for x in range(3 * j, 3 * j + 3):
            matrix[y][x] = num = rd.choice(lst_1_to_9)
            lst_1_to_9.remove(num)

    return matrix


def add_diagonals(matrix):
    # Fill Diagonal Boxes First
    for i in range(3):
        add_nums(i, i, matrix)

    return matrix


def is_valid(matrix, row, column, number):
    # Check if row, column, and box are valid
    not_in_row = number not in matrix[row]
    not_in_column = number not in [matrix[i][column] for i in range(9)]
    not_in_box = number not in [matrix[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3)
                                for j in range(column // 3 * 3, column // 3 * 3 + 3)]

    return not_in_row and not_in_column and not_in_box


def solve(matrix, row=0, column=0):
    # Backtracking function to check the validity of each number entry
    if row == 9:
        return True

    elif column == 9:
        return solve(matrix, row + 1, 0)

    elif matrix[row][column] != 0:
        return solve(matrix, row, column + 1)

    else:
        for number in range(1, 10):
            if is_valid(matrix, row, column, number):
                matrix[row][column] = number

                if solve(matrix, row, column + 1):
                    return True

                matrix[row][column] = 0
        return False


def set_difficulty(puzzle_matrix, flag):
    # this functions changes the difficulty depending on the difficulty flag
    removed_elements = [5, 6, 7, 7]

    # a list of number's to remove in case of extreme difficulty
    random_number = list(range(1, 10))

    # in case of extreme difficulty, we choose a random number to remove
    if flag == 3:
        num = rd.choice(random_number)
        random_number.remove(num)
        # we iterate over the matrix to remove the number we chose from the matrix
        for j in range(9):
            for k in range(9):
                if puzzle_matrix[j][k] == num:
                    puzzle_matrix[j][k] = ' '

    # we then remove a specific number of elements from each box
    for i in range(3):
        for j in range(3):
            # we remove a specific number of elements depending the flag,
            # in case of removing a number in extreme difficulty we remove a less number from each box
            for _ in range(removed_elements[flag] + 1):

                # getting the rows in the list and all columns for each box
                random_row = list(range(3 * i, 3 * i + 3))
                random_column = list(range(3 * j, 3 * j + 3))

                # going to each box and removing from random columns and rows
                puzzle_matrix[rd.choice(random_row)][rd.choice(random_column)] = ' '

    return puzzle_matrix


def rowCheck(lst: list):
    # Checks the validity of each row in user solution
    for i in lst:
        if len(set(i)) < 9:
            return False
    return True


def columnCheck(lst: list):
    # Checks the validity of each column in user solution
    for j in range(9):
        temp_lst = []
        for i in lst:
            temp_lst.append(i[j])
        if len(set(temp_lst)) < 9:
            return False
    return True


def overallBoxCheck(lst: list):
    # Checks the validity of each box in user solution
    for g in range(0, 9, 3):
        for h in range(0, 9, 3):
            check_lst = []
            for i in range(g, 3 + g):
                for j in range(h, 3 + h):
                    check_lst.append(lst[i][j])

            if len(set(check_lst)) < 9:
                return False

    return True


def get_input():
    # Welcomes the user and Prompts him with what to type if he wants to quit
    print("Welcome to sudoku!")

    # Difficulty List Choice
    difficulty_list = ["easy", "medium", "hard", "extreme"]

    # Set a default difficulty in case of any errors
    difficulty = "medium"

    # Get the correct input from the user
    try:
        difficulty = input("Choose your difficulty (easy - medium - hard - extreme) or quit using (Q/q): ")
        print()
        if difficulty.lower() == 'q':
            print("Exited!")
            exit()

        # Re-ask the user if he has entered a wrong input
        while difficulty.lower() not in difficulty_list:
            print("Please enter a valid difficulty!")
            difficulty = input("Choose your difficulty (easy - medium - hard - extreme) or quit using (Q/q):")
            if difficulty.lower() == 'q':
                print("Exited!")
                exit()
            print()

    except ValueError:
        print("Please enter a valid difficulty!")
        print()

    except KeyboardInterrupt:
        print("\nExited!")
        exit()

    return difficulty_list.index(difficulty)


def display_solution():
    see_solution = 0
    try:
        see_solution = input("Want to see a solution?, press(Y/y): ")
    except KeyboardInterrupt:
        print("\nExited!")
        exit()

    if see_solution.lower() == 'y':
        file_operations.generate_file(board, "solution.txt")
        print('\n')
        print("The solution is here")
        print(__file__.replace("sudoku.py", "solution.txt"))

    print("Thanks for playing")


def check_solution(flag: bool):
    # Print necessary strings and guidelines for the user
    print()
    if flag:
        print("Your solution is correct")
        display_solution()

    else:
        print("Your solution is wrong")
        display_solution()


if __name__ == '__main__':

    # Set the difficulty the user asked for
    diff_flag = get_input()

    # Create the sudoku board by starting with diagonals
    board = add_diagonals(board)

    # Fill out the rest of the board
    solve(board)

    # Create a copy of board then start to empty it depending on the difficulty
    unsolved_board = [x[:] for x in board]
    unsolved_board = set_difficulty(unsolved_board, diff_flag)

    start_flag = 0
    end_flag = 0

    print()
    print("You have chosen your difficulty and your board is ready\n")
    try:
        start_flag = input("Please press (Y/y) to start: ")
    except KeyboardInterrupt:
        print("\nExited!")
        exit()
        
    start_time = 0
    end_time = 0

    # Generates the unsolved board in a file and starts time
    if start_flag.lower() == 'y':
        file_operations.generate_file(unsolved_board, "sudoku_game.txt")
        start_time = file_operations.start_end_time()
        print()
        print("The sudoku board is ready here")
        print(__file__.replace("sudoku.py", "sudoku_game.txt"))
        print("Your time has started, Good Luck")
        print()

    else:
        print("Exited")
        exit()

    try:
        end_flag = input("When you finish, save the file and press (Y/y): ")
    except KeyboardInterrupt:
        print("\nExited!")
        exit()
        
    # Stops time when user have finished
    if end_flag.lower() == 'y':
        end_time = file_operations.start_end_time()
    else:
        print("Exited")
        exit()

    print()
    print("You have spent", end_time - start_time, "solving this puzzle")

    check_flag = False

    # Read the users solution
    try:
        entered_matrix = file_operations.read_solution()
        check_flag = rowCheck(entered_matrix) and columnCheck(entered_matrix) and overallBoxCheck(entered_matrix)
    except FileNotFoundError:
        print("File Not Found!")
        exit()
        
    except ValueError:
        print("You have probably left empty boxes in your solution")
        
    except KeyboardInterrupt:
        print("\nExited!")
        exit()

    check_solution(check_flag)
