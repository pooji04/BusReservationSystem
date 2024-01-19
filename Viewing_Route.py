from tabulate import tabulate
import pandas as pd

def create_dict(data, keys):
    dict_list = []
    for row in data:
        dic = dict(zip(keys, row))
        dict_list.append(dic)
    return dict_list

def view_route():
    import mysql.connector as sqlcon
    mycon=sqlcon.connect(host='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
    cursor=mycon.cursor()
    choice = 'Y'
    
    while choice:
        start = input("Enter start location : ")
        end = input("Enter end location : ")
        date = input("Enter date (YYYY-MM-DD) : ")
        values = (start.upper(), end.upper(), date)
        cursor.execute("select name, age, gender, bg, phno, address, tid, seatno from pass_det where Starting_Point = '{}' and End_Point = '{}' and Date = '{}'" .format(start, end, date))
        data = cursor.fetchall()
        count = cursor.rowcount
        if count == 0:
            print("No records exist for this trip. Please try again.")
            choice = input("Do you want to try again? Enter Y/N : ")
            choice = choice.upper()
            if choice == 'Y':
                continue
            elif choice == 'N':
                break
            else:
                print("Invalid option.")
