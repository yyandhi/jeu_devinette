"""
Projet réalisé par Jia Lin Wan gr.403
Programme qui permet à l'utilisateur de deviner un nombre entre deux bornes choisis
"""

from random import randint

jouer = True
rejouer = ""


def jouer_a_nouveau():
    """
    Fonction qui permet de rejouer ou de quitter le programme lorsque l'utilisateur devine le nombre
    """
    global not_found, jouer, rejouer
    rejouer = input("Voulez-vous rejouer? (y/n)")
    not_found = False

    if rejouer == "y":
        jouer = True

    elif rejouer == "n":
        print("Au revoir")
        jouer = False


while jouer:
    borne_minimale = int(input("Borne minimale:"))
    borne_maximale = int(input("Borne maximale:"))

    random_number = randint(borne_minimale, borne_maximale)
    nb_essaie = 1

    not_found = True
    while not_found:
        try:
            user_guess = int(input("Quelle numéro devinez-vous?\n"))
        except ValueError:
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
                jouer_a_nouveau()
