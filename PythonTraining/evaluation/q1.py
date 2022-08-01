import random

category = ['Hygiene', 'Health', 'Staples',  'Sports', 'Fashion']
p = {}

class ProductCategory():

    def __init__(self, c, capacity = 10):
        self.category = category[c]
        self.product = {}
        self.capacity = capacity
        '''
        self.counter += 1
        if self.counter >= self.capacity:
            print('Category capacity reached')
            return
        '''

    def prodName(self):
        while True:
            str = input('Enter product name:')
            if len(str) >= 3 and str.isalpha():
                return str
            else:
                print('Product must be atleast 3 characters long and should only contain characters')


    def getPrice(self):
        ch = input('1. Price before tax 2. MRP. Select:')
        if ch == "1":
            bp = int(input('Enter basic price:'))
            tax = int(input('Enter tax %:'))
            MRP = bp + (bp*tax/100)
        elif ch == "2":
            MRP = int(input('Enter MRP:'))
            tax = int(input('Enter tax %:'))
            bp = MRP*100/(tax+100)
        return round(bp, 2), round(tax, 2), round(MRP, 2)

    def discount(self, MRP):
        ch = input('Discount as 1. Rate or 2. Amount. Select:')
        if ch == "1":
            dr = int(input('Enter discount rate:'))
            discountPrice = MRP - (MRP*dr/100)
            return str(dr)+'%', round(discountPrice, 2)
        elif ch == "2":
            da = int(input('Enter discount amount:'))
            discountPrice = MRP - da
            return str(da), round(discountPrice, 2)
    
    def code(self, name, c, p):
        codes = [i[:4] for i in p.keys()]
        tmpCode = name[:2].upper() + c[:2].upper()
        productCode = tmpCode + str(codes.count(tmpCode)) + str(random.randrange(1000)).zfill(3)
        return productCode
        
    def addProduct(self):
        name = self.prodName()
        bp, tax, mrp = self.getPrice()
        d, dp = self.discount(mrp)
        global p
        product = [name, self.category, bp, tax, mrp, d, dp]
        pcode = self.code(name, self.category, p)
        p.update({pcode : product}) 
        print('Product added\n')
    
    @staticmethod
    def displayProduct():
        global p
        if not p:
            print('\nNo products\n')
        else:
            for i, k in p.items():
                print(f'\nProduct name : {k[0]}')
                print(f'Category : {k[1]}')
                print(f'Product code : {i}')
                print(f'Base Price : {k[2]}')
                print(f'GST : {k[3]}')
                print(f'MRP : {k[4]}')
                print(f'Discount : {k[5]}')
                print(f'Discounted Price : {k[6]}\n')


while True:
    print("1. Add products 2. List products 3. Exit")
    ch = input("Enter you choice:")
    if ch == '1':    
        print("\n1.Hygiene 2.Health 3.Staples 4.Sports 5.Fashion")
        c = int(input('Enter product category:'))-1
        prod = ProductCategory(c)
        prod.addProduct()
    elif ch == "2":
        ProductCategory.displayProduct()
    elif ch == "3":
        break
    else:
        print("Wrong choice!")