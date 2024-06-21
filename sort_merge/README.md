## Algoritmo Merge Sort
## Descrição
O Merge Sort é um algoritmo de ordenação baseado na técnica "Dividir para Conquistar". Ele funciona dividindo recursivamente a lista em sublistas menores até que cada sublista tenha apenas um elemento. Em seguida, as sublistas são mescladas de forma ordenada para criar listas maiores, até que toda a lista seja ordenada.

## Notação Assintótica
**Melhor Caso:**
    - **Descrição:** A lista já está ordenada.
    - **Comportamento:** O algoritmo ainda precisa realizar todas as operações de divisão e mesclagem, mas não há comparações extras necessárias para ordenar os elementos.
    - **Número de Comparações:** N log N (onde N é o número de elementos)
    - **Complexidade:** O(N log N)

**Pior Caso:**
    - **Descrição:** A lista está ordenada inversamente.
    - **Comportamento:** O algoritmo precisa realizar o máximo de comparações para ordenar cada elemento em relação aos outros.
    - **Número de Comparações:** N log N
    - **Complexidade:** O(N log N)

**Caso Médio:**
    - **Descrição:** A lista está desordenada com elementos aleatórios.
    - **Comportamento:** O algoritmo realiza um número de comparações próximo ao pior caso.
    - **Número de Comparações:** N log N
    - **Complexidade:** O(N log N)

## Vantagens
+ Eficiência: Tem uma complexidade de tempo de O(N log N) em todos os casos, tornando-se um algoritmo eficiente para ordenar grandes conjuntos de dados.
+ Paralelismo: Pode ser facilmente paralelizado, o que o torna ideal para processamento em paralelo e desempenho otimizado.

## Desvantagens
+ Espaço Extra: O Merge Sort requer espaço extra para armazenar as sublistas durante o processo de mesclagem. Isso pode ser uma desvantagem para conjuntos de dados muito grandes onde a memória é limitada.
+ Complexidade de Implementação: A implementação do Merge Sort pode ser um pouco mais complexa em comparação com outros algoritmos de ordenação, como o Insertion Sort ou Bubble Sort.

## Fontes para Estudo
+ [Wikipedia](https://pt.wikipedia.org/wiki/Merge_sort)
+ [GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)
+ [Youtube](https://www.youtube.com/watch?v=4VqmGXwpLqc)

## Considerações
O Merge Sort é uma excelente escolha para ordenar grandes conjuntos de dados. Ele é eficiente, estável e pode ser paralelizado para desempenho otimizado. No entanto, a necessidade de espaço extra pode ser uma desvantagem para conjuntos de dados muito grandes.

