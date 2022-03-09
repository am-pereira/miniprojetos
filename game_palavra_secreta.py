secreto = "perfume"         # Palavra secreta
digitadas = []              
jogadas = 3                 # Número de erros permitidos

while True:
    if jogadas <= 0:
        print("Você perdeu!!! :(")      # Quando zerar o número de erros o jogo é encerrado
        break
        
    letra = input("Digite uma letra: ")

    if len(letra) > 1 or letra != str(letra) or letra == "":        # Limita o jogo ao uso de apenas letras e somente uma por vez
        print("Opa!!! Você só pode digitar uma letra.")
        continue

    digitadas.append(letra)             # Letra jogada é adicionada à lista "digitadas"

    if letra in secreto:
        print(f"Muito bem!!! A letra {letra} faz parte da palavra.")
    else:
        print(f"Sinto muito, mas o caratere '{letra}' não faz parte da palavra secreta")
        digitadas.pop()

    # Loop exibe a letra jogada quando faz parte da palavra e oculta as demais letras
    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"
    
    # Caso todas as palavras sejam encontrada, encerra o jogo. Caso contrário, mostra a situação atual de letras descobertas
    if secreto_temporario == secreto:
        print(f"Parabéns!!! Você achou a palavra '{secreto_temporario}'.")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")

    if letra not in secreto:    # Se a letra não faz parte da palavra secreta, é decrementado uma jogada.
        jogadas -= 1

    print(f"Você ainda tem {jogadas} jogadas.\n")
