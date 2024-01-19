def admin():
  
    import mysql.connector as sqlcon
    mycon = mysql.connect(host = 'localhost', user = 'root', password = 'poojitha', database = 'bus_reservation_system')
    cursor = mycon.cursor()
  
    while True:
        ans = int(input('''1. Login
Please press 1: '''))
      
        if ans == 1:
            while True:
                userid = input("Enter your UserID: ")
                pwd = input("Enter your password: ")
                cursor.execute("select * from admin where adminid = '{}' and password = '{}'".format(userid, pwd))
                data = cursor.fetchall()
                count = cursor.rowcount
              
                if count == 0:
                    print("Incorrect UserID or Password. Please try again.")
                  
                else:
                    print("Successfully logged in.")
                    break
                  
        else:
            print("That was an invalid option. Please try again.")
                
