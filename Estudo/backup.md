# FOR 

A instrução 'for' tem uma utilização simples.
Repare na linha 5, que reduziu linhas de codigo do exercicio anterior.

A lógica desta instrução é 'iterar', para isso necessitar de uma variavel (variavel iteradora), que neste caso é representada por n.

Utiliza-se tambem a função 'range'. O range estabelece um dominio (a,b) ex: range(1,91). Não esquecer que a função é aberta/fechada o quer dizer que o ultimo numero nao conta, neste caso para o dominio ser de 1 a 90 terá de ser 1 a 91.

Tambem se pode usar a função range com apenas 1 numero, se o utilizador quiser um dominio de 0 a n pode usar range(90).

### ver imagem pagina 58

A funcao range tambme pode dar um 'salto' entre cada elemento do seu dominio. 
'range(x,y,z)' , em que x é o limite inferior, o y o limite superior e o z o 'salto' que se da entre x e y.




# Porque será que o programa tal como é apresentado em cima, entra em ‘loop’ ? … e onde entra em ‘loop’ ?

Porque a linha 5 carrega a lista com 90 numeros , mas que vão de 0 a 89. O programa entra em loop na linha 7 , porque o numero '0' nunca é extraido uma vez que na linha 8 , apenas escolhe numero de 1 a 90.
Entao o '0'0 ficará sempre na lista, e a linha 7 é testada incondicionalmente , porque a condição será sempre maior que 0.

# Ver exercicio pagina 60

Neste exercicio , recorreu-se a um for encadeado (um 'for' dentro de outro 'for').
A linha 4 , inicia um ciclo de iterador 'n' de 0 a 10 , sendo que cada elemento deve dar um passo de  2 em 2.

Como a ideia seria sequenciar uma lista de numeros (de 0 ate ao limite) por cada elemento do primerio ciclo . então cria-se outro ciclo (linha6)