import random
from time import sleep

class Player():
    def __init__(self,name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f'{self.name}'

def player_input():

        marker = ''
    
        while not (marker == 'X' or marker == 'O'):
            marker = input(f'{player1}: Czy chcesz byc X czy O? ').upper()

            if marker == 'X':
                return ('X', 'O')
            elif marker == "O":
                return ('O', 'X')
            else:
                print('Podaj poprawnie znak, z ktorym chcesz grac',end='\n')

def display_board(board):

    print("\t"+board[7]+' | '+board[8]+' | '+board[9])
    print("\t"+board[4]+' | '+board[5]+' | '+board[6])
    print("\t"+board[1]+' | '+board[2]+' | '+board[3])
    

def place_marker(board, marker, position):
        board[position] = marker
        return board

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    result = random.randint(1,2)
    if result == 1:
        return player1
    else:
        return player2

def space_check(board, position):
    if board[int(position)] == " ":
        return True
    else:
        return False

def full_board_check(board):
    if " " not in board:
        return True
    else:
        return False

def player_choise(board):
    position = "Wrong"
    act = range(1,10)
    with_range = False

    while position.isdigit() == False or with_range == False or not space_check(board, position):
        position = input("Podaj pozycje na planszy (1-9): ")

        if position.isdigit() == False:
            print("to nie jest cyfra",end='\n')

        if position.isdigit() == True:
            if int(position) in act:
                with_range = True
            else:
                with_range = False

       
    return int(position)

def replay():
    return input("Czy chcecie zagrac ponownie (Tak czy Nie): ").lower().startswith('t')

print("Witajcie w grze Tik Tak Toe")
print("Zasady znane, tak wygladaja pozycje na tablicy",end='\n')
test_board = ["#","1",'2','3','4','5','6','7','8','9']
display_board(test_board)
print("\n")

while True:
    board = [" "] * 10
    player1 = Player(input("Graczu 1 podaj swoja nazwę: "))
    player2 = Player(input("Graczu 2 podaj swoja nazwę: "))
    player1_marker, player2_marker = player_input()
    print(f"Gracz {player2} jest {player2_marker}",end="\n")
    turn = choose_first()
    print(f'Zaczyna {turn}',end="\n")
    game_on = True;

    while game_on:
        print("\033[H\033[J", end="")
        if turn == player1:
            print(f"Tura gracza: {player1}",end='\n')
            display_board(board)
            position = player_choise(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display_board(board)
                print(f"Gratuluje wygrales {player1}")
                game_on = False
            else:
                if full_board_check(board):
                    print("Jest remis")
                    game_on = False
                    break
                else:
                    turn = player2
        else:

            print(f"Tura gracza: {player2}",end='\n')
            display_board(board)
            position = player_choise(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display_board(board)
                print(f"Gratuluje wygrales {player2}")
                game_on = False
            else:
                if full_board_check(board):
                    print("Jest remis")
                    game_on = False
                    break
                else:
                    turn = player1

    if not replay():
        print("Dzieki za gre i do zoba")
        break
