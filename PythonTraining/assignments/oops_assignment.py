class Patient:
    def __init__(self, name, gender, age, dob, b_g):
            self.name = name
            self.gender = gender
            self.age = age
            self.dob = dob
            self.b_g = b_g
    
    def printPatientDetails(self):
        print('Name:', self.name)
        print('Gender:', self.gender)
        print('Age:', self.age)
        print('DOB:', self.dob)
        print('Blood Group:', self.b_g)

    def update(self, name, gender, age, dob, b_g):
        self.name = name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.b_g = b_g


class CMS:

    patients = dict()
    ops = dict()
    slno = 0
    opno = 0
    

    def register(name, gender, age, dob, b_g):
        p = Patient(name, gender, age, dob, b_g)
        CMS.slno += 1
        CMS.patients[CMS.slno] = p
        return CMS.slno
    
    
    def listPatients():
        print('Patient Directory\n')
        for id, p in CMS.patients.items():
            print('\nID:', id)
            p.printPatientDetails()
    
    def listOP():
        print('\nOP:')
        for id, p in CMS.ops.items():
            print('OP No:', id)
            p.printPatientDetails()
        

    def search(id):
        if CMS.patients.get(id):
            print('\nThe searched patient is ..')
            print('ID:', id)
            CMS.patients[id].printPatientDetails()
        else:
            print('ID doesn\'t exist')

    def delete(id):
        if CMS.patients.get(id):
            del CMS.patients[id]
            print('Patient record deleted')
        else:
            print('ID doesn\'t exist')
    
    def update(id, name, gender, age, dob, b_g):
        if CMS.patients.get(id):
            CMS.patients[id].update(name, gender, age, dob, b_g)
        else:
            print(id, 'does not exist')
        
    def admit(id, disease, noOfDays):
        if CMS.patients.get(id):
            op = OP(CMS.patients[id].name, CMS.patients[id].gender, CMS.patients[id].age, CMS.patients[id].dob, CMS.patients[id].b_g, disease, noOfDays)
            CMS.ops[CMS.opno] = op
        else:
            print(id, 'does not exist')

    
class OP(Patient):
    def __init__(self, name, gender, age, dob, b_g, disease, noOfDays):
        super().__init__(name, gender, age, dob, b_g)
        self.disease = disease
        self.noOfDays = noOfDays
    
    def printPatientDetails(self):
        super().printPatientDetails()
        print('Disease:', self.disease)
        print('No of Days:', self.noOfDays)

class nonOP(Patient):
    opTicketNo = 0

    def generateToken():
        nonOP.opTicketNo += 1
        return nonOP.opTicketNo

id = CMS.register('superman', 'M', 12, '01/02/2010', 'O+')
print(id)
id = CMS.register('spiderman', 'M', 12, '01/02/2010', 'A+')
print(id)
CMS.listPatients()
CMS.update(2, 'spiderman', 'M', 12, '10/02/2010', 'B+')
CMS.listPatients()
CMS.admit(2, 'broken leg', 10)
CMS.listOP()
print(nonOP.generateToken())
