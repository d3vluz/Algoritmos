# Algoritmo Heap Sort
## Descrição
O algoritmo Heap Sort é um algoritmo de ordenação baseado em comparação que utiliza a estrutura de dados heap (pilha de prioridades). Ele funciona em duas fases principais:
- 1. **Construção do Heap:** A lista de entrada é transformada em um heap máximo (ou mínimo, dependendo da ordem desejada). Um heap máximo é uma árvore binária quase completa, onde o valor de cada nó pai é maior ou igual aos valores dos seus filhos.
- 2. **Ordenação:** O elemento raiz do heap (o maior elemento) é trocado com o último elemento da lista. O tamanho do heap é reduzido em 1 e a operação de heapify é aplicada à nova raiz para manter a propriedade do heap. Esse processo se repete até que a lista esteja ordenada.

## Notação Assintótica
|            | Melhor Caso                                 | Pior Caso                                  | Caso Médio                                |
|------------|---------------------------------------------|---------------------------------------------|--------------------------------------------|
| Descrição | A lista já está ordenada como um heap.     | A lista está em ordem inversa.             | A lista está em ordem aleatória.           |
| Comportamento | O algoritmo realiza menos comparações.     | O algoritmo realiza o máximo de comparações. | O algoritmo tem um desempenho intermediário. |
| Comparações| O(n log n)                                  | O(n log n)                                  | O(n log n)                                 |
| Complexidade | O(n log n)                                  | O(n log n)                                  | O(n log n)                                 |
## Vantagens
+ **Complexidade de Tempo Consistente:** O Heap Sort possui complexidade de tempo O(n log n) em todos os casos (melhor, pior e médio). Isso o torna uma boa escolha quando a previsibilidade do tempo de execução é crucial.
+ **Eficiente em Grandes Conjuntos de Dados:** O Heap Sort tem um bom desempenho em grandes conjuntos de dados, pois realiza um número relativamente baixo de comparações e trocas.
+ **Ordenação no Local:** O Heap Sort requer apenas uma quantidade constante de espaço adicional, tornando-o uma ordenação no local.

## Desvantagens
+ **Não Estável:** O Heap Sort não mantém a ordem relativa de elementos iguais.
+ **Implementação Complexa:** A implementação do Heap Sort é mais complexa em comparação com outros algoritmos de ordenação, como o Bubble Sort e o Insertion Sort.
+ **Menos Eficaz que o Quick Sort em Média:** Embora o Heap Sort tenha um limite superior garantido de O(n log n), ele geralmente é menos eficaz que o Quick Sort em cenários de caso médio.

## Fontes para Estudo
+ **Khan Academy:** [https://www.khanacademy.org/computing/computer-science/algorithms/heap-sort/a/overview-of-heap-sort]
+ **GeeksforGeeks:** [https://www.geeksforgeeks.org/heap-sort/]
+ **Programiz:** [https://www.programiz.com/dsa/heap-sort]

## Considerações
O Heap Sort é uma boa escolha para ordenação quando a previsibilidade do tempo de execução é crucial e o conjunto de dados é grande. No entanto, ele pode não ser a melhor escolha para conjuntos de dados pequenos ou quando a estabilidade da ordenação é importante.