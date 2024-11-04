# Algoritmo Merge Sort
## Descrição
O Merge Sort é um algoritmo de ordenação estável baseado na técnica "Dividir para Conquistar". Ele funciona dividindo recursivamente a lista em sublistas menores até que cada sublista tenha apenas um elemento. Em seguida, as sublistas são mescladas de forma ordenada para criar listas maiores, até que toda a lista esteja ordenada.

## História Prática do Merge Sort
Imagine uma vila com vários carteiros encarregados de entregar cartas para todas as casas. Mas, ao final de um dia de trabalho, todas as cartas estão desorganizadas, sem qualquer ordem específica. Para garantir que cada carta seja entregue rapidamente no dia seguinte, o chefe dos carteiros decide organizar as cartas em ordem alfabética de destinatários. No entanto, a vila é grande e as cartas são muitas, então, em vez de tentar ordenar todas de uma vez, o chefe propõe uma estratégia “dividir para conquistar”.

Primeiro, ele divide o grupo de carteiros em pares e dá a cada dupla uma pilha menor de cartas para organizar. Cada dupla de carteiros, então, divide suas pilhas ao meio e começa a colocar as cartas em ordem, comparando-as e montando duas listas separadas de destinatários ordenados. Quando as listas de cada par estão em ordem, elas são mescladas de volta em uma única pilha ordenada.

Em seguida, o chefe une duas duplas de carteiros para formar um grupo de quatro, que então junta suas pilhas organizadas. Esse processo continua até que todos os carteiros tenham organizado e mesclado suas cartas, uma etapa por vez, até que não reste mais nenhuma divisão e todas as cartas estejam em uma única pilha ordenada. Agora, com todas as cartas organizadas, os carteiros podem começar a entrega de maneira rápida e eficiente no dia seguinte, poupando tempo e evitando confusões.

## Conclusão
O Merge Sort, assim como os carteiros que organizam as cartas em pequenas pilhas antes de juntá-las, é eficiente porque divide a tarefa em partes menores e organiza cada uma separadamente antes de mesclá-las. Dessa forma, ele garante uma ordenação rápida e consistente, ideal para grandes quantidades de dados, mantendo sempre uma eficiência de O(N log N).

## Notação Assintótica
| Caso        | Complexidade de Tempo | Custo de Memória |
|:-----------:|:---------------------:|:-----------------:|
| Melhor Caso | O(N log N)            | O(N)             |
| Caso Médio  | O(N log N)            | O(N)             |
| Pior Caso   | O(N log N)            | O(N)             |

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
O Merge Sort é uma excelente escolha para ordenar grandes conjuntos de dados. Ele é eficiente, estável e pode ser paralelizado para desempenho otimizado. Contudo, para conjuntos de dados extremamente grandes em ambientes de memória muito limitada, outras abordagens in-place podem ser mais apropriadas.