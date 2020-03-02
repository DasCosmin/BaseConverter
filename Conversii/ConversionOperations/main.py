'''
@author: Dascalu Cosmin-Andrei
'''

from domeniu.entitati import Numar 
from valid.validatoare import Validator 
from teste.teste import Teste 
from infrastrctura.repos import Repo 
from business.services import ServiceNumere 
from prezentare.ui import Console 

teste = Teste()
teste.ruleaza_toate_testele()

repo = Repo() 
valid = Validator()

serviceNumere = ServiceNumere(repo, valid)

consola = Console(serviceNumere)

consola.runProcess()
