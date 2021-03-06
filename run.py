'''
Battleship game Portfolio Project 3
'''

# Imports randint so a random integer can be used
from random import randint
# Imports os libary to clear the screen
import os
# Imports sys library to restart the game without previous data
import sys
# Imports colorama library so colors can be used in the terminal
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Index 0 are the 'row headings'
board = [
    ['+', '1', '2', '3', '4', '5'],
    ['1', '.', '.', '.', '.', '.'],
    ['2', '.', '.', '.', '.', '.'],
    ['3', '.', '.', '.', '.', '.'],
    ['4', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '.', '.'],
]
board_with_moves = [
    ['+', '1', '2', '3', '4', '5'],
    ['1', '.', '.', '.', '.', '.'],
    ['2', '.', '.', '.', '.', '.'],
    ['3', '.', '.', '.', '.', '.'],
    ['4', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '.', '.'],
]


def create_player():
    '''
    Creates a username
    This is required
    '''
    username_input = input('Create your username:\n')
    if username_input == '':
        print('You need to fill in a name. Try again')
        create_player()
    else:
        print('\nHi ' + username_input + ', Let\'s start the game')
        print('-----------------------------------')


def game_rules():
    '''
    Displays the game rules if input answer is 'y'
    Continues without displaying the rules if answer is 'n'
    If answered otherwise, the user is asked to give valid input
    '''
    rules_answer = input('Would you like to read the rules? y/n\n')
    if rules_answer == 'y':
        print('-----------------------------------')
        print('On the battleship board there are 4 hidden ships.')
        print('You have 10 bullets to find all of them.')
        print('When you find all 4 ships, you win.')
        print('If you run out of bullets, you lose.\n')
        print('Use numbers 1 2 3 4 or 5.\n')
        print('To quit: set the coordinates to 0\n')
        print('M = missed shot\n$ = Ship that sunk')
        print('-----------------------------------')
    elif rules_answer != 'n':
        print('Input is invalid, try again')
        game_rules()


def display_battleship_game(board):
    '''
    Prints the battleship game board
    On this board the ships will be placed
    The player will not see this board as the ships location is secret
    '''
    for row in board:
        print(" ".join(row))


def display_board_with_moves(board_with_moves):
    '''
    Prints the game board without the ships
    The input coordinates are being placed on this board
    '''
    for row in board_with_moves:
        print(" ".join(row))


def place_random_ships(board):
    '''
    This function will place the ships.
    The while loop will place 4 ships at a random location.
    Only om empty grids so there are no ships on the same location.
    The ships are marked with an 'X' on the board.
    '''
    added_ships = 0
    while True:
        # Starting from 1 instead of 0 to avoid
        # ships being placed on the headings
        ships_row = randint(1, 5)
        ships_column = randint(1, 5)
        if board[ships_row][ships_column] == '.':
            board[ships_row][ships_column] = 'X'
            added_ships += 1

        if added_ships == 4:
            break


def turns_and_moves(board, board_with_moves):
    '''
    Mananges the input of the player with several if statements
    Within a for loop and a while loop
    It catches all different kinds of input so that all errors
    are being handled correctly without breaking the game
    '''
    points_player = 0
    bullets_left = 10

    for rounds in range(15):
        # While loop with try except statement to check if input is valid
        while True:
            try:
                print('-----------------------------------')
                move_row = int(input('Choose your row number: 1 - 5\n'))
                move_column = int(input('Choose your column number: 1 - 5\n'))
                print('-----------------------------------')
                if move_row > 5 or move_column > 5:
                    print('That\'s out of range. Try again')
                    continue
                elif move_row == 0 or move_column == 0:
                    ex_now = input('Are you sure you want to quit? y/n\n')
                    if ex_now == 'y':
                        print('Till next time!')
                        quit_game()
                    else:
                        continue
            except ValueError:
                print('Input is not valid!')
            else:
                break

        if board[move_row][move_column] == 'X':
            print(f'{Fore.GREEN}Hit! You sunk a battleship!\n')
            board[move_row][move_column] = '$'
            board_with_moves[move_row][move_column] = '$'
            points_player += 1
            bullets_left -= 1
            print(f'Sunken ships: {points_player}')
            print(f'Bullets left: {bullets_left}\n')
            display_board_with_moves(board_with_moves)
        elif board[move_row][move_column] == 'M':
            print('You already choose these coordinations.\n')
            bullets_left -= 1
            print(f'Sunken ships: {points_player}')
            print(f'Bullets left: {bullets_left}\n')
        elif board[move_row][move_column] == '$':
            print('You already choose these coordinations.\n')
            bullets_left -= 1
            print(f'Sunken ships: {points_player}')
            print(f'Bullets left: {bullets_left}\n')
        else:
            print(f'{Fore.RED}You missed... \nTry again\n')
            bullets_left -= 1
            print(f'Sunken ships: {points_player}')
            print(f'Bullets left: {bullets_left}\n')
            board[move_row][move_column] = 'M'
            board_with_moves[move_row][move_column] = 'M'
            display_board_with_moves(board_with_moves)

        if points_player == 4:
            print('-----------------------------------')
            print('You sunk all the battleships and won this game!')
            print(f'{Fore.YELLOW}Congratulations!')
            break
        if bullets_left == 0:
            print('-----------------------------------')
            print(f'No more bullets left\n{Fore.RED}Game over!\n')
            display_battleship_game(board)
            break


def reset_data():
    '''
    Restarts the game without data from the previous game
    '''
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Restarts the program so the data of the previous game will not
    # be displayed on the new game
    os.execl(sys.executable, sys.executable, *sys.argv)


def quit_game():
    '''
    Function to quit the game while playing
    '''
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Exits the game
    sys.exit()


def restart_game():
    '''
    Restarts the game if input is 'y'
    Resets all data
    '''
    print('-----------------------------------')
    restart = input('Do you want to play again? y/n\n')
    if restart == 'y':
        reset_data()
        main()
    elif restart != 'n':
        print('Invalid input, try again')
        restart_game()
    else:
        print('Good bye! See you next time.')


def main():
    '''
    Main function where all other functions are being called from.
    This functions runs the game
    '''
    print(f'\n{Fore.BLUE}Welcome to the Battleships game!')
    print('-----------------------------------')
    game_rules()
    create_player()
    display_board_with_moves(board_with_moves)
    place_random_ships(board)
    turns_and_moves(board, board_with_moves)
    restart_game()


if __name__ == '__main__':
    main()
