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

# X - computer
# O - user
import random
from termcolor import colored

def list_board_create():
    list_board = [".", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    return list_board

def printing_board(list_board):
    print(colored((" --- --- ---"), "yellow"))
    print(colored((f"| {list_board [1]} | {list_board [2]} | {list_board [3]} |"), "yellow"))
    print(colored((" --- --- ---"), "yellow"))
    print(colored((f"| {list_board [4]} | {list_board [5]} | {list_board [6]} |"), "yellow"))
    print(colored((" --- --- ---"), "yellow"))
    print(colored((f"| {list_board [7]} | {list_board [8]} | {list_board [9]} |"), "yellow"))
    print(colored((" --- --- ---"), "yellow"))
    return list_board

def computer_move(list_board):
    y = random.choice([i for i in range(1, 10)])
    if list_board[y] == "-":
        list_board[y] = "X"
    elif list_board[y] == "X" or list_board[y] == "O":
        y = random.choice([i for i in range(1, 10)])
        while list_board[y] == "X" or list_board[y] == "O":
            y = random.choice([i for i in range(1, 10)])
            if list_board[y] == "-":
                list_board[y] = "X"

    print(f"Computer chose: {y}")
    print(f"The actual list of board: {list_board[1:10]}")
    printing_board(list_board)
    return list_board

def human_move(list_board):
    x = int(input("Please enter your move, choose number (1-9): "))
    if list_board[x] == "-":
        list_board[x] = "O"
    elif list_board[x] == "X" or list_board[x] == "O":
        print("Please choose another number")
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
        if list_board[options[i][0]] == list_board[options[i][1]] == list_board[options[i][2]] != "-":
            if list_board[options[i][0]] == "X":
                win = "Computer won"
                print(f"Win: {win}")
                return win
                break
            elif list_board[options[i][0]] == "O":
                win = "Human won"
                print(f"Win: {win}")
                return win
                break
            elif "-" not in list_board:
                win = "R"
                print(f"Win: {win}")
                return win
                break
            else:
                continue

# unfinished, to verification
def game():
    x = printing_board(list_board_create())
    for i in range(1, 10):
        y = computer_move(x)
        check_if_win(y)
        human_move(y)
        check_if_win(y)

game()