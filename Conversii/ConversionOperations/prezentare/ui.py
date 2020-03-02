'''
@author: Dascalu Cosmin-Andrei
'''
import sys 
from erori.exceptii import ValidError, RepoError
class Console(object):
    
    def __init__(self, serviceNumere):
        '''
        Functie de tip constructor care construieste un obiect de tip Console
        Input: serviceNumere - entitate de tip ServiceNumere
        Output: - 
        '''
        self.__serviceNumere = serviceNumere
        self.__comenzi = {
            '+': self.__add,
            '-': self.__substract,
            '*': self.__multiply,
            '/': self.__divide
        }
        self.__commandsProcess = {
            '+': self.__addProcess,
            '-': self.__substractProcess,
            '*': self.__multiplyProcess,
            '/': self.__divideProcess,
        }

    def __add(self, params):
        '''
        Functie care calculeaza suma a doua numere intr-o anumita baza
        Input: params - o lista de parametri
        Output: - 
        '''
        numarA, numarB, baza_numarA, baza_numarB, baza_calcul = params 
        rezultat = self.__serviceNumere.add(numarA, numarB, baza_numarA, baza_numarB, baza_calcul)
        print (numarA, "(", baza_numarA, ")", " + ", numarB, "(", baza_numarB, ")",
               " = ", rezultat.get_valoare(), "(", baza_calcul, ")\n", sep='')

    def __addProcess(self, params):
        '''
        Function that performs addition of 2 numbers in the given base, hexadecimal, decimal and binary. It is used for the interprocess between Python and C#
        Input: params - a list of parameters
        Output: - 
        '''
        numberA, numberB, base_numberA, base_numberB, base_result = params
        result = self.__serviceNumere.add(numberA, numberB, base_numberA, base_numberB, base_result)
        resultHexadecimal = self.__serviceNumere.add(numberA, numberB, base_numberA, base_numberB, 16)
        resultDecimal = self.__serviceNumere.add(numberA, numberB, base_numberA, base_numberB, 10)
        resultBinary = self.__serviceNumere.add(numberA, numberB, base_numberA, base_numberB, 2)
        print (result.get_valoare() + "|" + resultHexadecimal.get_valoare() + "|" + resultDecimal.get_valoare() + "|" + resultBinary.get_valoare())

    def __substractProcess(self, params):
        '''
        Function that performs substraction of 2 numbers in a given base, hexadecimal, decimal and binary. It is used for the interprocess between Python and C#
        Input: params - a list of parameters
        Output: -
        Raises: Exception
            if the first number is lower than the second number -> "Negative substraction!\n"
        '''
        numberA, numberB, base_numberA, base_numberB, base_result = params
        result = self.__serviceNumere.substract(numberA, numberB, base_numberA, base_numberB, base_result)
        resultHexadecimal = self.__serviceNumere.substract(numberA, numberB, base_numberA, base_numberB, 16)
        resultDecimal = self.__serviceNumere.substract(numberA, numberB, base_numberA, base_numberB, 10)
        resultBinary = self.__serviceNumere.substract(numberA, numberB, base_numberA, base_numberB, 2)
        print (result.get_valoare() + "|" + resultHexadecimal.get_valoare() + "|" + resultDecimal.get_valoare() + "|" + resultBinary.get_valoare())

    def __multiplyProcess(self, params):
        '''
        Function that performs multiplication of 2 numbers in a given base, hexadecimal, decimal and binary. It is used for the interprocess between Python and C#
        Input: params - a list of parameters
        Output: -
        '''
        numberA, numberB, base_numberA, base_numberB, base_result = params
        result = self.__serviceNumere.multiply(numberA, numberB, base_numberA, base_numberB, base_result)
        resultHexadecimal = self.__serviceNumere.multiply(numberA, numberB, base_numberA, base_numberB, 16)
        resultDecimal = self.__serviceNumere.multiply(numberA, numberB, base_numberA, base_numberB, 10)
        resultBinary = self.__serviceNumere.multiply(numberA, numberB, base_numberA, base_numberB, 2)
        print (result.get_valoare() + "|" + resultHexadecimal.get_valoare() + "|" + resultDecimal.get_valoare() + "|" + resultBinary.get_valoare())

    def __divideProcess(self, params):
        '''
        Function that performs division of 2 numbers in a given base, hexadecimal, decimal and binary. It is used for the interprocess between Python and C#
        Input: params - a list of parameters
        Output: -
        Raises: Exception
            if the second number is zero -> "Divide by 0!\n"
        '''
        numberA, numberB, base_numberA, base_numberB, base_result = params
        quotient, remainder = self.__serviceNumere.divide(numberA, numberB, base_numberA, base_numberB, base_result)
        quotientHexadecimal, remainderHexadecimal = self.__serviceNumere.divide(numberA, numberB, base_numberA, base_numberB, 16)
        quotientDecimal, remainderDecimal = self.__serviceNumere.divide(numberA, numberB, base_numberA, base_numberB, 10)
        quotientBinary, remainderBinary = self.__serviceNumere.divide(numberA, numberB, base_numberA, base_numberB, 2)
        print(quotient.get_valoare() + " .r " + remainder.get_valoare() + "|" +
              quotientHexadecimal.get_valoare() + " .r " + remainderHexadecimal.get_valoare() + "|" + 
              quotientDecimal.get_valoare() + " .r " + remainderDecimal.get_valoare() + "|" + 
              quotientBinary.get_valoare() + " .r " + remainderBinary.get_valoare())

    def __substract(self, params):   
        '''
        Functie care calculeaza diferenta a doua numere intr-o anumita baza
        Input: params - o lista de parametri
        Output: - 
        Raises: Exception
            daca primul numar este mai mic decat al doilea numar -> "Scadere negativa!\n"
        ''' 
        numarA, numarB, baza_numarA, baza_numarB, baza_calcul = params 
        rezultat = self.__serviceNumere.substract(numarA, numarB, baza_numarA, baza_numarB, baza_calcul)
        print (numarA, "(", baza_numarA, ")", " - ", numarB, "(", baza_numarB, ")",
               " = ", rezultat.get_valoare(), "(", baza_calcul, ")\n", sep='')
    
    def __multiply(self, params):
        '''
        Functie care calculeaza produsul a doua numere intr-o anumita baza
        Input: params - o lista de parametri
        Output: - 
        Raises: Exception
            daca al doilea numar are mai mult de o cifra in baza de calcul -> "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        ''' 
        numarA, numarB, baza_numarA, baza_numarB, baza_calcul = params 
        rezultat = self.__serviceNumere.multiply(numarA, numarB, baza_numarA, baza_numarB, baza_calcul)
        print (numarA, "(", baza_numarA, ")", " * ", numarB, "(", baza_numarB, ")",
               " = ", rezultat.get_valoare(), "(", baza_calcul, ")\n", sep='')
    
    def __divide(self, params):
        '''
        Functie care calculeaza catul si restul impartirii a doua numere intr-o anumita baza
        Input: params - o lista de parametri
        Output: - 
        Raises: Exception
            daca al doilea numar are mai mult de o cifra in baza de calcul -> "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        ''' 
        numarA, numarB, baza_numarA, baza_numarB, baza_calcul = params 
        cat, rest = self.__serviceNumere.divide(numarA, numarB, baza_numarA, baza_numarB, baza_calcul)
        print (numarA, "(", baza_numarA, ")", " / ", numarB, "(", baza_numarB, ")",
               " = cat ", cat.get_valoare(), "(", baza_calcul, ") rest ", rest.get_valoare(),
               "(", baza_calcul, ")\n", sep='')
    
    def runProcess(self):
        '''
        Functie care ruleaza programul propriu-zis
        Input: - 
        Output: -
        '''
        # Citirea operatiei aritmetice: 
        operatie = sys.argv[1]
        try: 
            self.__serviceNumere._validatorNumar.valideaza_operatie_input(operatie)
        except ValidError as ve: 
            print("Valid Error: ", str(ve))
            return 
            
        # Citirea bazelor de numeratie:
        try: 
            baza_numarA = sys.argv[2]
            self.__serviceNumere._validatorNumar.valideaza_baza(baza_numarA)
        except ValidError as ve: 
            print("Valid Error: ", str(ve), "Baza trebuie sa apartina multimii {2, 3, ..., 10, 16}!\n")
            return 

        try:
            baza_numarB = sys.argv[3]
            self.__serviceNumere._validatorNumar.valideaza_baza(baza_numarB)
        except ValidError as ve: 
            print("Valid Error: ", str(ve), "Baza trebuie sa apartina multimii {2, 3, ..., 10, 16}!\n")
            return 

        try: 
            baza_calcul = sys.argv[4]
            self.__serviceNumere._validatorNumar.valideaza_baza(baza_calcul)
        except ValidError as ve: 
            print("Valid Error: ", str(ve), "Baza trebuie sa apartina multimii {2, 3, ..., 10, 16}!\n")
            return

        # Citirea celor doua numere: 
        try: 
            numarA = sys.argv[5]
            numarA = numarA.upper()  # Capitalizam numarul 
            self.__serviceNumere._validatorNumar.valideaza_numar(numarA, baza_numarA)
        except ValidError as ve: 
            print("Valid Error: ", str(ve), " Numarul trebuie sa fie in baza ", baza_numarA, "!\n", sep='')
            return
                
        try: 
            numarB = sys.argv[6]
            numarB = numarB.upper()  # Capitalizam numarul 
            self.__serviceNumere._validatorNumar.valideaza_numar(numarB, baza_numarB)
        except ValidError as ve: 
            print("Valid Error: ", str(ve), " Numarul trebuie sa fie in baza ", baza_numarB, "!\n", sep='')
            return 

        # "Impachetam" parametrii
        params = numarA, numarB, int(baza_numarA), int(baza_numarB), int(baza_calcul)
        
        try: 
            self.__commandsProcess[operatie](params)
        except RepoError as re: 
            print ("Repo Error: ", str(re))
    
    def run(self):
        '''
        Functie care ruleaza programul propriu-zis
        Input: - 
        Output: -
        '''
        print("""Autor: Dascalu Cosmin-Andrei, Specializarea Informatica Romana, Nivel licenta, an 1, grupa 212
        
Programul permite utilizatorului sa introduca, pe rand, o operatie aritmetica de baza, 
3 numere intregi, pozitive, reprezentand bazele de numeratie ale celor 2 numere, 
respectiv baza de numeratie in care se va efectua calculul, cat si cele 2 numere in bazele date.
Toate datele de intrare se valideaza! 
""")
        while True: 
            # Citirea operatiei aritmetice: 
            operatie = input("\n--Introduceti o operatie aritmetica de baza: +, -, *, /:  ") 
            try: 
                self.__serviceNumere._validatorNumar.valideaza_operatie_input(operatie)
            except ValidError as ve: 
                print("Valid Error: ", str(ve))
                continue 
            
            # Citirea bazelor de numeratie:
            print("--Introduceti 3 numere intregi, ce apartin {2, 3, ..., 10, 16} pentru cele 3 baze:  ")
            try: 
                baza_numarA = input("Introduceti baza primului numar:  ")
                self.__serviceNumere._validatorNumar.valideaza_baza(baza_numarA)
            except ValidError as ve: 
                print("Valid Error: ", str(ve), "Baza trebuie sa apartina multimii {2, 3, ..., 10, 16}!\n")
                continue 
            
            try: 
                baza_numarB = input("Introduceti baza celui de-al doilea numar:  ")
                self.__serviceNumere._validatorNumar.valideaza_baza(baza_numarB)
            except ValidError as ve: 
                print("Valid Error: ", str(ve), "Baza trebuie sa apartina multimii {2, 3, ..., 10, 16}!\n")
                continue 
            
            try: 
                baza_calcul = input("Introduceti baza in care doriti sa fie efectuat calculul:  ")
                self.__serviceNumere._validatorNumar.valideaza_baza(baza_calcul)
            except ValidError as ve: 
                print("Valid Error: ", str(ve), "Baza trebuie sa apartina multimii {2, 3, ..., 10, 16}!\n")
                continue  

            # Citirea celor doua numere: 
            print("--Introduceti 2 numere intregi:  ")
            try: 
                mesaj = "Introduceti primul numar, in baza " + baza_numarA + ":  "
                numarA = input(mesaj)
                numarA = numarA.upper()  # Capitalizam numarul 
                self.__serviceNumere._validatorNumar.valideaza_numar(numarA, baza_numarA)
            except ValidError as ve: 
                print("Valid Error: ", str(ve), " Numarul trebuie sa fie in baza ", baza_numarA, "!\n", sep='')
                continue 
                
            try: 
                mesaj = "Introduceti al doilea numar, in baza " + baza_numarB + ":  "
                numarB = input(mesaj)
                numarB = numarB.upper()  # Capitalizam numarul 
                self.__serviceNumere._validatorNumar.valideaza_numar(numarB, baza_numarB)
            except ValidError as ve: 
                print("Valid Error: ", str(ve), " Numarul trebuie sa fie in baza ", baza_numarB, "!\n", sep='')
                continue 

            # "Impachetam" parametrii
            params = numarA, numarB, int(baza_numarA), int(baza_numarB), int(baza_calcul)
            try: 
                self.__comenzi[operatie](params)
            except RepoError as re: 
                print ("Repo Error: ", str(re))
