# create a table to store employee information
#	* empid
#	* name
#	* department
#	* email
#	* salary
#	* date of joining

#import module
import mysql.connector

#create connection with database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdata"
)
#create a query
empid = int(input("Enter Empid :"))
name = input("Enter Name :")
department = input("Enter Department :")
email = input("Enter Emailid :")
salary = float(input("Enter Salary :"))
joining = input("Enter Date of joining :")

query = f"insert into Employee values({empid},'{name}','{department}','{email}',{salary},'{joining}');"

#create a cursor to execute the query
cursor = connection.cursor()

#execute query using cursor
cursor.execute(query)

#after execution of query commit your changes
connection.commit()

#close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()
