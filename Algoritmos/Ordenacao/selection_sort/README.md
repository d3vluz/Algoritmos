# Algoritmo Selection Sort

## Descrição
O Selection Sort é um algoritmo de ordenação simples e intuitivo. Ele funciona encontrando, a cada iteração, o menor elemento da parte não ordenada da lista e trocando-o com o primeiro elemento não ordenado. O algoritmo mantém duas sublistas dentro da lista original:
1. A parte já ordenada (no início da lista)
2. A parte ainda não ordenada (resto da lista)

A cada iteração, o algoritmo encontra o menor elemento da parte não ordenada e o move para o final da parte ordenada. Este processo continua até que toda a lista esteja ordenada.

## Funcionamento Passo a Passo

1. Encontre o menor elemento na parte não ordenada da lista
2. Troque este elemento com o primeiro elemento não ordenado
3. Mova a fronteira da parte ordenada uma posição à direita
4. Repita os passos 1-3 até que toda a lista esteja ordenada

## Exemplo Visual

Considere a lista: [5, 2, 9, 1, 7]

1. Iteração 1:
   - Lista inicial: [5, 2, 9, 1, 7]
   - Menor elemento na parte não ordenada: 1 (na posição 3)
   - Trocar com o primeiro elemento: [1, 2, 9, 5, 7]
   - Parte ordenada: [1]

2. Iteração 2:
   - Lista atual: [1, 2, 9, 5, 7]
   - Menor elemento na parte não ordenada: 2 (na posição 1)
   - Já está na posição correta
   - Parte ordenada: [1, 2]

3. Iteração 3:
   - Lista atual: [1, 2, 9, 5, 7]
   - Menor elemento na parte não ordenada: 5 (na posição 3)
   - Trocar com o elemento na posição 2: [1, 2, 5, 9, 7]
   - Parte ordenada: [1, 2, 5]

4. Iteração 4:
   - Lista atual: [1, 2, 5, 9, 7]
   - Menor elemento na parte não ordenada: 7 (na posição 4)
   - Trocar com o elemento na posição 3: [1, 2, 5, 7, 9]
   - Parte ordenada: [1, 2, 5, 7]

5. Iteração 5:
   - Lista atual: [1, 2, 5, 7, 9]
   - Parte ordenada: [1, 2, 5, 7, 9]
   - Lista completamente ordenada!

## Complexidade

| Caso          | Complexidade de Tempo | Complexidade de Espaço |
|---------------|:---------------------:|:----------------------:|
| Melhor Caso   | O(n²)                 | O(1)                   |
| Caso Médio    | O(n²)                 | O(1)                   |
| Pior Caso     | O(n²)                 | O(1)                   |

## Vantagens
- **Implementação simples**: Fácil de entender e codificar
- **In-place**: Não requer memória adicional além da lista original
- **Número mínimo de trocas**: Realiza no máximo n-1 trocas (onde n é o tamanho da lista)

## Desvantagens
- **Ineficiente para listas grandes**: A complexidade O(n²) torna o algoritmo lento para listas com muitos elementos
- **Não adaptativo**: O desempenho não melhora mesmo se a lista já estiver parcialmente ordenada

## Aplicações Práticas
- Útil para ordenar pequenas listas onde a simplicidade de implementação é mais importante que a eficiência
- Bom para sistemas com limitações de memória, devido à sua natureza in-place
- Situações onde minimizar o número de operações de troca é crucial

## Comparação com Outros Algoritmos
- **Bubble Sort**: Ambos têm complexidade O(n²), mas o Selection Sort geralmente realiza menos trocas
- **Insertion Sort**: Mais eficiente que o Selection Sort para listas quase ordenadas
- **Quick Sort/Merge Sort**: Significativamente mais rápidos para listas grandes (O(n log n))

## Fontes para Estudo
- [GeeksforGeeks](https://www.geeksforgeeks.org/selection-sort/)
- [Programiz](https://www.programiz.com/dsa/selection-sort)
- [Visualgo](https://visualgo.net/en/sorting)
- [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)