import pyautogui as pag,time,random
from msvcrt import getch
import os

keymap = {}

px = (87,87,86)
px2= (82,82,82)
px3 = (216, 183, 79)
px4 = (221, 193, 104)

currentmoney = 117000

players = [
# ('McGeady','1200')
# ('Ben Arfa','5000')
# ,('Boufal','1200')
# ('Bolasie','8500')
# ,('Kishna','900')
# ,('Krychowiak','9000')
# ,('Fellaini','2200')
# ,('Deulofeu','2400')
# ,('Benteke','8800')
# ,('Lukaku','6800')
# ,('Origi','900')
# ,('Ibarbo','9000')
# ,('Lennon','1000')
# ,('Townsend','1200')
# ,('Campbell','3000')
# ,('Oxlade','4900')
# ,('Mirallas','6500')
# ,('Dembele','8000')
('Aubameyang','8200'),
('Douglas Costa','11500'),
('Dybala','3500'),
('Gotze','2600'),
('Hulk','3300'),
('Iniesta','23000'),
('Isco','2000'),
('Kroos','8200'),
('Lacazette','6200'),
('Lewandowski','38000'),
('Marcelo','5000'),
('Matic','1000'),
('Pedro','900'),
('Pepe','1100'),
('Rakitic','2500'),
('Ramires','2800'),
('Schweinsteiger','3200'),
('Sterling','4100'),
('Sturridge','6500')

]


def shiftloc(loc,shift):
    return (loc[0]+shift[0],loc[1]+shift[1])


def find_and_shift(image,shift=(0,0)):
    loc = pag.locateCenterOnScreen(image)
    return shiftloc(loc,shift)

def enter_name(name):
    pag.click(keymap['discard'])
    pag.click(keymap['name'])
    pag.typewrite(name,0.02)
    pag.press('enter')


def enter_bin(bin):
    pag.moveTo(keymap['bin'],duration=0.2)
    pag.click()
    pag.press('backspace',6)
    pag.typewrite(bin,0.1)
    pag.press('enter')


def click_search():
    pag.click(keymap['search'])
    time.sleep(0.3)


def click_ok():
    x,y = keymap['ok']
    print(pag.pixel(x,y))
    pag.click(keymap['ok'])



def click_player():
    x,y = keymap['player']
    pag.moveTo(x,y,0.3)
    pag.click()
    time.sleep(0.5)


def click_buynow():
    pag.click(keymap['buynow'])
    time.sleep(0.5)


def click_cancel():
    x,y = keymap['binok']
    pag.click(x+50,y)
    time.sleep(0.5)


def click_back():
    pag.click(keymap['back'])
    time.sleep(2.0)

def click_discard():
    pag.click(keymap['discard'])

def click_binok():
    pag.click(keymap['binok'])
    time.sleep(0.5)

def testPix():
    x,y = samplepos
    pag.moveTo(x,y,0.1)
    px = pag.pixel(x,y)
    return px==sample


def testPix2():
    x,y = keymap['ok']
    pix = pag.pixel(x,y)
    return pix==px



def wait_for_response():
    while testPix2():
        time.sleep(0.1)
    time.sleep(0.3)

def initButtonsCords():
    global keymap

    text = find_and_shift('playername.png')
    keymap['name'] = shiftloc(text,(-50,0))

    keymap['discard'] = shiftloc(text,(-20,0))

    bin = find_and_shift('bin.png', (-60, 70))
    keymap['bin'] = bin

    search = find_and_shift('search.png')
    keymap['search'] = search
    x,y = search

    enter_name('Schweinsteiger')

    enter_bin('200')
    click_search()
    time.sleep(1)

    ok = find_and_shift('ok.png')
    keymap['ok'] = ok


    click_ok()

    enter_bin('0')
    click_search()
    time.sleep(1)

    cmb = find_and_shift('player.png')
    player = shiftloc(cmb,(-20,50))
    back = shiftloc(cmb,(50,0))
    keymap['back'] = back
    keymap['player'] = player
    click_player()

    global samplepos
    samplepos = pag.position()
    global sample
    x,y = samplepos
    sample = pag.pixel(x,y)

    buynow = find_and_shift('buynow.png')
    keymap['buynow'] = buynow

    click_buynow()

    binok = find_and_shift('binok.png')
    keymap['binok'] = binok

    click_cancel()

    click_back()

    x,y = keymap['player']


def notfound():
    x,y = keymap['player']
    pix = pag.pixel(x,y)
    return px2==pix

def checkIfInterrupted():
    time.sleep(0.5)
    x,y = keymap['search']
    if not pag.pixelMatchesColor(x+20,y,px3,25):
        print(px3,pag.pixel(x+20,y))
        print("error ocured")
        exit()

def tryBuyingPlayer(player,price):
    binprice = str(min(int(price),currentmoney))
    time.sleep(0.5 + random.random()/2)
    click_discard()
    enter_name(player)
    enter_bin(binprice)
    click_search()
    wait_for_response()
    if notfound():
        click_ok()
        return
    if not testPix():
        click_player()
    click_buynow()
    click_binok()
    click_ok()
    time.sleep(0.2)
    click_back()

initButtonsCords()




while True:
    name,price = random.choice(players)
    print(name,price)
    checkIfInterrupted()
    tryBuyingPlayer(name,price)
    










