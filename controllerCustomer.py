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
    user_id = 0
    user_balance = 0
    def __init__(self, username, password, role):
        super().__init__(username, password, role)

    def set_userID(self):
        read = 'SELECT id_user FROM users WHERE username = %s AND password = %s'
        v = (self.username, self.password)
        cursor.execute(read,v)
        a = cursor.fetchone()
        self.user_id = a[0]

    def set_userBalance(self):
        read ='SELECT amount FROM user_balances WHERE id_user =%s'
        v =(self.user_id,)
        cursor.execute(read,v)
        a = cursor.fetchone()
        self.user_balance = a[0]

    def topUp(self):
        n = int(input('masukan jumlah saldo yang ingin anda tambahkan : '))
        self.user_balance +=n
        sql = 'UPDATE user_balances SET amount = %s WHERE id_user = %s'
        v = (self.user_balance, self.user_id,)
        cursor.execute(sql,v)
        mConnection.db.commit()

    @staticmethod
    def menu():
        print('\t\t'+'='*10+'MENU'+'='*10)
        print('\t\t1. Lihat Jadwal')
        print('\t\t2. Lihat Topping')
        print('\t\t3. Pesan Tiket')
        print('\t\t4. Top up saldo')
        print('\t\t5. Olah akun')
        print('\t\t0. logout')
        n = int(input('masukan pilihan : '))
        return n

    def boking(self, schedule_now):
        hargaTotal = 40000
        print(schedule_now)
        getStudio = ''
        kodeTransact = mRandomCode.randomTransaction(5);
        kodeTicket = mRandomCode.randomTransaction(5);
        dateNow = date.today().strftime("%d/%m/%Y")
        toppingID = 0

        permit = modelPermission.permission(0)
        toping = modelPermission.permission(0)

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

        print(toping.get_topping_data())
        toppingID = int(input("Masukkan ID Topping :"))
        topping_harga = toping.temporary_data[0][2]
        print(topping_harga)
        hargaTotal += int(topping_harga)
        print(hargaTotal)

        print(permit.get_chairs_free(getStudio))

        chairID = int(input("Masukkan ID Pilihan Kursi :"))

        #konfirmasi pembelian
        konfirmasiPembelian = input('apakah anda yakin ingin melanjutkan proses transaksi (y/n) : ').upper()
        if konfirmasiPembelian == 'Y':
            if self.user_balance < hargaTotal:
                print('saldo user tidak mencukupi untuk melakukan transaksi')
            else:
                #=============================================================
                self.user_balance -= hargaTotal
                sql = 'UPDATE user_balances SET amount = %s WHERE id_user = %s'
                v = (self.user_balance, self.user_id,)
                cursor.execute(sql,v)
                mConnection.db.commit()
                # ============================================================
                cmdInsert = '''INSERT INTO transactions (code_transaction, order_date, operator_id, customer_id, ticket_code, topping_id, schedule_id) VALUES (%s, NOW(), %s, %s, %s, %s, %s)'''
                valInsert = (kodeTransact, '', cusLog[0], kodeTicket, toppingID, scheduleID)
                cursor.execute(cmdInsert, valInsert)
                mConnection.db.commit()
                # ============================================================
                cmdInserts = '''INSERT INTO tickets (code_ticket, chair_id, price) VALUES (%s,%s,%s)'''
                valInserts = (kodeTicket, chairID, hargaTotal)
                cursor.execute(cmdInserts, valInserts)
                mConnection.db.commit()
                # ============================================================
                cmdUpdate = '''UPDATE chairs SET status = 1 WHERE id_chair = %s'''
                valUpdate = (chairID,)
                executed = (cmdUpdate, valUpdate)

                kodeTransact = mRandomCode.randomTransaction(10);
                kodeTicket = mRandomCode.randomTransaction(10);

                return executed

        elif konfirmasiPembelian == 'N':
            print('transaksi dibatalkan')



    @staticmethod
    def olahAkun_menu(userData):
        print(userData)
        print('\t\t1. ubah nama')
        print('\t\t2. ubah username')
        print('\t\t3. ubah password')
        print('\t\t4. ubah contact')
        print('\t\t5. ubah address')
        print('\t\t0. kembali')
        n = int(input('masukan pilihan : '))
        return n

    def ubahData(self, ubah, konfirm):
        inputan = None
        if ubah == 'password':
            konfirmator = input('masukan password lama : ')
            if konfirmator == konfirm:
                inputan = input('masukan password baru : ')
            else :
                print('\npassword yang anda masukan salah')
        else:
            inputan = input('masukan '+ubah+' baru yang anda inginkan :')

        if inputan != None:
            sql = 'UPDATE users SET {} = %s WHERE id_user = %s'.format(ubah)
            val = (inputan, self.user_id,)
            cursor.execute(sql, val)
            mConnection.db.commit()
            print('\n berhasil mengubah data')
        else:
            print('\nanda belum melakukan input data')

