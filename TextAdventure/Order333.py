from random import randrange
import time
import threading
import os
import pickle
from pathlib import Path


Überlebenschancen = int(1)
Ruestung = int(0)
Leben = int(100)
Health = Leben + Ruestung
Attack = 75
Resourcen = 50
Gegner1Health = 50
Gegner1Attack = 50
Gegner2Health = 100
Gegner2Attack = 75
ergebnis = 0
base_nummer = int(2)
Hunger = 50
count = 1
meat = 5
anbauchecker = 0
feldchecker = 0
my_file = Path('store.pckl')
Sauerstoff = 100
inbase = False
planetfinder = 0
randomplanet = 0
onplanet = False
name = "Default"
computersperre = False
treibstoff = 100
insonde = False
sondezustand = 19
entfernung = 400
roverzustand = 15
roveraktiv = False
sondeaktiv = False
roverlevel = 2
nasaconnection = False


planet_list = []
base_list = []
anbau_list = []
material_list = ['Schraubenzieher']
info_list_marsianer = []
info_list_selbst = []

if Überlebenschancen == 10:
    print("Du hast es geschafft.Eine Sonde wird losgeschickt um dich zu holen")
    print('#####WINNER#####')


def game_base():
    global inbase
    print("Du bist jetzt in deinem selsbtgebauten Unterschlupf.\nWas willst du jetzt machen?")
    inbase = True
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands2:
            Commands2[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")

def get_back():
    global inbase
    inbase = False
    print(ContinueMission())

def testLeben():
    global Leben
    Leben -= 20

def game_sleep():
    global Leben
    print("Du schläfst jetzt")
    Leben = 100
    print("Du hast dich jetzt ausgeruht.Weiter gehts")


def game_help():
    print(Commands.keys())
    print("Wenn du noch mehr Hilfe brauchst besuche unsere Website unter https://Order333.com/help")


def move_walk():
    global Gegner1Attack
    global Gegner1Health
    global Gegner2Attack
    global Gegner2Health
    global Ruestung
    global Attack
    global Resourcen
    global ergebnis
    global Hunger
    global material_list
    global Sauerstoff
    random = randrange(21)
    leben2 = 100
    if random == 0 or random == 1 or random > 16:
        print("Du hast hier nichts gefunden")
    if random == 2:
        print("Du siehst ein Gegner.Willst du kämpfen?")
        answer = str(input("YES or NO\n>"))
        if answer == "YES":

            print("Der Kampf beginnt")
            if Attack > Gegner1Health:
                print("Du hast gewonnen")
            elif Gegner1Attack > Health:
                print("Du hast verloren")
            elif Attack == Gegner1Health:
                print("UNENTSCHIEDEN")
            elif Gegner1Attack == Health:
                print("UNENTSCHIEDEN")
            else:
                print("Beide sind verletzt")

        if answer == "NO":
            print("Du rennst weg.Glück gehabt")
        else:
            print("Das war keine richtige Antwort")
    if random == 3:
        print("Du hast einen Hut gefunden.Das verbessert deine Rüstung")
        if Ruestung > 100:
            print("Maximum der Rüstung erreicht")
        else:
            Ruestung += 10


    if random == 4:
        print("Du hast Steifel gefunden")
        if Ruestung > 100:
            print("Maximum der Rüstung erreicht")
        else:
            Ruestung += 10


    if random == 5:
        print("Du hast eine Panzerbrustplatte gefunden.")
        if Ruestung > 100:
            print("Maximum der Rüstung erreicht")
        else:
            Ruestung += 25

    if random == 6:
        print("Du hast eine Hose gefunden.")
        if Ruestung > 100:
            print("Maximum der Rüstung erreicht")
        else:
            Ruestung += 15

    if random == 7:
        print("Du hast ein Schraubenzieher gefunden.Diesen kann man gut als Waffe verwenden")
        Attack + 10

    if random == 8:
        print("Du hast eine kaputte Pistole gefunden.\nWillst du sie reparieren?Das kostet dich 25 Resourcen\n>")
        answer2 = str(input("YES or NO"))
        if answer2 == "YES":
            if Resourcen >= 25:
                print("Die Pistole ist jetzt repariert.")
                Attack += 50
                Resourcen -= 25
            elif Resourcen < 25:
                print("Du hast leider zu wenige Resourcen.")
        elif answer2 == "NO":
            print("Du hättest es gebrauchen können!")

    if random == 9:
        print("Du hast Gold gefunden")
        Resourcen += 15
        print("Deine Resourcen betragen jetzt " + str(Resourcen))

    if random == 10:
        print("Du hast Diamanten gefunden!")
        Resourcen += 25
        print("Deine Resourcen betragen jetzt " + str(Resourcen))
    if random == 11:
        print("Du hast einen toten Masianer gefunden!Den kann man gut essen!")
        Hunger += 2
    if random == 12:
        print("Du hast 2 mal Holz gefunden!")
        material_list.append('Holz')
        material_list.append('Holz')
    if random == 13:
        print("Du hast ein Eisen gefunden")
        material_list.append('Eisen')
    if random == 14:
        print("Du hast 2 Seil gefunden")
        material_list.append('Seil')
    if random == 15:
        print("Du hast 5 Steine gefunden")
        material_list.append('Stein')
        material_list.append('Stein')
        material_list.append('Stein')
        material_list.append('Stein')
        material_list.append('Stein')
    if random == 16:
        print("Du hast eine Sauerstoffflasche gefunden.")
        Sauerstoff += 20



def game_connection():
    global Überlebenschancen
    rvalue = randrange(11)
    if rvalue <=9:
        print("Connection to earth failed")
    if rvalue == 10:
        print("Du hast eine Verbindung aufgebaut.Deine Überlebenschancen verbessern sich")
        Überlebenschancen += 1

def resourcen():
    print("Deine Aktuellen Resourcen betragen " +str(Resourcen))

def health():
    print(Leben + Ruestung)

def attack():
    print("Dein Angriff beträgt " + str(Attack))

def rüstung():
    print(Ruestung)

def leben():
    print(Leben)

def game_chance():
    print(Überlebenschancen)
    print("Deine Überlebenschance muss mindestens 20 betragen damit du zurück zur Erde kannst")

def baselevel():
    print("Dein BaseLevel beträgt " +str(base_nummer))


def spaceshuttle():
    global base_nummer
    global Überlebenschancen
    if base_nummer == 5 and Überlebenschancen == 20:
        print("SPACESHUTTLE WIRD GESTARTET")
        print("SPACESHUTTLE HEBT AB")
        print("MISSION COMPLETED")
        print("+++++Mission Completed+++++++++")
        print("Du landest auf der Erde und hast überlebt.Glückwunsch!")
    else:
        print("Spaceshuttle konnte nicht gestartet werden")
        print("Deine Basis muss ein Level von 5 haben und deine Überlebenschance muss 20 betragen.")

def exit():
    print("Schalte Computer aus...")
    print("Du bist wieder in deiner Base")
    print(ContinueMission())

def infos():
    global sondezustand
    print("Über was willst du Infos haben?")
    infoinput = str(input("Marsianer,Sonde oder die Erde?\n>"))
    if infoinput == "Marsianer":
        print("Okay...\nInfos werden geladen...")
        print("Wir haben noch keine Infos über die Marsianer erhalten")
    elif infoinput == "Erde":
        print("Okay\nInfos werden geladen..")
        print("Wir haben noch keine Infos über die Marsianer erhalten")
    elif infoinput == "Sonde":
        print("Deine Sonde hat einen Zustand von " +str(sondezustand))
    else:
        print("Infos konnten nicht geladen werden")

def chat():
    print("Verbindung des Chats zwischen dir und Erde werden aufgebaut.\nVerbindung konnte nicht hergestellt werden..")

def computer_help():
    print(Commands3.keys())

Commands3 = {
    'help': computer_help,
    'info': infos,
    'exit': exit,
    'chat': chat

}


def ComputerCommands():
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands3:
            Commands3[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")


def computer():
    global base_nummer
    if base_nummer >= 2:
        print("Du befindest dich jetzt in dem Computer")
        print("CODE erforderlich:")
        codeinput = str(input("Tipp Erscheinungsdatum des Spiels\n"))
        if codeinput == "2020":
            print("ACCES ACCEPT")
            print(ComputerCommands())

        else:
            print("ACCES DENIED")

    else:
        print("Du brauchst ein Basis-Level von über 2")

def base_upgrade():
    global material_list
    global base_nummer
    if 'Holz' in material_list and 'Stein' in material_list and 'Eisen' in material_list and 'Seil' in material_list:
        print("Deine Basis wurde erfolgreich geupgraded!")
        base_nummer += 1
        material_list.remove('Holz')
        material_list.remove('Stein')
        material_list.remove('Eisen')
        material_list.remove('Seil')
    else:
        print("Dir fehlen noch verschiedene Materialien")
        print(material_list)
        print("Das sind deine Materialien")
        print("Insgesamt brauchst du Holz,Stein,Eisen und ein Seil")

def hunger():
    print(Hunger)

def essen():
    global meat
    global Hunger
    if meat > 0:
        print("Du hast etwas gegessen.Jetzt hast du nicht mehr so viel Hunger")
        Hunger += 5
        meat -= 1

def anbau():
    global material_list
    global anbauchecker
    global feldchecker
    if anbauchecker <= 0:
        if 'Holz'  in material_list and 'Glass' in material_list and 'Erde' in material_list:
            print("Du hast ein Feld für Nahrung angebaut")
            feldchecker += 1
            material_list.remove('Holz')
            material_list.remove('Glass')
            material_list.remove('Erde')
        else:
            print("Du hast nicht alle Materialien.Du brauchst Holz,Glass und Erde")


    else:
         print("Du hast schon ein Feld")

def materialien():
    global materialien
    print(materialien)

def help_game():
    print(Commands2.keys())

def save():
    global my_file
    global Überlebenschancen
    global Ruestung
    global Leben
    global Health
    global Attack
    global Resourcen
    global Gegner1Health
    global Gegner1Attack
    global Gegner2Health
    global Gegner2Attack
    global ergebnis
    global base_nummer
    global Hunger
    global count
    global meat
    global anbauchecker
    global feldchecker
    global base_list
    global anbau_list
    global material_list
    if my_file.is_file():
        os.remove(my_file)
        f = open('store.pckl', 'wb')
        pickle.dump(Überlebenschancen, f)
        pickle.dump(Ruestung, f)
        pickle.dump(Leben, f)
        pickle.dump(Health, f)
        pickle.dump(Attack, f)
        pickle.dump(Resourcen, f)
        pickle.dump(ergebnis, f)
        pickle.dump(base_nummer, f)
        pickle.dump(Hunger, f)
        pickle.dump(count, f)
        pickle.dump(meat, f)
        pickle.dump(anbauchecker, f)
        pickle.dump(base_list, f)
        pickle.dump(anbau_list, f)
        pickle.dump(material_list, f)
        f.close()
        print("Erfolgreich gespeichert")
    else:
        f = open('store.pckl', 'wb')
        pickle.dump(Überlebenschancen, f)
        pickle.dump(Ruestung, f)
        pickle.dump(Leben, f)
        pickle.dump(Health, f)
        pickle.dump(Attack, f)
        pickle.dump(Resourcen, f)
        pickle.dump(ergebnis, f)
        pickle.dump(base_nummer, f)
        pickle.dump(Hunger, f)
        pickle.dump(count, f)
        pickle.dump(meat, f)
        pickle.dump(anbauchecker, f)
        pickle.dump(base_list, f)
        pickle.dump(anbau_list, f)
        pickle.dump(material_list, f)
        f.close()
        print("Erfolgreich gespeichert")

def nahrung():
    print(meat)


def sonde():
    global base_nummer
    global treibstoff
    global sondezustand
    global insonde
    global sondeaktiv
    if base_nummer >= 2 and treibstoff >= 20 and sondezustand > 5:
        starten = input("Willst du die Sonde wirklick starten um neue Planeten zu entdecken?\n>")
        if starten == "Ja":
            sondeaktiv = True
            print("Sonde wird gestartet.")
            print("READY FOR LAUNCH")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(2)
            print("START")
            insonde = True
            insonde1()
        elif starten == "NEIN":
            print("ABBRUCH\nSonde wird nicht gestartet")
        else:
            print("Eingabe konnte nicht verstanden werden.Antworte in Ja oder Nein")
            print(sonde())
    else:
        print("Sonde konnte nicht gestartet werden.\nDeine Basis muss ein Level von über 2 haben,\n,mehr Treibstoff als 20 und ein Zustand von über 5 haben")
        print("Dein Basislevel:")
        print(base_nummer)
        print("Dein Treibstoff:")
        print(treibstoff)
        print("Dein Zustand der Sonde")
        print(sondezustand)


def sauerstoff():
    print(Sauerstoff)

def load():
    global my_file
    global Überlebenschancen
    global Ruestung
    global Leben
    global Health
    global Attack
    global Resourcen
    global Gegner1Health
    global Gegner1Attack
    global Gegner2Health
    global Gegner2Attack
    global ergebnis
    global base_nummer
    global Hunger
    global count
    global meat
    global anbauchecker
    global feldchecker
    global base_list
    global anbau_list
    global material_list
    f = open('store.pckl', 'rb')
    Überlebenschancen = pickle.load(f)
    Ruestung = pickle.load(f)
    Leben = pickle.load(f)
    Health = pickle.load(f)
    Attack = pickle.load(f)
    Resourcen = pickle.load(f)
    ergebnis = pickle.load(f)
    base_nummer = pickle.load(f)
    Hunger = pickle.load(f)
    count = pickle.load(f)
    meat = pickle.load(f)
    anbauchecker = pickle.load(f)
    base_list = pickle.load(f)
    anbau_list = pickle.load(f)
    material_list = pickle.load(f)
    f.close()
    print("Erfolgreich geladen")


def onplanet():
    global randomplanet
    global onplanet
    global insonde
    onplanet = True
    print("Du bist jetzt auf deinem Planet "  +str(randomplanet))
    insonde = False
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in PlanetCommands:
            PlanetCommands[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")


def planet():
    global planetfinder
    global randomplanet
    global planet_list
    global insonde
    if planetfinder > 3 or planetfinder ==  0:
        print("Es sind keine Planeten in der Nähe")
        print(insonde2())
    elif planetfinder == 1 or planetfinder == 2 or planetfinder == 3:
        print("Es wurde ein Planet gefunden")
        randomplanet = randrange(4)
        if randomplanet == 0:
            randomplanet = "Nibiru"
        if randomplanet == 1:
            randomplanet = "Coruscant"
        if randomplanet == 2:
            randomplanet = "Titan"
        if randomplanet == 3:
            randomplanet = "Xena"
        if randomplanet == 4:
            randomplanet = "Xena"
        else:
            pass
        print("Dein Planet ist " + str(randomplanet))
        travel = input("Willst du zu dem Planeten reisen?\n>")
        if travel == "Ja":
            planet_list.append(randomplanet)
            print("Okay")
            insonde = False
            print(onplanet())
        if travel == "Nein":
           print("Okay.Du reißt nicht zu dem Planeten")


def find():
    global planetfinder
    print("Suche nach neuen Planeten")
    randomnumber = randrange(11)
    planetfinder = randomnumber
    print(planet())




def mars():
    global insonde
    print("Du kehrst zurück auf den Mars")
    print("Du bist wieder auf dem Mars")
    insonde = False
    print(ContinueMission())



def in_sonde_computer():
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in SondeComputerCommands:
            SondeComputerCommands[command[0]]()


def sonde_computer():
    global name
    global computersperre
    print("Einloggen in Computer..")
    if computersperre == False:
        passwort = str(input("Gebe das Passwort ein.\nTipp:Das Passwort ist dein Name\n:"))
        if name == passwort:
            print("Login erfolgreich")
            computersperre = False
            print(in_sonde_computer())
        else:
            print("Login nicht erfolgreich")
            print("Computer gesperrt")
            computersperre = True
            print(insonde1())
    elif computersperre == True:
        print("Dein Computer ist gesperrt.Da du das letzte mal,dass passwort falsch eingegeben hast.")
        print("Warte noch 20 Sekunden.")
        time.sleep(20)
        print("Starte Computer neu...")
        computersperre = False
        print(sonde_computer())


def sonde_computer_help():
    print(SondeComputerCommands.keys())

def computer_exit():
    print("Computer wird verlassen.")
    print(insonde1())


def planet_infos():
    global planet_list
    print("Auf diesen Planeten warst du schon:")
    print(planet_list)


def zustand():
    global sondezustand
    print("Der Zustand deiner Sonde beträgt " + str(sondezustand))

def erde_entfernung():
    global entfernung
    entfernunginput = input("Willst du die Entfernung zum Mars oder der Erde wissen?\n>")
    if entfernunginput == "Erde":
        entfernung = randrange(400,800)
        print("Deine Entfernung zu Erde beträgt " +str(entfernung) + "km")
    elif entfernunginput == "Mars":
        entfernung = randrange(200, 600)
        print("Deine Entfernung zum Mars beträgt " +str(entfernung) + "km")

SondeComputerCommands = {

    'help': sonde_computer_help,
    'exit': computer_exit,
    'infos': planet_infos,
    'zustand': zustand,
    'entfernung': erde_entfernung

}


def sonde_help():
    print(Sonde_Commands.keys())


def reparieren():
    global sondezustand
    global material_list
    reparierenfrage = input("Was willst du reparieren?\nSonde,....\n>")
    if reparierenfrage == "Sonde":
        if sondezustand < 20 and 'Eisen' in material_list and 'Seil' in material_list and 'Schraubenzieher' in material_list:
            antwortreparieren = input("Willst du deine Sonde wirklich reparieren?\n>")
            if antwortreparieren == "Ja":
                print("Okay deine Sonde wird repariert")
                sondezustand = 20
            elif antwortreparieren == "Nein":
                print("Okay deine Sonde wird nicht repariert")
                print(ContinueMission())

        elif sondezustand == 20:
            print("Deine Sonde hat schon den besten Zustand von 20")

        else:
            print("Du hast nicht alle Materialien\nDu brauchst Eisen,ein Seil und ein Schraubenzieher")
            print("Deine Materialien sind gerade:")
            print(material_list)



def roboter():
    global treibstoff
    global material_list
    global roverzustand
    global roveraktiv
    global roverlevel
    global Überlebenschancen
    global nasaconnection
    if roverzustand <= 15 and roveraktiv == False:
        repariereninput = input("Dein Rover ist aktuell kaputt willst du ihn reparieren?\n>")
        if repariereninput == "Ja":
            if 'Schraubenzieher' in material_list:
                print("Dein Roboter wird repariert.Warte 5 Sekunden.")
                time.sleep(5)
                print("Dein Roboter wurde repariert")
                roverzustand = 20
            else:
                print("Du hast nicht das nötige Equipment")
                print("Du brauchst einen Schraubenzieher.Deine Materialien sind:")
                print(material_list)
        if repariereninput == "Nein":
            print("Schade.Er ist wirklich sehr hilfsvoll")
    else:
        pass

    if roverzustand == 20 and roveraktiv == False:
        startrover = input("Soll der Roboter gestartet werden?")
        if startrover == "Ja":
            if treibstoff >= 25:
                print("Rover wird gestartet,er wird dir viele Informationen sammeln")
                roveraktiv = True

            elif treibstoff < 25:
                print("Du brauchst ein Treibstoff von mindestens 25")
                print("Dein Treibstoff beträgt " +str(treibstoff))
        else:
            print("Dann nicht...")
    elif roverzustand == 20 and roveraktiv == True:
        doroboter = input("Was willst du machen?\nVerbinden...exit\n>")
        if doroboter == 'Verbinden' and roverlevel == 2:
            if nasaconnection == False:
                print("Dein Roboter verbindet sich mit den NASA Servern...")
                print("Verbindung zu den NASA Servern wurde hergestellt.\nDeine Überlebenschancen haben sich um 7 Verbessert.")
                nasaconnection = True
                Überlebenschancen += 7
                print("++++INFO++++")
                print("Die NASA weiß jetzt deinen Standort")
                print("Sie wird dich in nächster Zeit mit Essen versorgen...")
            elif nasaconnection == True:
                print("Es besteht schon eine Verbindung zur Nasa")
            else:
                print("Es ist ein Fehler aufgetreten")
        elif doroboter == 'Verbinden' and roverlevel < 2:
            print("Dein Roboter muss ein Level von mindestens 2 betragen")
        else:
            print("Es ist ein Fehler aufgetreten.")
    else:
        print("Dein Roboter läuft schon")

    #if roveraktiv == True:



def upgrade():
    global roverlevel
    global material_list
    upgradeinput = input("Was willst du Upgraden\nMarsRover,...exit\n>")
    if upgradeinput == 'MarsRover':
        if 'Solarpanel' in material_list and 'MiniComputer' in material_list:
            print("Dein Rover wird geupgraded")
            roverlevel += 1
            print("Dein Rover wurde geupgraded")
            print("Deine Materialien sind jetzt noch:\n")
            print(material_list)
        else:
            print("Du hast nicht genug Materialien\nDu brauchst ein Solarpanel und ein MiniComputer.")
            print("Deine Materialien sind gerade:")
            print(material_list)
    elif upgradeinput == 'exit':
        print("Schließung...")
    else:
        print("Inkorrekte Eingabe.Kehre zurück")
        print(upgrade)





Sonde_Commands = {
    'help': sonde_help,
    'planet': planet,
    'find': find,
    'mars': mars,
    'computer': sonde_computer,



}


Commands2 = {
    'sleep': game_sleep,
    'back': get_back,
    'upgrade': base_upgrade,
    'baselevel': baselevel,
    'spaceshuttle': spaceshuttle,
    'computer': computer,
    'anbau': anbau,
    'help': help_game,
    'materialien': materialien,
    'resourcen': resourcen,
    'health': health,
    'attack': attack,
    'ruestung': rüstung,
    'self':testLeben,
    'leben': leben,
    'chance':game_chance,
    'hunger': hunger,
    'essen': essen,
    'connection': game_connection,
    'nahrung': nahrung,
    'sauerstoff': sauerstoff



}

PlanetCommands = {
    'help': game_help,
    'walk': move_walk,
    'resourcen': resourcen,
    'health': health,
    'attack': attack,
    'ruestung': rüstung,
    'self':testLeben,
    'leben': leben,
    'chance':game_chance,
    'hunger': hunger,
    'essen': essen,
    'save': save,
    'load': load,
    'nahrung': nahrung,
    'sauerstoff': sauerstoff,
    'sonde': sonde,
    'mars': mars



}


Commands = {
    'help': game_help,
    'base': game_base,
    'walk': move_walk,
    'resourcen': resourcen,
    'health': health,
    'attack': attack,
    'ruestung': rüstung,
    'self':testLeben,
    'leben': leben,
    'chance':game_chance,
    'hunger': hunger,
    'essen': essen,
    'save': save,
    'load': load,
    'nahrung': nahrung,
    'sauerstoff': sauerstoff,
    'sonde': sonde,
    'reparieren': reparieren,
    'roboter': roboter,
    'upgrade': upgrade



}


def insonde1():
    global insonde
    print("Du bist jetzt in deiner Sonde.Drücke help für deine Befehle")
    insonde = True
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Sonde_Commands:
            Sonde_Commands[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")


def insonde2():
    global insonde
    insonde = True
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Sonde_Commands:
            Sonde_Commands[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")


def ContinueMission():
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands:
            Commands[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")



def StartMission():

    print("Hello Astronaut.You are lost on the Mars after a failed Mission")
    print("You have to choose between several Options to Survive and go backt to earth.Good Luck")
    print("Press Help to see the Commands")
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands:
            Commands[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")


def essensfeld():
    global feldchecker
    global meat
    while True:
        if feldchecker >= 1:
            meat += 5
            print("Dein Feld hat dir 5 Essensstücke gegeben.")
            time.sleep(60)
        else:
            pass



def Spieler():
    global autosave
    global name
    health = 100
    name = str(input("Wie ist dein Name?\n>"))
    autosave = input("Soll das Spiel alle 15 Minuten automatisch gespeichert werden?\nJa oder Nein\n>")
    if autosave == "Ja":
        print("Das Spiel wird ab jetzt alle 15 Minuten gespeichert")
    elif autosave == "Nein":
        print("Das Spiel wird nicht automatisch gespeichert.")
    else:
        print("Das war keine gültige Antwort")
        print(Spieler())
    print(StartMission())

def Loop():
    global Hunger
    while True:
        Hunger -= 1
        time.sleep(20)

def SauerStoffLoop():
    global Sauerstoff
    global inbase
    while True:
        if inbase == False:
            Sauerstoff -= 1
            time.sleep(10)
        else:
            pass

def HungerLoop():
    global Hunger
    while True:
        if Hunger >= 50:
            Hunger = 50
        else:
            pass

def roverloop():
    global roveraktiv
    global info_list_marsianer
    global info_list_selbst
    global name
    global Überlebenschancen
    if roveraktiv == True:
        time.sleep(120)
        roverinfo = randrange(11)
        if roverinfo == 1:
            info_list_marsianer.append('Stärke:50')
        if roverinfo == 2:
            info_list_marsianer.append('Leben:50')
        if roverinfo == 3:
            info_list_marsianer.append('Vorhanden: > 100')
        if roverinfo == 4:
            info_list_marsianer.append('Gefahr:Gering')
        if roverinfo == 5:
            info_list_marsianer.append('Waffen:UNBEKANNT')
        if roverinfo == 6:
            info_list_selbst.append('Dein Name: ' + name)
        if roverinfo == 7:
            info_list_selbst.append('Deine Überlebenschance:' +str(Überlebenschancen))
        if roverinfo == 8:
            info_list_selbst.append('Connection Status: ERROR404')
        if roverinfo == 9:
            if sondeaktiv == False:
                info_list_selbst.append('Sonde nicht aktiv')
            elif sondeaktiv == True:
                if 'Sonde nicht aktiv' in info_list_selbst:
                    info_list_selbst.remove('Sonde nicht aktiv')
                    info_list_selbst.append('Sonde ist aktiv')
                else:
                    info_list_selbst.append('Sonde ist aktiv')
            else:
                info_list_selbst.append('Sondenstatus nicht erkennbar...')


    else:
        pass

def saveloop():
    global autosave
    global my_file
    global Überlebenschancen
    global Ruestung
    global Leben
    global Health
    global Attack
    global Resourcen
    global Gegner1Health
    global Gegner1Attack
    global Gegner2Health
    global Gegner2Attack
    global ergebnis
    global base_nummer
    global Hunger
    global count
    global meat
    global anbauchecker
    global feldchecker
    global base_list
    global anbau_list
    global material_list
    while True:
        time.sleep(900)
        if autosave == "Ja":
            print("Das Spiel wird alle 15 Minuten gespeichert")
            if my_file.is_file():
                os.remove(my_file)
                f = open('store.pckl', 'wb')
                pickle.dump(Überlebenschancen, f)
                pickle.dump(Ruestung, f)
                pickle.dump(Leben, f)
                pickle.dump(Health, f)
                pickle.dump(Attack, f)
                pickle.dump(Resourcen, f)
                pickle.dump(ergebnis, f)
                pickle.dump(base_nummer, f)
                pickle.dump(Hunger, f)
                pickle.dump(count, f)
                pickle.dump(meat, f)
                pickle.dump(anbauchecker, f)
                pickle.dump(base_list, f)
                pickle.dump(anbau_list, f)
                pickle.dump(material_list, f)
                f.close()
                print("Erfolgreich gespeichert")
            else:
                f = open('store.pckl', 'wb')
                pickle.dump(Überlebenschancen, f)
                pickle.dump(Ruestung, f)
                pickle.dump(Leben, f)
                pickle.dump(Health, f)
                pickle.dump(Attack, f)
                pickle.dump(Resourcen, f)
                pickle.dump(ergebnis, f)
                pickle.dump(base_nummer, f)
                pickle.dump(Hunger, f)
                pickle.dump(count, f)
                pickle.dump(meat, f)
                pickle.dump(anbauchecker, f)
                pickle.dump(base_list, f)
                pickle.dump(anbau_list, f)
                pickle.dump(material_list, f)
                f.close()
                print("Erfolgreich gespeichert")
                time.sleep(900)


def sondezustandloop():
    global sondezustand
    global insonde
    while True:
        if sondezustand <= 0 and insonde == True:
            print("Sonde würde zerstört.")
            print("Du bist gestorben")
            exit()

def meterioitloop():
    global insonde
    global sondezustand
    while True:
        if insonde == False:
            pass
            time.sleep(10)

        elif insonde == True:
            meterioit = randrange(21)
            if meterioit > 1:
                pass
                time.sleep(5)
            elif meterioit == 1:
                print("++++++++++Achtung++++++++++")
                print("Meterioit wurde gesichtet")
                print("++++++++++Achtung++++++++++")
                print("Sonde wurde getroffen")
                sondezustand -= 5
                print("Landen sie auf einem Planeten und reparieren sie dort die Sonde")
                print("Notlandung muss in den nächsten 20 Sekunden erfolgen")
                if insonde == True:
                    sondezustand -= 5
                    time.sleep(6)
                    sondezustand -= 5
                    time.sleep(6)
                    sondezustand -= 5
                    time.sleep(6)

                else:
                    pass



def essenloop():
    global Hunger
    while True:
        if Hunger <= 0:
            print("Du bist verhungert")
            exit(0)
        else:
            pass


def sauerstoff():
    global Sauerstoff
    if Sauerstoff >= 100:
        Sauerstoff = 100



def Menu():
    print("#######################")
    print("########Start##########")
    print("#######Return##########")
    c = str(input("#######################\n>"))
    if c == "Start":
        print("Lets go")
        print(Spieler())
    elif c == "Return":
        print("Schade")
        exit(0)

b = threading.Thread(name='Loop', target=Loop)
k = threading.Thread(name='sondezustand', target=sondezustandloop)
l = threading.Thread(name='meterioitloop', target=meterioitloop)
s = threading.Thread(name='saveloop', target=saveloop)
d = threading.Thread(name='essenloop', target=essenloop)
h = threading.Thread(name='sauerstoff', target=SauerStoffLoop)
a = threading.Thread(name='essenfeld', target=essensfeld)
c = threading.Thread(name='hungerloop', target=HungerLoop)
f = threading.Thread(name='Menu', target=Menu)


c.start()
s.start()
h.start()
a.start()
d.start()
k.start()
l.start()
b.start()
f.start()
