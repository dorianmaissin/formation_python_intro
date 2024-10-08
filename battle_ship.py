#  joueur a une map de 10x10 qui est initialement vide
#     chaque joueur a une liste de bateau disponible dans son inventaire

#     Etape 1 du jeu : chaque joueur place ses bateaux sur sa grille
#     Etape 2 du jeu : a chaque tour, les joueurs peuvent tirer sur l'adverssaire
#     le joueur ne connais pas la map du joueur adverse
#     le jeu prévient le joueur si il a toucher un bateau
#     si le joueur adverse a toucher un bateau, la case touchée, est montré

#     la partie se fini quand un des joueurs a sa grille qui est completement vide
from colorama import Fore
import pprint as pp

board_one = [[ "/","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
         ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

board_two = [[ "/","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
         ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

empty_board = [[ "/","A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
         ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
         ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

boat_list_one = [2,2,2,3,3,4]
boat_list_two = [2,2,2,3,3,4]
boat_postion_list_one = [['A1', 'A2'], ['B1', 'B2'], ['C1', 'C2'], ['D1', 'D2', 'D3'], ['E1', 'E2', 'E3'], ['F1', 'F2', 'F3', 'F4']]
boat_postion_list_two = [['A1', 'A2'], ['B1', 'B2'], ['C1', 'C2'], ['D1', 'D2', 'D3'], ['E1', 'E2', 'E3'], ['F1', 'F2', 'F3', 'F4']]
place_boat_choice = ""
player_placement_front = ""
player_placement_back = ""
player_one = 0
player_two = 1
player_one_score = 0
player_two_score = 0
player_one_score_position = []
player_two_score_position = []
counter = 1
current_player = player_one
def display_bord(array):
    for x in array:
        print(x)

def is_move_valid(place_boat_choice,player_placement_front,player_placement_back):
    if len(player_placement_front) == 2:
        front_col = player_placement_front[0]
        front_row = int(player_placement_front[1])
    else:
        front_col = player_placement_front[0]
        front_row = int(player_placement_front[-2:])
        
    if len(player_placement_back) == 2:
        back_col = player_placement_back[0]
        back_row = int(player_placement_back[1])
    else:
        back_col = player_placement_back[0]
        back_row = int(player_placement_back[-2:])
    
    if front_col == back_col:
        if front_row - back_row == int(place_boat_choice) - 1:
            return True
        elif back_row - front_row == int(place_boat_choice) - 1 :
            return True
        else:
            return False
    elif front_row == back_row:
        if ord(front_col) - ord(back_col) == int(place_boat_choice) - 1:
            return True
        elif ord(back_col) - ord(front_col) == int(place_boat_choice) - 1:
            return True
        else:
            return False
    else :
        return False
    
def ask_user_input(boat_list):
    global place_boat_choice
    global player_placement_front
    global player_placement_back
    place_boat_choice = input(f"Choose between witch boat you want to place from the list {boat_list}\n")
    if len(place_boat_choice)  > 1:
        print("This boat does not exist in the list try again")
        position_boat()
    elif int(place_boat_choice) in boat_list:
        boat_list.remove(int(place_boat_choice))
    else:
        print("This boat does not exist in the list try again")
        position_boat()
    player_placement_front = input(f"tell me the front position for the boat {place_boat_choice}: (exemple A3)\n")
    player_placement_back = input(f"tell me the back position for the boat {place_boat_choice}: (exemple B3)\n")
    return place_boat_choice, player_placement_front, player_placement_back

def place_boat(place_boat_choice,player_placement_front,player_placement_back,player_board,boat_position_list):
    if len(player_placement_front) == 2:
        front_col = player_placement_front[0]
        front_row = int(player_placement_front[1])
    else:
        front_col = player_placement_front[0]
        front_row = int(player_placement_front[-2:])
        
    if len(player_placement_back) == 2:
        back_col = player_placement_back[0]
        back_row = int(player_placement_back[1])
    else:
        back_col = player_placement_back[0]
        back_row = int(player_placement_back[-2:])
        
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    front_col_index = None
    back_col_index = None
    alphatbet_front_col_index = alphabet.index(front_col)

    if front_col in player_board[0]:
        front_col_index = player_board[0].index(front_col)
    if back_col in player_board[0]:
        back_col_index = player_board[0].index(back_col)

    if place_boat_choice == "2":
        player_board[front_row][front_col_index] = "2"
        player_board[back_row][back_col_index] = "2"
        boat_position_list.append([player_placement_front,player_placement_back])
    elif place_boat_choice == "3":
        if front_col == back_col:
            player_board[front_row][front_col_index] = "3"
            player_board[back_row][back_col_index] = "3"
            player_board[front_row + 1][front_col_index] = "3"
            boat_position_list.append([player_placement_front,str(front_col) + str(front_row + 1),player_placement_back])
        elif front_row == back_row:
            player_board[front_row][front_col_index] = "3"
            player_board[back_row][back_col_index] = "3"
            player_board[front_row][front_col_index + 1] = "3"
            boat_position_list.append([player_placement_front,str(alphabet[alphatbet_front_col_index + 1]) + str(front_row),player_placement_back])
    elif place_boat_choice == "4":
        if front_col == back_col:
            player_board[front_row][front_col_index] = "4"
            player_board[back_row][back_col_index] = "4"
            player_board[front_row + 1][front_col_index] = "4"
            player_board[front_row + 2][front_col_index] = "4"
            boat_position_list.append([player_placement_front,str(front_col) + str(front_row + 1),str(front_col) + str(front_row + 2),player_placement_back])
        elif front_row == back_row:
            player_board[front_row][front_col_index] = "4"
            player_board[back_row][back_col_index] = "4"
            player_board[front_row][front_col_index + 1] = "4"
            player_board[front_row][front_col_index + 2] = "4"
            boat_position_list.append([player_placement_front,str(alphabet[alphatbet_front_col_index + 1]) + str(front_row),str(alphabet[alphatbet_front_col_index + 2]) + str(front_row),player_placement_back])
    
    print(boat_position_list)

def position_boat():
    if len(boat_list_one) > 0:
        print("Player One Please Position Your Boats")
        display_bord(board_one)
        ask_user_input(boat_list_one)
        if is_move_valid(place_boat_choice,player_placement_front,player_placement_back):
            place_boat(place_boat_choice,player_placement_front,player_placement_back,board_one,boat_postion_list_one)
            position_boat()
        else :
            print("Invalide position")
            boat_list_one.append(int(place_boat_choice))
            boat_list_one.sort()
            position_boat()
    elif len(boat_list_two) > 0:
        print("Both user have place there boats")
        print("Player Two Please Position Your Boats")
        display_bord(board_two)
        ask_user_input(boat_list_two)      
        if is_move_valid(place_boat_choice,player_placement_front,player_placement_back):
            place_boat(place_boat_choice,player_placement_front,player_placement_back,board_two,boat_postion_list_two)
            position_boat()
        else :
            print("Invalide position")
            boat_list_two.append(int(place_boat_choice))
            boat_list_two.sort()
            position_boat()
    else:
        print("Both user have place there boats")

def battle(board,boat_list,score,player_one_position):
        pp.pprint(board)
        pp.pprint(empty_board)
        print(f"Your score is {score}")
        print(f"Target that as been hit {player_one_position}")
        attack_enemie = input(f"Give me a position to attack (exemple A3)\n")
        for x in boat_list:
            if attack_enemie in x:
                print("You hit one boat and score a point")
                player_one_position.append(attack_enemie)
                x.remove(attack_enemie)
                if len(x) == 0:
                    print("YOU KILLED A BOAT")
                return True
        
        return False

def game():
    global counter
    global player_one_score
    global player_two_score
    global current_player
    global player_one
    global player_two
    if counter % 2 > 0:
        current_player = player_one
    else:
        current_player = player_two

    if (player_one_score < 16) and (player_two_score < 16):
        if current_player == player_one:
            print(Fore.GREEN + "------------------>>>>>>>>>>>>>>>> Player One turn <<<<<<<<<<<<<<<<<-------------------------------")
            batle = battle(board_one,boat_postion_list_two,player_one_score,player_one_score_position)
            if batle:
                player_one_score += 1
                print(player_one_score)
            else:
                print("You missed the boat")
            counter += 1
            game()
        else:
            print(Fore.BLUE + f"------------------>>>>>>>>>>>>>>>> Player One turn <<<<<<<<<<<<<<<<<-------------------------------")
            battle_two = battle(board_two,boat_postion_list_one,player_two_score,player_two_score_position)
            if battle_two:
                player_two_score += 1
                print(player_two_score)
            else:
                print("You missed the boat")
            counter += 1
            game()
    else:
        if player_one_score > player_two_score:
            print("PLAYER ONE WIN THE GAME")
        else:
            print("PLAYER TWO WIN THE GAME")

position_boat()
game()