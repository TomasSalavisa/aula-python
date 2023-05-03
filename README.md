# aula-python

## Apontamento Pyhton

tudo dentro de aspas "" é string.

criar uma nova pasta e instalar as cenas nesse ambiente, e assim nao ficam no pc mas sim na pasta.


http://127.0.0.1:8888/?token=8b937d295235f976a2f2fee65218460fbe1f37415b8f444b link do ananconda


dir(int) para ver os numeros magicos dos integer

dir(float) para ver os numeros magicos dos float



numero magico  ->  'is_integer', ve se o output é int ou não

10.0 pode ter decimal mas como a decimal é 0, o python conta como se nao tivesse anda como os humanos.

__pow__(x,y) é o numero magico da potencia, x é elevado a y.


As funçoes sao:

Entrada->Processamento->Saida    Nome(...,...,...) ->return o output.

import decimal-> importa as funções todas do decimal

Mas se eu nao quiser todas e só 2 faço 'from decimal import Decimal, getcontext(nome das funçoes)

from biblioteca import nome das funções a importar(querer usar).


---------------------------------------------------------------------------------------------------------

nome="Filipe"

Uma string é uma estrutura de dados primaria que representam um conjunto de caracteres textoalmente.

'len' é usado para ver quantos caracters existem numa string

para ver a posiçao de uma string -> cidade[10]; nome da variavel e a posição da string/array


lingua estrutural diff de lingua funcional


TUDO QUE O SETOR FAZ NA AULA É PARECIDO AO DOS EXAMES.

--------------------------------------------------------------------------------------

função split() --> corta a string por espaços.
 split("L") --> corta a string sempre que houver um L --> ex: "Vila real de santo antonio --> 
 "Vi","a rea","de santo antonio";

 numero magico "x__lt__(y)" less then --> se um numero é menor que o outro, i.e, se o x é menor que o y

 python é uma lingua dinamica heterogenica --> pode ter mais do que um tipo de dados na mesma variavel(heterogenea) + podes adicionar mais numero a lista(dinamica).

 l= 1,2 ---> posso adicionar mais elementos se for dinamica, nao posso adicionar nada se for estatica.

 l = 'A', 'B', 1, 2, 43,67 ---> hetereogennea, se nao poder ter então é homogenea

 É UMA LISTA SE TIVER [].

 a funçao .append() cria um elemento dentro da lista.

 a função .insert() cria um elemento dentro da lista numa posição especifica --> insert(2,"maria")

 a funçao .count() conta e diz te o numero de vezes que esse elemento existe na lista.

 del alunos[6] remove o elemento que estiver na posição 6 da lista.

 del alunos [4::] remove todo o que estiver depois da posição 4.

 index.(2) diz te que elemento esta na posição 2 na lista.

 clear() apaga o conteudo da lista mas ela ainda existe

 del() apaga a lista, assim deixa de haver lista


O tipo de dados tuple() é um tipo estatico, neste caso nao deixa adiconar nada a lista, teria de criar a lista denovo com os elementos novos.


estrutura de dados --> linahs e colunas ou atributos e registos.

 class dict --> dicionario


 atributo vs metodo:

 atributo nao tem () mas metodo tem ().

 atributo so tem um valor --> ex: len só te diz um valor 10,20....

 metodo tem mais ações, tem varios maneiras de construir --> values() depois podes construir depois --> ex: values().len().
