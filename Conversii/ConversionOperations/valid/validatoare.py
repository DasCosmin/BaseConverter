'''
@author: Dascalu Cosmin-Andrei
'''

from erori.exceptii import ValidError , RepoError
from utils.dictionare import character_to_decimal

class Validator(object):
    
    def __init__(self):
        '''
        Functie de tip constructor care construieste un obiect de tip Validator
        Input: - 
        Output: -
        '''
        pass 

    def valideaza_operatie(self, numarA, numarB, operatie):
        '''
        Functie care valideaza operatiile ce pot fi efectuate intre cele 2 numere
        Input: numarA, numarB - entitati de tip Numar
               operatie - un caracter 
        Output: - 
        Raises: Exception
            if operations is '/' and the second number is 0 -> "Divide by 0!\n"
            if operation is '-' and the second number is bigger than the first number -> "Scadere negativa!\n"
        '''
        erori = ''
        if operatie == '/': 
            if numarB.get_valoare() == '0': 
                erori += "Divide by 0!\n"
        elif operatie == '-': 
            if len(numarA.get_valoare()) < len(numarB.get_valoare()):
                erori += "Scadere negativa!\n"
            elif len(numarA.get_valoare()) == len(numarB.get_valoare()):
                # Verific daca de la stanga la dreapta numarulA are o cifra mai mica decat numarulB.
                scadereNegativa = False 
                index = 0 
                while index < len(numarA.get_valoare()) and scadereNegativa == False: 
                    if numarA.get_valoare()[index] < numarB.get_valoare()[index]: 
                        scadereNegativa = True 
                    index = index + 1 
                if scadereNegativa == True: 
                    erori += "Scadere negativa!\n"
        if len(erori) > 0:  # Exista erori 
            raise RepoError(erori)

    def valideaza_operatie_input(self, operatie):
        '''
        Functie care valideaza operatia aritmetica de baza
        Input: operatie - un string 
        Output: - 
        Raises: Exception 
            daca operatia este diferita de '+-*/' -> "Operatie aritmetica nevalida!\n"
        '''
        if len(operatie) != 1 or operatie not in '+-*/': 
            raise ValidError("Operatie aritmetica nevalida!\n")

    def valideaza_baza(self, baza):
        '''
        Functie care valideaza baza de numeratie a unui numar
        Input: baza - un numar intreg 
        Output: - 
        Raises: Exception
            daca baza nu apartine multimii {2,3, 4, ..., 10, 16} -> "Baza de numeratie nevalida!\n"
        '''
        if baza not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '16']:
            raise ValidError("Baza de numeratie nevalida!")

    def valideaza_numar(self, valoare_numar, baza):
        '''
        Functie care valideaza daca un numar are toate cifrele intr-o baza de numeratie
        Input: valoare_numar - un string
               baza - un string, pentru care valoarea sa apartine {2, 3, ..., 10, 16}
        Output: - 
        Raises: Exception
            daca numarul contine o cifra care nu este in baza transmisa ca parametru -> "Numar nevalid!"
        '''
        # Verificam daca toate cifrele sunt cel putin in bazele admise (2, 3, ..., 10, 16)
        for digit in valoare_numar:
            if digit not in character_to_decimal:
                raise ValidError("Numar nevalid!")
        # Verificam toate toate cifrele sunt mai mici decat baza data
        for digit in valoare_numar: 
            digit_integer = character_to_decimal[digit]
            baza_integer = int(baza)
            if digit_integer >= baza_integer: 
                raise ValidError("Numar nevalid!")
