'''#list.append(x)#
Adiciona um item ao fim da lista. Equivalente a a[len(a):] = [x].

#list.extend(iterable)#
Prolonga a lista, adicionando no fim todos os elementos do argumento iterable passado como parâmetro. Equivalente a a[len(a):] = iterable.

#list.insert(i, x)#
Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x) insere um elemento na frente da lista e a.insert(len(a), x) e equivale a a.append(x).

#list.remove(x)#
Remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError é levantada.

#list.pop([i])#
Remove um item em uma dada posição na lista e o retorna. Se nenhum índice é especificado, a.pop() remove e devolve o último item da lista. (Os colchetes ao redor do i na demonstração do método indica que o parâmetro é opcional, e não que é necessário escrever estes colchetes ao chamar o método. Você verá este tipo de notação frequentemente na Biblioteca de Referência Python.)

#list.clear()#
Remove todos os itens de uma lista. Equivalente a del a[:].

#list.index(x[, start[, end]])#
Devolve o índice base-zero do primeiro item cujo valor é igual a x, levantando ValueError se este valor não existe.

Os argumentos opcionais start e end são interpretados como nas notações de fatiamento e são usados para limitar a busca para uma subsequência específica da lista. O índice retornado é calculado relativo ao começo da sequência inteira e não referente ao argumento start.

#list.count(x)#
Devolve o número de vezes em que x aparece na lista.

#list.sort(*, key=None, reverse=False)#
Ordena os itens na lista (os argumentos podem ser usados para personalizar a ordenação, veja a função sorted() para maiores explicações).

#list.reverse()#
Inverte a ordem dos elementos na lista.

#list.copy()#
Devolve uma cópia rasa da lista. Equivalente a a[:].

lista_compras = ['banana','laranja','maçã']
print(lista_compras)
['banana', 'laranja', 'maçã']
Cada item da lista possui uma posição. Por padrão, as posições não iniciam do 1 (um) e sim do 0 (ZERO). Nos códigos seguintes temos as formas de acessar uma informação da lista.

#Para acessarmos um item da lista vamos utilizar a estrutura: nomedalista[posição].#

Buscando a posição [1]:

print(lista_compras[1])
laranja
Buscando a posição [0]:

print(lista_compras[0])
banana
Se tentarmos buscar a posição [3] teremos um erro. Isso corre, porque não existe uma posição 3. Apenas as posições [0], [1], [2]:

print(lista_compras[3])

#Agora vamos analisar alguns métodos do Python como: append e insert (para inserir informações na lista); del, pop e remove (para remover itens da lista).

Para adicionar um item a lista:

#.append(): adiciona o item ao final da lista;
#.insert(): insere um item na lista na posição indicada
Para deletar um item da lista:#

#del: remove um item da lista baseado na posição indicada;
.remove(): remove um item baseado no seu valor e não na sua posição;
.pop(): remove da lista_compras o último item, mas não o exclui.#

 atividade = input(Insira uma atividade: ')
   tarefas.append(atividade)

lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000, 20000, 50000]

#O .sort() ordena os valores do maior para o menor. Atenção: as duas listas não estão conectadas.#

lojas.sort()
vendas.sort()
Perceba que ao mudarmos a ordem, não temos mais a Rio de Janeiro -> 10000 / São Paulo -> 20000 / Curitiba -> 50000:

print(lojas)
print(vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo']
[10000, 20000, 50000]

print(lista_compras[1])

laranja

#Concatenar lista Python (operador +)#

Em um exemplo, [2, 4, 6] + [3, 5] retorna [2, 3, 4, 5, 6]

#Multiplicação (operador *)#

Esse operador repete (replica) uma lista diversas vezes. Se multiplicarmos nossa lista_compras por 3, teremos:

[‘banana’,’laranja’,’maçã’,’banana’,’laranja’,’maçã’,’banana’,’laranja’,’maçã’]

#Descobrindo o tamanho das listas Python (operador len() )#

#A função len() retorna a quantidade de elementos existentes#. Na nossa lista_compras, teríamos:

print(len(lista_compras))

#Verificando a existência de itens nas listas Python (operador in)#

Esse operador percorre todos os itens e retorna “True”, se houver equivalência, e “False”, se não houver o valor. Veja:

lista_compras = [‘banana’,’laranja’,’maçã’]

‘banana’ in lista_compras

True

‘mamão’ in lista_compras

False

#Descobrindo os valores mínimos, máximos e soma (operadores min(), max() e sum())#

Com esses operadores, você encontra o menor ou maior valor da lista, ou ainda soma de todos os elementos dela. Na Listagem 3 podemos ver como utilizá-las.

Veja o exemplo com uma lista numérica:

numeros = [1, 3, 5, 7, 9]

print(min(numeros))

#Resultado: 1

print(max(numeros))

#Resultado: 9

print(sum(numeros))

#Resultado: 25'''