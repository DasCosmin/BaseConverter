'''
@author: Dascalu Cosmin-Andrei
'''

from domeniu.entitati import Numar
from infrastrctura.repos import Repo
from erori.exceptii import RepoError, ValidError
from business.services import ServiceNumere
from valid.validatoare import Validator
class Teste(object):
    
    def __init__(self):
        '''
        Functie de tip constructor care construieste un obiect de tip Teste
        Input: -
        Output: - 
        '''
        pass 

    def __test_creeaza_numar(self):
        '''
        Functie de tip test care verifica daca un obiect de tip Numar a fost creat cu succes
        '''
        numar = Numar('120', 3)
        assert numar.get_valoare() == '120'
        assert numar.get_baza() == 3
        numar.set_valoare('122')
        assert numar.get_valoare() == '122'
        numar.set_baza(4)
        assert numar.get_baza() == 4

    def __test_repo_add(self):
        '''
        Functie de tip test care verifica daca adunarea a doua numere intr-o anumita baza a fost realizata cu succes
        '''
        repo = Repo()
        numarA = Numar('120', 3)
        numarB = Numar('102', 3)
        rezultat = repo.add(numarA, numarB, 3)
        assert rezultat.get_valoare() == '222'
        assert rezultat.get_baza() == 3
        
        numarA = Numar('120', 3)
        numarB = Numar('110', 3)
        rezultat = repo.add(numarA, numarB, 3)
        assert rezultat.get_valoare() == '1000'
        
        numarA = Numar('2A', 16)
        numarB = Numar('14', 16)
        rezultat = repo.add(numarA, numarB, 16)
        assert rezultat.get_valoare() == '3E'
        assert rezultat.get_baza() == 16
        
        numarA = Numar('2A', 16)
        numarB = Numar('17', 16)
        rezultat = repo.add(numarA, numarB, 16)
        assert rezultat.get_valoare() == '41'
        
        numarA = Numar('1235', 10)
        numarB = Numar('0', 10)
        rezultat = repo.add(numarA, numarB, 10)
        assert rezultat.get_valoare() == '1235'
        assert rezultat.get_baza() == 10
        
        numarA = Numar('1235', 10)
        numarB = Numar('65', 10)
        rezultat = repo.add(numarA, numarB, 10)
        assert rezultat.get_valoare() == '1300'

    def __test_repo_multiply(self):
        '''
        Functie de tip test care verifica daca inmultirea a doua numere intr-o anumita baza a fost realizata cu succes
        '''
        repo = Repo()
        numarA = Numar('120', 6)
        numarB = Numar('2', 6)
        rezultat = repo.multiply(numarA, numarB, 6)
        assert rezultat.get_valoare() == '240'
        assert rezultat.get_baza() == 6
        
        numarA = Numar('120', 6)
        numarB = Numar('3', 6)
        rezultat = repo.multiply(numarA, numarB, 6)
        assert rezultat.get_valoare() == '400' 
        
        numarA = Numar('52', 16)
        numarB = Numar('3', 16)
        rezultat = repo.multiply(numarA, numarB, 16)
        assert rezultat.get_valoare() == 'F6'
        
        numarA = Numar('57', 16)
        numarB = Numar('7', 16)
        rezultat = repo.multiply(numarA, numarB, 16)
        assert rezultat.get_valoare() == '261'
        
        numarA = Numar('130', 10)
        numarB = Numar('0', 10)
        rezultat = repo.multiply(numarA, numarB, 10)
        assert rezultat.get_valoare() == '0'

    def __test_repo_substract(self):
        '''
        Functie de tip test care verifica daca scaderea a doua numere intr-o anumita baza a fost realizata cu succes
        '''
        repo = Repo()
        numarA = Numar('54', 6)
        numarB = Numar('32', 6)
        rezultat = repo.substract(numarA, numarB, 6)
        assert rezultat.get_valoare() == '22'
        assert rezultat.get_baza() == 6
        
        numarA = Numar('54', 6)
        numarB = Numar('35', 6)
        rezultat = repo.substract(numarA, numarB, 6)
        assert rezultat.get_valoare() == '15'
        
        numarA = Numar('54', 6)
        numarB = Numar('45', 6)
        rezultat = repo.substract(numarA, numarB, 6)
        assert rezultat.get_valoare() == '5'
        
        numarA = Numar('154', 6)
        numarB = Numar('55', 6)
        rezultat = repo.substract(numarA, numarB, 6)
        assert rezultat.get_valoare() == '55'
        
        numarA = Numar('AB', 16)
        numarB = Numar('3C', 16)
        rezultat = repo.substract(numarA, numarB, 16)
        assert rezultat.get_valoare() == '6F'
        assert rezultat.get_baza() == 16

        numarA = Numar('127', 10)
        numarB = Numar('30', 10)
        rezultat = repo.substract(numarA, numarB, 10)
        assert rezultat.get_valoare() == '97'
        assert rezultat.get_baza() == 10 
        
        numarA = Numar('13', 10)
        numarB = Numar('13', 10)
        rezultat = repo.substract(numarA, numarB, 10)
        assert rezultat.get_valoare() == '0'
        assert rezultat.get_baza() == 10

    def __test_repo_divide(self):
        '''
        Functie de tip test care verifica daca impartirea a doua numere intr-o anumita baza a fost realizata cu succes
        '''
        repo = Repo()
        numarA = Numar('243', 5)
        numarB = Numar('3', 5)
        cat, rest = repo.divide(numarA, numarB, 5)
        assert cat.get_valoare() == '44'
        assert cat.get_baza() == 5 
        assert rest.get_valoare() == '1'
        assert rest.get_baza() == 5 
        
        numarA = Numar('8140', 10)
        numarB = Numar('3', 10)
        cat, rest = repo.divide(numarA, numarB, 10)
        assert cat.get_valoare() == '2713'
        assert cat.get_baza() == 10
        assert rest.get_valoare() == '1'
        assert rest.get_baza() == 10
        
        numarA = Numar('A5', 16)
        numarB = Numar('D', 16)
        cat, rest = repo.divide(numarA, numarB, 16)
        assert cat.get_valoare() == 'C'
        assert cat.get_baza() == 16
        assert rest.get_valoare() == '9'
        assert rest.get_baza() == 16

    def __test_repo_subtitutie(self):
        '''
        Functie de tip test care verifica daca conversia prin metoda subtitutiei a unui numar a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('1010', 2)
        rezultat = repo.convert_subtitutie(numar)
        assert rezultat.get_valoare() == '10'
        assert rezultat.get_baza() == 10 
        
        numar = Numar('153', 6)
        rezultat = repo.convert_subtitutie(numar)
        assert rezultat.get_valoare() == '69'
        
        numar = Numar('A3', 16)
        rezultat = repo.convert_subtitutie(numar)
        assert rezultat.get_valoare() == '163'
        
        numar = Numar('132', 10)
        try: 
            rezultat = repo.convert_subtitutie(numar)
            assert False 
        except RepoError as re: 
            assert str(re) == "Baza nevalida!\n"

    def __test_repo_impartiri_succesive(self):
        '''
        Functie test care verifica daca un numar a fost convertit cu succes prin imparitiri succesive
        '''
        repo = Repo()
        numar = Numar('34', 10)
        rezultat = repo.convert_impartiri_succesive(numar, 2)
        assert rezultat.get_valoare() == '100010'
        assert rezultat.get_baza() == 2 
        
        numar = Numar('63', 10)
        rezultat = repo.convert_impartiri_succesive(numar, 16)
        assert rezultat.get_valoare() == '3F'
        assert rezultat.get_baza() == 16
        
        numar = Numar('43', 10)
        rezultat = repo.convert_impartiri_succesive(numar, 3)
        assert rezultat.get_valoare() == '1121'
        assert rezultat.get_baza() == 3
        
        numar = Numar('17', 9)
        try: 
            rezultat = repo.convert_impartiri_succesive(numar, 3)
            assert False 
        except RepoError as re: 
            assert str(re) == "Baza nevalida!\n"

    def __test_repo_convert_to_another_base(self):
        '''
        Functie test care verifica daca un numar este convertit dintr-o baza in alta cu succes
        '''
        repo = Repo()
        numar = Numar('120', 3)
        rezultat = repo.convert_to_another_base(numar, 7)
        assert rezultat.get_valoare() == '21'
        assert rezultat.get_baza() == 7
        
        numar = Numar('A7', 16)
        rezultat = repo.convert_to_another_base(numar, 5)
        assert rezultat.get_valoare() == '1132'
        assert rezultat.get_baza() == 5
        
        numar = Numar('35', 10)
        rezultat = repo.convert_to_another_base(numar, 2)
        assert rezultat.get_valoare() == '100011'
        assert rezultat.get_baza() == 2 
        
        numar = Numar('163', 9)
        rezultat = repo.convert_to_another_base(numar, 10)
        assert rezultat.get_valoare() == '138'
        assert rezultat.get_baza() == 10 
        
        numar = Numar('150', 10)
        rezultat = repo.convert_to_another_base(numar, 10)
        assert rezultat.get_valoare() == '150'
        assert rezultat.get_baza() == 10
        
        numar = Numar('1EF', 16)
        rezultat = repo.convert_to_another_base(numar, 2)
        assert rezultat.get_valoare() == '111101111'
        assert rezultat.get_baza() == 2 
        
        numar = Numar('10101011', 2)
        rezultat = repo.convert_to_another_base(numar, 8)
        assert rezultat.get_valoare() == '253'
        assert rezultat.get_baza() == 8
 
    def __test_repo_convert_base4_to_base2(self):
        '''
        Functie care verifica daca conversia unui numar din baza 4 in baza 2 a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('31', 4)
        rezultat = repo.convert_base4_to_base2(numar)
        assert rezultat.get_valoare() == '1101'
        assert rezultat.get_baza() == 2
        
        numar = Numar('1203', 4)
        rezultat = repo.convert_base4_to_base2(numar)
        assert rezultat.get_valoare() == '1100011'
        
        numar = Numar('21', 6)
        try: 
            rezultat = repo.convert_base4_to_base2(numar)
            assert False 
        except RepoError as re:
            assert str(re) == "Baza nevalida!\n"
 
    def __test_repo_convert_base8_to_base2(self):
        '''
        Functie care verifica daca conversia unui numar din baza 8 in baza 2 a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('1430', 8)
        rezultat = repo.convert_base8_to_base2(numar)
        assert rezultat.get_valoare() == '1100011000'
        assert rezultat.get_baza() == 2
       
        numar = Numar('7256', 8) 
        rezultat = repo.convert_base8_to_base2(numar)
        assert rezultat.get_valoare() == '111010101110'
        
        numar = Numar('23', 7)
        try: 
            rezultat = repo.convert_base8_to_base2(numar)
            assert False 
        except RepoError as re:
            assert str(re) == "Baza nevalida!\n"
 
    def __test_repo_convert_base16_to_base2(self):
        '''
        Functie care verifica daca conversia unui numar din baza 16 in baza 2 a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('25AF', 16)
        rezultat = repo.convert_base16_to_base2(numar)
        assert rezultat.get_valoare() == '10010110101111'
        assert rezultat.get_baza() == 2 
        
        numar = Numar('60BC', 16)
        rezultat = repo.convert_base16_to_base2(numar)
        assert rezultat.get_valoare() == '110000010111100'
        
        numar = Numar('D179', 16)
        rezultat = repo.convert_base16_to_base2(numar)
        assert rezultat.get_valoare() == '1101000101111001'
        
        numar = Numar('348E', 16)
        rezultat = repo.convert_base16_to_base2(numar)
        assert rezultat.get_valoare() == '11010010001110'
        
        numar = Numar('63', 10)
        try:
            rezultat = repo.convert_base16_to_base2(numar)
            assert False 
        except RepoError as re: 
            assert str(re) == "Baza nevalida!\n"

    def __test_repo_convert_base2_to_base4(self):
        '''
        Functie care verifica daca conversia unui numar din baza 2 in baza 4 a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('111000', 2)
        rezultat = repo.convert_base2_to_base4(numar)
        assert rezultat.get_valoare() == '320'
        assert rezultat.get_baza() == 4
        
        numar = Numar('101', 2)
        rezultat = repo.convert_base2_to_base4(numar)
        assert rezultat.get_valoare() == '11'
        
        numar = Numar('123', 5)
        try: 
            rezultat = repo.convert_base2_to_base4(numar)
            assert False 
        except RepoError as re: 
            assert str(re) == "Baza nevalida!\n"
         
    def __test_repo_convert_base2_to_base8(self):
        '''
        Functie care verifica daca conversia unui numar din baza 2 in baza 8 a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('101111011', 2)
        rezultat = repo.convert_base2_to_base8(numar)
        assert rezultat.get_valoare() == '573'
        assert rezultat.get_baza() == 8 
        
        numar = Numar('1110', 2)
        rezultat = repo.convert_base2_to_base8(numar)
        assert rezultat.get_valoare() == '16'
        
        numar = Numar('11000', 2)
        rezultat = repo.convert_base2_to_base8(numar)
        assert rezultat.get_valoare() == '30'
        
        numar = Numar('1101', 5)
        try: 
            rezultat = repo.convert_base2_to_base8(numar)
            assert False 
        except RepoError as re: 
            assert str(re) == "Baza nevalida!\n"
         
    def __test_repo_convert_base2_to_base16(self):
        '''
        Functie care verifica daca conversia unui numar din baza 2 in baza 16 a fost realizata cu succes
        '''
        repo = Repo()
        numar = Numar('101111110101', 2)
        rezultat = repo.convert_base2_to_base16(numar)
        assert rezultat.get_valoare() == 'BF5'
        assert rezultat.get_baza() == 16 
        
        numar = Numar('11100', 2)
        rezultat = repo.convert_base2_to_base16(numar)
        assert rezultat.get_valoare() == '1C'
        
        numar = Numar('101101', 2)
        rezultat = repo.convert_base2_to_base16(numar)
        assert rezultat.get_valoare() == '2D'
        
        numar = Numar('1001110', 2)
        rezultat = repo.convert_base2_to_base16(numar)
        assert rezultat.get_valoare() == '4E'
        
        numar = Numar('110001', 5)
        try: 
            rezultat = repo.convert_base2_to_base16(numar)
            assert False 
        except RepoError as re: 
            assert str(re) == "Baza nevalida!\n"
         
    def __test_service_add(self):
        '''
        Functie test care verifica daca adunarea a doua numere a fost realizata cu succes
        '''    
        repo = Repo()
        validator = Validator()
        serviceNumere = ServiceNumere(repo, validator)
        rezultat = serviceNumere.add('15', '47', 3, 8, 5)
        assert rezultat.get_valoare() == '142'
        assert rezultat.get_baza() == 5
        
        rezultat = serviceNumere.add('23', '47', 10, 10, 10)
        assert rezultat.get_valoare() == '70'
        assert rezultat.get_baza() == 10
        
        rezultat = serviceNumere.add('F5', '72', 16, 8, 2)
        assert rezultat.get_valoare() == '100101111'
        assert rezultat.get_baza() == 2
        
        rezultat = serviceNumere.add('37', '32', 9, 4, 6)
        assert rezultat.get_valoare() == '120'
        assert rezultat.get_baza() == 6
         
    def __test_service_multiply(self):
        '''
        Functie test care verifica daca inmultirea a doua numere a fost realizata cu succes
        '''     
        repo = Repo()
        validator = Validator()
        serviceNumere = ServiceNumere(repo, validator)
        rezultat = serviceNumere.multiply('137', '3', 8, 8, 8)
        assert rezultat.get_valoare() == '435'
        assert rezultat.get_baza() == 8 
        
        rezultat = serviceNumere.multiply('120', '5', 3, 7, 16)
        assert rezultat.get_valoare() == '4B'
        assert rezultat.get_baza() == 16
        
        rezultat = serviceNumere.multiply('120', '13', 10, 6, 10)
        assert rezultat.get_valoare() == '1080'
        assert rezultat.get_baza() == 10
        
        rezultat = serviceNumere.multiply('20', 'F', 10, 16, 16)
        assert rezultat.get_valoare() == '12C'
        assert rezultat.get_baza() == 16 
        
        try: 
            rezultat = serviceNumere.multiply('120', '3', 10, 4, 2)
            assert False 
        except RepoError as re: 
            assert str(re) == "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        
        try: 
            rezultat = serviceNumere.multiply('120', '15', 10, 6, 10)
            assert False
        except RepoError as re:  
            assert str(re) == "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        
        try: 
            rezultat = serviceNumere.multiply('20', 'F', 10, 16, 10)
            assert False 
        except RepoError as re:  
            assert str(re) == "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
         
    def __test_service_substract(self):
        '''
        Functie test care verifica daca scaderea a doua numere a fost realizata cu succes
        ''' 
        repo = Repo()
        validator = Validator()
        serviceNumere = ServiceNumere(repo, validator)
        rezultat = serviceNumere.substract('45', '7', 6, 8, 16)
        assert rezultat.get_valoare() == '16'
        assert rezultat.get_baza() == 16 
        
        rezultat = serviceNumere.substract('12', '5', 3, 5, 4)
        assert rezultat.get_valoare() == '0'
        assert rezultat.get_baza() == 4
        
        rezultat = serviceNumere.substract('10', '7', 10, 16, 2)
        assert rezultat.get_valoare() == '11'
        assert rezultat.get_baza() == 2
        
        rezultat = serviceNumere.substract('F', '7', 16, 8, 4)
        assert rezultat.get_valoare() == '20'
        assert rezultat.get_baza() == 4
        
        try: 
            rezultat = serviceNumere.substract('17', '17', 8, 9, 3)
            assert False 
        except RepoError as re: 
            assert str(re) == "Scadere negativa!\n"
            
        try: 
            rezultat = serviceNumere.substract('7', 'F', 8, 16, 4)
            assert False 
        except RepoError as re:  
            assert str(re) == "Scadere negativa!\n"
                 
    def __test_service_divide(self):
        '''
        Functie test care verifica daca impartirea a doua numere a fost realizata cu succes
        '''         
        repo = Repo()
        validator = Validator()
        serviceNumere = ServiceNumere(repo, validator)
        cat, rest = serviceNumere.divide('42', '3', 7, 4, 16)
        assert cat.get_valoare() == 'A'
        assert cat.get_baza() == 16
        assert rest.get_valoare() == '0'
        assert rest.get_baza() == 16

        cat, rest = serviceNumere.divide('10', '2', 3, 5, 4)
        assert cat.get_valoare() == '1'
        assert cat.get_baza() == 4
        assert rest.get_valoare() == '1'
        assert rest.get_baza() == 4 
        
        cat, rest = serviceNumere.divide('79B', '2', 16, 3, 16)
        assert cat.get_valoare() == '3CD'
        assert cat.get_baza() == 16
        assert rest.get_valoare() == '1'
        assert cat.get_baza() == 16
        
        try: 
            cat, rest = serviceNumere.divide('20', '8', 7, 9, 2)
            assert False 
        except RepoError as re: 
            assert str(re) == "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        
        try: 
            cat, rest = serviceNumere.divide('37E', '78', 16, 9, 16)
            assert False
        except RepoError as re: 
            assert str(re) == "Numar nevalid! Al doilea numar trebuie sa aiba o singura cifra!\n"
        
    def __test_validator_valideaza_numar(self):
        '''
        Functie de tip test care verifica daca un numar este validat cu succes
        '''  
        validator = Validator()
        validator.valideaza_numar('1234567890', '10')
        validator.valideaza_numar('2301', '4')
        validator.valideaza_numar('1AEF2B', '16') 
        try: 
            validator.valideaza_numar('2310 ', '4')
            assert False 
        except ValidError as ve: 
            assert str(ve) == "Numar nevalid!"
        
        try: 
            validator.valideaza_numar('2380a', '9')
            assert False 
        except ValidError as ve: 
            assert str(ve) == "Numar nevalid!"
        
        try: 
            validator.valideaza_numar("21073", '5')
            assert False 
        except ValidError as ve: 
            assert str(ve) == "Numar nevalid!"
                 
    def ruleaza_toate_testele(self):
        self.__test_creeaza_numar()
        self.__test_repo_add()
        self.__test_repo_multiply()
        self.__test_repo_substract()
        self.__test_repo_divide()
        self.__test_repo_subtitutie()
        self.__test_repo_impartiri_succesive()
        self.__test_repo_convert_to_another_base()
        self.__test_repo_convert_base4_to_base2()
        self.__test_repo_convert_base8_to_base2()
        self.__test_repo_convert_base16_to_base2()
        self.__test_repo_convert_base2_to_base4()
        self.__test_repo_convert_base2_to_base8()
        self.__test_repo_convert_base2_to_base16()
        self.__test_service_add()
        self.__test_service_multiply()
        self.__test_service_substract()
        self.__test_service_divide()
        self.__test_validator_valideaza_numar()
