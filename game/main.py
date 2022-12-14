import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
      print("Esa opci贸n no es v谩lida . El round se anula!!")
      return None, None

    computer_option = random.choice(options)

    print("Computer option =>", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):

    if (user_option, computer_option) == (None, None):
        print("Lee las opciones para el siguiente round")
    elif user_option == computer_option:
        print("Empate!")

    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra 馃拵 gana a tijera 鉁傦笍")
            print("Usuario gan贸!")
            user_wins += 1
        else:
            print("Papel 馃埗 gana a piedra 馃拵")
            print("Computadora gan贸!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel 馃埗 gana a piedra 馃拵")
            print("Usuario gan贸")
            user_wins += 1
        else:
            print("tijera 鉁傦笍 gana a papel 馃埗")
            print("Computadora gan贸!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera 鉁傦笍 gana a papel 馃埗")
            print("Usuario gan贸!")
            user_wins += 1
        else:
            print("piedra 馃拵 gana a tijera 鉁傦笍")
            print("Computadora gan贸!")
            computer_wins += 1
    return user_wins, computer_wins

def conclussion(user_wins, computer_wins):
    if computer_wins == 2:
      print("El ganador es la Computadora!! 馃捇")
      exit()
    if user_wins == 2:
      print("El ganador es el Usuario!! 馃槑")
      exit()

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds=1

    print("""

    Bienvenido Jugador. Preparado para un nuevo reto? 馃幃 Vs 馃幃
    
    馃敟 驴Humano o M谩quina? 馃敟

    Solo lo sabremos con un juego donde se arriesga todo... 

    """)


    while True:

        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)

        print("computer_wins", computer_wins)
        print("user_wins", user_wins)

        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules (user_option, computer_option, user_wins, computer_wins)
        
        conclussion(user_wins, computer_wins)


if __name__ == "__main__":
    run_game()