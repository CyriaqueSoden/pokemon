import random

# import pour clear()
from os import system, name
from time import sleep

liste = [["pika", 50, 10, 10, 10], ["pskycokouak", 1, 50, 70, 5],
         ["drakofeu", 50, 10, 5, 20], ["electron", 20, 25, 30, 15]]

POKEBALLS = [["pokeball", 30, 200], ["superball", 50, 600],
             ["hyperball", 70, 1200], ["masterball", 100, 50000]]

inventaire = [[["pokeball", 0], ["superball", 0],
               ["hyperball", 0], ["masterball", 0]], [], [100000000000000]]


def clear():

    if name == 'nt':
        _ = system('cls')


def new_pokemon():
    pourcent = random.randint(1, 100)
    nb_liste = random.randint(1, len(liste)) - 1
    while True:
        if liste[nb_liste][1] >= pourcent:
            return liste[nb_liste]
        else:
            pourcent = random.randint(1, 100)
            nb_liste = random.randint(1, len(liste)) - 1


# calcule des % de spawn des pokemons


# count = [0]len(liste)

# for i in range(10000):
#    poke = new_pokemon()
#    for j in range(len(liste)) :
#        if liste[j][0] == poke :
#            count[j] += 1

#total = 0

# for i in range(len(liste)) :
#    total += liste[i][1]

# for i in range(len(count)) :
#            print( count[i]//100,  "%    " , int((liste[i][1])(100/total)) , "%")


def capture():
    print(rando_pokemon)
    print("quelle pokeball utiliser ?")
    for i in range(len(inventaire[0])):
        print(inventaire[0][i], "(", i, ")")
    quelle_pokeball = input(str())
    if quelle_pokeball == "q":
        return menu()
    if inventaire[0][int(quelle_pokeball)][1] == 0:
        clear()
        print("pas de ", inventaire[0][int(quelle_pokeball)][0])
        return capture()
    inventaire[0][int(quelle_pokeball)][1] -= 1
    if quelle_pokeball == "3":
        print("réussi ", rando_pokemon[0], " est dans l'inventaire")
        inventaire[1].append(rando_pokemon)
        return go_menu()
    pc_capture = random.randint(1, 100)
    if POKEBALLS[int(quelle_pokeball)][1] <= pc_capture:
        pc_capture = random.randint(1, 100)
        if rando_pokemon[2] <= pc_capture:
            print("réussi ", rando_pokemon[0], " est dans l'inventaire")
            inventaire[1].append(rando_pokemon)
            return go_menu()
        else:
            print("raté ,", rando_pokemon[0], "est parti")
            return go_menu()
    else:
        print("raté ,", rando_pokemon[0], "est partie")
        return go_menu()


def combat():
    print("quel pokemon utiliser ?")
    for i in range(len(inventaire[1])):
        print(inventaire[1][i][0] , i)
    nb_pokemon_used = str(input())
    if nb_pokemon_used == "q" :
        return menu()
    if not inventaire[1]:
        print("pas de pokemon")
        return 0
    if not inventaire[1][int(nb_pokemon_used)] :
        print("pokemon non existant")
        return combat()
    
    if random.randint(0, int(inventaire[1][int(nb_pokemon_used)][3]/inventaire[1][int(nb_pokemon_used)][4])) == random.randint(0, int(rando_pokemon[3]/rando_pokemon[4])):
        argent_gagne = random.randint(1, 2000)
        print("combat gagné , vous remporter ", argent_gagne, "$")
        inventaire[2][0] += argent_gagne
        return go_menu()
    else:
        print("combat perdu")
        return go_menu()


def shop():
    for i in range(len(inventaire[0])):
        print(inventaire[0][i], POKEBALLS[i][2], "$")
    print("Que voulez vous acheter ? solde :", inventaire[2], "$")
    type = input(str())
    if type == "q":
        return menu()
    for j in range(len(inventaire[0])):
        if type == (inventaire[0][j][0]):
            inventaire[2][0] -= POKEBALLS[j][2]
            inventaire[0][j][1] += 1
            clear()
            print("vous avez acheté : 1",
                  POKEBALLS[j][0], "(", POKEBALLS[j][2], "$)")
    return shop()


def menu():
    clear()
    print("""\
                                          
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|""")

    print(" shop (1) \n spawn (2) \n inventaire objets (3) \n inventaire pokemon(4) \n q pour quitter n'importe quelle question")
    choix_menu = input(str())

    if choix_menu == "1":
        clear()
        shop()

    if choix_menu == "2":
        clear()
        rando_pokemon = new_pokemon()
        print(rando_pokemon)
        print("combat (1) ou capture (2) ?")
        choix_combat = input(str())
        if choix_combat == "q":
            return menu()
        if choix_combat == "1":
            clear()
            combat()
        if choix_combat == "2":
            clear()
            capture()

    if choix_menu == "3":
        for i in range(len(inventaire[0])):
            print(inventaire[0][i])
        print(inventaire[2][0], "$")
        return go_menu()

    if choix_menu == "4":
        clear()
        if not inventaire[1]:
            print("pas de pokemon")
            return 0
        for i in range(len(inventaire[1])):
            print(inventaire[1])
        return go_menu()


def go_menu():
    blbl = input(str())
    if blbl == "q" or not blbl:
        menu()


clear()
rando_pokemon = new_pokemon()
inventaire[1].append(new_pokemon())
inventaire[1].append(new_pokemon())
inventaire[1].append(new_pokemon())
inventaire[1].append(new_pokemon())

menu()


#            comment calculer le % de chance de spawn
#            % /(100/nb_total_de_%)
