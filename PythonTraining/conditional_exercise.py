month = input("Enter birth month:")

if month == 'January':
    print('Birthstone is Garnet')
elif month == 'February':
    print('Brithstone is Amethyst')
elif month == 'March':
    print('Brithstone is Aquamarine')
elif month == 'April':
    print('Brithstone is Diamond')
elif month == 'May':
    print('Brithstone is Emerald')
elif month == 'June':
    print('Brithstone is Alexandrite')
elif month == 'July':
    print('Brithstone is Ruby')
elif month == 'August':
    print('Brithstone is Peridot')
elif month == 'September':
    print('Brithstone is Sapphire')
elif month == 'October':
    print('Brithstone is Tourmaline')
elif month == 'November':
    print('Brithstone is Citrine')
elif month == 'December':
    print('Brithstone is Zircon')
else:
    print('Wrong month name')

def birthstone(month):
    match month:
        case 'January':
            return 'Birthstone is Garnet'
        case 'February':
            return 'Brithstone is Amethyst'
        case 'March':
            return 'Brithstone is Aquamarine'
        case 'April':
            return 'Brithstone is Diamond'
        case 'May':
            return 'Brithstone is Emerald'
        case 'June':
            return 'Brithstone is Alexandrite'
        case 'July':
            return 'Brithstone is Ruby'
        case 'August':
            return 'Brithstone is Peridot'
        case 'September':
            return 'Brithstone is Sapphire'
        case 'October':
            return 'Brithstone is Tourmaline'
        case 'November':
            return 'Brithstone is Citrine'
        case 'December':
            return 'Brithstone is Zircon'
        case _:
            return 'Wrong month name'

print(birthstone(month))