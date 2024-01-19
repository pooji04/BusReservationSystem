# Bus Reservation System Project

This is a simple bus reservation system project implemented in Python. Before running the application, make sure to follow the steps below.

## Prerequisites

1. **Install SQL Database:**
   - Download and install a SQL database (e.g., MySQL, SQLite).
   - Create a database named `bus_reservation_system`.

2. **Install Required Python Modules:**
   - Make sure to install the following Python modules before running the application:
     ```bash
     pip install mysql.connector random termtables smtplib tabulate pandas
     ```

3. **Create Tables:**
   - Run the following SQL commands to create the necessary tables in the `bus_reservation_system` database.

   ```sql
   CREATE TABLE bus_information (
       License_Plate_Number VARCHAR(100),
       Starting_Point VARCHAR(100),
       End_Point VARCHAR(100),
       Distance VARCHAR(100),
       Fare INT(5),
       Start_Time VARCHAR(20),
       End_Time VARCHAR(20)
   );

   CREATE TABLE admin (
       adminID INT(4) PRIMARY KEY,
       password VARCHAR(30)
   );

   CREATE TABLE paid (
       Name VARCHAR(100),
       Starting_Point VARCHAR(100),
       End_Point VARCHAR(100),
       Date VARCHAR(20),
       UserID VARCHAR(20),
       Fare INT(5),
       Mode VARCHAR(10)
   );

   CREATE TABLE cancel_rec (
       name VARCHAR(100),
       age INT(3),
       gender VARCHAR(1),
       phno INT(10),
       address VARCHAR(200),
       tid INT(10),
       date VARCHAR(100),
       Starting_Point VARCHAR(100),
       End_Point VARCHAR(100),
       Distance VARCHAR(100),
       Fare INT(5),
       Start_Time VARCHAR(20),
       End_Time VARCHAR(20),
       UserID VARCHAR(20),
       Refund VARCHAR(10)
   );

   CREATE TABLE pass_det (
       name VARCHAR(100),
       age INT(3),
       gender VARCHAR(1),
       phno INT(10),
       address VARCHAR(200),
       tid INT(10),
       date VARCHAR(100),
       Starting_Point VARCHAR(100),
       End_Point VARCHAR(100),
       Distance VARCHAR(100),
       Fare INT(5),
       Start_Time VARCHAR(20),
       End_Time VARCHAR(20),
       UserID VARCHAR(20)
   );

   CREATE TABLE user (
       userid VARCHAR(20),
       pwd VARCHAR(30)
   );
   ```

## Modules

### 1. Booking

- Contains a function `booking(userid)` to book a ticket for the user.

### 2. Viewing_Route

- Contains a function `view_route()` that allows the admin to view the passenger list taking a particular route.

### 3. Viewing_Cancellation

- Contains a function `view_cancel()` that allows the admin to view the list of passengers who have canceled.

### 4. Admin

- Contains a function that validates the admin login.

### 5. Cancellation

- Contains a function `cancel()` that allows the user to cancel their ticket.

### 6. Payment

- Contains a function `pay(userid, fr, to, no, date, fare)` that allows the user to pay for their tickets.

### 7. User_Login

- Contains a function `user()` that validates user login.

### 8. Viewing_Schedule

- Contains a function `view_schedule()` that allows the passenger to check their bus schedule.

### 9. Mail

- Contains a function `mail(userid, date)` that sends a copy of the ticket to the user.

## How to Run

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/pooji04/bus-reservation-system.git
   ```

2. Navigate to the project directory.
   ```bash
   cd bus-reservation-system
   ```

3. Run the main Python script.
   ```bash
   python main.py
   ```

Follow the on-screen prompts to interact with the bus reservation system.
