# Programme de jeu de devinette entre 0 à 100

from random import *
nb_essaie = 0

jouer = True

while jouer:
    random_number = randint(0, 100)

    not_found = True
    while not_found:

        print(random_number)
        user_guess = int(input("Quelle numéro devinez-vous?\n"))

        if user_guess < random_number:
            print("Vôtre numéro est trop petit")
            nb_essaie += 1

        elif user_guess > random_number:
            print("Vôtre numéro est trop grand.")
            nb_essaie += 1

        elif user_guess == random_number:
            print(f"Bravo! Vous avez devinez le numéro en {nb_essaie} essaies.")
            rejouer = input("Voulez-vous rejouer? (y/n)")
            if rejouer == "y":
                pass
            elif rejouer == "n":
                break