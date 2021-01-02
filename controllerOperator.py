from os import read

import mConnection

from mConnection import cursor
from prettytable import PrettyTable
from modelLogin import login

import modelPermission

opLog = []

class op(login):
    user_balance = 0
    def __init__(self, username, password, role):
        super().__init__(username, password, role)

    @staticmethod
    def menu():
        print('\t\t'+'='*10+'input data'+'='*10)
        print('\t\t1. Cek Ticket Pending')
        print('\t\t2. Konfirmasi Ticket Pending')
        print('\t\t3. Cek Ticket Terselesaikan')
        print('\t\t4. add movie')
        print('\t\t5. add schedule')
        print('\t\t6. add topping')
        print('\t\t7. Topup saldo')
        print('\t\t0. logout')
        n = int(input('masukan pilihan : '))
        return n

    @staticmethod
    def confirm_ticket(data_tiket):
        print(data_tiket)
        transactID = input('masukkan ID transaksi yang mau di konfirmasi : ')
        cmdUpdate = 'UPDATE transactions SET operator_id = %s WHERE code_transaction = %s'
        valUpdate = (opLog[0], transactID)
        execute = (cmdUpdate, valUpdate)
        return execute

    @staticmethod
    def add_schedule(movie_data, studio_data):
        tanggal = int(input('masukan tanggal (numerik): '))
        bulan = int(input('masukan bulan (numerik): '))
        tahun = int(input('masukan tanggal (numerik): '))
        date = '{}-{}-{}'.format(tahun, bulan, tanggal)
        startInput = input('masukan jam film mulai(jam:menit) : ')
        start = '{}:00'.format(startInput)
        endInput = input('masukan jam film selesai(jam:menit) : ')
        end = '{}:00'.format(endInput)
        print(movie_data)
        film = int(input('masukan id film : '))
        print(studio_data)
        studio = int(input('masukan id studio : '))
        sql = 'INSERT INTO schedules (id_schedule, date_schedule, start, end, film_code, id_studio) VALUES (NULL, %s, %s, %s, %s, %s)'
        val = (date, start, end, film, studio)
        sqlQuery = (sql, val)
        return sqlQuery

    @staticmethod
    def add_movie(genre_data, company_data):
        judul = input('masukan judul film : ')
        print(genre_data)
        genre = int(input('masukan id genre : '))
        print(company_data)
        company = int(input('masukan id company : '))
        sql = 'INSERT INTO movies (code_film, title, genre_id, company_id) VALUES (NULL, %s, %s, %s)'
        val = (judul, genre, company)
        sqlQuery = (sql, val)
        return sqlQuery
    
    @staticmethod
    def add_topping():
        topping = input('masukan nama snack/minuman : ')
        harga = int(input('masukan harga : '))
        sql = 'INSERT INTO toppings (id_topping, topping_name, price) VALUES (NULL, %s, %s)'
        val = (topping, harga)
        sqlQuery = (sql, val)
        return sqlQuery

    def add_amount(self, balances):
        print(balances)
        idBalance = int(input("Masukkan ID saldo yang ingin ditambahkan  : "))
        banyakSaldo = int(input("Masukkan total saldo yang ingin ditambahkan : "))

        read ='SELECT amount FROM user_balances WHERE id_balance =%s'
        v =(idBalance,)
        cursor.execute(read,v)
        a = cursor.fetchone()
        self.user_balance = a[0]

        total = self.user_balance + banyakSaldo
        sql = 'UPDATE user_balances SET amount = %s WHERE id_balance = %s'
        v = (total, idBalance,)
        execute = (sql, v)
        return execute