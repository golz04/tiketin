import os
import time

import modelPermission
import modelLogin
import controllerAdmin
import controllerCustomer
import controllerOperator

from modelExec import sql_execute

permisi = modelPermission.permission(0)
login_status = False
data_login = []
time.sleep(1)
os.system('cls')

while True:
    print('=+='*20)
    print('\t\t\t-LOGIN-')
    username = input('\t\tusername : ')
    password = input('\t\tpassword : ')
    print('=+='*20)
    permisi.get_users_data()
    for i in range(len(permisi.temporary_data)):
        if username in permisi.temporary_data[i]:
            if password in permisi.temporary_data[i]:
                data_login = permisi.temporary_data[i]
                controllerCustomer.cusLog = permisi.temporary_data[i]
                controllerOperator.opLog = permisi.temporary_data[i]
                login_status = True
                get_role = permisi.temporary_data[i][7]
                break
    if login_status == True:
        break
    else:
        print('username / password salah')
        time.sleep(1.5)
        os.system('cls')

permisi.set_role_id(get_role)
loginn = modelLogin.login(username, password, permisi.role_id)
time.sleep(1)
os.system('cls')

if loginn.get_role() == 1:
    sadmin = controllerAdmin.admin(username, password, loginn.get_role())
    while True:
        print('\n\t\t  -LOGIN as ADMIN-')
        print('\t\t  Hi -', data_login[1])
        menuInput = sadmin.menu()

        #tambah user
        if menuInput == 1:
            os.system('cls')
            sql_execute(sadmin.add_user())
            time.sleep(1)
            os.system('cls')

        #tambah film
        elif menuInput == 2:
            os.system('cls')
            sql_execute(sadmin.add_movie(permisi.get_genres_data(), permisi.get_companies_data()))
            time.sleep(1)
            os.system('cls')

        #tambah jadwal
        elif menuInput == 3:
            os.system('cls')
            sql_execute(sadmin.add_schedule(permisi.get_movies_data(), permisi.get_studio_data()))
            time.sleep(1)
            os.system('cls')

        #tambah topping
        elif menuInput == 4:
            os.system('cls')
            sql_execute(sadmin.add_topping())
            time.sleep(1)
            os.system('cls')

        #hapus user
        elif menuInput == 5:
            os.system('cls')
            sql_execute(sadmin.delete_user(permisi.get_users_data()))
            time.sleep(1)
            os.system('cls')

        #hapus film
        elif menuInput == 6 :
            os.system('cls')
            sql_execute(sadmin.delete_movie(permisi.get_movies_data()))
            time.sleep(1)
            os.system('cls')

        #hapus jadwal
        elif menuInput == 7 :
            os.system('cls')
            sql_execute(sadmin.delete_schedule(permisi.get_schedules_data()))
            time.sleep(1)
            os.system('cls')

        #hapus topping
        elif menuInput == 8 :
            os.system('cls')
            sql_execute(sadmin.delete_topping(permisi.get_topping_data()))
            time.sleep(1)
            os.system('cls')

elif loginn.get_role() == 2:
    myUser = controllerCustomer.user(username, password, loginn.get_role())
    while True:
        print('\n\t\t  -LOGIN as Customer-')
        print('\t\t  Hi -', data_login[1])

        userMenu = myUser.menu()
        if(userMenu == 1):
            os.system('cls')
            print(permisi.get_schedules_all())
            time.sleep(1)
            os.system('cls')
        elif(userMenu == 2):
            os.system('cls')
            print(permisi.get_topping_data())
            time.sleep(1)
            os.system('cls')
        elif(userMenu == 3):
            os.system('cls')
            sql_execute(myUser.boking(permisi.get_schedules_today(), permisi.get_topping_data()))
            time.sleep(1)
            os.system('cls')
elif loginn.get_role() == 3:
    myOp = controllerOperator.op(username, password, loginn.get_role())
    while True:
        print()
        print('\n\t\t  -LOGIN as Operator-')
        print('\t\t  Hi -', data_login[1])

        operatorMenu = myOp.menu()
        if(operatorMenu == 1):
            os.system('cls')
            print(permisi.get_ticket_pending())
            time.sleep(1)
            os.system('cls')
        elif(operatorMenu == 2):
            os.system('cls')
            sql_execute(myOp.confirm_ticket(permisi.get_ticket_pending()))
            time.sleep(1)
            os.system('cls')
        elif(operatorMenu == 3):
            os.system('cls')
            print(permisi.get_ticket_done())
            time.sleep(1)
            os.system('cls')
        elif(operatorMenu == 4):
            os.system('cls')
            sql_execute(myOp.add_movie(permisi.get_genres_data(), permisi.get_companies_data()))
            print(permisi.get_movies_data())
            time.sleep(1)
            os.system('cls')
        elif(operatorMenu == 5):
            os.system('cls')
            sql_execute(myOp.add_schedule(permisi.get_movies_data(), permisi.get_studio_data()))
            print(permisi.get_schedules_all())
            time.sleep(1)
            os.system('cls')
        elif(operatorMenu == 6):
            os.system('cls')
            sql_execute(sadmin.add_topping())
            print(permisi.get_topping_data())
            time.sleep(1)
            os.system('cls')
        elif(operatorMenu == 7):
            print("Belum")
else:
    print('user tidak memiliki role')
