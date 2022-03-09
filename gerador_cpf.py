from random import randint


numero = str(randint(100000000, 999999999)) # Gera os 9 primeiros números do CPF (aleatório)

novo_cpf = numero     # Recebe os 9 dígitos do CPF
reverso = 10          # Contador reverso
total = 0


# Loop do CPF
for index in range(19):
    if index > 8:        
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1            # Decrementa o contador
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0           # Zera o total
        novo_cpf += str(d)  # Concatena o dígito gerado na variável novo_cpf

print(novo_cpf)
