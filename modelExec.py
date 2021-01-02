from os import read
import mConnection
from mConnection import cursor
from prettytable import PrettyTable

def sql_execute(temporary):
    if temporary !=None:
        cursor.execute(temporary[0], temporary[1])
        mConnection.db.commit()
        print('Eksekusi Sukses')
    else:
        print('esekusi gagal')