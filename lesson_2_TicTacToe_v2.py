"""Napisz program do gry w kółko i krzyżyk z przeciwnikiem komputerowym. Główne założenia:
1. Gracz komputerowy rozpoczyna grę.
2. Gracz komputerowy jest reprezentowany przez krzyżyk.
3. Użytkownik programu jest reprezentowany przez kółko.
4. Przeciwnik komputerowy gra optymalnie, tzn. zawsze wybiera najlepszy możliwy ruch. W połączeniu z pkt 1 oznacza to, że gracz komputerowy nigdy nie przegra.
5.Identyfikatory pól na tablicy są rozmieszczone następująco:
   1 2 3
   4 5 6
   7 8 9 .
Przebieg gry (działanie programu):
1. Przeciwnik komputerowy wykonuje ruch. Jeśli komputer wygrał, wyświetla komunikat "Przegrana". Jeśli ostatnie pole zostało wypełnione, wyświetla komunikat "Remis" i kończy działanie.
2. Program zaczyna działanie od wyświetlenia tablicy jako trzech linii w terminalu. Minus "-" symbolizuje pole jeszcze nie wypełnione.
---
-X-
---
3. Program pobiera od użytkownika identyfikator pola, które ma być wypełnione kółkiem i oczekuje naciśnięcia <Enter>.
4. Jeśli identyfikator pola jest nieprawidłowy (zły identyfikator lub pole jest już zajęte), program wyświetla napis "Błąd", i wraca do punktu 4.
5. Program wraca do punktu 1."""

import random
from termcolor import colored

def list_board_create():
    list_board = [".", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    return list_board

def printing_board(list_board):
    print(colored((" --- --- ---"), "yellow"))
    print(colored((f"| {list_board [1]} | {list_board [2]} | {list_board [3]} |")
        , "yellow"))
    print(colored((" --- --- ---"), "yellow"))
    print(colored((f"| {list_board [4]} | {list_board [5]} | {list_board [6]} |")
                  , "yellow"))
    print(colored((" --- --- ---"), "yellow"))
    print(colored((f"| {list_board [7]} | {list_board [8]} | {list_board [9]} |")
                  , "yellow"))
    print(colored((" --- --- ---"), "yellow"))
    return list_board


def computer_move(list_board):
    list_of_available_places = []
    for idx, place in enumerate(list_board):
        if place == "-":
            list_of_available_places.append(idx)

    bc = the_best_choice(list_of_available_places)
#    list_of_available_places = bc
    print(f"BC = {bc}")
    y = random.choice(bc)
    print(f"y(index) z BC:{y}")
    if list_board[y+1] == "-":
        list_board[y+1] = "X"
    print(f"Computer chose: {y}")
    print(f"The actual list of board: {list_board[1:10]}")
    printing_board(list_board)
    return list_board


def the_best_choice(list_of_available_places):
    best_choice = list_of_available_places
    print(f"Best_choice = {best_choice}")
    z = random.randrange(0, len(best_choice))
    print(f"losowy index z z listy = {z}")
    print(f"wartość indexu z = {best_choice[z]}")
    list = []
    if best_choice[z] == best_choice[0]:
        list = [1, 2, 3, 6, 4, 8]
#        for i, j in enumerate(list):
#            if j != "-":
#                if j in best_choice:
#                    best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[1]:
        list = [0, 2, 4, 7]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
#                    best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[2]:
        list = [0, 1, 5, 8, 4, 6]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[3]:
        list = [0, 6, 4, 5]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[4]:
        list = [3, 5, 1, 7, 0, 8]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[5]:
        list = [2, 8, 3, 4]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[6]:
        list = [0, 3, 7, 8, 4, 2]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return best_choice
    if best_choice[z] == best_choice[7]:
        list = [6, 8, 1, 4]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return
    if best_choice[z] == best_choice[8]:
        list = [6, 7, 5, 2, 4, 0]
        # for i, j in enumerate(list):
        #     if j != "-":
        #         if j in best_choice:
        #             best_choice.remove(j)
        best_choice = list
        return best_choice
    print(list)
    return best_choice

def human_move(list_board):
    x = int(input("Please enter your move, choose number (1-9): "))
    if list_board[x] == "-":
        list_board[x] = "O"
    elif list_board[x] == "X" or list_board[x] == "O":

        print("you have chose existed number, choose other.")
        print("Please choose another number")
        return human_move(list_board)
    else:
        print("Please choose correct number (1-9)")

    print(f"Human chose: {x}")
    print(f"The actual list of board: {list_board[1:10]}")
    printing_board(list_board)
    return list_board

def check_if_win(list_board):
    options = [[1, 2, 3], [4, 5, 6], [7, 8, 9],  #rows
                [1, 4, 7], [2, 5, 8], [3, 6, 9], #columns
                [1, 5, 9,], [3, 5, 9]]           #cross
    for i, j in enumerate(options):
        if list_board[options[i][0]] == list_board[options[i][1]]\
                == list_board[options[i][2]] != "-":
            if list_board[options[i][0]] == "X":
                print("Computer win")
                w = 1
                return w
            elif list_board[options[i][0]] == "O":
                print("Human win")
                w = 1
                return w
            elif "-" not in list_board:
                print("Remis")
                w = 1
                return w
    w = 0
    return w


def game():
    x = printing_board(list_board_create())
    w = 0
    while w == 0:
        y = computer_move(x)
        w = check_if_win(y)
        if w:
            break
        human_move(y)
        w = check_if_win(y)


game()