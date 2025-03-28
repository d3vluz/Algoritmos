# Insertion Sort: O Algoritmo da Carta

## O que é o Insertion Sort?
O Insertion Sort é um algoritmo de ordenação que funciona de forma semelhante a como organizamos cartas em nossa mão durante um jogo. Pegamos uma carta de cada vez e a inserimos na posição correta entre as cartas que já organizamos.

## Como funciona na prática?

Imagine que você está organizando cartas de baralho em sua mão:

1. Começamos com a primeira carta já "ordenada" na mão
2. Pegamos a segunda carta e decidimos se ela vai antes ou depois da primeira
3. Pegamos a terceira carta e a inserimos na posição correta entre as duas cartas que já estão organizadas
4. Continuamos pegando uma carta por vez e inserindo-a na posição correta
5. Ao final, todas as cartas estarão organizadas em ordem

## Exemplo visual
```
Lista inicial: [5, 2, 4, 6, 1, 3]

Primeira carta já está "ordenada": [5]
Segunda carta (2): 2 < 5, então inserimos antes → [2, 5]
Terceira carta (4): 2 < 4 < 5, então inserimos no meio → [2, 4, 5]
Quarta carta (6): 6 > 5, então inserimos depois → [2, 4, 5, 6]
Quinta carta (1): 1 < 2, então inserimos antes de todos → [1, 2, 4, 5, 6]
Sexta carta (3): 2 < 3 < 4, então inserimos no meio → [1, 2, 3, 4, 5, 6]

Lista ordenada: [1, 2, 3, 4, 5, 6]
```

## Desempenho

O desempenho do Insertion Sort varia conforme a situação:

| Situação         | Velocidade         | Espaço usado na memória |
|:----------------:|:------------------:|:-----------------------:|
| Melhor caso      | Rápido (O(n))      | Mínimo (O(1))           |
| Caso comum       | Lento (O(n²))      | Mínimo (O(1))           |
| Pior caso        | Lento (O(n²))      | Mínimo (O(1))           |

> **Nota:** O(n) significa que o tempo de ordenação cresce proporcionalmente ao tamanho da lista. O(n²) significa que o tempo cresce quadraticamente - ou seja, se dobrarmos o tamanho da lista, o tempo pode quadruplicar.

## Vantagens
+ Muito eficiente para listas pequenas ou quase ordenadas
+ Simples de entender e implementar
+ Usa pouca memória (ordena "no lugar")
+ É estável (mantém a ordem de elementos iguais)
+ Pode começar a ordenar antes de receber toda a lista

## Desvantagens
+ Lento para listas grandes e desordenadas
+ Não é tão eficiente quanto outros algoritmos para listas maiores
+ Faz muitas movimentações de elementos

## Quando usar
O Insertion Sort é ideal quando:
+ A lista é pequena (menos de 20 elementos)
+ A lista já está parcialmente ordenada
+ A simplicidade do código é mais importante que a velocidade
+ Precisamos de um algoritmo estável (que mantenha a ordem de itens iguais)
+ Estamos ordenando dados que chegam em tempo real (um por vez)

## Para aprender mais
+ [Visualização animada do Insertion Sort](https://visualgo.net/en/sorting)
+ [GeeksforGeeks: Explicação detalhada](https://www.geeksforgeeks.org/insertion-sort/)
+ [Vídeo: Insertion Sort explicado](https://www.youtube.com/watch?v=JU767SDMDvA)