from os import read

import mConnection
from datetime import date

from mConnection import cursor
from prettytable import PrettyTable
from modelLogin import login

from random import randint
import mRandomCode
import modelPermission

cusLog = []


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
    def boking(schedule_now, topping):
        ulang = True
        print(schedule_now)
        getStudio = ''
        kodeTransact = mRandomCode.randomTransaction(10);
        kodeTicket = mRandomCode.randomTransaction(10);
        dateNow = date.today().strftime("%d/%m/%Y")
        toppingID = 0

        permit = modelPermission.permission(0)

        print("Kode Transaksi\t : TR-", kodeTransact)
        print("Kode Tiket\t : TK-", kodeTicket)
        print("Tanggal Order\t :", dateNow)
        print("ID Customer\t :", cusLog[0])
        print("Nama Customer\t :", cusLog[1])
        scheduleID = int(input("Masukkan ID Jadwal : "))

        for i in range(len(permit.temporary_data)):
            for getStudd in permit.temporary_data[i]:
                if (scheduleID in permit.temporary_data[i]):
                    getStudio = permit.temporary_data[i][5]

        while ulang == True:
            konfirmasi = input("Mau tambah snack / lainnya ? (y/n) :")
            if(konfirmasi == 'y' or konfirmasi == 'Y'):
                print(topping)
                toppingID = int(input("Masukkan ID Topping :"))
                ulang = False
            elif(konfirmasi == 'n' or konfirmasi == 'N'):
                ulang = False
            else:
                ulang = True
        print(permit.get_chairs_free(getStudio))

        chairID = int(input("Masukkan ID Pilihan Kursi :"))
        # ============================================================
        cmdInsert = '''INSERT INTO transactions (code_transaction, order_date, operator_id, customer_id, ticket_code, topping_id, schedule_id) VALUES (%s, 'now()', %s, %s, %s, %s, %s)'''
        valInsert = (kodeTransact, '', cusLog[0], kodeTicket, toppingID, scheduleID)
        cursor.execute(cmdInsert, valInsert)
        mConnection.db.commit()
        # ============================================================
        cmdInserts = '''INSERT INTO tickets (code_ticket, chair_id, price) VALUES (%s,%s,%s)'''
        valInserts = (kodeTicket, chairID, 40000)
        cursor.execute(cmdInserts, valInserts)
        mConnection.db.commit()
        # ============================================================
        cmdUpdate = '''UPDATE chairs SET status = 1 WHERE id_chair = %s'''
        valUpdate = (chairID,)
        executed = (cmdUpdate, valUpdate)

        return executed