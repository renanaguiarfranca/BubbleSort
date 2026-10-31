def bubbleSort():
    import time
    import json
    bubbleSort = []

    print('===Organizador de numeros===')
    time.sleep(0.10)

    # Adicionado a opção 4 no texto explicativo do menu
    print('[1] insira seu arquivo Json\n[2] Arquivo TXT\n[3] insira os numeros 1 por vez\n[4] insira os numeros todos de uma vez (separados por virgula)')
    while True:
        try:
            menu = int(input('Selecione o metodo de entrada\n>>> '))
            if menu == 1: #opção arquivo Json
                nomeArquivoJson = input("Digite o nome do arquivo JSON (Ex: dados.json): ")

                with open(nomeArquivoJson, "r") as arquivo:
                    bubbleSort = json.load(arquivo)
                    break
            
            elif menu == 2: #opção arquivo TXT
                nomeArquivoTxt = input("Digite o nome do arquivo TXT (Ex: dados.txt): ")

                with open(nomeArquivoTxt, "r") as arquivo:
                    conteudo = arquivo.read()
                    textos = conteudo.split(',')
                for item in textos:
                    bubbleSort.append(int(item.strip()))
                break
            
            elif menu == 3: #opção numero individual
                while True: # while que pega os numeros e decide se quer adicionar mais numeros e validção se o arrombado coloco letra ao invez d numero
                    try:
                        numero = int(input('digite o numero\n>> '))
                        bubbleSort.append(numero)
                    except ValueError:
                        print("só pode numeros seu folder!")
                        time.sleep(0.7)
                        continue
                    
                    
                    while True: #se ele escolher algo diferente de 's' ou 'n' ele toma um fallback
                        escolha = input('quer adicionar mais um numero? S/N?\n').lower()
                        if escolha == 's' or escolha == 'n':
                            break
                        else:
                            print('Apenas sim(S) ou Não(N)!')
                            time.sleep(0.7)
                    if escolha == 'n':
                        time.sleep(0.3)
                        print("numeros adicionados {}".format(bubbleSort))
                        time.sleep(0.10)
                        break
                break

            elif menu == 4: # opção de numeros continuos após a virgula
                while True:
                    try:
                        entrada = input('Digite os numeros separados por virgula (Ex: 10,20,30):\n>> ')
                        textos = entrada.split(',')
                        for item in textos:
                            if item.strip(): # Garante que não vai tentar converter espaços vazios
                                bubbleSort.append(int(item.strip()))
                        
                        if len(bubbleSort) == 0:
                            print("voce nao digitou nenhum numero!")
                            continue
                            
                        print("numeros adicionados {}".format(bubbleSort))
                        time.sleep(0.10)
                        break
                    except ValueError:
                        print("digite apenas numeros e virgula!")
                        bubbleSort = []
                        time.sleep(0.7)
                break

            else:
                print('selecione uma opção válida\n')
        except ValueError:
            print('selecione uma opção válida')
            continue

    lista = len(bubbleSort) #len conta os itens da lista 
    print(lista) #só pra ver quantos itens tem na lista 
    for i in range(lista - 1): 
        for comparador in range(lista-1-i): #comparador é a variavel que vê se o numero vizinho é maior ou menor que o outro
            if bubbleSort[comparador] > bubbleSort[comparador+1]:
                bubbleSort[comparador],bubbleSort[comparador+1] = bubbleSort[comparador+1],bubbleSort[comparador]
                print("Aqui está sua lista Organizada {}".format(bubbleSort))
bubbleSort()


#explicação:

#para que serve o (i): ele meio que salva a posição da ultima alteração, no caso de traz pra frente, porque ele começa do maior para o menor, no caso, deixa o 9 em ultimo(por ser o maior valor da lista) e põe "uma parede" para que ele faça mais uma comparação com o comparador, fazendo ele identificar o maior numero agora(no caso o 8) e faz esse processo repedidamente ate finalizar.

#para que serve o (comparador): ele é o responsavel por percorrer a lista e verificar qual o maior numero e colocar ele em ordem, como o i coloca a "parede" depois de organizar o numero maior, ele só vai mandando os numeros maiores pra traz, sem mexer noque já foi organizado.

#para que serve o len: o len basicamente conta quantos itens tem na lista, no caso do exemplo acima, 10 itens