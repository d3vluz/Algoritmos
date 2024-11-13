# Algoritmo Heap Sort
## Descrição
O Heap Sort é um algoritmo de ordenação baseado em comparação que utiliza a **Estrutura de Dados Heap** (ou pilha de prioridades) para ordenar os elementos. Ele funciona em três etapas principais:

1. **Construção do Heap:** A lista de entrada é transformada em um heap máximo (ou heap mínimo, dependendo da ordem desejada). Em um heap máximo, o maior valor está sempre na raiz da estrutura de dados, enquanto em um heap mínimo, o menor valor ocupa essa posição. Esse processo de construção começa nos nós internos (os que têm filhos) e se expande até a raiz, garantindo que cada nó pai seja maior (ou menor) que seus filhos. Isso cria uma árvore binária quase completa que facilita o ordenamento dos elementos.

2. **Ordenação:** O processo de ordenação começa trocando o maior elemento (raiz do heap máximo) com o último elemento da lista. Essa troca move o maior valor para sua posição final na lista ordenada. Em seguida, o tamanho do heap é reduzido em 1 (desconsiderando o último elemento já ordenado) para que o processo possa continuar.

3. **Heapify:** Após a troca, a operação de heapify é aplicada à nova raiz do heap para restaurar a estrutura de heap e garantir que o próximo maior (ou menor) elemento suba para a raiz. Esse ajuste é feito repetidamente a cada troca e reorganização, até que toda a lista esteja ordenada.

## História Prática do Heap Sort
Imagine que você está lidando com uma pilha de malas de viagem para preparar uma grande mudança. Você precisa organizar as malas de tal forma que seja mais fácil pegar as maiores primeiro, garantindo que tudo fique bem ordenado e seguro. Sua missão é empilhar as malas de maneira que as menores fiquem no topo e as maiores fiquem na base, assegurando estabilidade e ordem.

O primeiro passo é organizar as malas na pilha de forma eficiente. Ao começar, você se certifica de que as malas maiores fiquem por baixo, pois elas são mais resistentes e estáveis, e as menores ficam por cima, onde podem ser mais facilmente removidas. Isso é semelhante ao Heap Sort transformando a lista de elementos em um "heap máximo". Assim como a mala maior precisa dar suporte às menores, o heap máximo garante que o maior elemento esteja sempre no topo da hierarquia, garantindo que a pilha esteja estável.

Uma vez que você montou essa pilha inicial de malas, chega o momento de movê-las uma a uma para o caminhão de mudança. Você começa pegando a mala maior que está na base. Quando você retira a maior mala, cria um espaço vazio que precisa ser preenchido por uma das malas que ainda restam na pilha. A melhor forma de fazer isso é pegar a mala que estava mais ao topo e colocá-la naquele espaço. Mas isso pode bagunçar a organização, então você ajusta tudo novamente para garantir que a pilha continue estável — sempre com as malas maiores abaixo das menores.

Esse processo continua até que todas as malas sejam retiradas e estejam colocadas no caminhão em ordem de tamanho, do maior para o menor. Cada vez que você ajusta a pilha, está certificando-se de que a estrutura continue a mesma, onde cada mala maior está em uma posição que sustenta as menores que vêm depois dela. Dessa forma, tudo acaba perfeitamente organizado, evitando riscos de colapso e garantindo uma ordem eficiente.

Assim como organizar uma pilha de malas para facilitar a mudança, o Heap Sort é sobre construir uma estrutura organizada e, em seguida, extrair cada elemento de forma ordenada e eficiente. Ele transforma uma lista desorganizada em uma estrutura estável e previsível, e depois vai removendo e ajustando os elementos para garantir que a ordem desejada seja mantida. No final, a mudança está pronta, e todas as malas estão cuidadosamente empilhadas no caminhão, da maior para a menor, prontas para seguir o caminho.

## Conclusão
O Heap Sort é uma opção eficiente para ordenação, pois possui uma complexidade constante de O(N log N) em todos os casos. Sua abordagem baseada em heap permite que a ordenação seja feita no local, economizando memória, o que o torna uma escolha sólida para grandes conjuntos de dados. No entanto, ele não mantém a ordem de elementos iguais, o que pode ser uma limitação em alguns cenários.

## Notação Assintótica

| Caso        | Complexidade de Tempo | Custo de Memória |
|:-----------:|:---------------------:|:-----------------:|
| Melhor Caso | O(N log N)            | O(1)             |
| Caso Médio  | O(N log N)            | O(1)             |
| Pior Caso   | O(N log N)            | O(1)             |

## Vantagens
+ **Presvisibilidade:**  O Heap Sort tem uma complexidade de tempo de O(N log N) para todos os casos (melhor, médio e pior), o que garante previsibilidade durante a execução.
+ **Ordenação no Local:** O Heap Sort realiza a ordenação "in-place", ou seja, não requer um uso excessivo de memória adicional, utilizando apenas um espaço extra constante **O(1)**.

## Desvantagens
+ **Não Estável:** Heap Sort não preserva a ordem dos elementos iguais, o que pode ser problemático em situações em que a estabilidade é importante, como quando há necessidade de manter a sequência original de dados com valores iguais.
+ **Complexidade de Implementação:** A lógica de construção e manutenção do heap pode ser mais difícil de implementar corretamente em comparação com algoritmos mais simples de ordenação, o que aumenta a complexidade do código e a chance de erros.
+ **Número de Trocas:** O processo de re-heapificação exige várias trocas de elementos, o que pode tornar o Heap Sort menos eficiente para dados que já estão quase ordenados, além de não ser ideal para contextos onde o número de trocas deve ser minimizado.

## Fontes para Estudo
+ [GeeksforGeeks](https://www.geeksforgeeks.org/heap-sort/)
+ [Programiz](https://www.programiz.com/dsa/heap-sort)
+ [YouTube](https://www.youtube.com/watch?v=2DmK_H7IdTo)
+ [Wikipedia](https://en.wikipedia.org/wiki/Heapsort)

## Considerações
O Heap Sort é uma boa escolha quando precisamos de um tempo de execução previsível, especialmente ao lidar com grandes volumes de dados. No entanto, ele não é ideal quando a estabilidade é crucial — ou seja, quando precisamos que a ordem original de elementos iguais seja preservada. Nesse caso, o Merge Sort é uma opção melhor, pois é um algoritmo estável. Além disso, o Heap Sort tende a ser menos eficiente em média em comparação com outros algoritmos, como o Quick Sort, que geralmente é mais rápido para ordenar conjuntos de dados típicos, apesar de não ter garantia de bom desempenho no pior caso.