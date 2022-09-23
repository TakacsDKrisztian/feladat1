
def feladat1():
    postcode = int(input('Add meg az irányítószámodat: '))
    city = input('Add meg a városodat: ')
    street = input('Add meg az utca nevét: ')
    nature_of_public_space = input('Add meg a közterület jellegét: ')
    house_number = int(input('Add meg aház számot: '))

    print(f'{postcode} {city} {street} {nature_of_public_space} {house_number}')

feladat1()

def feladat2():
    lname1 = input('Add meg az első vezetéknevet: ')
    fname1 = input('Add meg az első keresztnevet: ')
    lname2 = input('Add meg a második vezetéknevet: ')
    fname2 = input('Add meg a második keresztnevet: ')
    
    print(f'{lname1} {fname1}')
    print(f'{lname1} {fname2}')
    print(f'{lname2} {fname1}')
    print(f'{lname2} {fname2}')

feladat2()

def feladat3():
    monthly_payment = int(input('Add meg a havi fizetésedet: '))

    print(f'{monthly_payment*12}')

feladat3()

def feladat4():
    exchange_rate = float(input('Add meg az euró árfoyamát: '))
    count = int(input('Mennyi eurót akarsz átváltani? '))

    print(f'{count*exchange_rate}')

feladat4()

def feladat5():
    a = float(input('Add meg a téglalap egyik oldalát: '))
    b = float(input('Add meg a téglalap másik oldalát: '))

    print(f'A oldal = {a}')
    print(f'B oldal = {b}')
    print(f'Kerület = {2*(a+b)}')
    print(f'Terület = {a*b}')

feladat5()

from cmath import pi


def feladat6():
    r = float(input('Add meg a kör sugarát: '))

    print(f'Kerülete: {2*r*pi}')
    print(f'Területe: {r**2*pi}')

feladat6()



import math


def feladat7():
    a = int(input('Add meg a derékszögű háromszög A oldalát: '))
    b = int(input('Add meg a derékszögű háromszög B oldalát: '))
    c = round(math.sqrt(a**2+b**2), 2)

    print(f'Az átfogó hossza: {c}') 

feladat7()  





def feladat8():
    length = float(input('Add meg az út hosszát (km): '))
    time = float(input('Add meg az út hosszát(órában)'))

    print(f'A sebességed: {round(length/time, 2)}')

feladat8()



