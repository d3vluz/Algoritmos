# Bubble Sort: O Algoritmo da Bolha

## O que é o Bubble Sort?
O Bubble Sort é um dos algoritmos de ordenação mais simples que existe. Ele funciona comparando cada elemento com o próximo e trocando-os de lugar se estiverem na ordem errada. É como se os elementos mais "leves" fossem subindo como bolhas na água até chegarem ao topo.

## Como funciona na prática?

Imagine uma fila de pessoas organizadas por altura, do menor para o maior:

1. Começamos pelo início da fila
2. Comparamos a primeira pessoa com a segunda
3. Se a primeira for mais alta que a segunda, trocamos suas posições
4. Seguimos comparando e trocando até o final da fila
5. Ao final da primeira rodada, a pessoa mais alta estará no final da fila
6. Repetimos o processo, mas agora ignorando a última posição (que já está correta)
7. Continuamos até que todas as pessoas estejam ordenadas

## Exemplo visual
```
Lista inicial:  [5, 3, 8, 4, 2]

Primeira rodada:
  Comparar 5 e 3: Troca → [3, 5, 8, 4, 2]
  Comparar 5 e 8: Não troca → [3, 5, 8, 4, 2]
  Comparar 8 e 4: Troca → [3, 5, 4, 8, 2]
  Comparar 8 e 2: Troca → [3, 5, 4, 2, 8]
  
Segunda rodada:
  Comparar 3 e 5: Não troca → [3, 5, 4, 2, 8]
  Comparar 5 e 4: Troca → [3, 4, 5, 2, 8]
  Comparar 5 e 2: Troca → [3, 4, 2, 5, 8]
  
Terceira rodada:
  Comparar 3 e 4: Não troca → [3, 4, 2, 5, 8]
  Comparar 4 e 2: Troca → [3, 2, 4, 5, 8]
  
Quarta rodada:
  Comparar 3 e 2: Troca → [2, 3, 4, 5, 8]
  
Lista ordenada: [2, 3, 4, 5, 8]
```

## Desempenho

O Bubble Sort é simples, mas não é o mais rápido:

| Situação         | Velocidade         | Espaço usado na memória |
|:----------------:|:------------------:|:-----------------------:|
| Melhor caso      | Rápido (O(n))      | Mínimo (O(1))           |
| Caso comum       | Lento (O(n²))      | Mínimo (O(1))           |
| Pior caso        | Lento (O(n²))      | Mínimo (O(1))           |

> **Nota:** O(n) e O(n²) são formas de representar a velocidade do algoritmo. O(n) significa que o tempo cresce de forma proporcional ao tamanho da lista. O(n²) significa que o tempo cresce de forma quadrática - se dobrarmos o tamanho da lista, o tempo será 4 vezes maior.

## Vantagens
+ Muito fácil de entender e implementar
+ Não precisa de memória extra para funcionar
+ Funciona bem para listas pequenas
+ É estável (itens iguais mantêm a ordem original)

## Desvantagens
+ Muito lento para listas grandes
+ Faz muitas comparações desnecessárias
+ Existem algoritmos muito mais eficientes para a maioria das situações

## Quando usar
O Bubble Sort é mais útil como ferramenta de aprendizado do que para uso real. Use-o quando:
+ Estiver aprendendo sobre algoritmos de ordenação
+ A lista for muito pequena (menos de 10 elementos)
+ A simplicidade for mais importante que a velocidade

## Para aprender mais
+ [Visualização animada do Bubble Sort](https://visualgo.net/en/sorting)
+ [GeeksforGeeks: Explicação detalhada](https://www.geeksforgeeks.org/bubble-sort/)
+ [Vídeo: Bubble Sort explicado](https://www.youtube.com/watch?v=xli_FI7CuzA)