def pay(userid, fr, to, no, date,fare):
    import time
    import sys
    from bus import Mail
    import mysql.connector as sqlcon

    mycon=sqlcon.connect(host='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
    cursor=mycon.cursor()
    
    while True:
        choice = int(input('''
1. Credit Card
2. Debit Card
Please choose your method of payment: '''))
        if choice == 1:
            print("The following details will be strictly confidential and not stored anywhere in the database.")
            name = input("Enter your name as on the card: ")
            card_no = input("Enter your card number: ")
            cvv = input("Enter your CVV number: ")
            data = 'P R O C E S S I N G . . .'
            for l in data:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.5)
            credit = 'Credit'
            cursor.execute("insert into paid values('{}', '{}', '{}','{}', '{}', '{}','{}')".format(name, fr, to, date, userid, fare, credit))
            mycon.commit()
            Mail.mail(userid, date)
            break
        
        elif choice == 2:
            print("The following details will be strictly confidential and not stored anywhere in the database.")
            name = input("Enter your name as on the card: ")
            card_no = input("Enter your card number: ")
            cvv = input("Enter your CVV number: ")
            data = 'P R O C E S S I N G . . .'
            for l in data:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.5)
                print()
                debit = 'Debit'
                cursor.execute("insert into paid values('{}', '{}', '{}','{}', '{}','{}','{}')".format(name, fr, to, date, userid, fare, debit))
            mycon.commit()
            print()
            Mail.mail(userid, date)
            break
    else:
         print("That was an invalid option. Please try again.")
