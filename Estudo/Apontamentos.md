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

Analise a figura retirada do vs code, como as variaveis são preenchidas (atraves de valores atribuidos) e como a lista é preenchida.


![Markdown Preview](./image.jpg)

Note como as linhas 3 e 7 funcionam de igual forma.

Da mesma forma que as linhas 11 e 14 produzem o mesmo resultado.

Também a multiplicação e a divisão podem ser usadas através do mesmo método (analisar linhas 21 e 27)

Assim como o resto da divisão (módulo) (analisar linha 34)e a divisão com resultado inteiro (linha 48).

Operadores de Atribuição : "=" , "+=" , "-=" , "*=" , "/=" , "%=" , "**=" , "//="

De facto o operador de atribuição é o ‘=‘ que pode ser associado a todos os operadores aritméticos.


# Operadores Logicos

Analise as tabelas de verdade


![Markdown Preview](./tabelaverdade.jpg)

------------------------------------------------------------------------

Operadores Logicos : 'and' , 'or' consideramos em python 0 '!=' como sendo o 'xor' e o 'not' como negação.

Apenas como curiosidade existe a possibilidade de utilizar em python os operadres logicos 'bit a bit' . Neste caso consideramos o '&' ,     '|' , e '^' como sendo o 'and' o 'or' e 'xor' da relação bit a bit . Cuidado para não confundir...
(NAO VAI SER USADA NESTA UC)

![Markdown Preview](./image3.jpg)

-----------------------------------------------------------------

### Ex: Um aluno teve 16 na media dos testes e 12 faltas num total de 20 aulas. O aluno fica aprovado se e só se a sua media for maior que 9 e a % de faltas nao pode utrapassar os 20%.

![Markdown Preview](./image4.jpg)

--------------------------------------------------------------------------------------

# Operadores Unários

Um operador unário possui apenas um operando.

Por exemplo para o efeito que é comum verificar-se , 'x++' que incrementava uma unidade à variavel 'x', em pyton pode fazer-se com 'x +=1 ', mas já não é um operador unário.

++ ou - ou +- não incrementa nem decrementa valores, apenas servem para reforçar o operador aritmetico . O facto é que neste caso o '+' e o '-' é que são os operadores unários.

Note que a partir da linha 5 não existem atribuiçõs pelo que nenhuma dessas linhas altera o conteudo das variaveis.


![Markdown Preview](./image5.jpg)

--------------------------------------------------------------------------------------------

# Operadores Ternários

Este operador ternário consista na aplicação de duas respostas possíveis respetivamente a uma variavel.

No exemplo verifica-se uma concatenação que testa se o aluno é aprovado ou reprovado( as duas possibilidades possiveis) atraves da variavel 'aprovado'.

Se a variavel for 'False' assume a primeira possibilidade, caos seja 'true' assume a segunda possibilidade.

Outra forma será utilizar o operador ternário com o comando 'if'. Neste caso a primeira possibilidade fica antes do 'if' e a segunda condição depois do 'else'.


![Markdown Preview](./image6.png)


--------------------------------------------------------------------------------------------------

# Outros operadores

O operador "in" (operador de membro) serve para testar se determinado valor se encontra dentro de uma estrutura de dados complexa.

Operador "is" (operador de indentidae) serve para testar se o conteudo de uma determinada estrutura de dados é o mesmo.

Pode existir uma dificuldade em perceber a diferença entre o comportamento do 'is' numa estrutura de daos complexa e o comportamento do 'is' numa estrutura de dados simples.

Porque o 'is' atua sobre o endereço de memória das estruturas de dados (linha 25,26,27 comparadas com as linhas 11 a 14).

![Markdown Preview](./image7.jpg)

--------------------------------------------------------------------------------------------------------

O quadro em baixo explica o porquê da diferença . Percebe-se que a lista 'alunos2' tem um endereçamento de memória diferente das listas 'alunos' e 'alunos1' , por isso são 'objetos diferentes'.

