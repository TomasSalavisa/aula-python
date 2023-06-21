# 1 - Peça ao utilizador que insira um número inteiro acima de 100 e, em seguida,insira um número abaixo 10 e diga-lhes quantas vezes o número menor cabe no maior número (utilize uma formatação condigna).

# num1 = int(input('Enter a number above 100: '))
# num2 = int(input('Enter a number under 10: '))
# result = num1 // num2
# print(f'{num2} fits {result} times inside {num1}')

# 2 - Peça ao utilizador que insira uma frase completa (sujeito, predicado e complemento direto). De seguida, informe o utilizador de quantos caracteres tem a frase que o mesmo introduziu (devem ser mais de 20). Finalmente pergunte a partir de que posição inicial e posição final da frase (inclusive), o utilizador pretende extrair, e apresente e referida extração na consola. A posição inicial deve ser menor ou igual que a posição final. Ambas as posições de extração devem ser valores validos de acordo com o comprimento da frase introduzida.

# frase = str(input('Enter a sentence with more than 20 caracters: '))
# comprimento = len(frase)
# print(f'Your sentence has {comprimento} letters.')
# pInicial = int(input('Insert a position number of sentence where you want to start taking from: '))
# pFinal = int(input('Insert a position number of sentence where you want to finish taking from: '))
# print(f'Your sentence is {frase[pInicial:pFinal]}')

# 3 - Peça ao utilizador escolha uma direção, para cima (c) ou para baixo (b). O programa deve fazer uma contagem crescente no caso da escolha ser “c”, de 0 até a um numero escolhido pelo utilizador de 0 a 20. Já no caso da escolhado utilizador ser “b”, o programa deverá efetuar uma contagem regressiva de 20 até ao numero escolhido. Naturalmente que deverá efetuar as validações necessárias de acordo com as limitações impostas, em ambas as escolhas os números devem estar compreendidos entre 0 e 20 ou 20 e 0 respetivamente. Em ambos os casos (escolha “c” ou “b”), deve o programa apresentar todos os números da iteração. Por fim, se escolha do utilizador não se situar nos valores “c” ou “b”, o programa deverá apresentar a mensagem “Não consigo entender.”.

# direction = input('What is the direction your excellency want "c" or "b": ')

# if direction == 'c':
#     num=int(input('Whats the dsired number 0-20: '))
#     for i in range(0,num+1):
#         print(i)
# elif direction == 'b':
#     num=int(input('Whats the dsired number 0-20: '))
#     for i in range(20,num-1,-1):
#         print(i)

# 4 - Faça um jogo que consiste, numa serie de 5 perguntas efetuadas pelo programa. As perguntas baseiam-se em 4 importantes operações da matemática, a soma (+), a multiplicação (x), a subtração (-) e a divisão (:). Neste contexto, o utilizador deve responder a 5 questões aleatórias no que diz respeito às operações já apresentadas. Os operandos, ambos aleatórios, devem situarem-se entre 1 e 50. Já o operador deve ser aleatório também compreendido nos operadores já referidos. No entanto, quando o programa escolher o operador ‘:’ deverá considerar para a resposta o operador ‘+’, isto é a divisão é substituída pela adição, e neste caso se a resposta for correta em vez de 1 ponto o utilizador recebe 2 pontos, mas neste caso o utilizador deverá ser informado que está numa situação de bónus se acertar. No final o utilizador deverá receber a sua pontuação no formato “x de 5”, em que x é a soma das suas respostas corretas, um ponto por cada. Naturalmente e por causa da situação do bónus, é admissível que o “x” seja maior que 5, sempre que existirem bónus numa das 5 iterações.

import random 

pontuacao = 0
operacoes = '+-x:'

for i in range(1,6):
    bonus = 0
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    respostaCerta = 0
    escolha = random.randint(0,3)
    operacao = operacoes[escolha]
    print(num1, operacao if operacao != ':' else '+', num2, '=')
    if operacao == ':':
        bonus = 1
        print('Está numa situação de bonus, 2 pontos se acertar: ')
    if operacao == '+':
        respostaCerta = num1 + num2
    elif operacao == '-':
        respostaCerta = num1 - num2
    elif operacao == 'x':
        respostaCerta = num1 * num2
    else:
        respostaCerta = num1 + num2
    resposta=int(input('A sua resposta: '))
    print()
    if resposta == respostaCerta:
        pontuacao += 1 + bonus
    print(f'Pontuação: {pontuacao} de 5')

