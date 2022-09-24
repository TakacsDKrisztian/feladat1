
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


def feladat9():
    consumption = float(input('Add meg a kocsi fogyasztását (literben 100km-en): '))
    gasoline_price = float(input('Add meg a benzin árát: '))
    road_length = float(input('Add meg az út hosszát: '))

    print(f'Az uti költséged: {((road_length/100)*consumption)*gasoline_price} Ft')

feladat9()

def feladat10():
    body_mass = int(input('Add meg a testsúlyodat (kg): '))
    tall = int(input('Add meg a test magasságodat (cm): '))

    print(f'Testtömeg indexed: {round(body_mass/((tall/100)**2),2)}')

feladat10()

def feladat11():
    apple_price = 450
    plum_price = 650
    grape_price = 800

    print('Alma -------- 450Ft/kg')
    print('Szilva ------ 650Ft/kg')
    print('Szőlő ------- 800Ft/kg\n')

    apple = int(input('Hány kiló almát szeretnél? '))
    plum = int(input('Hány kiló szilvát szeretnél? '))
    grape = int(input('Hány kiló szőlöt szeretnél? '))

    total_amount = (apple*apple_price)+(plum*plum_price)+(grape*grape_price)

    print('-----------------------')
    print(f'Alma ára: \t{apple*apple_price} Ft')
    print(f'Szilva ára: \t{plum*plum_price} Ft')
    print(f'Szőlő ára: \t{grape*grape_price} Ft')
    print('-----------------------')
    print(f'Ősszesen: {total_amount} Ft')

feladat11()

def feladat12():
    barrel_volume = int(input('Add meg a hordó térfogatát (liter): '))
    jug_volume = int(input('Add meg a kancsó térfogatát (liter): '))

    print(f'Ennyi teli kancsó merhető ki a hordóból: {barrel_volume//jug_volume}')
    print(f'Ennyi víz marad ahordóban: {barrel_volume%jug_volume}')
    print(f'A hordó és a kancsó térfogat hányadosa: {barrel_volume/jug_volume}')

feladat12()

def feladat13():
    print('Bankjegy automata\n')
    print('A legkisebb címlet 1000Ft a maximálisan felvehető összeg 300000Ft\n')
    amount = int(input('Adja meg mekkora összeget kíván felvenni! '))

    teszt_10 = amount//10000
    teszt_5 = (amount-(teszt_10*10000))//5000
    teszt_1 = (amount-((teszt_10*10000)+(teszt_5*5000)))//1000

    print('\nKiadott bankjegyek:\n')
    print(f'{round(teszt_10, 0)}\t*\t 10 000\t = \t {teszt_10*10000} ')
    print(f'{teszt_5}\t*\t 5000\t = \t {teszt_5*5000} ')
    print(f'{teszt_1}\t*\t 1000\t = \t {teszt_1*1000} \n')

    print('--------------------------------------\n')
    print(f'Összeg: \t\t\t {teszt_10*10000+teszt_5*5000+teszt_1*1000} Ft')

feladat13()

def feladat14():

    seconds = int(input('Adja meg az eszköz működési idejét másodpercben: '))
    seconds_in_day = 60*60*24
    seconds_in_hour = 60*60
    seconds_in_minute = 60

    days = seconds//seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute

    print(f'{days} nap {hours} óra {minutes} perc')

feladat14()


def feladat15():

    print('Utazási költségtérítés\n')
    road_length = float(input('Add meg a megtett utat km-ben! '))
    consumption = float(input('Add meg az autó fogyaztását 100km-re literben! '))
    gasoline_price = float(input('Add meg az üzemanyagárat ft-ban! '))
    if road_length <= 100:
        print(f'\nKöltségtérítés: {(road_length*consumption*gasoline_price)/100}')
    else:
        print(f'\nKöltségtérítés: {((road_length*consumption*gasoline_price)/100)+25*road_length}')

feladat15()


def feladat16():

    temperature = int(input('Add emga külső hőmérsékletet'))

    if temperature <0:
        print('Fagy van kint')
    else:
        print('Nincs fagy kint')

feladat16()

def feladat17():

    answer = input('Szeretsz programozni?')

    if answer == 'Igen':
        print('Még sokra viszed az életben')
    else:
        print('Viszlát')

feladat17()


def feladat18():

    number = int(input('Adj meg eg yszámot: '))

    if number%2 == 0:
        print('A szám páros')
    else:
        print('A szám páratlan')

feladat18()

def feladat19():

    number = int(input('Adj meg egy számot: '))

    if number%3 == 0:
        print('A szám osztható 3-mal')
    else:
        print('A szám nem osztható 3-mal')

feladat19()


def feladat20():

    number = int(input('Adj meg egy számot: '))

    if number<0:
        print('A szám negatív')
    elif number ==0:
        print('A szám nem pozitív és nem negatív')
    else:
        print('A szám pozitív')

feladat20()


def feladat21():

    number_1 = int(input('Adj meg egy számot: '))
    number_2 = int(input('Adj megy egy másik számot: '))

    if number_1 == number_2:
        print(f'{number_1} = {number_2}')
    elif number_1 < number_2:
        print(f'{number_1} < {number_2}')
    else:
        print(f'{number_1} > {number_2}')

feladat22()

def feladat21():

    number = int(input('Adj meg egy számot: '))

    if number >= -30 and number <= 40:
        print('A szám -30 és 40 között van')
    else:
        print('A szám -30 és 40 között nincs benne')

feladat22()


def feladat23():

    score = int(input('Add meg a dolgozat pont számát: '))

    if score >= 0 and score <= 42: print('A dolgozat: Elégtleen')
    elif score >= 43 and score <= 57: print('A dolgozat: Elégséges')
    elif score >= 58 and score <= 72: print('A dolgozat: Közepes')
    elif score >= 73 and score <= 87: print('A dolgozat: Jó')
    elif score >= 88 and score <= 100: print('A dolgozat: Jeles')
    else: print('0-100 között add meg a pontot')


feladat23()


def feladat24():

    settlement = input('Adj meg egy települsé nevet: ')
    person_number = int(input('Add meg a lélekszámot a telpüléshez: '))

    if person_number < 5000: print('Község')
    elif person_number >= 5000 and person_number < 20000: print('kisváros')
    elif person_number >= 20000 and person_number < 100000: print('középváros')
    elif person_number >= 100000 and person_number < 1000000: print('naygváros')
    elif person_number >= 1000000: print('metropolis')
    else: print('Hibás adat bevitel!')

feladat24()