![Markdown Preview](./image8.jpg)

--------------------------------------------------------------------------------------------------------

# Modulos 'BUILTIN' e Ambito Global


Numa primeira abordagem o python carrega para o ambito global variaveis e funçoes que vao sendo utilizadas ao longo de cada sessao/programa.

A funçao 'dir' permite verificar qual o ambito global de uma detrminada 'sessao'/programa num determinado momento.

No primeiro exemplo verifica-se poucos 'elementos' , mas à medida que o software vai evluindo relativamente às execuções que fazem este 'Ambito 
Global' vai aumentando no numero de elementos (ver exemplo 2)

No exemplo 2, verifca-se que a variavel 'a' foi adicionada à lista.

![Markdown Preview](./image9.jpg)

----------------------------------------------------------------------------------------------------------

O pyhton assente sobre uma estrutura modelar. E como estrutura modelar , possiblita a incorporação de modulos de acordo com as necessidades de momento quer podem variar de programa a programa.

Existe um modulo chamado '__builtin__' , que ao repararem na imagem anterior conseguem visualizar a sua presença no 'Ambito Global' , precisamente porque foi carregado com o própio python.

O comando 'dir' mostra os recursos de cada modulo. Utilizando o 'dir' sem argumentos 'dir()' , visualizam-se os recursos do ' Ambito Global' que é dinamico . Então pode-se perguntar :

### Porque é que não aparece o comando 'dir'?

 R: porque o comando dir encontra-se no modulo '__builtin__' entre muitos outros comandos.


![Markdown Preview](./image10.jpg)

----------------------------------------------------------------------------------------------------------


Escreva uma linha 'import math' . Obviamente que este comando irá importar o modulo 'math' , um modulo com mias funçoes matematicas.

Agora pretende-se verificar o conteudo desse modulo.

![Markdown Preview](./image11.jpg)


Na imagem , os recursos do modulo 'math'

Fica claro então que o comando 'dir' pode receber um argumento que representa o modulo que se pretende ver o seu conteudo .

--------------------------------------------------------------------------------------------------------------

# Conversões entre tipos de dados

A função 'type' serve para identificar o tipo de dados das estruturas de dados.

Pode ser utilizada com o print.

<Ex: print(x, type(x))

![Markdown Preview](./image12.jpg)

------------------------------------------------------------------------------------------------------------------

![Markdown Preview](./image13.jpg)

Regras de concatenação:

- So pode concatenar 'str' com 'str', nao pode 'int' com 'str'
- Nao posso mudar uma 'str' com decimais para int .
- So pode concatenar 'str' com 'str', nao pode 'bool' com 'str'

--------------------------------------------------------------------------------------------------------------------

Neste exemplo vêm-se vários tipos de dados e comportamento do Python nas conversões implícitas e explicitas entre os diversos tipos de dados.

A Linha 8 produz o seguinte resultado: note-se que as variáveis x e y são do tipo ‘str’ e as variáveis z e w são do tipo ‘int’ e ‘float’respetivamente.
No entanto a aparência do output não reflete essas diferenças.

A Linha 9 aparentemente reflete duas somas. Mas não se tratam de duas somas, a primeira (x+y) é uma concatenação e a segunda uma operação aritmética precisamente porque a primeira diz respeito a duas variáveis do tipo ‘str’ e a segunda diz respeito a duas variáveis numéricas que apesar de serem tipos difentes ‘int’ e ‘float’, são ambas numéricas e o Python não margem para dúvidas que pode utilizar uma conversão implícita para poder somar neste caso as variáveis z e w. 

A linha 10 acusa um erro, pois tenta concatenar tipo de dados ‘str’ (x) com um tipo de dados ‘float’ (w).

Esta situação deixa margem para dúvidas porque tanto se pode fazer uma concatenação como se poderia querer fazer uma soma. Então o Python deixa que o programador torne explicita a sua intenção, sugerindo que se faça a conversão que se pretende.

A linha 11 não tem qualquer problema pois é uma soma com o mesmo tipo de dados dos operandos.

