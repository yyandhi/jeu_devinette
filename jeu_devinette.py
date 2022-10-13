# Programme de jeu de devinette entre 0 à 100
#allosg4r

from random import *

jouer = True

while jouer:
    random_number = randint(0, 100)
    nb_essaie = 1

    not_found = True
    while not_found:

        try:
            user_guess = int(input("Quelle numéro devinez-vous?\n"))

        except:
            print("Veuillez ecrire un nombre s'il vous plaît.")

        else:

            if user_guess < random_number:
                print("Vôtre numéro est trop petit")
                nb_essaie += 1

            elif user_guess > random_number:
                print("Vôtre numéro est trop grand.")
                nb_essaie += 1

            elif user_guess == random_number:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essaie} essaies.")
                rejouer = input("Voulez-vous rejouer? (y/n)")
                not_found = False

                if rejouer == "y":
                    jouer = True

                elif rejouer == "n":
                    print("Au revoir")
                    jouer = False