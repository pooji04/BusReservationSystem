import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
cursor=mycon.cursor()
from tabulate import tabulate

def view_cancel():
    while True:
        print("1.View cancelled tickets on a particular date")
        print("2.View all cancelled tickets")
        print("3. Exit")
        choice=input("Enter your choice(1/2):")
        if choice=="1":
            date=input("Enter date:")
            cursor.execute("selectname,age,gender,phno,tid,date,starting_point,end_point,seatno,license_plate_number,fare from cancel_rec where date='{}'".format(date))
            data1=cursor.fetchall()
            print(tabulate(data1,headers=["Name","Age","Gender","Phno","Tid","Date","Starting_point","End_point","Seatno","License_Plate_Number"]))
            choice = input('Do you want to continue? Enter Y/N: ')
            if choice == 'Y':
                continue
            else:
                break
        elif choice=="2":
            cursor.execute("select name,age,gender,phno,tid,date,starting_point,end_point,seatno,license_plate_number,fare from cancel_rec")
            data2=cursor.fetchall()
            print(tabulate(data2,headers=["Name","Age","Gender","Phno","Tid","Date","Starting_point","End_point","Seatno","License_Plate_Number"]))
            choice = input('Do you want to continue? Enter Y/N: ')
            if choice == 'Y':
                continue
            else:
                break
        elif choice == '3':
            break
        else:
            print("Enter valid choice!")
