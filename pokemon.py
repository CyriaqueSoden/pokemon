import random

liste = [["pika", 50, 10, 10, 10], ["pskycokouak", 1, 50, 70, 5],
         ["drakofeu", 50, 10, 5, 20], ["electron", 20, 25, 30, 15]]


def new_pokemon():
    pourcent = random.randint(1, 100)
    nb_liste = random.randint(1, len(liste)) - 1
    while True:
        if liste[nb_liste][1] >= pourcent:
            return liste[nb_liste]
        else:
            pourcent = random.randint(1, 100)
            nb_liste = random.randint(1, len(liste)) - 1


rando_pokemon = new_pokemon()

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


pokeballs = [["pokeball", 30,200], ["superball", 50,600],
             ["hyperball", 70,1200], ["masterball", 100,50000]]

inventaire = [[["pokeball", 0], ["superball", 0],
               ["hyperball", 0], ["masterball", 0]], [], [0]]


def capture():
    pc_capture = random.randint(1, 100)
    if pokeballs[0][1] <= pc_capture:
        pc_capture = random.randint(1, 100)
        if rando_pokemon[2] <= pc_capture:
            print("the ", rando_pokemon[0], " in the pocket")
            inventaire[1].append(rando_pokemon)
        else:
            print("bonobo gameplay ,", rando_pokemon[0], "est parti")
    else:
        print("bonobo gameplay ,", rando_pokemon[0], "est partie")


def combat():
    if not inventaire[1]:
        print("pas de pokemon")
        return 0
    if random.randint(0, int(inventaire[1][0][3]/inventaire[1][0][4])) == random.randint(0, int(rando_pokemon[3]/rando_pokemon[4])):
        argent_gagne = random.randint(1, 2000)
        print("combat gagné , vous remporter ", argent_gagne, "$")
        return argent_gagne
    else:
        print("combat perdu")
        return 0

def shop() :
    for i in range(len(inventaire[0])):
        print(inventaire[0][i] , pokeballs[i][2], "$")
    print("Que voulez vous acheter ? solde :", inventaire[2] ,"$")
    type = input(str())
    for j in range(len(inventaire[0])):
        if type == (inventaire[0][j][0]) :
            inventaire[2][0] -= pokeballs[j][2]
            inventaire[0][j][1] += 1
            print("vous avez acheté : 1" ,pokeballs[j][0] ,"(" ,pokeballs[j][2] ,"$)")


def menu() :
    print( " shop (1) \n spawn (2) \n inventaire objets (3) \n inventaire pokemon(4)")
    choix_menu = input(str())

    if choix_menu == "1" :
        shop()

    if choix_menu == "2" :
        print("combat (1) ou capture (2) ?")
        choix_combat = input(str())
        if choix_combat == "1" :
            combat()
        if choix_combat == "2" :
            capture()
    if choix_menu == "3" :
        for i in range(len(inventaire[0])):
            print(inventaire[0][i])
        

    if choix_menu == "4" :
        if not inventaire[1] :
            print("pas de pokemon")
            return 0
        for i in range(len(inventaire[0])):
            print(inventaire[1])







menu()





















#            comment calculer le % de chance de spawn
#            % /(100/nb_total_de_%)
