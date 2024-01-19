import mysql.connector as mysql
db = mysql.connect(host = 'localhost', user = 'root', password = 'poojitha', database = 'bus_reservation_system')
cursor = db.cursor(buffered = True)

def cancel():
    ch = 'Y'
  
    while ch == 'Y':
        tno = input('Enter ticket number for cancellation: ')
        tcheck = 'select tid, fare from pass_det where tid = "{}"'.format(tno)
        cursor.execute(tcheck)
        cdata=cursor.fetchall()
      
        if cursor.rowcount == 0:
            print("Ticket no. is invalid. Please try again." )
            ch = input('Do you want to continue?(Y/N): ')
            continue
          
        fare = cdata[0][1]
        refund = float(fare) * 0.75
        cursor.execute("insert into cancel_rec(name, age, gender, bg, phno, address, tid, date, Starting_point, End_ point, seatno, License_Plate_Number, Distance, fare, Start_Time, End_Time, UserID) select * from pass_det where tid = '{}'".format(tno))
        crefund =" update cancel_rec set refund = '{}' where tid ='{}'".format(refund, tno)
      
        cursor.execute(crefund)
        db.commit()
      
        cursor.execute("delete from pass_det where tid = '{}'".format(tno))
        db.commit()
      
        print('Your ticket has been successfully cancelled.')
        print('Your refunded amount is:', refund)
        ch = input('Do you want to continue?(Y/N):')

