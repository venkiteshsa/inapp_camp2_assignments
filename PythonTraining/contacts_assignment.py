import numbers
import os
import re
from tkinter.font import ROMAN
#
#print(os.getcwd())
#os.chdir('Contacts')
#print(os.getcwd())
#myFile = open("contacts.txt", "w")
def init():
    if not os.path.exists('Contacts'):
        os.mkdir('Contacts')
    
    os.chdir('Contacts')

    if not os.path.exists('Contacts.txt'):
        f = open('Contacts.txt', 'x')
        f.close()

def load():
    with open('Contacts.txt', 'r') as file:
        for i in file.readlines():
            name, number = i.strip().split(',')
            contacts[name] = number

def save():
    with open('contacts.txt', 'w') as file:
        file.writelines([f'{name},{no}\n' for name, no in contacts.items()])

contacts = dict()

def sort():
    if len(contacts) > 0:
        print('\nContact directory:\n')
        names = list(contacts.keys())
        names.sort()
        for name in names:
            print(f'Name: {name}')
            print(f'Number: {contacts[name]}')
    else:
        print('No contacts')
    

def add():
    while True:
        name = input('\nEnter name:').strip()
        if ',' in name:
            print(', not allowed in name')
        else:
            break
    while True:
        number = input('Enter number:').strip()
        if re.match(r'\+[0-9]*', number):
            break
        else:
            print('Invalid input')
    contacts[name] = number
    print('Contact added')
    save()
    pass


def searchName():
    n = input('\nEnter name to search:')
    for name, number in contacts.items():
        if name.lower() == n.lower():
            print(f'\nName: {name}')
            print(f'Number: {number}')
            return
    print(f'{name} does not exist')


def searchNo():
    while True:
        n = input('\nEnter number to search:').strip()
        if re.match(r'\+[0-9]*', n):
            break
        else:
            print('Invalid input')
    for name, no in contacts.items():
        if no == n:
            print(f'\nName: {name}')
            print(f'Number: {no}')
            return
    print(f'{n} does not exist')

def delete():
    n = input('\nEnter name to delete:')
    if contacts.get(n):
        del contacts[n]
        print('Deleted')
    save()

opt = 0

init()
load()

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