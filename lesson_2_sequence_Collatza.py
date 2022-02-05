"""Ciąg Collatza zdefiniowany jest następująco:
Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.
Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
X może przyjmować wartości od 1 do 100. """

import matplotlib.pyplot as plt

start_number = 90   # start_number = input(int("Please enter your number from 1 to 100: "))


def sequence(start_number):
    list = []
    i = 0
    number = start_number
    while number > 1:
        if number % 2 == 0:
            list.append(number)
            next_number = number / 2
            number = next_number
            i += 1
        else:
            list.append(number)
            next_number = 3 * number + 1
            number = next_number
            i += 1
        print(list)                       # for checking is next_number adding correctly
    print(list)
    print(f"Sequence was done in {i} steps.")
    return list


# simple plot of sequence value versus number of iterations
def plot_of_sequence():
    result = sequence(start_number)
    x = []
    y = []
    for id, item in enumerate(result):
        x.append(id)
        y.append(item)
#    print(x)                        # for check
#    print(y)                        # for check
    plt.plot(x, y)
    plt.show()

plot_of_sequence()


