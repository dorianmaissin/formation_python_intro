import tkinter as tk

#Game set up
player_one = "X"
player_two = "O"
current_player = player_one
winning_game = False
counter = 0
# Board
board = [[" "," "," "],
        [" "," "," "],
        [" "," "," "],]


def horizontal_rules(token, index):
    global winning_game
    count = 0
    for x in board[index]:
        if x == token:
            count += 1
    if count == 3:
        winning_game = True
        return winning_game
    

def vertical_rules(token):
    global winning_game
    if board[0][0] == token and board[1][0] == token and board[2][0] == token:
        winning_game = True
        return winning_game
    elif board[0][1] == token and board[1][1] == token and board[2][1] == token:
        winning_game = True
        return winning_game
    elif board[0][2] == token and board[1][2] == token and board[2][2] == token:
        winning_game = True
        return winning_game

def diagonal_rules(token):
    global winning_game
    if board[0][0] == token and board[1][1] == token and board[2][2] == token:
        winning_game = True
        return winning_game
    if board[0][2] == token and board[1][1] == token and board[2][0] == token:
        winning_game = True
        return winning_game

def apply_position(player_position, player_token):
    if player_position == 0:
        board[0][0] = player_token
    if player_position == 1:
        board[0][1] = player_token
    if player_position == 2:
        board[0][2] = player_token
    if player_position == 3:
        board[1][0] = player_token
    if player_position == 4:
        board[1][1] = player_token
    if player_position == 5:
        board[1][2] = player_token
    if player_position == 6:
        board[2][0] = player_token
    if player_position == 7:
        board[2][1] = player_token
    if player_position == 8:
        board[2][2] = player_token


while winning_game == False:
    if counter % 2 > 0:
        current_player = player_one
    else:
        current_player = player_two
    board_one = " | ".join(board[0])
    board_two = " | ".join(board[1])
    board_three = " | ".join(board[2])
    print(board_one)
    print(board_two)
    print(board_three)
    player_choice = input(f"{current_player} From position 1 to 9, where do you want to place your game\n")
    player_choice_corrected_index = int(player_choice) - 1
    apply_position(player_choice_corrected_index, current_player)
    horizontal_rules(player_one, 0)
    horizontal_rules(player_one, 1)
    horizontal_rules(player_one, 2)
    horizontal_rules(player_two, 0)
    horizontal_rules(player_two, 1)
    horizontal_rules(player_two, 2)
    vertical_rules(player_one)
    vertical_rules(player_two)
    diagonal_rules(player_one)
    diagonal_rules(player_two)
    counter += 1
else:
    print(board_one)
    print(board_two)
    print(board_three)
    print(f"Game Over {current_player} as won the game")

