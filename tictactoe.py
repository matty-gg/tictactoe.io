#Author: Matthew Ghanie
#Date: 1/2/22

import random

choice = ['x','o']
line = '-------------------------------------------'
def even(x):
    if x%2 == 0:
        return True
    else:
        False
def create():
    board = []
    for i in range(9):
        board.append('-')
    return board

def properboard(board):
    new = []
    for i in range(0, len(board),3):
        new.append(board[i:i+3])
    for row in new:
        print(''.join(row))

def check(board):
    if board is not None:
        for i in range(3):
            if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != '-':
                return True,board[i*3]
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] and board[i] != '-':
                return True,board[i]
        if board[0] == board[4] == board[8] and board[0] != '-':
            return True,board[0]
        if board[2] == board[4] == board[6] and board[2] != '-':
            return True,board[2]
def easy_play(board):
    k = 9
    p1 = input('Choose (x/o): ')
    print(line)
    if p1 == 'x':
        print("You are player x...")
        ai = 'o'
    else:
        print("You are player o...")
        ai = 'x'
    while k!= 0:
        if check(board) is not None:
            checker = check(board)
            if checker[0] == True:
                print("Game over, player {} has won!".format(checker[1]))
                handle_menu(k, checker)
                return
        else:
            if even(k):
                if p1 == 'x':
                    board[easy_bot(board,ai) - 1] = ai
                    k-=1
                    properboard(board)
                    print(line)
                else:
                    move = int(input("Enter(O) with (1-9): "))
                    while board[move-1] == 'x' or board[move-1] == 'o':
                        move = int(input("Spot already taken try again: "))
                    board[move-1] = 'o'
                    k-=1
                    properboard(board)
                    print(line)
            else:
                if p1 == 'o':
                    board[easy_bot(board,ai) - 1] = ai
                    k-=1
                    properboard(board)
                    print(line)
                else:
                    move = int(input("Enter(X) with (1-9): "))
                    while board[move-1] == 'x' or board[move-1] == 'o':
                        move = int(input("Spot already taken try again: "))
                    board[move-1] = 'x'
                    k-=1
                    properboard(board)
                    print(line)
    if k == 0:
        return handle_menu(k, None)

def play(board):
    k = 9
    handle_menu(k, None)
    dif = input('Select difficulty (easy/hard): ')
    print(line)
    if dif == 'easy':
        easy_play(board)
    else:
        p1 = input('Choose (x/o): ')
        print(line)
        if p1 == 'x':
            print("You are player x...")
            ai = 'o'
        else:
            print("You are player o...")
            ai = 'x'        
        while k!= 0:
            if check(board) is not None:
                checker = check(board)
                if checker[0] == True:
                    print("Game over, player {} has won!".format(checker[1]))
                    handle_menu(k, checker)
                    return 
            else:
                if even(k):
                    #ai implementation
                    if p1 == 'x':
                        best_move = None
                        best_score = float("-inf")
                        for index, element in enumerate(board): #run through every possible move on the board
                            if element  == '-':
                                board[index] = 'o'
                                score = minimax(board, False,ai) #utilize the minimax function to go through every scenario from that specific move
                                board[index] = '-'
                                if score > best_score:
                                    best_score = score
                                    best_move = index #choose the best move and use it
                        board[best_move] = 'o'
                        k-=1
                        properboard(board)
                        print(line)
                    else:
                        move = int(input("Enter(O) with (1-9): "))
                        while board[move-1] == 'x' or board[move-1] == 'o':
                            move = int(input("Spot already taken try again: "))
                        board[move-1] = 'o'
                        k-=1
                        properboard(board)
                        print(line)
                else:
                    if p1 == 'o':
                        best_move = None
                        best_score = float("-inf")
                        for index, element in enumerate(board):
                            if element  == '-':
                                board[index] = 'x'
                                score = minimax(board, False,ai)
                                board[index] = '-'
                                if score > best_score:
                                    best_score = score
                                    best_move = index
                        board[best_move] = 'x'
                        k-=1
                        properboard(board)
                        print(line)
                    else:
                        move = int(input("Enter(X) with (1-9): "))
                        while board[move-1] == 'x' or board[move-1] == 'o':
                            move = int(input("Spot already taken try again: "))
                        board[move-1] = 'x'
                        k -= 1
                        properboard(board)
                        print(line)
    if k == 0:
        return handle_menu(k, None)

#implementation of the minimax algorithim
def minimax(board, maxing, ai):
    if ai == 'x':
        p1 = 'o'
    else: p1 = 'x'
    result = check(board)
    if result is not None: #checks the outcome of the game prior to recursive call
        if result[1] == ai:
            return 1
        elif result[1] == p1:
            return -1
        else:
            return 0
    if maxing: 
        best_score = float('-inf')
        for index,element in enumerate(board):
            if element == '-':
                board[index] = ai
                score = minimax(board,False,ai)
                board[index] = '-'
                best_score = max(score,best_score) #recursively using the max function to find the best move based on series of next moves
        return best_score
    else:
        best_score = float('inf')
        for index,element in enumerate(board):
            if element == '-':
                board[index] = p1
                score = minimax(board,True,ai)
                board[index] = '-'
                best_score = min(score,best_score)
        return best_score

def easy_bot(board, ai):
    if ai == 'x':
        p1 = 'o'
    else: p1 = 'x'
    result = check(board)
    if result is not None:
        if result[1] == ai:
            return 1
        elif result[1] == p1:
            return -1
        else:
            return 0
    #generate a list of free spaces on our board
    options = []
    for i in range(len(board)):
        if board[i] == '-':
            options.append(i+1)
    move = random.choice(options)
    return move

def handle_menu(k, check):
    if k == 9 and check == None:
        print('Welcome to tic-tac-toe!')
    if check is not None:
        if check[0] == True:
            print('Good job player {}!'.format(check[1]))
            decision = input('Play again? (Y/N): ')
            print(line)
            if decision == 'Y':
                nb = create()
                play(nb)
            else:
                return
    if k == 0 and check == None:
        print('Game has ended in a draw...')
        decision = input('Play again? (Y/N): ')
        print(line)
        if decision == 'Y':
            nb = create()
            play(nb)
        else:
            return

if __name__ == "__main__":
    b = create()
    play(b)
