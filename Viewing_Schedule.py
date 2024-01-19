from tabulate import tabulate
import pandas as pd

def create_dict(data, keys):
    '''Function to create a dictionary out of tuples'''

    dict_list = []
    for row in data:
        dic = dict(zip(keys, row))
        dict_list.append(dic)
    return dict_list

def view_schedule():
    import mysql.connector as sqltor
    mycon=sqltor.connect(host='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
    cursor=mycon.cursor()
    from tabulate import tabulate
    import pandas as pd
    choice="Y"
    while choice:
        tno=input("Enter your ticket number:")
        cursor.execute ( " select name, tid , date , Starting_point , End_point, seatno, Fare , Start_time , End_time from pass_det where tid ='{}'".format(tno))
        data = cursor.fetchall()
        count = cursor.rowcount
        if count == 0 :
            print ( " Ticket no. is invalid. Please try again. " )
            choice = input ( " Do you want to try again? Enter ( Y/N )")
            if choice == "Y":
                continue
            else:
                break
        keys = ['Name', 'TicketID', 'Date', 'Starting Point', 'End Point', 'SeatNumber', 'Fare', 'Start Time', 'End Time']
        rows_as_dict = create_dict(data, keys)
        df = pd.DataFrame(rows_as_dict)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
        choice = input("Do you want to try again? Enter Y/N : ")
        choice = choice.upper()
        if choice == 'Y':
            continue
        else:
            break
