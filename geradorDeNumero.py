#Gerador de numeros aleatórios para teste do BubbleSort

import json
import random

numeros = list(range(1, 501)) # <= caso queira alterar o numero de numeros
random.shuffle(numeros)
with open("dados.json", "w") as arquivo: # <= nome do arquivo que será gerado (dados.json)
    json.dump(numeros, arquivo)