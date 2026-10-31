🫧 Ordenador Bubble Sort em Python

Uma aplicação interativa de linha de comando (CLI) que implementa o famoso algoritmo de ordenação Bubble Sort. Este projeto permite organizar listas de números através de diversas formas de entrada (arquivos ou digitação manual) e inclui um script gerador de dados para testes pesados.

📁 Arquivos do Projeto

bubbleSort.py: O aplicativo principal que contém o menu interativo e a lógica do algoritmo Bubble Sort.

geradorDeNumero.py: Um script auxiliar que gera uma lista de números aleatórios (embaralhados) e os salva em um arquivo .json para testar a capacidade do algoritmo.

🚀 Funcionalidades

O script principal (bubbleSort.py) possui um menu interativo com 4 opções de entrada de dados, além de tratamento de erros para evitar que o programa quebre caso o usuário digite letras ao invés de números.

Arquivo JSON: Lê uma lista de números diretamente de um arquivo .json (ideal para usar junto com o gerador).

Arquivo TXT: Lê números de um arquivo de texto comum, separados por vírgula.

Entrada Individual: Permite adicionar números um por um pelo terminal, com confirmação a cada inserção.

Entrada Contínua: Permite digitar todos os números de uma vez em uma única linha, separados por vírgula (ex: 10, 20, 30).

🛠️ Como usar

Pré-requisitos

Certifique-se de ter o Python 3 instalado na sua máquina.

1. Gerando dados de teste (Opcional)

Se você quiser testar o algoritmo com muitos números (por padrão, 500 números embaralhados), execute o gerador primeiro:

python geradorDeNumero.py


Isso criará um arquivo chamado dados.json no mesmo diretório. Nota: Você pode alterar a quantidade de números editando a variável range dentro deste arquivo.

2. Executando o Bubble Sort

Inicie a aplicação principal:

python bubbleSort.py


Siga as instruções na tela e escolha o método de entrada desejado. Se gerou o arquivo no passo anterior, escolha a Opção 1 e digite dados.json.

🧠 Como o Bubble Sort funciona (Por trás dos panos)

O algoritmo utiliza uma lógica simples de comparação de vizinhos para ordenar a lista. Aqui está a explicação dos principais componentes do código:

O loop externo (i): Ele serve para salvar a posição da última alteração. Ele trabalha "de trás pra frente", porque a cada passagem completa, o maior número da lista é empurrado para o final. O i coloca uma "parede" imaginária, garantindo que o programa não perca tempo comparando novamente os maiores números que já foram posicionados corretamente no final da lista.

O comparador (loop interno): É a variável responsável por percorrer a lista e verificar quem é o maior número entre dois vizinhos (comparador e comparador + 1). Se o número da esquerda for maior que o da direita, eles trocam de lugar. Ele vai "empurrando" os números maiores para trás até bater na "parede" definida pelo i.

A função len(): Conta quantos itens existem dentro da lista que precisa ser organizada, definindo o tamanho dos loops de repetição.

⚠️ Tratamento de Erros

A aplicação foi construída com blocos try/except robustos. Se o usuário tentar inserir texto onde apenas números são permitidos, o sistema exibirá um aviso customizado e pedirá a entrada novamente, sem interromper ou "crashar" o script.
