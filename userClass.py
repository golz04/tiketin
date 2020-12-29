from os import read

import mConnection

from mConnection import cursor
from prettytable import PrettyTable
from modelLogin import login

class user(login):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)

    @staticmethod
    def menu():
        print('\t\t'+'='*8+'input data'+'='*8)
        print('\t\t1. See schedule movie')
        n = int(input('masukan pilihan : '))
        return n
        
# if __name__ == "__main__":
#     permisi = permission(1)
#     print(permisi.get_schedules_today())