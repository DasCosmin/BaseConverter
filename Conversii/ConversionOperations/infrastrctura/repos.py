'''
@author: Dascalu Cosmin-Andrei
'''

from utils.dictionare import *
from domeniu.entitati import Numar
from erori.exceptii import RepoError


class Repo(object):
    
    def __init__(self):
        '''
        Functie care creeaza un obiect de tip Repo 
        Input: -
        Output: - 
        '''
        pass

    def add(self, stNumber, ndNumber, baza):
        '''
        Functie care aduna doua numere intr-o anumita baza
        Input: stNumber - un obiect de tip Numar
               ndNumber - un obiect de tip Numar
               baza - un numar intreg, pozitiv
        Output: un obiect de tip Numar 
        '''
        self.__stNumber = stNumber
        self.__ndNumber = ndNumber
        self.__baza = baza 
        
        rezultatNumber_value = ''
        carryDigit = 0
        while len(self.__stNumber.get_valoare()) > 0 or len(self.__ndNumber.get_valoare()) > 0: 
            # Convertim cele mai din dreapta cifre ale celor doua numere la integer. 
            # Totodata, elimanam cea mai dreapta cifra a fiecarui numar 
            if len(self.__stNumber.get_valoare()) == 0: 
                digit_stNumber = 0 
            else:  # Numarul nu este inca zero   
                digit_stNumber = character_to_decimal[self.__stNumber.get_valoare()[-1]]
                self.__stNumber.set_valoare(self.__stNumber.get_valoare()[:-1])
            
            if len(self.__ndNumber.get_valoare()) == 0:
                digit_ndNumber = 0
            else: # Numarul nu este inca zero
                digit_ndNumber = character_to_decimal[self.__ndNumber.get_valoare()[-1]]
                self.__ndNumber.set_valoare(self.__ndNumber.get_valoare()[:-1])
            
            rezultat_adunare = digit_stNumber + digit_ndNumber + carryDigit
            digit_rezultat = rezultat_adunare % self.__baza 
            carryDigit = rezultat_adunare // self.__baza
            
            character_rezultat = decimal_to_character[digit_rezultat]  # Transformam cifra in caracter
            rezultatNumber_value = character_rezultat + rezultatNumber_value
        # Verificam daca a mai ramas o cifra de transport 
        if carryDigit != 0: 
            character_rezultat = decimal_to_character[carryDigit]  # Transformam cifra in caracter
            rezultatNumber_value = character_rezultat + rezultatNumber_value
            
        return Numar(rezultatNumber_value, self.__baza)

    def multiply(self, stNumber, ndNumber, baza):
        '''
        Functie care inmulteste doua numere intr-o anumita baza
        Input: stNumber - un obiect de tip Numar
               ndNumber - un obiect de tip Numar
               baza - un numar intreg, pozitiv 
        Output: un obiect de tip Numar 
        '''
        self.__baza = baza 
        
        if (stNumber.get_valoare() == '0' or ndNumber.get_valoare() == '0'):
            return Numar('0', self.__baza)
        
        intermediaryResult_value = ''
        finalResult_value = ''
        carryDigit = 0
        numberOfDigits_stNumber = len(stNumber.get_valoare())
        numberOfDigits_ndNumber = len(ndNumber.get_valoare())
        firstNumber = stNumber.get_valoare()
        secondNumber = ndNumber.get_valoare()
        
        for index_SecondNumber in range (numberOfDigits_ndNumber - 1, -1, -1):
            for index_FirstNumber in range(numberOfDigits_stNumber - 1, -1, -1):
                # Convert rightmost digits to decimal
                digit_stNumber = character_to_decimal[firstNumber[index_FirstNumber]]
                digit_ndNumber = character_to_decimal[secondNumber[index_SecondNumber]]
                
                result_Multplication = digit_stNumber * digit_ndNumber + carryDigit
                digit_result = result_Multplication % self.__baza
                carryDigit = result_Multplication // self.__baza
                
                character_result = decimal_to_character[digit_result]  # Digit to character
                intermediaryResult_value = character_result + intermediaryResult_value
            
            # Check for carry digit
            if carryDigit != 0: 
                character_result = decimal_to_character[carryDigit]  # Digit to character
                intermediaryResult_value = character_result + intermediaryResult_value    
                carryDigit = 0
            
            if numberOfDigits_ndNumber >= 2:  # Multidigit Multiplication, then add an extra zero to the end of the final result
                intermediaryResult_value = intermediaryResult_value + (numberOfDigits_ndNumber - index_SecondNumber - 1) * '0'
            
            # Perform a simple addition between the final result and the intermediary result
            dummy_FirstNumber = Numar(finalResult_value, self.__baza)
            dummy_SecondNumber = Numar(intermediaryResult_value, self.__baza) 
            dummy_ResultNumber = self.add(dummy_FirstNumber, dummy_SecondNumber, self.__baza)
            finalResult_value = dummy_ResultNumber.get_valoare()  # Update the final result
                
            # Update the intermediary result
            intermediaryResult_value = '' 
        
        return Numar(finalResult_value, self.__baza)

    def substract(self, stNumber, ndNumber, baza):
        '''
        Functie care scade doua numere intr-o anumita baza
        Input: stNumber - un obiect de tip Numar
               ndNumber - un obiect de tip Numar
               baza - un numar intreg, pozitiv 
        Output: un obiect de tip Numar        
        '''
        self.__stNumber = stNumber
        self.__ndNumber = ndNumber
        self.__baza = baza 
        
        rezultatNumber_value = ''
        borrowDigit = 0
        while len(self.__stNumber.get_valoare()) > 0 or len(self.__ndNumber.get_valoare()) > 0: 
            # Convertim cele mai din dreapta cifre ale celor doua numere la integer. 
            # Totodata, elimanam cea mai dreapta cifra a fiecarui numar 
            if len(self.__stNumber.get_valoare()) == 0: 
                digit_stNumber = 0 
            else:  # Numarul nu este inca zero   
                digit_stNumber = character_to_decimal[self.__stNumber.get_valoare()[-1]]
                self.__stNumber.set_valoare(self.__stNumber.get_valoare()[:-1])
                
            if len(self.__ndNumber.get_valoare()) == 0:
                digit_ndNumber = 0
            else:  # Numarul nu este inca zero
                digit_ndNumber = character_to_decimal[self.__ndNumber.get_valoare()[-1]]
                self.__ndNumber.set_valoare(self.__ndNumber.get_valoare()[:-1])
                
            rezultat_scadere = digit_stNumber - digit_ndNumber + borrowDigit
            if rezultat_scadere < 0: 
                rezultat_scadere = self.__baza + rezultat_scadere
                borrowDigit = -1 
            else: 
                borrowDigit = 0 
            character_rezultat = decimal_to_character[rezultat_scadere]  # Transformam cifra in caracter
            rezultatNumber_value = character_rezultat + rezultatNumber_value
        
        # Elimin zerourile din fata numarului 
        while len(rezultatNumber_value) > 1 and rezultatNumber_value[0] == '0':
            rezultatNumber_value = rezultatNumber_value[1:]
        return Numar(rezultatNumber_value, self.__baza)
    
    def division_decimalBase(self, stNumber, ndNumber):
        '''
        Function that divides two numbers in base 10 
        Input: stNumber, ndNumber - entities of type Numar, with decimal base 
        Output: two objects of type Numar, one representing the quotient, while the other representing the remainder, both in base 10
        '''
        self.__stNumber = stNumber
        self.__ndNumber = ndNumber
        quotient = int(self.__stNumber.get_valoare()) // int(self.__ndNumber.get_valoare())
        remainder = int(self.__stNumber.get_valoare()) % int(self.__ndNumber.get_valoare())
        return Numar(str(quotient), 10), Numar(str(remainder), 10)
    
    def divide(self, stNumber, ndNumber, base):
        '''
        Functie care inmulteste doua numere intr-o anumita baza
        Input: stNumber - un obiect de tip Numar
               ndNumber - un obiect de tip Numar
               base - un numar intreg, pozitiv 
        Output: doua obiecte de tip Numar, primul reprezentand catul impartirii, iar al doilea restul 
        '''
        self.__stNumber = stNumber
        self.__ndNumber = ndNumber
        
        # Convert both numbers to base 10 
        self.__stNumber = self.convert_to_another_base(self.__stNumber, 10)
        self.__ndNumber = self.convert_to_another_base(self.__ndNumber, 10)
        
        # Now that they're both in decimal base, perform simple division between them
        quotient, remainder = self.division_decimalBase(self.__stNumber, self.__ndNumber)
        
        # Now, convert the quotient and remainder to the given base 
        quotient = self.convert_to_another_base(quotient, base)
        remainder = self.convert_to_another_base(remainder, base)
        
        return quotient, remainder

    def convert_subtitutie(self, number):
        '''
        Functie care converteste un numar dintr-o baza diferita de 10 in baza 10. (Metoda subtitutiei)
        Input: number - un obiect de tip Numar, pentru care baza este diferita de 10 
        Output: un obiect de tip Numar, pentru care baza este egala cu 10
        Raises: Exception
            daca numarul transmis ca parametru are baza 10 -> "Baza nevalida!\n"
        '''
        self.__number = number
        if self.__number.get_baza() == 10:
            raise RepoError("Baza nevalida!\n")
        
        rezultat_integer = 0
        factor = 1 
        for index in range(len(self.__number.get_valoare()) -1, -1, -1):
            digit = character_to_decimal[self.__number.get_valoare()[index]]
            rezultat_integer = rezultat_integer + factor * digit 
            factor = factor * self.__number.get_baza()
        return Numar(str(rezultat_integer), 10)

    def convert_impartiri_succesive(self, number, baza):
        '''
        Functie care converteste un numar din baza 10 intr-o alta baza. (Metoda impartirii succesive)
        Input: number - un obiect de tip Numar, pentru care baza este egala cu 10
               baza - un numar intreg, pozitiv, ce apartine multimii {2, 3, ..., 10, 16}
        Output: un obiect de tip Numar, pentru care baza este diferita de 10 
        Raises: Exception 
            daca numarul transmis ca parametru are baza diferita de 10 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 10:
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        if self.__number.get_valoare() == '0':
            return Numar('0', baza)
        
        while self.__number.get_valoare() != '0': 
            number_value_integer = int(self.__number.get_valoare())
            digit = number_value_integer % baza 
            digit = decimal_to_character[digit]
            rezultatNumber_value = digit + rezultatNumber_value
            
            # Actualizam numarul
            number_value_integer = number_value_integer // baza 
            self.__number.set_valoare(str(number_value_integer))
        return Numar(rezultatNumber_value, baza)

    def convert_to_another_base(self, number, noua_baza):
        '''
        Functie care converteste un numar dintr-o baza in alta baza
        Input: number - un obiect de tip Numar
               noua_baza - un numar intreg, pozitiv 
        Output: un obiect de tip Numar 
        '''
        self.__number = number 
        conversie_rapida = False  # Daca se foloseste conversia rapida, nu mai convertim prin subtitutie si impartiri succesive 
        # Daca baza numarului este egala cu 2, iar noua_baza este 4, 8 sau 16 convertim numarul prin Metoda Conversiei Rapide 
        if self.__number.get_baza() == 2: 
            if noua_baza == 4: 
                self.__number = self.convert_base2_to_base4(self.__number)
                conversie_rapida = True
            elif noua_baza == 8: 
                self.__number = self.convert_base2_to_base8(self.__number)
                conversie_rapida = True
            elif noua_baza == 16: 
                self.__number = self.convert_base2_to_base16(self.__number)
                conversie_rapida = True
        
        # Daca baza numarul este egala cu 4, 8 sau 16, iar noua_baza este 2 convertim numarul prin Metoda Conversiei Rapide
        if noua_baza == 2:
            if self.__number.get_baza() == 4:
                self.__number = self.convert_base4_to_base2(self.__number)  
                conversie_rapida = True
            if self.__number.get_baza() == 8:
                self.__number = self.convert_base8_to_base2(self.__number)
                conversie_rapida = True
            if self.__number.get_baza() == 16:
                self.__number = self.convert_base16_to_base2(self.__number)
                conversie_rapida = True
        if conversie_rapida == False:  # Nu s-a folosit metoda Conversiilor Rapide
            # Daca baza numarului este diferita de 10, atunci convertim numarul prin Metoda Subtitutiei la baza 10 
            #                     este egala cu 10, atunci nu mai este nevoie sa il convertim.
            
            if self.__number.get_baza() != 10: 
                self.__number = self.convert_subtitutie(self.__number)
            
            # Daca noua baza este diferita de 10, atunci convertim numarul prin Metoda Impartirilor Succesive la noua baza
            #                este egala cu 10, atunci nu mai este nevoie sa il convertim.
            if noua_baza != 10: 
                self.__number = self.convert_impartiri_succesive(self.__number, noua_baza)
        return Numar(self.__number.get_valoare(), self.__number.get_baza())

    def convert_base4_to_base2(self, number):
        '''
        Functie care converteste un numar din baza 4 in baza 2 (Conversie rapida)
        Input: number - obiect de tip Numar, pentru care baza este egala cu 4 
        Output: un obiect de tip Numar, pentru care baza este egala cu 2 
        Raises: Exception
            daca baza numarului transmis ca parametru nu este 4 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 4:
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        for index in range(len(self.__number.get_valoare())):
            digit = self.__number.get_valoare()[index]
            
            # Convertim cifra in baza 4 a numarului la grupul de 2 cifre binare 
            grup_cifre_binare = base4_to_base2[digit]
            
            # Adaugam grupul de cifre binare la numar 
            rezultatNumber_value = rezultatNumber_value + grup_cifre_binare
            
        # Elimin zerourile din fata numarului 
        while rezultatNumber_value[0] == '0':
            rezultatNumber_value = rezultatNumber_value[1:]    
        return Numar(rezultatNumber_value, 2)

    def convert_base8_to_base2(self, number):
        '''
        Functie care converteste un numar din baza 8 in baza 2 (Conversie rapida)
        Input: number - obiect de tip Numar, pentru care baza este egala cu 8
        Output: un obiect de tip Numar, pentru care baza este egala cu 2 
        Raises: Exception
            daca baza numarului transmis ca parametru nu este 8 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 8:
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        for index in range(len(self.__number.get_valoare())):
            digit = self.__number.get_valoare()[index]
            
            # Convertim cifra in baza 8 a numarului la grupul de 3 cifre binare 
            grup_cifre_binare = base8_to_base2[digit]
            
            # Adaugam grupul de cifre binare la numar 
            rezultatNumber_value = rezultatNumber_value + grup_cifre_binare
            
        # Elimin zerourile din fata numarului 
        while rezultatNumber_value[0] == '0':
            rezultatNumber_value = rezultatNumber_value[1:]    
        return Numar(rezultatNumber_value, 2)

    def convert_base16_to_base2(self, number):
        '''
        Functie care converteste un numar din baza 16 in baza 2 (Conversie rapida)
        Input: number - obiect de tip Numar, pentru care baza este egala cu 16
        Output: un obiect de tip Numar, pentru care baza este egala cu 2 
        Raises: Exception
            daca baza numarului transmis ca parametru nu este 16 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 16:
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        for index in range(len(self.__number.get_valoare())):
            digit = self.__number.get_valoare()[index]
            
            # Convertim cifra in baza 16 a numarului la grupul de 4 cifre binare 
            grup_cifre_binare = base16_to_base2[digit]
            
            # Adaugam grupul de cifre binare la numar 
            rezultatNumber_value = rezultatNumber_value + grup_cifre_binare
            
        # Elimin zerourile din fata numarului 
        while rezultatNumber_value[0] == '0':
            rezultatNumber_value = rezultatNumber_value[1:]    
        return Numar(rezultatNumber_value, 2)

    def convert_base2_to_base4(self, number):
        '''
        Functie care converteste un numar din baza 2 in baza 4 (Conversie rapida)
        Input: number - obiect de tip Numar, pentru care baza este egala cu 2
        Output: un obiect de tip Numar, pentru care baza este egala cu 4 
        Raises: Exception
            daca baza numarului transmis ca parametru nu este 2 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 2: 
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        while self.__number.get_valoare() != '':
            # Luam cel mai din dreapta grup de 2 cifre binare (sau de o singura cifra binara, daca a mai ramas una singura)
            grup_cifre_binare = self.__number.get_valoare()[-2:]
    
            # Convertim grupul de 2 cifre binare (sau de o singura cifra binara, daca a mai ramas una singura)
            digit = base2_to_base4[grup_cifre_binare]
            
            # Adaugam grupul de cifre binare la numar
            rezultatNumber_value = digit + rezultatNumber_value
            
            # Scoatem cele mai din dreapta grup de 2 cifre binare
            self.__number.set_valoare(self.__number.get_valoare()[:-2])
        return Numar(rezultatNumber_value, 4) 

    def convert_base2_to_base8(self, number):
        '''
        Functie care converteste un numar din baza 2 in baza 8 (Conversie rapida)
        Input: number - obiect de tip Numar, pentru care baza este egala cu 2
        Output: un obiect de tip Numar, pentru care baza este egala cu 8 
        Raises: Exception
            daca baza numarului transmis ca parametru nu este 2 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 2: 
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        while self.__number.get_valoare() != '':
            # Luam cel mai din dreapta grup de 3 cifre binare (sau de cate au mai ramas)
            grup_cifre_binare = self.__number.get_valoare()[-3:]
    
            # Convertim grupul de 3 cifre binare (sau de cate au mai ramas)
            digit = base2_to_base8[grup_cifre_binare]
            
            # Adaugam grupul de cifre binare la numar
            rezultatNumber_value = digit + rezultatNumber_value
            
            # Scoatem cele mai din dreapta grup de 3 cifre binare
            self.__number.set_valoare(self.__number.get_valoare()[:-3])
        return Numar(rezultatNumber_value, 8)

    def convert_base2_to_base16(self, number):
        '''
        Functie care converteste un numar din baza 2 in baza 16 (Conversie rapida)
        Input: number - obiect de tip Numar, pentru care baza este egala cu 2
        Output: un obiect de tip Numar, pentru care baza este egala cu 16 
        Raises: Exception
            daca baza numarului transmis ca parametru nu este 2 -> "Baza nevalida!\n"
        '''
        self.__number = number 
        if self.__number.get_baza() != 2: 
            raise RepoError("Baza nevalida!\n")
        
        rezultatNumber_value = ''
        while self.__number.get_valoare() != '':
            # Luam cel mai din dreapta grup de 4 cifre binare (sau de cate au mai ramas)
            grup_cifre_binare = self.__number.get_valoare()[-4:]
    
            # Convertim grupul de 4 cifre binare (sau de cate au mai ramas)
            digit = base2_to_base16[grup_cifre_binare]
            
            # Adaugam grupul de cifre binare la numar
            rezultatNumber_value = digit + rezultatNumber_value
            
            # Scoatem cele mai din dreapta grup de 4 cifre binare
            self.__number.set_valoare(self.__number.get_valoare()[:-4])
        return Numar(rezultatNumber_value, 16)
