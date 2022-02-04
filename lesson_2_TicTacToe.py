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


def printing_board(list):
#    list = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    print(" --- --- ---")
    print(f"| {list[0]} | {list[1]} | {list[2]} |")
    print(" --- --- ---")
    print(f"| {list[3]} | {list[4]} | {list[5]} |")
    print(" --- --- ---")
    print(f"| {list[6]} | {list[7]} | {list[8]} |")
    print(" --- --- ---")

def computer_move():
    list = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    start = random.choices([i for i in range(8)])
    print(start[0])                 #check
    for id in range(9):
        if list[start[0]] == "-":
            list[start[0]] = "X"

    printing_board(list)
    print(list)                     #check
    return list

def user_move():
    list = computer_move()
    user = int(input("Your move, enter number for your choice: "))
    for i in range(len(list)):
        if list[i] == list[user]:
            if list[user] == "-":
                list[user] = "O"
            else:
                continue
        else:
            print("Please choose other option")
    printing_board(list)
    print(list)

user_move()
