def mail(userid,date):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from tabulate import tabulate
    import pandas as pd
    import mysql.connector as sqlcon
    
    mycon=sqlcon.connect(host='localhost',user='root',passwd='poojitha',database='bus_reservation_system')
    cursor=mycon.cursor()
    
    fromaddr = 'testtttmail123@gmail.com'
    toaddr = input("Enter your email address: ")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Invoice'
    body = 'Thank you for booking with ABC Travels. Here is the ticket.'
    msg.attach(MIMEText(body, 'plain'))

    def create_dict(data, keys):
        dict_list = []
        for row in data:
            dic = dict(zip(keys, row))
            dict_list.append(dic)
        return dict_list
    
    with open("ticket.txt", 'w') as file:
        file.write("Here is your ticket. Please take a printout and present it on the day of your travel.")
        file.write('\n')
        cursor.execute("select name, age, gender, tid, seatno from pass_det where userid = '{}' and date = '{}'".format(userid,date))
        data = cursor.fetchall()
        keys = ['Name', 'Age', 'Gender', 'Ticket ID', 'Seat Number']
        rows_as_dict = create_dict(data, keys)
        df = pd.DataFrame(rows_as_dict)
        file.write(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    filename = 'ticket.txt'
    attachment = open(r'C:\Users\PoojithaSai\AppData\Local\Programs\Python\Python37\Lib\sitepackages\bus\ticket.txt', 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" %filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, 'testmail123')
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
