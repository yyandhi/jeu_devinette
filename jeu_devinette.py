# Programme de jeu de devinette entre 0 à 100

from random import *
nb_essaie = 0

jouer = True

while jouer:
    random_number = randint(0, 100)

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
                    nb_essaie == 0

                elif rejouer == "n":
                    print("Au revoir")
                    jouer = False