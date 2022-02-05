"""Stwórz program, który na podstawie tabeli inflacji wartości oprocentowania kredytu,
kwoty początkowej kredytu i stałej wartości raty wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.
Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.
Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację),
i kwota raty były pobierane ze standardowego wejścia (terminal).
Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej.
Skopiuj z niego wartości inflacji dla każdego miesiąca."""

from termcolor import colored
from time import process_time

credit = int(input("Podaj wysokość kredytu: "))
loan_installment = int(input("Podaj wysokość raty miesięcznej: "))
interest_rate = float(input("Podaj oprocentowanie kredytu(np. 0.05): "))


# pobieranie danych o inflacji z pliku inflation.txt
def import_data():
    with open("inflation.txt") as file:
        inflation1 = [float((i.replace(",\n", ""))) for i in file.readlines()]
    return inflation1


def calculation(credit1, loan_installment2, interest_rate1):
    start_time = process_time()
    inflation2 = import_data()
#   for i in range(len(inflation2)):
    for idx, value in enumerate(inflation2):
        oprocentowanie = 1 + ((value/100 + interest_rate1)/12)
        credit_new_value = (1 + ((value / 100 + interest_rate1)/12)) * credit1 - loan_installment2                                         # obliczanie nowej wartości kredytu po racie
        difference_value = credit1 - credit_new_value                                                    # obliczanie różnicy między starą wartością kredytu a nową
        credit1 = credit_new_value

        print(colored(f"rata numer {idx+1}. Inflacja jest na poziomie: {value:.4}% ", "yellow"))
        print(f"Twoja pozostała kwota kredytu to {(round(credit_new_value, 2))} PLN, to {difference_value:.2f} PLN mniej niż w poprzednim miesiącu.")
        print(colored(("-" * 100), "blue"))
    print("")
    end_time = process_time()
    print(f"{(end_time - start_time):.4f}")

calculation(credit, loan_installment, interest_rate)


# inflation = [1.592824484,
#             -0.453509101,
#             2.324671717,
#             1.261254407,
#             1.782526286,
#             2.329384541,
#             1.502229842,
#             1.782526286,
#             2.328848994,
#             0.616921348,
#             2.352295886,
#             0.337779545,
#             1.577035247,
#             -0.292781443,
#             2.48619659,
#             0.267110318,
#             1.417952672,
#             1.054243267,
#             1.480520104,
#             1.577035247,
#             -0.07742069,
#             1.165733399,
#             -0.404186718,
#             1.499708521]


