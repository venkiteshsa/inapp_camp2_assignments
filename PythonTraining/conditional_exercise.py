month = input("Enter birth month no.:")

if month == '1':
    print('Birthstone is Garnet\nPeople born in January are bold and alert.')
elif month == '2':
    print('Brithstone is Amethyst\nPeople born in February are lucky and loyal.')
elif month == '3':
    print('Brithstone is Aquamarine\nPeople born in March are naughty and genius.')
elif month == '4':
    print('Brithstone is Diamond\nPeople born in April are caring and strong.')
elif month == '5':
    print('Brithstone is Emerald\nPeople born in May are loving and pratical.')
elif month == '6':
    print('Brithstone is Alexandrite\nPeople born in June are romantic and curious.')
elif month == '7':
    print('Brithstone is Ruby\nPeople born in July are adventurous and honest.')
elif month == '8':
    print('Brithstone is Peridot\nPeople born in August are active and hardworking.')
elif month == '9':
    print('Brithstone is Sapphire\nPeople born in September are sensitive and pretty.')
elif month == '10':
    print('Brithstone is Tourmaline\nPeople born in October are stylish and friendly.')
elif month == '11':
    print('Brithstone is Citrine\nPeople born in November are nice and creative.')
elif month == '12':
    print('Brithstone is Zircon\nPeople born in December are confident and freedom loving.')
else:
    print('Wrong month no')

def birthstone(month):
    match month:
        case '1':
            return 'Birthstone is Garnet\nPeople born in January are bold and alert'
        case '2':
            return 'Brithstone is Amethyst\nPeople born in February are lucky and loyal'
        case '3':
            return 'Brithstone is Aquamarine\nPeople born in March are naughty and genius'
        case '4':
            return 'Brithstone is Diamond\nPeople born in April are caring and strong'
        case '5':
            return 'Brithstone is Emerald\nPeople born in May are loving and pratical'
        case '6':
            return 'Brithstone is Alexandrite\nPeople born in June are romantic and curious.'
        case '7':
            return 'Brithstone is Ruby\nPeople born in July are adventurous and honest'
        case '8':
            return 'Brithstone is Peridot\nPeople born in August are active and hardworking'
        case '9':
            return 'Brithstone is Sapphire\nPeople born in September are sensitive and pretty'
        case '10':
            return 'Brithstone is Tourmaline\nPeople born in October are stylish and friendly'
        case '11':
            return 'Brithstone is Citrine\nPeople born in November are nice and creative'
        case '12':
            return 'Brithstone is Zircon\nPeople born in December are confident and freedom loving'
        case _:
            return 'Wrong month no'

print(birthstone(month))