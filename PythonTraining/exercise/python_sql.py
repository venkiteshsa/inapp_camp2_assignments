import pyodbc

#create a connection string
conString = 'Driver={SQL Server};Server=DESKTOP-VBFB99F\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with the connection string
myconn = pyodbc.connect(conString)
#get the curson object
#mycursor = myconn.cursor()

"""
#using cursor, execute SQl commands
try:
    mycursor.execute('''CREATE TABLE EmployeeMaster3
    (
        Id INT IDENTITY PRIMARY KEY,
        EmployeeCode VARCHAR(10),
        EmployeeName VARCHAR(25),
        DepartmentCode VARCHAR(10),
        LocationCode VARCHAR(10),
        Salary INT
    )''')
except Exception as e:
    print("Cannot create the table because:")
    print(f"{type(e).__name__} was occured.")
    print(e)
mycursor.commit() #commiting the transaction(required for all write/update/delete statements)
myconn.close()

print("Statement after the query")


try:
    mycursor = myconn.cursor()
    mycursor.execute("SELECT * FROM EmployeeMaster")
except Exception as e:
    print("Cannot read the table because:")
    print(e)

#for row in mycursor.fetchall():
#    print(row)

employees  = [{'empcode':row[1], 'empname':row[2]} for row in mycursor.fetchall()]

print(employees)

myconn.close()
"""