Então fica claro que o Python privilegia sempre o explicito sobre o implícito no que diz respeito a eventuais conversões que possam vir a ser necessárias.

As conversões explicitas deverão ser sempre feitas com o tipo de dados que se pretende obter seguido do valor ou variável entre parenteses. 
Ver linhas 13, 15, 17, 25, etc…

### É possivel converter str com decimais para int, se primerio convertermos para float e dps para int. EX: str = "10.6" --> float = 10.6 --> int = 10 

------------------------------------------------------------------------------------------------------

# Tipos de Dados Inteiro e Float


Como já referido o conando 'dir' serve para visualizar o conteudo de um modulo .
Veja o resultado de dir(int) na imagem abaixo.

![Markdown Preview](./image14.jpg)


<br>

Agora o resultado de dir(float) na imagem abaxio.

![Markdown Preview](./image15.jpg)

<br>

Qualquer tipo de dados conjugado com um float , o resultado dessa operação será sempre do tipo 'float', excluindo funções/operações que forçem o contrário.

x=100
y=10.563

print (x*y ,"\n" , x/y,"\n" , x+y ,"\n", x-y ,"\n" ,x/x)

Para verificar se um determinado dado é inteiro ,pode-se utilizar a funçao 'is_integer()' .

EX: Verifique se as variaveis 'x' e 'y' são inteiros ou não:

print(x.is_integer())

R: dá erro, porque a funçao is_integer() não existe para tipos 'int' só para tipos 'float'
print(y.is_integer())

R: False

y=10.0

print(y.is_integer())

R: True   --> Se a variavel for float mas tiver '.0' é como se não existisse e conta como int.

-----------------------------------------------------------------------------------------------------------------------------

No exemplo abaixo pode verificar-se que as funções disponiveis em cada uma dad funções (neste caso tipo de dados) podem utilizar-se de forma 'primária, tal como o própio Python utiliza.

Utilizamos o tipo de dados int e associamos uma das funções disponiveis (dir(int)). No caso deste exemplo , temos uma função para a subtração '__sub__'
, para a soma '__add__' , e para as potencias '__pow__' , todas admitindo dois parameteos de entrada.

As duas primeiras para os operandos e a terceira tendo como dados de entrada a base e a potência . Este racicionio pode ser aplicado a todas as funções existentes em cada 'classe'.


![Markdown Preview](./image16.jpg)

-------------------------------------------------------------------------------------------------------------------------

# Problemática de Precisão

 A questão do 'form' e do 'import' será estudada mais á frente. AGORA NÃO

 Apenas fique a saber que são funções que importam modulos .

Neste caso importamos o modulo 'Decimal' e 'getcontext' que estão dentro do modulo 'decimal'.

Se fizer dir(decimal) irá apresentar erro, pois foram os modulos 'Decimal' e 'getcontext' que foram importados do modulo 'decimal' e não o modulo 'decimal' completo.

Se fizer 'import decimal' e depois dir(decimal) , irá verificar que existem esses dois modulos 'Decimal' e 'getcontext'.

![Markdown Preview](./image17.jpg)

-----------------------------------------------------------------------------------------------------------------

Repare-se que uma simples divisão entre x e y neste caso apresentou uma pecisão de muitos numeros ,por questoes relacionadas com a performance e metodos de calculo matematico.

Repare no caso da soma das variaveis z com y ,(122.30000000001) , é estarnho, mas relaciona-se precisamente com forma de linguagens de programação ligam a performance de resposta com a necessidade de precisão esse mesmo calculo.

Mas existe uma possibilidade de 'acertar' essa precisão através do metodo 'getcontext().prec'  e da função 'decimal' , que apresenta a precisão até ao numero das casas decimais pretendidos, ver imagem abaixo.

![Markdown Preview](./image18.jpg)

--------------------------------------------------------------------------------------------------------------

# Strings

Existem muitas funções que podem utilizadas com o tipo de dados 'str'.
Resultado de dir(str).

