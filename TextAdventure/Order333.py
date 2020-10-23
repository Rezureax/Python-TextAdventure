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
base_nummer = int(0)
Hunger = 50
count = 1
meat = 5
anbauchecker = 0
feldchecker = 0
my_file = Path('store.pckl')



base_list = []
anbau_list = []
material_list = []

if Überlebenschancen == 10:
    print("Du hast es geschafft.Eine Sonde wird losgeschickt um dich zu holen")
    print('#####WINNER#####')


def game_base():
    print("Now, you are in your little selfbuild base.What do you want to do?")
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands2:
            Commands2[command[0]]()
        else:
            print("You run around in circles and don't know what to do.")

def get_back():
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
    random = randrange(21)
    leben2 = 100
    if random == 0 or random == 1 or random > 15:
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
        print("Du hast eine kaputte Pistole gefunden.\nWillst du sie reparieren?Das kostet dich 25 Resourcen")
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
    print("Über was willst du Infos haben?")
    infoinput = str(input("Marsianer oder die Erde?\n>"))
    if infoinput == "Marsianer":
        print("Okay...\nInfos werden geladen...")
        print("Wir haben noch keine Infos über die Marsianer erhalten")
    elif infoinput == "Erde":
        print("Okay\nInfos werden geladen..")
        print("Wir haben noch keine Infos über die Marsianer erhalten")
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
    'load': load



}

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
    health = 100
    name = input("Wie ist dein Name?\n>")
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

def HungerLoop():
    global Hunger
    while True:
        if Hunger >= 50:
            Hunger = 50
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



def essenloop():
    global Hunger
    while True:
        if Hunger <= 0:
            print("Du bist verhungert")
            exit(0)
        else:
            pass

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
s = threading.Thread(name='saveloop', target=saveloop)
d = threading.Thread(name='essenloop', target=essenloop)
a = threading.Thread(name='essenfeld', target=essensfeld)
c = threading.Thread(name='hungerloop', target=HungerLoop)
f = threading.Thread(name='Menu', target=Menu)


c.start()
s.start()
a.start()
d.start()
b.start()
f.start()
