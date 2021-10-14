# region import

import random
# import for clear()
from os import system, name
from time import sleep

# endregion

# region instantiation

liste = [["pika", 50, 10, 10, 10], ["pskycokouak", 1, 50, 70, 5],
         ["drakofeu", 50, 10, 5, 20], ["electron", 20, 25, 30, 15]]

POKEBALLS = [["pokeball", 30, 200], ["superball", 50, 600],
             ["hyperball", 70, 1200], ["masterball", 100, 50000]]

inventory = [[["pokeball", 0], ["superball", 0],
              ["hyperball", 0], ["masterball", 0]], [   ], [0]]

# endregion

# region def fonction

#reset the cmd so its clean
def clear():

    if name == 'nt':
        _ = system('cls')

#generate a random pokemon using liste
def new_pokemon():
    percentage = random.randint(1, 100)
    start_in_liste = random.randint(1, len(liste)) - 1
    while True:
        if liste[start_in_liste][1] >= percentage:
            return liste[start_in_liste]
        else:
            percentage = random.randint(1, 100)
            start_in_liste = random.randint(1, len(liste)) - 1

#try to catch a random pokemon created in menu() -> 2 using the pokeball the user choose 
def catch():
    print(random_pokemon)
    print("quelle pokeball utiliser ?")
    for i in range(len(inventory[0])):
        print(inventory[0][i], "(", i, ")")
    pokeball_used = input(str())
    if pokeball_used == "q":
        return menu()
    if inventory[0][int(pokeball_used)][1] == 0:
        clear()
        print("pas de ", inventory[0][int(pokeball_used)][0])
        return catch()
    inventory[0][int(pokeball_used)][1] -= 1
    if pokeball_used == "3":
        print("réussi ", random_pokemon[0], " est dans l'inventory")
        inventory[1].append(random_pokemon)
        return go_menu()
    capture_percentage = random.randint(1, 100)
    if POKEBALLS[int(pokeball_used)][1] <= capture_percentage:
        capture_percentage = random.randint(1, 100)
        if random_pokemon[2] <= capture_percentage:
            print("réussi ", random_pokemon[0], " est dans l'inventory")
            inventory[1].append(random_pokemon)
            return go_menu()
        else:
            print("raté ,", random_pokemon[0], "est parti")
            return go_menu()
    else:
        print("raté ,", random_pokemon[0], "est partie")
        return go_menu()

#fight a random pokemon created in menu() -> 2 using the pokemon the user choose and give you money if you win
def combat():
    print("quel pokemon utiliser ?")
    for i in range(len(inventory[1])):
        print(inventory[1][i][0], i)
    id_pokemon_used = str(input())
    if id_pokemon_used == "q":
        return menu()
    if not inventory[1]:
        print("pas de pokemon")
        return 0
    if not inventory[1][int(id_pokemon_used)]:
        print("pokemon non existant")
        return combat()

    if random.randint(0, int(inventory[1][int(id_pokemon_used)][3]/inventory[1][int(id_pokemon_used)][4])) == random.randint(0, int(random_pokemon[3]/random_pokemon[4])):
        money_earned = random.randint(1, 2000)
        print("combat gagné , vous remporter ", money_earned, "$")
        inventory[2][0] += money_earned
        return go_menu()
    else:
        print("combat perdu")
        return go_menu()

#allow the user to buy pokeballs if he has enough money
def shop():
    for i in range(len(inventory[0])):
        print(inventory[0][i], POKEBALLS[i][2], "$")
    print("Que voulez vous acheter ? solde :", inventory[2], "$")
    id_pokeball_buying = input(str())
    if id_pokeball_buying == "q":
        return menu()
    for j in range(len(inventory[0])):
        if id_pokeball_buying == (inventory[0][j][0]):
            inventory[2][0] -= POKEBALLS[j][2]
            inventory[0][j][1] += 1
            clear()
            print("vous avez acheté : 1",
                  POKEBALLS[j][0], "(", POKEBALLS[j][2], "$)")
    return shop()

#the start menu
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

    print(" shop (1) \n spawn (2) \n inventory objets (3) \n inventory pokemon(4) \n q pour quitter n'importe quelle question")
    menu_choice = input(str())

    if menu_choice == "1":
        clear()
        shop()

    if menu_choice == "2":
        clear()
        random_pokemon = new_pokemon()
        print(random_pokemon)
        print("combat (1) ou catch (2) ?")
        combat_choice = input(str())
        if combat_choice == "q":
            return menu()
        if combat_choice == "1":
            clear()
            combat()
        if combat_choice == "2":
            clear()
            catch()

    if menu_choice == "3":
        for i in range(len(inventory[0])):
            print(inventory[0][i])
        print(inventory[2][0], "$")
        return go_menu()

    if menu_choice == "4":
        clear()
        if not inventory[1]:
            print("pas de pokemon")
            return 0
        for i in(inventory[1]):
            print(i)
        return go_menu()


def go_menu():
    go_menu_key = input(str())
    if go_menu_key == "q" or not go_menu_key:
        menu()

# endregion

# region code starter
clear()
random_pokemon = new_pokemon()
inventory[1].append(new_pokemon())
inventory[1].append(new_pokemon())
inventory[1].append(new_pokemon())
inventory[1].append(new_pokemon())

menu()

# endregion

# region percentage_finder
#            comment calculer le % de chance de spawn
#            A /(100/B + A)
#
#            A = % de spawn voulu pour le pokemon
#            B = somme de tous les % de spawn des pokemons deja existant
#            
def percentage_finder() :
    print("Quel chance de spawn voulez vous ?")
    a = int(input())
    b = 0
    for i in range(len(liste)) :
        b += liste[i][1]
    result = a /(100/(b + a))
    print("le vrai nombre a utiliser est " ,result)

#endregion
