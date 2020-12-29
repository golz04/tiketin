from os import read

import mConnection
from datetime import date

from mConnection import cursor
from prettytable import PrettyTable
from modelLogin import login

from random import randint
import mRandomCode

class user(login):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)

    @staticmethod
    def menu():
        print('\t\t'+'='*10+'input data'+'='*10)
        print('\t\t1. Lihat Jadwal')
        print('\t\t2. Lihat Topping')
        print('\t\t3. Pesan Tiket')
        n = int(input('masukan pilihan : '))
        return n

    @staticmethod
    def boking(schedule_now):
        print(schedule_now)
        kodeTransact = mRandomCode.randomTransaction(10);
        dateNow = date.today().strftime("%Y/%m/%d")
        print("Kode Transaksi :", kodeTransact)
        print("Tanggal Order :", dateNow)
        print("ID Customer :", maindata_login[0])
        print("Nama Customer :", data_login[1])

        a = int(input("asdas :"))



