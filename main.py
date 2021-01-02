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
        while login_status == True:
            print('\n\t\t  -LOGIN as ADMIN-')
            print('\t\t  Hi -', data_login[1])
            menuInput = sadmin.menu()

            #tambah user
            if menuInput == 1:
                os.system('cls')
                sql_execute(sadmin.add_user())
                sadmin.initiate_userBalance()
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

            #logout
            elif menuInput == 0:
                os.system('cls')
                login_status = False
                del sadmin
                print('mencoba log out...')
                time.sleep(1)
                os.system('cls')
                continue

    elif loginn.get_role() == 2:
        myUser = controllerCustomer.user(username, password, loginn.get_role())
        myUser.set_userID()
        myUser.set_userBalance()
        while login_status == True:
            print('\t\t  -LOGIN as Customer-')
            print('\n\t Hi {} selamat datang di aplikasi tiketin'.format(data_login[1]))
            print('\t\t user saldo : {}'.format(myUser.user_balance))

            userMenu = myUser.menu()
            #menampilkan jadwal
            if(userMenu == 1):
                os.system('cls')
                print(permisi.get_schedules_all())
                time.sleep(1)
                os.system('cls')

            #menampilkan topping
            elif(userMenu == 2):
                os.system('cls')
                print(permisi.get_topping_data())
                time.sleep(1)
                os.system('cls')

            #pemesanan tiket    
            elif(userMenu == 3):
                os.system('cls')
                sql_execute(myUser.boking(permisi.get_schedules_today()))
                time.sleep(1)
                os.system('cls')

            #topup saldo
            elif userMenu == 4:
                os.system('cls')
                myUser.topUp()
                time.sleep(1)
                os.system('cls')

            #olah akun
            elif userMenu == 5:
                back = False
                os.system('cls')
                while back == False:
                    olahmenu = myUser.olahAkun_menu(permisi.get_personalData(myUser.user_id))
                    if olahmenu == 1:
                        os.system('cls')
                        ubah = 'name'
                        myUser.ubahData(ubah, permisi.temporary_data[0][3])
                        time.sleep(1)
                        os.system('cls')

                    elif olahmenu == 2:
                        os.system('cls')
                        ubah = 'username'
                        myUser.ubahData(ubah, permisi.temporary_data[0][3])
                        time.sleep(1)
                        os.system('cls')

                    elif olahmenu == 3:
                        os.system('cls')
                        ubah = 'password'
                        myUser.ubahData(ubah, permisi.temporary_data[0][3])
                        time.sleep(1)
                        os.system('cls')
                        
                    elif olahmenu == 4:
                        os.system('cls')
                        ubah = 'contact'
                        myUser.ubahData(ubah, permisi.temporary_data[0][3])
                        time.sleep(1)
                        os.system('cls')
                        
                    elif olahmenu == 5:
                        os.system('cls')
                        ubah = 'address'
                        myUser.ubahData(ubah, permisi.temporary_data[0][3])
                        time.sleep(1)
                        os.system('cls')
                        
                    elif olahmenu == 0:
                        back = True
                os.system('cls')

            #logout
            elif userMenu == 0:
                os.system('cls')
                login_status = False
                del myUser
                print('mencoba log out...')
                time.sleep(1)
                os.system('cls')
                continue

    elif loginn.get_role() == 3:
        myOp = controllerOperator.op(username, password, loginn.get_role())
        while login_status == True:
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
                os.system('cls')
                #print(permisi.get_user_balances())
                sql_execute(myOp.add_amount(permisi.get_user_balances()))
                time.sleep(1)
                os.system('cls')

            #logout
            elif operatorMenu == 0:
                os.system('cls')
                login_status = False
                print('mencoba log out...')
                time.sleep(1)
                os.system('cls')
                continue
    else:
        print('user tidak memiliki role')
