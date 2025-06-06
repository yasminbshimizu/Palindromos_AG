import random
from itertools import product
# import numpy as np

###############################################################################
#                                 Cria População                              #
###############################################################################
def gene_palindromo(letras_possiveis):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    """
    letra = random.choice(letras_possiveis)
    return letra

def cria_candidato_palindromo(letras_possiveis, tamanho_palavra=5):
    """Cria um candidato para o problema do palíndromo.

    Args:
      letras_possiveis: letras possíveis de serem sorteadas.
      tamanho_palavra: inteiro representando o tamanho da senha. (valor padrão = 5)

    """
    candidato = []
    

    for _ in range(tamanho_palavra-1):
        candidato.append(gene_palindromo(letras_possiveis))
        
    vogal_obrigatoria = random.choice(["a", "e", "i", "o", "u"])
    posicao_vogal_aleatoria = random.choice([0, 1, 2, 3, 4])
    candidato.insert(posicao_vogal_aleatoria, vogal_obrigatoria)

    return candidato


def populacao_palindromo(tamanho_populacao, letras_possiveis):
    """Cria população inicial no problema do palíndromo.

    Args
      tamanho_populacao: tamanho da população.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_palindromo(letras_possiveis))

    return populacao


###############################################################################
#                                Função Objetivo                              #
###############################################################################

def calcula_distancia(palavra1, palavra2):
    """Calcula a distância entre as letras de duas palavras.
    
    Args:
    palavra1 e palavra2: palavras que estão sendo comparadas.
    """
    distancia = 0
    #print(palavra1, palavra2)
    for letra_palavra1, letra_palavra2 in zip(palavra1, palavra2):
        #print(letra_palavra1, letra_palavra2)
        num_palavra1 = ord(letra_palavra1)
        num_palavra2 = ord(letra_palavra2)
        distancia += abs(num_palavra1- num_palavra2)
    return distancia
    
def funcao_objetivo_palindromo(candidato):
    """Computa a funcao objetivo de um candidato no problema do palíndromo.
    Calcula a diferença entre as duas partes da palavra com 5 letras (último elemento com o primeiro, antepenúltimo com o segundo).
    Caso a palavra não tenha uma vogal, a penalização será proporcional a maior distância entre uma letra da palavra e uma vogal.

    Args:
    candidato: um palpite para o palíndromo.
    """
    parte1 = [candidato[0], candidato[1]]
    parte2 = [candidato[-1], candidato[-2]]
    #print(candidato)
    distancia = calcula_distancia(parte1, parte2)
        
    vogais = ["a", "e", "i", "o", "u"]
    vogal  = False
    
    for letra in candidato:
        if letra in vogais:
            vogal = True
    
    distancia_vogais = [0]
    if not vogal:
        for i in product(vogais, candidato):
            distancia_vogais.append(calcula_distancia(i[0], i[1]))
    distancia += max(distancia_vogais) * 10
    
    return distancia

def funcao_objetivo_pop_palindromo(populacao):
    """Computa a funcao objetivo de uma populaçao no problema dos palíndromos.

    Args:
      populacao: lista contendo os individuos do problema.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_palindromo(individuo))

    return fitness
###############################################################################
#                                 Seleção                                     #
###############################################################################

def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema.
      fitness: lista contendo os valores computados da funcao objetivo.
      tamanho_torneio: quantidade de invíduos que batalham entre si.

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################
    
def cruzamento_ponto_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo.

    Args:
      pai: lista representando um individuo.
      mae: lista representando um individuo.
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento.

    """
        
    if random.random() < chance_de_cruzamento:
        corte1 = random.randint(1, len(mae) - 2)
        corte2 = random.randint(corte1 + 1, len(mae) - 1)
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    else:
        return pai, mae
    
###############################################################################
#                                Mutação                                      #
###############################################################################
def mutacao_salto(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de salto.

    Args:
      populacao: lista contendo os indivíduos do problema.
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.
      valores_possiveis: lista com todos os valores possíveis dos genes.

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            indice_letra = valores_possiveis.index(valor_gene)
            indice_letra += random.choice([1, -1])
            indice_letra %= len(valores_possiveis)
            individuo[gene] = valores_possiveis[indice_letra]
            
            
def mutacao_letra_repetida(populacao, chance_de_mutacao):
    """Implementa um novo tipo de mutação, no qual uma letra sorteada, 
    caso a palavra não tenha letras repetidas, muda de valor para uma já pré-existente na palavra.

    Args:
    populacao: população para a resolução do problema do palindromo.
    chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.
    
    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao and len(set(individuo)) == 5:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            indice_letra = individuo.index(valor_gene)
            
            posicoes_possiveis = [0, 1, 2, 3, 4]
            
            posicoes_possiveis.pop(indice_letra)
            posicao_troca = random.choice(posicoes_possiveis)
            
            valores_possiveis_individuo = individuo.copy()
            valores_possiveis_individuo.pop(posicao_troca)
            
            # print(indice_letra)
            # print(individuo)
        
            individuo[indice_letra] = random.choice(valores_possiveis_individuo)
            
            
    
            
