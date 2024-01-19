def user():
    import mysql.connector as sqlcon
    mycon=sqlcon.connect(host='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
    cursor=mycon.cursor()
    
    while True:
        ans = int(input('''1. First time user
2. Previous user
Please select one of the above options: '''))
        if ans == 1:
            while True:
                count = 0
                userid = input("Enter a UserID: ")
                cursor.execute("select userid from user where userid ='{}'".format(userid))
                data = cursor.fetchall()
                count = cursor.rowcount
                if count == 0:
                    print("UserID accepted.")
                    break
                else:
                    print("That UserID is already taken. Please try again.")
                    continue
                pwd = input("Enter a password: ")
                cursor.execute("insert into user values ('{}', '{}')".format(userid,
                pwd))
                mycon.commit()
                while True:
                    pwd2 = input("Please enter your password again for verification: ")
                    if pwd == pwd2:
                        print("Registered User.")
                        break
                    else:
                        print("That was incorrect. Please try again.")
        elif ans == 2:
            while True:
                userid = input("Enter your UserID: ")
                pwd = input("Enter your password: ")
                cursor.execute("select * from user where userid = '{}' and pwd = '{}'".format(userid, pwd))
                data = cursor.fetchall()
                count = cursor.rowcount
                if count == 0:
                    print("Incorrect UserID or Password. Please try again.")
                else:
                    print("Successfully logged in.")
                    break
        else:
            print("That was an invalid option. Please enter again.")
        return userid
