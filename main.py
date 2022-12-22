import random

bord = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
pc_points, user_points = 0, 0


def place_x(bord):
    row = int(input('Select row: '))
    column = int(input('Select column: '))
    try:
        # checking if free spot
        if bord[row-1][column-1] == '_':
            bord[row-1][column-1] = 'x'
        else:
            print('Cannot place there! Try again.')
            place_x(bord)
    # if user used number larger than 3
    except IndexError:
        print('Please use numbers from 1 to 3 only.')
        place_x(bord)


def pc_turn(bord):
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    # checking if free spot
    if bord[row][column] == '_':
        bord[row][column] = 'o'
    else:
        pc_turn(bord)


def check_3(bord):
    # checking rows
    for row in bord:
        if row.count(row[0]) == len(row) and row[0] != '_':
            return True
    # checking columns
    for i in range(3):
        if bord[0][i] == bord[1][i] == bord[2][i] and bord[0][i] != '_':
            return True
    # checking diagonals
    if (bord[1][1] == bord[0][0] == bord[2][2] and bord[1][1] != '_') or \
       (bord[1][1] == bord[0][2] == bord[2][0] and bord[1][1] != '_'):
        return True


def get_random_player(bord):
    return pc_turn(bord) if random.randint(0, 1) == 1 else ' '


def display_bord(bord):
    global pc_points
    global user_points
    print(f'You:{user_points} | PC:{pc_points}')
    for item in bord:
        print(f'{"  |  ".join(item)}\n')


def is_board_filled(bord):
    for row in bord:
        for item in row:
            if item == '_':
                return False
    print('DRAW')
    return True


def game(bord):
    global pc_points
    global user_points
    get_random_player(bord)
    while True:
        display_bord(bord)
        place_x(bord)
        if check_3(bord):
            user_points += 1
            print(f'You win!')
            break
        elif is_board_filled(bord):
            break
        pc_turn(bord)
        if check_3(bord):
            pc_points += 1
            print(f'PC wins!')
            break
        elif is_board_filled(bord):
            break
    display_bord(bord)
    if input('Wanna play again? Y/N').lower() == 'y':
        bord = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        game(bord)
    print("Thanks for playing!")


game(bord)
