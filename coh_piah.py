import re
def main():
    ass_main = le_assinatura()
    textos_main = le_textos()
    matriz_ass = calcula_assinatura(textos_main)
    ass_comparadas = compara_assinatura(ass_main, matriz_ass)
    copiah = avalia_textos(textos_main, ass_comparadas) + 1
    return print(f"O autor do texto {copiah} está infectado com COH-PIAH.")


def le_assinatura():
    """
    A função lê os valores dos traços linguísticos do modelo e devolve uma
    assinatura a ser comparada com os textos fornecidos.
    """
    print("Bem-vindo ao detector automático de COH-PIAH.")

    tam_m_pal = float(input("Entre o tamanho medio de palavra: "))
    type_token = float(input("Entre a relação Type-Token: "))
    h_lego = float(input("Entre a Razão Hapax Legomana: "))
    tam_m_sent = float(input("Entre o tamanho médio de sentença: "))
    compx_med = float(input("Entre a complexidade média da sentença: "))
    tam_m_frase = float(input("Entre o tamanho medio de frase: "))

    return [tam_m_pal, type_token, h_lego, tam_m_sent, compx_med, tam_m_frase]


def le_textos():
    i = 1
    textos = []
    texto = input(f"Digite o texto {str(i)} (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f"Digite o texto {str(i)} (aperte enter para sair): ")

    return textos


def calcula_assinatura(texto):
    """
    Essa função recebe um texto e deve devolver a assinatura
    do texto.
    """
    if type(texto) != list:
        aux = texto
        texto = []
        texto.append(aux)
    matriz_ass_input = []
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(i)  # sentenças = lista comum, ~matriz
        frases = []
        num_tot_sentencas = 0
        soma_cat_sentencas = 0
        for i in range(len(sentencas)):
            frase_i = separa_frases(sentencas)
            frases.append(frase_i)  # frases = matriz, lista de listas
            num_tot_sentencas += 1
            soma_cat_sentencas = soma_cat_sentencas + len(sentencas)
        palavras = []
        num_tot_frases = 0
        soma_cat_frases = 0
        for lin in range(len(frases)):
            for col in range(len(frases[lin])):
                palavra_i = separa_palavras(frases[lin][col])
                palavras.append(palavra_i)  # palavras = matriz, lista de listas
                num_tot_frases += 1
                soma_cat_frases = soma_cat_frases + len(str(frases[lin][col]))
        mtrx_para_lista = []  # transforma palavras de matriz para lista
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                mtrx_para_lista.append(palavras[lin][col])
        palavras = mtrx_para_lista[:]
        soma_comp_palavras = 0
        num_tot_palavras = 0
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                soma_comp_palavras = soma_comp_palavras + len(str(palavras[lin][col]))
            num_tot_palavras += 1
        ass_txt = []
        ass_txt.append(tam_m_pal(soma_comp_palavras, num_tot_palavras))
        ass_txt.append(type_token(palavras, num_tot_palavras))
        ass_txt.append(h_lego(palavras, num_tot_palavras))
        ass_txt.append(tam_m_sent(soma_cat_sentencas, num_tot_sentencas))
        ass_txt.append(compx_med(num_tot_frases, num_tot_sentencas))
        ass_txt.append(tam_m_frase(soma_cat_frases, num_tot_frases))
        matriz_ass_input.append(ass_txt)
    return matriz_ass_input  # matriz, lista de listas dos valores das assinaturas


def tam_m_pal(soma_comp_palavras, num_tot_palavras):
    if num_tot_palavras != 0:
        tam_m_pal = soma_comp_palavras / num_tot_palavras
    else:
        tam_m_pal = 0
    return tam_m_pal


def type_token(lista_palavras, num_tot_palavras):
    num_pal_dif = n_palavras_diferentes(lista_palavras)
    if num_tot_palavras != 0:
        type_token = num_pal_dif / num_tot_palavras
    else:
        type_token = 0
    return type_token


def h_lego(lista_palavras, num_tot_palavras):
    num_pal_uni = n_palavras_unicas(lista_palavras)
    if num_tot_palavras != 0:
        h_lego = num_pal_uni / num_tot_palavras
    else:
        h_lego = 0
    return h_lego


def tam_m_sent(soma_num_cat, num_sent):
    if num_sent != 0:
        tam_m_sent = soma_num_cat / num_sent
    else:
        tam_m_sent = 0
    return tam_m_sent


def compx_med(num_tot_frases, num_tot_sentencas):
    if num_tot_sentencas != 0:
        compx_med = num_tot_frases / num_tot_sentencas
    else:
        compx_med = 0
    return compx_med


def tam_m_frase(soma_cat_frases, num_tot_frases):
    if num_tot_frases != 0:
        tam_m_frase = soma_cat_frases / num_tot_frases
    else:
        tam_m_frase = 0
    return tam_m_frase


def separa_sentencas(texto):
    """
    A função recebe um texto e devolve uma lista das sentencas dentro
    do texto.
    """
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """
    A função recebe uma sentenca e devolve uma lista das frases dentro
    da sentenca.
    """
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """
    A funçãoo recebe uma frase e devolve uma lista das palavras dentro
    da frase.
    """
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """
    Essa função recebe uma lista de palavras e devolve o número de palavras
    que aparecem uma unica vez.
    """
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """
    Essa função recebe uma lista de palavras e devolve o número de palavras
    diferentes utilizadas.
    """
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(ass_main, matriz_ass_input):
    """
    Essa função recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.
    """
    lista_Sab = []
    soma_mod = 0
    if type(matriz_ass_input[0]) is list:
        for lin in range(len(matriz_ass_input)):
            for col in range(len(matriz_ass_input[lin])):
                soma_mod += abs(ass_main[col] - matriz_ass_input[lin][col])
            Sab = soma_mod / 6
            lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(matriz_ass_input)):
            soma_mod += abs(ass_main - matriz_ass_input)
        Sab = soma_mod / 6
        return Sab


def avalia_textos(textos_main, ass_comparadas):
    """
    Essa função recebe uma lista de textos e deve devolver o número (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    """
    aux_ass_com = ass_comparadas[:]
    aux_ass_com.sort()
    for indice in range(len(ass_comparadas)):
        if aux_ass_com[0] == ass_comparadas[indice]:
            copiah = indice
    return copiah