![Markdown Preview](./image19.jpg)

-----------------------------------------------------------------------------------------------------------

Veja a string cidade.

Em pyhton uma string é representada por 'str'.

Uma string é um array? Porque cada caracter de uma detrminada string é um elemento de um array que é uma string.

Assim como é possivel aceder a cada um dos caracters de uma determinada string (linha4), e até saber que comprimento a string tem (linha 3).
Para o efeito usaram-se as funções 'len' e 'array[x]' em que 'x' é o indice do array, partindo do principio que o indice começa no 0.

No entanto apesar de se afirmar que uma string é um array, este tipo de dados não aceita poder ser alterado a partir dos elementos, como de um array se trata,(linha5).

![Markdown Preview](./image20.jpg)

-----------------------------------------------------------------------------------------------------------

Sugere-se algum cuidado na utilização das aspas simples e aspas duplas. Apesar de poder utilizar qualquer uma delas no python , pode geral alguma confusão (e até erro) quando se utilizam aspas que se querem mesmo como parte integrante do texto.

As linhas 6 e 9 representam uma utilização valida das aspas simples e duplas em conjunto.

Imagine que queria imprimir a mensagem :“Nota da semana ‘D’el re’ :Festa no “Castelo.” Como faria?

Podem-se utilizar caracteres de escape (‘\’) para incluir mais aspas das que foram utilizadas como aspas da string (exemplos nas linhas 10 e 11).

Perceb-se também que o símbolo ‘\’ funciona também para partir o texto apenas no editor, ficando continuo na apresentação do seu output 
(linhas 6 e 8).

![Markdown Preview](./image21.jpg)

-------------------------------------------------------------------------------------------------------------


Quando se pretende partir uma string por questões estéticas de visualização da string no editor , não se pode partir simplesmente a linha como no exemplo abaixo.

