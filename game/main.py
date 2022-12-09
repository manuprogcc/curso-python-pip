import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
      print("Esa opción no es válida . El round se anula!!")
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
            print("piedra 💎 gana a tijera ✂️")
            print("Usuario ganó!")
            user_wins += 1
        else:
            print("Papel 🈶 gana a piedra 💎")
            print("Computadora ganó!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel 🈶 gana a piedra 💎")
            print("Usuario ganó")
            user_wins += 1
        else:
            print("tijera ✂️ gana a papel 🈶")
            print("Computadora ganó!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera ✂️ gana a papel 🈶")
            print("Usuario ganó!")
            user_wins += 1
        else:
            print("piedra 💎 gana a tijera ✂️")
            print("Computadora ganó!")
            computer_wins += 1
    return user_wins, computer_wins

def conclussion(user_wins, computer_wins):
    if computer_wins == 2:
      print("El ganador es la Computadora!! 💻")
      exit()
    if user_wins == 2:
      print("El ganador es el Usuario!! 😎")
      exit()

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds=1

    print("""

    Bienvenido Jugador. Preparado para un nuevo reto? 🎮 Vs 🎮
    
    🔥 ¿Humano o Máquina? 🔥

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