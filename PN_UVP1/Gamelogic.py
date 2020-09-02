import bottle
import random
from bottle import template, redirect
from random import randint

board = [' ' for x in range(9)]
turn = 0
moznosti = [x for x in range(9)]
moje_poteze = []

def zbrisi_x(moznosti, board):
    if "X" in board:
        moznosti.remove(moje_poteze[-1])

def stevilo_x(board):
    return board.count("X")
    
def take_input(player_token, my_turn):
    if board[my_turn-1] == " ":
        board[my_turn-1] = player_token
    else:
        return False

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5),
                 (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            if board[each[0]] != ' ':
                return board[each[0]]
    if stevilo_x(board) == 5:
        return "remi"

def winner():

    global congrats
    if check_win(board) == 'X':
        redirect('Konec')
        return "X"

    elif check_win(board) == 'O':
        redirect('Konec')
        return "O"
    elif check_win(board) == 'remi':
        redirect('Konec')
        
    


def prosto_mesto(pos):
    if board[pos] == " ":
        return True
    

        
#PREGLEJ ZA POPRAVKE
    
def comp_win_place(token, board):
    for i in range(0,9,3):
        #Vrsta
        if board[i] == token and board[i+2] == token:
            return i+1
        elif board[i] == token and board[i+1] == token:
            return i+2
        elif board[i+1] == token and board[i+2] == token:
            return i
    for i in range(0,3):
        #Stolpec
        if board[i] == token and board[i+6] == token:
            return i+3
        elif board[i] == token and board[i+3] == token:
            return i+6
        elif board[i+3] == token and board[i+6] == token:
            return i
        #Diagonala 1
    if board[0] == token and board[8] == token:
        return 4
    elif  board[1] == token and board[4] == token:
        return 7
    elif board[0] == token and board[4] == token:
        return 8
    elif board[4] == token and board[8] == token:
        return 0
    #Diagonala 2
    elif board[2] == token and board[6] == token:
        return 4
    elif board[6] == token and board[4] == token:
        return 2
    elif board[2] == token and board[4] == token:
        return 6
    else:
        return board.index("X")  
    
#Logika Racunalnik

def comp_input(comp_token):
    while board.count("X") > board.count("O"):
        if stevilo_x(board) == 1:
            global moznosti
            zbrisi_x(moznosti, board)
            comp_ans_one = random.choice(moznosti)
            board[comp_ans_one] = comp_token
            moznosti.remove(board.index("O"))
        elif stevilo_x(board) == 2:
            zbrisi_x(moznosti, board)
            if prosto_mesto(comp_win_place("X", board)) == True:
                comp_ans_drugi = comp_win_place("X", board)
                board[comp_ans_drugi] = comp_token
                moznosti.remove(comp_ans_drugi)
            else:
                comp_ans_drugi = random.choice(moznosti)
                board[comp_ans_drugi] = comp_token
                moznosti.remove(comp_ans_drugi)
        elif stevilo_x(board) == 3 or stevilo_x(board) == 4:
            zbrisi_x(moznosti, board)
            if prosto_mesto(comp_win_place("O", board)) == True :
                comp_ans_three = comp_win_place("O", board)
                board[comp_ans_three] = comp_token
                moznosti.remove(comp_ans_three)
            elif prosto_mesto(comp_win_place("X", board)) == True :
                comp_ans_three = comp_win_place("X", board)
                board[comp_ans_three] = comp_token
                moznosti.remove(comp_ans_three)
            else:
                zanka = 1
                while zanka == 1:
                    comp_ans_three = random.choice(moznosti)
                    if board[comp_ans_three] == " ":
                        zanka = 2   
                board[comp_ans_three] = comp_token
                moznosti.remove(comp_ans_three)

        break

def game_loop(my_turn):
    global turns_remaining
    global turn
    while check_win(board) != "X" and check_win(board) != "O" :
        if turn % 2 == 0:
            if take_input("X", my_turn) == False:
                moje_poteze.append(my_turn-1)
                turn += 1
                winner()
                return None
        else:
            comp_input("O")
            turn += 1
            winner()
            return None