Pode para esse efeito utilizar a tecnica das 3 aspas, usar 3 aspas dupas ou simples (""" , ''') como no exemplo representado nas linhas 3 a 6.

![Markdown Preview](./image22.jpg)

---------------------------------------------------------------------------------------------------------------

Já se referiu que se pode extrair caracters de uma string tal como num array, 'a=array[indice].

Veja a string cidade.
Para imprimir a string, linha 2,
Para imprimir a string usando os indices da mesma, linha3,
Para imprimir o primeiro elemento da string, linha 5 e 6,
Para imprimir o comprimento da linha , linha 7,

<br>

Analisando a figura(linha6) e o gráfico , percebe-se que a string percebe que os seus elementos têm duplo sentido. Da esquerda para a direita a começar do 0 .... 25, e da direita para a esquerda a começar no -1.....26.

![Markdown Preview](./image23.jpg)

-----------------------------------------------------------------------------------------------------------------

Utilizando os ':' , pode-se percorrer os elementos iterativamente desde o incio ao fim, ou como já referido ser possivel do fim para o inicio. (com o sinal negativo ), linhas 9 a 10.

Tambem se pode percorrer a string entre limites , por exemplo desde o caracter 'R' até ao caracter 'S', linhas 11 e 12.

Percebe-se assim o ':' divide os limites dos elementos, como se à esquerda do ':' fosse 0 'de' e à direita do ':' fosse o ao .
Então [5:13]  e [-21:-14] é da posição 5 a posição 13 e da posição -21 a posição -14.

Reparar que quando trabalhamos com numeros positivos, a ultima posição NÃO conta(por causa do 0) , neste caso não acaba no -14 mas sim no -15 , (linhas 11 e 12).

Ainda podemos fazer um 'step' de 2 posições usando o '::' , aplica-se também aos dois sentidos com a mesma tecnica ('-') , (linhas 14 a 16)

![Markdown Preview](./image24.jpg)

-------------------------------------------------------------------------------------------------------------------

Pode-se verificar se um determinado caracter ou um conjunto de carcters existe numa string através da função ('in') (particular atençao ao 'case sensitive') ,ver figura abaixo.
Naturalmente que também se pode utilizar o 'not in' para verificar se o(s) caractere(s) existe(m) na string.

Ja verificamos que a funçao 'len' determina o numero de caracteres de uma estrutura de dados, neste caso o comprimento em caracteres da variavel 'cidade' que é 26.

Já os metodos 'upper()' e 'lower()' convertem a string para letras maisculas ou minusculas respetivamente, tal como apresentado na imagem abaixo.

![Markdown Preview](./image25.jpg)


EX : 

Faça com que se exiba no ecrã através da função ‘in’ a existência dos caracteres ‘REAL’ (sem utilizar o operador ‘not’).


print(cidade[4:9].upper())

R: REAL

-------------------------------------------------------------------------------------------------------------------

# Modulos

Existem várias bibliotecas que podem ser utilizadas em Python. Essas bibliotecas (módulos) contêm diversos métodos (funções) com muita utilidade e nas mais variadas áreas, por exemplo na matemática nós utilizamos o módulo 'math'.

Em Python para utilizar esses módulos utiliza-se o comando 'import' seguido do nome da biblioteca que se quer importar, por exemplo no caso da biblioteca 'math' faz-se: 

![Markdown Preview](./image26.jpg)

Para utilizar os métodos do modulo basta colocar o nome do módulo seguido de um '.'  e o vscode irá mostrar todos os métodos disponíveis no módulo. 
Basta selecionar o método pretendido e usar o mesmo com os respeito(s) parâmetro(s). 

Por exemplo no caso da raiz quadrada :

![Markdown Preview](./image27.jpg)

----------------------------------------------------------------------------------------------------------------------

Se fizer print(dir()) verifica quais sao os modulos e atributos que o python está a usar no momento. Repare que depois de utilizarmos o modulo 'math' o comando 'dir' mostrou-o também.

![Markdown Preview](./image28.jpg)


----------------------------------------------------------------------------------------------------------------------

## No entanto se quisermos apenas usar um dos métodos do módulo math, por exemplo método ‘sqrt’ devermos utilizar o comando:


![Markdown Preview](./image29.jpg)

## Ao fazer “print(dir())” irá verificar que em vez do módulo ‘math’ o Python apenas disponibiliza o método ‘sqrt’:


![Markdown Preview](./image30.jpg)

## Nota: naturalmente que desta forma ao utilizar o método ‘sqrt’ não necessita utilizar o ‘math.sqrt’, basta apenas utilizar o ‘sqrt(x)’ . Para remover o sqrt, fazer del sqrt.

--------------------------------------------------------------------------------------------------------------------------


Para intender o modulo '__name__' , vamos escrever 3 codigos.

### Codigo A /Modulo 1
<br>

import math 

c= math.sqrt(81)

print('Modulo : ', __name__)
<br>

### Codigo B /Modulo 2

<br>


import math 

c= math.sqrt(9)

print('Modulo : ', __name__)

<br>

### Codigo C /Modulo 3

import exercicios.Modulo1 as Modulo1
import exercicios.Modulo2 as Modulo2

print('Modulo : ', __name__)

print(Modulo1.c)
print(Modulo2.c)

<br>


Se executar o programa Codigo A, verá que o print indica que o “__name__” é : “__main__”
Se executar o programa Codigo B, verá que o print indica que o “__name__” é : “__main__”

Se executar o programa Codigo C, verá que o ‘__name__’ continua = ‘__main__’, no entanto os módulos que são importados Codigo A e Codigo B,assumem o ‘__name__’ de ‘Modulo 1’ e ‘Modulo 2’ respetivamente. 
Isto porque são módulos importados pelo programa Codigo C que é quem tem agora o ‘__name__’ igual a ‘__main__’.

<br>

### Resultado do codigo C /Modulo 3:

<br>

Modulo :  Modulo1
<br>
Modulo :  Modulo2
<br>
Modulo :  __main__
<br>
9.0
<br>
3.0

-------------------------------------------------------------------------------------------------------------------

## Exercicio 

Com os conhecimentos que já adquiriu (pode consultar os apontamentos).Tente programar em Python o teorema de Pitágoras 
(Atribua os valores que entender a ‘a’ e ’b’).

from math import sqrt

<br>
a= 10
<br>
b=10
<br>
c= sqrt(a**2 + b**2)

<br>
print( "O cateto de a : ", str(a) + "\nO cateto de b :", str(b) + "\na hipotenusa de c :", str(c))

<br>

### Agora com input de utilizador 

from math import sqrt

<br>

a = float(input("O cateto de a : "))
<br>
b = float(input("O cateto de b : "))
<br>
c= sqrt(a**2 + b**2)

<br>

print("A hipotenusa de c : ",c)

-------------------------------------------------------------------------------------------------------------------


# Funções sem retorno

As funções sem retorno definem-se a partir da palavra "def" do Python.

Neste caso a função não retorna valor nenhum (O print não é transportado pela função, é apenas uma instrução dentro da função. Por isso diz-se também que esta função é um procedimento).

Este procediemento recebe dois valores (fator1 e fator2). Estes valores chamam-se argumentos da função / procedimento. Os argumentos so têm signifcado dentro da função

Igualmente à instrução "if" a função é delimitada no seu dominio através da identação.

![Markdown Preview](./image31.jpg)

A estrutura de uma funçaõ é definida pro um nome, pode ter ou não parametros , um processamento e pode ter ou não um retorno.

Para chamar uma função em pyhton, invocar o nome da função (se for o caso com os respetivos parametros linha.13)

Repare no pormenor das linhas 11 e 12, utilizaram uma conversão explicita para garantir que o valor dos "input" sejam do tipo inteiro , caso contrário poderia afetar a linha 7.

A função só vai ser executada se a execução pertencer ao "main" .

------------------------------------------------------------------------------------------------------------------------


# Funções com retorno 

Funções com retorno são iguais aos procedimentos, mas utilizam a palavra "return" para retomar uma determinado valor.

Neste caso temos a função "calcular_produto()" que recebe dois parametros(fator1 e fator2) e devolvem um resultado(fator1 *fator2) para o exterior. 

![Markdown Preview](./image31.jpg)

-------------------------------------------------------------------------------------------------------------------

# IF/ELIF

As linhas 5 a 22 representam a função que converte a nota quantitativa em qualitativa. 
A função "converter_nota_quantitativa(x)" recebe um valor que será convertido através de encadeamento de "if" e "else(elif)", e no fim devolve a conversão respetiva ("return").

### Imagem página 43

Da linha 25 para a frente, o programa usa um "if" para se certificar que se encontra ou não no mesmo modulo "main". Em caso afirmativo e só nesse caso é solicitado ao utilizador que introduza uma nota, a qual será utilizada na chamada da função de conversão.

NA linha 9 utiliza-se um novo conceito (range) que serve para definir um intervalo entre (x e y), em que x pertence ao intervalo mas y não pertence. Se o numero não pertencer ao intervalo é considerado incorreto.

# WHILE

Tal como o xercicio sugere, deve-se utilizar o módulo "Random" e especificamente uma das suas funções "randint". Esta função serve para extração de numeros aleatórios.
As linhas 5 a 13 estão comentadas, apenas para informar que tambem se poderia criar uma estrutura de dados da forma que se apresenta na linha 7, mas o exercicio obriga a privilegiar as estruturas "while".

### Imagem página 51

A linha 14 declara uma estrutura do tipo list vazia , para se poder utilizar o metodo "pop". 

As linhas 15 a 18 inicializa uma varivael (y) para preencher a lista com os números do jogo sequencialmenete(1 a 90). Por isso inicializa-se com 0 e increemnta-se a variavel y através de um ciclo while enquanto o y for menor que 90. Este ciclo garante que quando começa o jogo a lista contém todas as bolas necessárias dosponiveis a aserem usadas.

