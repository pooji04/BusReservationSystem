import mysql.connector as sqlcon
mycon = sqlcon.connect(host ='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
cursor = mycon.cursor()
import random
import termtables as tt
                     
def booking(userid):
    data=[]
    ch='Y'
    noftickets=43
    
    while ch=='Y':
        print('COIMBATORE')
        print('OOTY')
        print('BANGALORE')
        print('MYSORE')
        print('CHENNAI')
        fr=input('Enter Starting point:').upper()
        to=input('Enter End Destination:').upper()
        date=input('Enter date(YYYY-MM-DD):')
        displayinfo='select * from bus_information where Starting_Point="{}" and End_Point="{}"'.format(fr,to)
        cursor.execute(displayinfo)
        data=cursor.fetchall()

        
        if data==[]:
            print('No such bus exists.Please try again')
            ch=input('Do you want to continue?(Y/N)')
            continue
        
        for i in data:
            License_Plate_Number,Starting_Point,End_Point,Distance,Fare,Start_Ti
            me,End_Time=i
            Fare=int(Fare)
            scheck="select seatno from pass_det where Starting_point='{}' and end_point='{}' and date='{}'".format(fr,to,date)
            cursor.execute(scheck)
            sdata=cursor.fetchall()
            
            for i in range(len(sdata)):
                (sdata[i],)=sdata[i]
            L=[]
            
            for i in range(1,37,4):
                L.extend([[i,i+1,' ',i+2,i+3]])
                
            L.extend([[37,38,' ',' ',' ']])
            L.extend([[39,40,41,42,43]])
            for i in range(11):
                for j in range(5):
                    if L[i][j] in sdata:
                        L[i][j]='X'
                        noftickets-=1
                        
            data[0]=list(data[0])
            data[0].append(noftickets)
            header= ['License_Plate_Number','Starting_Point','End_Point','Distance','Fare','Start_Time','End_Time','No of tickets']
            tt.print(data,header=header)

            tt.print(L)
            print('X-BOOKED')
            
            no=int(input('Please select the number of passengers:'))
            for j in range(no):
                print('Select a seat from 1 to 43')
                seatno=int(input('Enter the seat no:'))
                scheck="select seatno from pass_det where Starting_point='{}' and end_point='{}' and date='{}'".format(fr,to,date)
                cursor.execute(scheck)
                sdata=cursor.fetchall()
                while (seatno,) in sdata:
                    print('This seat is already booked' )
                    seatno=int(input('Please enter another seat no:'))
                else:
                    print('This seat is available','\n')
                    print('Enter passenger details:-')
                    name=input('Enter name:')
                    age=int(input('Enter age:'))
                    gender=input('Enter Gender')
                    bg=input('Enter Blood Group')
                    phno=int(input('Enter phone no:'))
                    add=input('Enter address:')
                    tid=random.randrange(9999999)
                    passinfo="insert into pass_det values('{}',{},'{}','{}','{}','{}',{},'{}','{}','{}',{},'{}','{}'{},'{}','{}','{}')".format(name,age,gender,bg,phno,add,tid,date,fr,to,seatno,License_Plate_Number,Distance,Fare,Start_Time,End_Time,userid)
                    cursor.execute(passinfo)
                    mycon.commit()
                    print('Ticket Booked')
                    print('Ticket Number is',tid)
            fare = Fare*no
            print('Total fare is:',"\u20B9"+str(Fare*no))
            ch=input('Do you want to continue?(Y/N)')
            return (fr, to, no, date, fare)

