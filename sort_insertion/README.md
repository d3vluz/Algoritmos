# Algoritmo Insertion Sort
## Descrição
O algoritmo Insertion Sort é um algoritmo de ordenação simples que funciona construindo uma lista ordenada, um elemento de cada vez. Ele pega um elemento da lista não ordenada e o insere na posição correta na lista ordenada.

## Notação Assintótica
+ **Melhor Caso:**
    - **Descrição:** A lista já está ordenada.
    - **Comportamento:** O algoritmo precisa apenas percorrer a lista uma vez, comparando cada elemento com o anterior.
    - **Número de Comparações:** n-1 comparações, onde n é o tamanho da lista.
    - **Complexidade:** O(n).

+ **Pior Caso:**
    - **Descrição:** A lista está ordenada de forma inversa.
    - **Comportamento:** Para cada elemento, o algoritmo precisa comparar com todos os elementos anteriores antes de encontrar sua posição correta.
    - **Número de Comparações:** 1 + 2 + 3 + ... + (n-1) = n(n-1)/2 comparações.
    - **Complexidade:** O(n²).

+ **Caso Médio:**
    - **Descrição:** A lista está parcialmente ordenada ou em uma ordem aleatória.
    - **Comportamento:** O número de comparações varia dependendo da ordem dos elementos, mas, em média, o algoritmo precisa comparar e trocar elementos um número significativo de vezes.
    - **Número de Comparações:** O número de comparações é difícil de calcular exatamente, mas, em média, ele se aproxima de n(n-1)/4 comparações.
    - **Complexidade:** O(n²).

## Vantagens
+ Eficiente para listas pequenas
+ Simples de entender e implementar
+ Adaptável para listas com elementos já quase ordenados

## Desvantagens
+ Requer memória adicional
+ Lentidão: O Insertion Sort é um algoritmo lento para listas grandes.
+ Ineficiente para listas grandes: o número de comparações aumenta exponencialmente com o tamanho da lista.

## Fontes para Estudo
+ [GeeksforGeeks](https://www.geeksforgeeks.org/insertion-sort/?ref=gcse)
+ [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
+ [Youtube](https://www.youtube.com/watch?v=JU767SDMDvA)

## Considerações
O Insertion Sort é geralmente mais eficiente que o Bubble Sort, mas ainda é considerado um algoritmo lento para listas grandes. Ele é mais adequado para listas pequenas ou listas quase ordenadas.