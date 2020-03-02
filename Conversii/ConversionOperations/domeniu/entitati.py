'''
@author: Dascalu Cosmin-Andrei
'''


class Numar(object):
    
    def __init__(self, valoare, baza):
        '''
        Functie de tip constructor care construieste un obiect de tip Numar
        Input: valoare - un string 
               baza - un numar intreg, pozitiv, ce apartine multimii {2, 3, ..., 10, 16}
        Output: - 
        '''
        self.__valoare = valoare
        self.__baza = baza 

    def get_valoare(self):
        '''
        Functie de tip get care determina valoarea unui numar 
        Input: - 
        Output: un string 
        '''
        return self.__valoare


    def get_baza(self):
        '''
        Functie de tip get care determina baza de reprezentare a unui numar 
        Input: - 
        Output: un numar intreg, pozitiv
        '''
        return self.__baza


    def set_valoare(self, value):
        '''
        Functie de tip set care seteaza valoarea unui numar 
        Input: value - un string
        Output: - 
        '''
        self.__valoare = value


    def set_baza(self, value):
        '''
        Functie de tip set care seteaza baza unui numar
        Input: baza - un numar intreg, pozitiv 
        Output: - 
        '''
        self.__baza = value
        
    def __str__(self):
        '''
        Functie care determina continutul unui obiect de tip Numar sub forma unui string
        Input: - 
        Output: un string
        '''
        return "Numarul este " + self.__valoare + " si este scris in baza " + str(self.__baza) 
