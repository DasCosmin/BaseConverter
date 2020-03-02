'''
@author: Dascalu Cosmin-Andrei
'''

from domeniu.entitati import Numar
class ServiceNumere(object):
    
    def __init__(self, repoNumar, validatorNumar):
        '''
        Functie de tip constructor care construieste un obiect de tip ServiceNumere
        Input: repoNumar - obiect de tip Repo
               validatorNumar - obiect de tip Validator
        Output: -
        '''
        self.__repoNumar = repoNumar 
        self.__validatorNumar = validatorNumar
        self._validatorNumar = validatorNumar

    def add(self, valoare_numarA, valoare_numarB, baza_numarA, baza_numarB, baza_calcul):
        '''
        Functie care aduna doua numere intr-o anumita baza
        Input: valoare_numarA, valoare_numarB - string-uri
               baza_numarA, baza_NumarB, baza_calcul - numere intregi, pozitive
        Output: un obiect de tip Numar, reprezentand rezultatul calculului de adunare 
        '''
        numarA = Numar(valoare_numarA, baza_numarA)
        numarB = Numar(valoare_numarB, baza_numarB)
        # Convertim numerele la baza in care se va efectua calculul 
        numarA_convertit = self.__repoNumar.convert_to_another_base(numarA, baza_calcul)
        numarB_convertit = self.__repoNumar.convert_to_another_base(numarB, baza_calcul)
        # Efectuam adunarea in baza de calcul 
        return self.__repoNumar.add(numarA_convertit, numarB_convertit, baza_calcul)

    def multiply(self, valoare_numarA, valoare_numarB, baza_numarA, baza_numarB, baza_calcul):
        '''
        Functie care inmulteste doua numere intr-o anumita baza
        Input: valoare_numarA, valoare_numarB - string-uri
               baza_numarA, baza_NumarB, baza_calcul - numere intregi, pozitive
        Output: un obiect de tip Numar, reprezentand rezultatul calculului de inmultire
        Raises: Exception
            daca al doilea numar are mai mult de o cifra in baza de calcul -> "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        '''
        numarA = Numar(valoare_numarA, baza_numarA)
        numarB = Numar(valoare_numarB, baza_numarB)
        # Convertim numerele la baza in care se va efectua calculul 
        numarA_convertit = self.__repoNumar.convert_to_another_base(numarA, baza_calcul)
        numarB_convertit = self.__repoNumar.convert_to_another_base(numarB, baza_calcul)
        # Validam al doilea numar: el trebuie sa aiba o singura cifra 
        self.__validatorNumar.valideaza_operatie(numarA_convertit, numarB_convertit, operatie='*')
        # Efectuam inmultirea in baza de calcul
        return self.__repoNumar.multiply(numarA_convertit, numarB_convertit, baza_calcul)

    def substract(self, valoare_numarA, valoare_numarB, baza_numarA, baza_numarB, baza_calcul):
        '''
        Functie care scade doua numere intr-o anumita baza
        Input: valoare_numarA, valoare_numarB - string-uri
               baza_numarA, baza_NumarB, baza_calcul - numere intregi, pozitive
        Output: un obiect de tip Numar, reprezentand rezultatul calculului de scadere
        Raises: Exception
            daca primul numar este mai mic decat al doilea numar -> "Scadere negativa!\n"
        '''
        numarA = Numar(valoare_numarA, baza_numarA)
        numarB = Numar(valoare_numarB, baza_numarB)
        # Convertim numerele la baza in care se va efectua calculul 
        numarA_convertit = self.__repoNumar.convert_to_another_base(numarA, baza_calcul)
        numarB_convertit = self.__repoNumar.convert_to_another_base(numarB, baza_calcul)
        # Validam cele doua numere: primul numar trebuie sa fie mai mare decat al doilea numar (in baza de calcul)
        self.__validatorNumar.valideaza_operatie(numarA_convertit, numarB_convertit, operatie='-')
        # Efectuam scaderea in baza de calcul
        return self.__repoNumar.substract(numarA_convertit, numarB_convertit, baza_calcul)
    
    def divide(self, valoare_numarA, valoare_numarB, baza_numarA, baza_numarB, baza_calcul):
        '''
        Functie care imparte doua numere intr-o anumita baza
        Input: valoare_numarA, valoare_numarB - string-uri
               baza_numarA, baza_NumarB, baza_calcul - numere intregi, pozitive
        Output: doua obiecte de tip Numar, reprezentand catul si restul calcului de impartire
        Raises: Exception
            daca al doilea numar are mai mult de o cifra in baza de calcul -> "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        '''
        numarA = Numar(valoare_numarA, baza_numarA)
        numarB = Numar(valoare_numarB, baza_numarB)
        # Convertim numerele la baza in care se va efectua calculul 
        numarA_convertit = self.__repoNumar.convert_to_another_base(numarA, baza_calcul)
        numarB_convertit = self.__repoNumar.convert_to_another_base(numarB, baza_calcul)
        # Validam cel de-al doilea numar: el trebuie sa aiba o singura cifra 
        self.__validatorNumar.valideaza_operatie(numarA_convertit, numarB_convertit, operatie='/')
        # Efectuam impartirea in baza de calcul 
        return self.__repoNumar.divide(numarA_convertit, numarB_convertit, baza_calcul)
