import mysql.connector as mysql
import Booking as b
import Viewing_Route as vr
import Viewing_Cancellation as vc
import Admin as a
import Cancellation as c
import Payment as p
import User_Login as u
import Viewing_Schedule as vs

db = mysql.connect(host = 'localhost', user = 'root', password = 'poojitha', database = 'bus_reservation_system')
mycursor = db.cursor(buffered = True)

def session():
    while True:
        print("Welcome to ABC Bookings.")
        print('''1. User
2. Admin
3. Exit''')
        first_choice = int(input("Please enter your choice: "))
        if first_choice == 1:
            userid = u.user()
            while True:
                print()
                print('''\nUser Menu
1. Booking
2. Viewing Schedule
3. Cancellation
4. Exit''')
                choice = int(input("Please enter your choice: "))
                if choice == 1:
                    fr, to, no, date, fare = b.booking(userid)
                    p.pay(userid, fr, to, no, date, fare)
                elif choice == 2:
                    vs.view_schedule()
                elif choice == 3:
                    c.cancel()
                elif choice == 4:
                    break
                else:
                    print("That was an invalid option.Please try again.")

        elif first_choice == 2:
            a.admin()
            while True:
                print("Login Successful.")
                print("1. View Passenger List.")
                print("2. View Cancelled Tickets.")
                print("3. Exit.")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    vr.view_route()
                elif choice == 2:
                    vc.view_cancel()
                elif choice == 3:
                    break

        elif first_choice == 3:
            print("Thank you for using our services. We hope to see you soon!")
            break
    else:
        print("That was an invalid option. Please try again.")

ssession()
