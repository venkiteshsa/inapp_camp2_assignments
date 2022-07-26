import re
import pyodbc

conString = 'Driver={SQL Server};Server=DESKTOP-VBFB99F\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
myconn = pyodbc.connect(conString)
mycursor = myconn.cursor()

def init():
    try:
        mycursor.execute('''CREATE TABLE Contacts
        (
            Contact VARCHAR(20),
            Phno VARCHAR(13)
        )''')
    except:
        print("Cannot create the table because:")
        print(Exception)

    mycursor.commit()





def sort():
    try:
        mycursor.execute("SELECT * FROM Contacts ORDER BY Contact")
        if mycursor.description is None:
            print("No data")
    except:
        print("Cannot read data")
        print(Exception)
    else:
        print('\nContact directory:\n')
        for name, phno in mycursor.fetchall():
            print(f'Name: {name}')
            print(f'Number: {phno}')
    


def add():
    while True:
        name = input('\nEnter name:').strip()
        if ',' in name:
            print(', not allowed in name')
        else:
            break
    while True:
        phno = input('Enter number:').strip()
        if re.match(r'\+[0-9]*', phno):
            break
        else:
            print('Invalid input')
    try:
        mycursor.execute("INSERT INTO Contacts VALUES(?, ?)", (name, phno))
    except Exception as e:
        print("Cannot insert data")
        print(e)
    else:
        print('Contact added')
    mycursor.commit()



def searchName():
    n = input('\nEnter name to search:')
    try:
        mycursor.execute("SELECT * FROM Contacts WHERE Contact = ?", (n))
        for name, number in mycursor.fetchall():
            print(f'\nName: {name}')
            print(f'Number: {number}')
    except:
        print(f'{n} does not exist')
        print(Exception)
    else:
        return
    
    


def searchNo():
    n = input('\nEnter name to search:')
    try:
        mycursor.execute("SELECT * FROM Contacts WHERE Phno = ?", (n))
        for name, number in mycursor.fetchall():
            print(f'\nName: {name}')
            print(f'Number: {number}')
    except:
        print(f'{n} does not exist')
        print(Exception)
    else:
        return

def delete():
    n = input('\nEnter name to delete:')
    try:
        mycursor = myconn.cursor()
        mycursor.execute("DELETE FROM Contacts WHERE Contact = ?", n)
    except Exception as e:
        print("Cannot delete the contact:")
        print(e)
    else:
        print('Deleted')
    mycursor.commit()

opt = 0

init()

while True:
    print("\nYellow Pages\n")
    print("1. List all contacts \n2. Add a new contact \n3. Search by name \n4. Search by number \n5. Delete a contact \n6. Exit")
    opt = int(input("\nEnter your choice:"))
    match opt:
        case 1: sort()
        case 2: add()
        case 3: searchName()
        case 4: searchNo()
        case 5: delete()
        case 6: break
        case _: print("\nInvalid choice!\n")

mycursor.close()
myconn.close()