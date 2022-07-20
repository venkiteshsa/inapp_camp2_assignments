#Q1

def gst():
    b_price = int(input("Enter the base price:"))
    a_gst = int(input("Enter the applicable gst rate:"))

    cgst = a_gst / 2
    sgst = cgst
    c_price = b_price*cgst/100
    s_price = b_price*sgst/100
    t_price = b_price + c_price + s_price

    print("Actual price :", b_price)
    print("Price after CGST:", c_price+b_price)
    print("Price after SGST:", s_price+b_price)
    print("Total price:", t_price)



#Q2


def phonebook():

    contacts = {
        'John' : 9932458301,
        'Ann' : 9929740301,
        'Paul' : 9935637301,
        'Steve' : 9778948301,
        'Rose' : 9936737845,
        'Jack' : 9996326373,
    }

    ch = 0
    while ch != 6:
        print("\tPhone Book App")
        print("\t1. List all contacts")
        print("\t2. Add a contact")
        print("\t3. Delete a contact")
        print("\t4. Search by name")
        print("\t5. Search by number")
        print("\t6. Exit")
        ch = int(input("Enter your choice:"))
        match ch:
            case 1: sort(contacts)
            case 2: add(contacts)
            case 3: delete(contacts)
            case 4: searchno(contacts)
            case 5: searchname(contacts)
            case 6: continue
            case _: print("Incorrect choice")

def sort(contacts):
    for i in sorted(contacts.keys()):
        print(i)

def add(contacts):
    pno = int(input("Enter phone number:"))
    cname = input("Enter contact name:")
    contacts[cname] = pno
    print("Added")

def delete(contacts):
    cname = input("Enter the contact name to delete:")
    if contacts.get(cname):
        del contacts[cname]
        print("Deleted")
    else:
        print("%s doesn't exist" %cname)

def searchno(contacts):
    cname = input("Enter the contact name to search:")
    if contacts.get(cname):
        print(contacts[cname])
    else:
        print("%s doesn't exist" %cname)
    

def searchname(contacts):
    pno = int(input("Enter the phone number to search:"))
    for k, v in contacts.items():
        if pno == v:
            print(k)


#Q3
def rockpaperscissor():
    import random
    actors = ['Rock', 'Paper', 'Scissor']
    c, cp, cpup = 0, 0, 0
    while c <5:
        ch = input("\nRock, Paper, Scissor ? : ")
        cpu = random.choice(actors)
        print('User:', ch, 'Cpu:', cpu)
        if ch == cpu:
            c = c + 1
        else:
            if (ch == 'Rock' and cpu == 'Paper') or (ch == 'Paper' and cpu == 'Scissor') or (ch == 'Scissor' and cpu == 'Rock'):
                cpup = cpup + 1
            else:
                cp = cp + 1
            c = c + 1
    if cp > cpup:
        print("\nThe winner is user(%d - %d)" %(cp, cpup))
    elif cp < cpup:
        print("\nThe winner is cpu (%d - %d)" %(cpup, cp))
    else:
        print("\nTie game !")

ch = 0
while ch != 4:
    print("\n\t 1. GST question")
    print("\t 2. Phonebook question")
    print("\t 3. Rock paper scissor question")
    print("\t 4. Exit")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1: gst()
        case 2: phonebook()
        case 3: rockpaperscissor()
        case 4: continue
        case _: print("Invalid choice")