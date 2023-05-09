# Apontamentos Python

## Estrutura de dados

Não são dados mas sim a estrutura pela qual esses dados são suportados.
Por exemplo 1 numero real é uma estrutura de dados.
Uma lista de dados, uma arvore de dados, ect.. são estrutura de dados.

---------------------------------------------------------------------

Uma FILA de dados é uma estrutura de dados:

Ex: Imagina uma fila de pessoas:
Pessoa1 , Pessoas2, Pessoa3...

O primeiro a entrar é a primeira a sair.

---------------------------------------------------------------------
uma PILHA de dados é uma estrutura de dados:

Ex: imagina uma pilha de livros:

1º, 2º, 3º ....

O primeiro a entrar é o ultimo a sair.

-----------------------------------------------------------------------

Tambem-se pode criar uma estrutura de dados nós mesmos, por exemplo, os conjuntos de dados associados a um cliente, a um produto, a um clube de futebol, etc...

As estruturas de dados regulam os dados e apoiam o algoritmo no seu tratamento.

# Tipos de dados

## bool

O tipo de dados boleano em python assume dois valores possiveis : "True" e "False"

Temos de respeitar as maisculas e minusculas, se eu escrever "true" em vez de "True" vai dar erro.


-------------------------------------------------------

## Float

O tipo de dados Real em python é o Float, porque têm casas decimais sendo numero positivos ou negativos.

0.0 = float
10 = not float but int

A virgula ',' em python é usada para separar argumentos, por exemplo o comando 'Print' pode assumir mais do que um argumento com a virgula.

<Print( 0.0, type(0.0)) --> o output será : 0.0 <float>

quando quisermos saber o tipo de dados de uma variavel qualquer seja, usamos 'type'

-----------------------------------------------------

## Int

O tipo de dados Inteiro em python é um int. São 'int' porque não têm casas decimais , sendo numeros positivos ou negativos.

10 = int, não tem decimais

10.0 = ja é float pois tem decimal.

<print(10, type(10)) --> output : <int>

-----------------------------------------------------------

## String

O tipo de dados Texto(string) em python é str. São str porque estao dentro de aspas dulpas ou simples.
Texto ou numeros, vai dar ao mesmo se estiverem dentro de aspas.

'Ola' = str, esta dentro de aspas

Ola = nao é str, nao esta dentro de aspas.

<print("Ola", type("Ola")) --> output : <str>

Que output pode produzir este codigo : print("2020" -23)

R: Erro pois o pyhton nao aceita que dois que 'str' e 'int' estejam juntos assim na frase, temos de explicitar o que queremos fazer.
Neste caso seria mudar o "str 2020" para "int".

<print(int("2020") -23 ) --> output : 1997.

O python prefere codigo explicito onde lhe dizes exatamente o que queres em vez de implicito onde nao lhe dizes extamente o que lhe dizes, na situação acima, é um exemplo onde podemos usar a conversao de tipo de dados para explicitar melhor o codigo ao python.

------------------------------------------------------------------------

## List

O tipo de dados lista em Python é list. São 'list' porque podem assumir uma serie de elementos, parecido com um array, porque uma lista em python o numeros de elementos pode ser dinamico . No entanto existe um indice para cada elemento tipicamente desde o '0'.

<lista=['Joaoa', 'Maria', 'Gui', 16.8, 78, True]

isto é uma lista, pode ter todos os tipos de dados dentro dela que nao deixa de ser uma lista.

-------------------------------------------------------------------------------

## dict

O tipo de dados dicionario em python é disc. São 'dict' porque podem assumir uma serie de elementos, mas cada elemento esta relacionado a uma chave. No exemplo abaixo o 1239 esta diretamente relacionado com a sua chave 'Numero de Aluno' e o 'Nome do aluno ' é a chave do valor 
'Alvaro Reis'.

-----------------------------------------------------------------------------

## None

O tipo de dados Null em python é none. São 'none' porque nem 'nada' são, são apenas 'null'.

<print(None, type(None)) --> output :None <class 'NoneType'>


---------------------------------------------------------------------------

# Tipificação - Variáveis

O pyhton é uma linguagem altamente dinamica relativamente à tipificaçáo. Por isso o utilizador não precisa indicar qual o tipo de dados que é reservado a uma determinada variavel ou estrutura de dados.

Quando se iguala valores, fala-se de atribuição  e não de comparação, por isso utiliza-se o sinal '=' para atribuição e '==' para comparação. Ao nome da variavel chamamos de 'Identifcador' ('AnoNascimento', 'NomeAluno', ect.. são identificadores)

