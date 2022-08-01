import pyodbc
import functools

def db(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conString = 'Driver={SQL Server};Server=DESKTOP-VBFB99F\SQLEXPRESS;Database=Assignments;Trusted_Connection=yes;'
            myconn = pyodbc.connect(conString)
        except:
            print('Connection Error')
            return None
        else:
            mycursor = myconn.cursor()
            value = func(mycursor, *args)
            myconn.commit()
            myconn.close()
            return value
    return innerWrapper

@db
def addPatient(mycursor: pyodbc.Cursor):
    name = input('Patient name:').strip()
    gender = input('Gender:').strip()
    age = int(input('Age:').strip())
    bloodGroup = input('Blood group:').strip()
    try:
        mycursor.execute("INSERT INTO Patient VALUES(?, ?, ?, ?)", (name, gender, age, bloodGroup))
    except Exception as e:
        print("Cannot insert data")
        print(e)
    else:
        print('Patient Added\n')


@db
def removePatient(mycursor: pyodbc.Cursor):
    name = input('Enter patient name to delete:').strip()
    try:
        mycursor.execute("DELETE FROM Patient WHERE name = ?", name)
        if mycursor.rowcount == 0:
            print('No matching data\n')
            return
    except Exception as e:
        print("Cannot delete the patient:")
        print(e)
    else:
        print('Patient Deleted\n')

@db
def updatePatient(mycursor: pyodbc.Cursor):
    name = input('Enter patient name to update:').strip()
    mycursor.execute("SELECT * FROM Patient where name = ?", name)
    if mycursor.rowcount == 0:
        print('No matching data\n')
        return
    gender = input('Gender:').strip()
    age = int(input('Age:'))
    bloodGroup = input('Blood group:').strip()
    try:
        mycursor.execute("UPDATE Patient SET gender = ?, age = ?, bloodGroup = ? WHERE name = ?", gender, age, bloodGroup, name)
    except Exception as e:
        print("Cannot delete the patient:")
        print(e)
    else:
        print('Patient Updated\n')

@db
def listPatient(mycursor: pyodbc.Cursor):
    try:
        mycursor.execute("SELECT * FROM Patient")
        if mycursor.rowcount == 0:
            print("No data\n")
            return
    except:
        print("Cannot read data")
        print(Exception)
    else:
        print('\nPatient directory\n')
        for id, name, gender, age, bg in mycursor.fetchall():
            print(f'Id: {id}'),
            print(f'Name: {name}')
            print(f'Gender: {gender}')
            print(f'Age: {age}')
            print(f'Blood Group: {bg}\n')


@db 
def searchPatient(mycursor: pyodbc.Cursor):
    n = input('\nEnter name to search:').strip()
    try:
        mycursor.execute("SELECT * FROM Patient WHERE name = ?", (n))
        if mycursor.rowcount == 0:
            print(f'{n} does not exist\n')
            return
        for id, name, gender, age, bg in mycursor.fetchall():
            print(f'Id: {id}'),
            print(f'Name: {name}')
            print(f'Gender: {gender}')
            print(f'Age: {age}')
            print(f'Blood Group: {bg}')
    except:
        print(f'{n} does not exist')
        print(Exception)
    else:
        return
    

while True:
    print('Patient dbms')
    print('1. Admit patient 2. Update patient 3. Delete patient 4. List patients 5. Search patients 6. Exit')
    ch = int(input('Enter your choice:'))
    match ch:
        case 1: addPatient()
        case 2: updatePatient()
        case 3: removePatient()
        case 4: listPatient()
        case 5: searchPatient()
        case 6: break
        case _: print("Wrong choice!")