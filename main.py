import random
words = ["secret", "gucci", "prada", "nike", "password", "classroom", "night", "cuban", "california", "silver", "fish", "gold", "ice", "get", "data", "cat", "dog", "set", "shady", "darkness", "door", "coffee", "habbit", "crazy", "love", "miss"]
p_secreta = random.choice(words)
digitados = []
chances = 3

print("Welcome to the game!")
print("You have 3 chances to got it right the secret word. Good luck!\n")

while True:
    if chances == 0:
        print("GAME OVER! Your chances are over!")
        break

    chute = input("Type a letter: ")
    if len(chute) > 1:
        print("Invalid! Type just a letter!")
        continue

    elif chute == "":
        print("Invalid! Type a letter!")

    elif chute in p_secreta:
        print(f"You're right! The letter '{chute}' is in the secret word.")
        digitados.append(chute)
        s_temp = ""
        for letra in p_secreta:
            if letra in digitados:
                s_temp += letra
            else:
                s_temp += "*"

        print(s_temp,"\n")

        if s_temp.count("*") == 0:
            print("You find the secret word!")
            print(f"The secret word was '{p_secreta}'")
            print("Congratulations!")
            break

    else:
        print(f"You're wrong! The letter '{chute}' is not in the secret word.")
        s_temp = ""
        for letra in p_secreta:
            if letra in digitados:
                s_temp += letra
            else:
                s_temp += "*"
        print(s_temp)
        chances = chances-1
        print(f"You still have {chances} chances.\n")

print("Jogo finalizado")