Naturalmente a vantagem das variaveis é poderem vir a ser "manipuladas" atraves de diversas operações e fazerem flutuar os seus valores ao longo do ciclo de cada programa.

No exemplo abaixo verifica-se uma de muitas formas de utilizar variaveis e manipula-las atraves de outras.


<AnoNascimento = 2002
AnoAtual=2023

<NumeroAnos = AnoAtual - AnoNascimento

<print('A sua idade :' +str(NumeroAnos) + '.')

<Output : A sua idade : 21.

Verifica-se tambem uma conversão explicita no que diz respeito à concatenação usada no comando 'print' através do 'str' antes do tipo de dados inteiro(Numero Anos).

Repare ainda que nao se indicou nehum tipo de dados no exemplo, pois é um proceso que o pyhton faz sozinho.

---------------------------------------------------------------------------------

Ao analisar o exemplo abaixo , verifica-se de facto que as variaveis em pyhton sao dinamicas. Note-se o caso da variavel "valor" que na linha 2 assume o tipo 'int' na linha assume o tipo 'tuple' e na linha 6 assume o tipo 'str'.

<total=0
Valor=75>

<print('O aluno teve ' + str(Valor) + '%')
Valor=1,75
print('O aluno mede ' + str(Valor)+ 'm.')
Valor = 'bem disposto'
print('Trata-se de um aluno ' +Valor + '.')>

Tambem se verificou que na linah 7, no que diz respeito a concatenação não foi necessário qualquer tipo de conversão porque todos os elementos já estavam em tipo 'str', portanto neste caso nao existe ambiguidade. Ja na linha 5 houve uma conversao de 'tuple' para 'str'.
(1,75) é diff de 1.75.

Importante ressalvar quue dinamico não é fraco , isto é, dizer que python é dinamico relativamente à tipificação não é a mesma coisa que dizer que python é de tipificação fraca, porque de facto o python apesar de dinamico nesse aspeto, preserva fortemente a tipificação na sua genese. Pode-se dizer que o python tem uma 'Intelegencia apurada' para identificar bem o tipo de variaveis.

# Operadores Aritmeticos

Os operadores aritmeticos do pyhton sao + , - , * 	, / : sao os operadores para somar, subtrair, multiplicar e dividir do pyhton.

Em relação à divisao inteira, o pyhton usa '//', como se ve abaixo o resultado não é arredondado, dividiu-se o numero 9 por 2 para apurar um resultado inteiro e a unica diferença da divisao normal da inteira é que a divisão inteira nao arredonda.

<print(4+3) Soma = 7
print(3-4) subtração = -1
print(4*3) multiplicação = 12
print(4/3) divisão = 1.3333333 
print(9//2) divisão inteira = 4.0
print(9**2) expoentes = 81
print(56%5) resto da divisão - modulo = 1>

Para os expoentes (por exemplo o 9*2) o pyhton reserva os simbolos **. Quando se pretende em python apurar o resto de uma divisão, tipicamente conhecido como operação modulo, utiliza-se o simbolo %.

Estes operadores sao tambem conhecidos como operadores binarrios por usarem por definição dois operadores. Chamam-se tambem notação 'infix' ou 'infixada' , porque o operador esta entre dois operandos.

EX: Existe uma universidade com 1500 alunos e reprovaram 137 alunos, qual foi a percentagem de alunos aprovados?

<alunos = 1500
 alunosReprovados = 137

<percentagemAlunosAprovados = 100-(alunosReprovados /alunos *100)
 print (percentegameAlunosAprovados)

<R: 90.8666666666667

# Operadores Relacionais

Os operadores relacionais projetam um resulatdo que pode assumir um de dois valores : True ou False.

Destacar a confusão que pode existir entre o igual '=' e a comparação '==' 

'<' menor , '<=' menor ou igual , '>' maior, '>=' maior ou igual , '==' comparação , '!=' diferente.

Como curiosidade , o exemplo demonstra que uma variavel '' sem nada é diferente de 'none' tal como é visto no resultado da linha 18 abaixo.

a= 10
b= -3
c 'A'
d= 'B'
e = ''

####  > maior >= maior ou igual
print( a > b , a >= b) 

#### > menor <= menor ou igual 
print(a < b , a <= b)

#### == igual 
print(c == d)
print(b == a-13)

#### != diferente
print(e != None)

R: 
True True
False False 
False
True
True


# Operadores de Atribuição

igual '=' é o operador de atribuição mais conhecido 

Analise a figura retirada do vs code, como as variaveis são preenchidas (atraves de valores atribuidos) e como a lista é preenchida
![Markdown Preview](image.jpg)



