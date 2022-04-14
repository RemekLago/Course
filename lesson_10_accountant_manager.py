from lesson_5_saldo import writing_data as func_saldo
from lesson_5_sprzedaz import writing_data as func_sprzedaz
from lesson_5_magazyn import writing_data as func_magazyn
from lesson_5_przeglad import writing_data as func_przeglad
from lesson_5_zakup import writing_data as func_zakup
from lesson_5_konto import writing_data as func_konto
import sys


"""instruction for input
saldo => ['Accountant_saldo.py' , 'file_to_save', 'saldo', 'ballance', 'comment']
sprzedaz =>  ['Accountant_sprzedaz.py' , 'file_to_save', 'sprzedaz', 'product_id', 'price', 'quantity']
zakup => ['Accountant_zakup.py' , 'file_to_save', 'zakup', 'product_id', 'price', 'quantity']
magazyn => ['Accountant_magazyn.py' , 'file_to_save', 'magazyn']
konto =>  ['Accountant_konto.py' , 'file_to_save', 'konto']
przeglad =>  ['Accountant_przeglad.py' , 'file_to_save', 'przeglad']"""


class Manager:
    def __init__(self):
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name]()


manager = Manager()


@manager.assign('saldo')
def saldo():
    func_saldo()

@manager.assign('sprzedaz')
def sprzedaz():
    func_sprzedaz()

@manager.assign('magazyn')
def magazyn():
    func_magazyn()

@manager.assign('przeglad')
def przeglad():
    func_przeglad()

@manager.assign('zakup')
def zakup():
    func_zakup()

@manager.assign('konto')
def konto():
    func_konto()
