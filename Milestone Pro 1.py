from __future__ import print_function
#from IPython.display import clear_output




def display_board(board):
    
    #clear_output()
  
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input("Player 1, want X or O:     ").upper()

    if marker== 'X':
        return('X','O')
    else:
        return('O','X')

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def space_check(board, position):
    return board[position] == ' ' #doubt



def player_choice(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = input('Choose your next pos: ')
    return int(position)

def place_marker(board,marker,position):
    board[position]= marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))


def full_bocheck(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True





print("WELCOME to TIC TAC TOE ")

#main
while True:
    theBoard = [' '] * 10      #reset
    P2_mark, P1_mark = player_input()
    turn = 'Player1';
    game_on = True

    while game_on:
        if turn=='Player 1':
            
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,P1_mark,position)

            if win_check(theBoard,P1_mark):
                display_board(theBoard)
                print('Coongo!!! Player 1 WOn')
                game_on = False

            else:
                if full_bocheck(theBoard):
                    display_board(theBoard)
                    print('Draw')
                    break
        
                else:
                    turn = 'Player 2'

           
        else:
            
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,P2_mark,position)

            if win_check(theBoard,P2_mark):
                display_board(theBoard)
                print('Coongo!!! Player 2 WOn')
                game_on = False

            else:
                if full_bocheck(theBoard):
                    display_board(theBoard)
                    print('Draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():   #check the function and then end or restart the game 
        break


