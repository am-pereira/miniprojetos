secreto = "perfume"
digitadas = []
jogadas = 3

while True:
    if jogadas <= 0:
        print("Você perdeu!!! :(")
        break
        
    letra = input("Digite uma letra: ")

    if len(letra) > 1 or letra != str(letra) or letra == "":
        print("Opa!!! Você só pode digitar uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"Muito bem!!! A letra {letra} faz parte da palavra.")
    else:
        print(f"Sinto muito, mas o caratere '{letra}' não faz parte da palavra secreta")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"Parabéns!!! Você achou a palavra '{secreto_temporario}'.")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")

    if letra not in secreto:
        jogadas -= 1

    print(f"Você ainda tem {jogadas} jogadas.\n")
