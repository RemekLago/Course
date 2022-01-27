"""Stwórz program, który na podstawie tabeli inflacji wartości oprocentowania kredytu,
kwoty początkowej kredytu i stałej wartości raty wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.
Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.
Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację),
i kwota raty były pobierane ze standardowego wejścia (terminal).
Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej.
Skopiuj z niego wartości inflacji dla każdego miesiąca."""

import math

credit = 1000000        # potem zmiecić na input
period = 20*12          # potem zmiecić na input
credit_value = 5000     # potem zmiecić na input
interest_rate = 0.015

inflation = [1.592824484,
            -0.453509101,
            2.324671717,
            1.261254407,
            1.782526286,
            2.329384541,
            1.502229842,
            1.782526286,
            2.328848994,
            0.616921348,
            2.352295886,
            0.337779545,
            1.577035247,
            -0.292781443,
            2.48619659,
            0.267110318,
            1.417952672,
            1.054243267,
            1.480520104,
            1.577035247,
            -0.07742069,
            1.165733399,
            -0.404186718,
            1.499708521]

for i in range(len(inflation)):
    credit_new_value = (1 + (inflation[i]/100 + interest_rate)/(20*12)) * credit - 5000
    difference_value = credit - credit_new_value
    credit = credit_new_value
    print("{:0.2f}".format(difference_value))
    print(f"rata numer {i+1}")
    print(f"Twoja pozostała kwota kredytu to {(round(credit_new_value, 2))}, to {difference_value:.2f} mniej niż w poprzednim miesiącu.")
    print()




