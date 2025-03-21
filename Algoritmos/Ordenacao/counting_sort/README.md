# Algoritmo Counting Sort
## Descrição
O Counting Sort é um algoritmo de ordenação não-comparativo que ordena elementos com base em contagens de ocorrências. Ele é especialmente eficiente quando o intervalo dos valores a serem ordenados não é significativamente maior que o número de elementos. O algoritmo funciona contando o número de elementos com valores distintos, calculando a posição de cada elemento na sequência de saída e então colocando cada elemento em sua posição correta.

## História Prática do Counting Sort
Imagine que você trabalha em uma fábrica de camisetas e precisa organizar um lote de 100 camisetas que chegaram da produção. As camisetas estão disponíveis em apenas 5 tamanhos (P, M, G, GG e XG), mas estão completamente desorganizadas no momento em que saem da linha de produção.

Em vez de comparar cada camiseta com outra para determinar sua ordem (o que seria feito em algoritmos como Bubble Sort ou Quick Sort), você pode adotar uma abordagem mais eficiente. Você coloca 5 caixas vazias no chão, cada uma rotulada com um dos tamanhos (P, M, G, GG, XG). Então, você simplesmente percorre todas as camisetas, uma por uma, e coloca cada uma na caixa correspondente ao seu tamanho.

Por exemplo, se a primeira camiseta for tamanho M, você a coloca na caixa M. Se a próxima for tamanho P, você a coloca na caixa P, e assim por diante. Este processo não requer nenhuma comparação entre as camisetas – você apenas verifica o tamanho de cada camiseta e a coloca na caixa correta.

Depois de processar todas as camisetas, você terá 5 caixas contendo camisetas de tamanhos específicos. Para finalizar a organização, você simplesmente esvazia as caixas em ordem (começando pela caixa P, depois M, G, GG e finalmente XG), resultando em todas as camisetas organizadas por tamanho. Este processo é exatamente como funciona o Counting Sort, mas em vez de caixas físicas, o algoritmo usa "contadores" (arrays) para rastrear a quantidade de cada valor e determinar sua posição final.

## Conclusão
O Counting Sort é incrivelmente eficiente para ordenar coleções de elementos onde a faixa de valores possíveis é conhecida e relativamente pequena em comparação com o número de elementos. Ele evita completamente as comparações entre elementos e, em vez disso, conta as ocorrências de cada valor. Esta abordagem permite que o algoritmo alcance uma complexidade linear O(n + k), onde n é o número de elementos a serem ordenados e k é a faixa de valores possíveis.

## Notação Assintótica
| Caso        | Complexidade de Tempo | Custo de Memória |
|:-----------:|:---------------------:|:-----------------:|
| Melhor Caso | O(n + k)              | O(k)             |
| Caso Médio  | O(n + k)              | O(k)             |
| Pior Caso   | O(n + k)              | O(k)             |

Onde:
- n é o número de elementos a serem ordenados
- k é a faixa de valores possíveis (valor máximo - valor mínimo + 1)

## Vantagens
+ **Eficiência Linear:** O Counting Sort possui complexidade de tempo O(n + k), tornando-o extremamente eficiente quando k é pequeno em relação a n.
+ **Estabilidade:** O algoritmo mantém a ordem relativa dos elementos de mesmo valor, o que o torna um algoritmo de ordenação estável.
+ **Simplicidade:** A implementação do Counting Sort é relativamente simples e direta.
+ **Zero Comparações:** Diferentemente de outros algoritmos de ordenação, o Counting Sort não realiza comparações entre os elementos, o que contribui para sua eficiência.

## Desvantagens
+ **Limitado a Inteiros:** O Counting Sort funciona apenas para valores inteiros (ou que possam ser mapeados para inteiros).
+ **Ineficiente para Grandes Intervalos:** Se a faixa de valores possíveis (k) for muito maior que o número de elementos (n), o algoritmo se torna ineficiente em termos de memória e tempo.
+ **Não In-place:** O algoritmo requer espaço adicional proporcional à faixa de valores, tornando-o não adequado quando o espaço de memória é uma restrição.
+ **Overhead de Memória:** O espaço adicional necessário para armazenar os contadores pode ser significativo, especialmente quando a faixa de valores é grande.

## Fontes para Estudo
+ [GeeksforGeeks](https://www.geeksforgeeks.org/counting-sort/)
+ [Programiz](https://www.programiz.com/dsa/counting-sort)
+ [YouTube](https://www.youtube.com/watch?v=OKd534EWcdk)
+ [Wikipedia](https://en.wikipedia.org/wiki/Counting_sort)

## Considerações
O Counting Sort é uma excelente escolha quando:
- O intervalo de valores possíveis é conhecido e não é significativamente maior que o número de elementos a serem ordenados.
- Os elementos são inteiros ou podem ser facilmente mapeados para inteiros.
- A estabilidade é um requisito importante.
- A eficiência de tempo é crítica e o espaço de memória não é uma grande restrição.

No entanto, para intervalos de valores muito grandes ou quando a memória é limitada, outros algoritmos como o Merge Sort ou o Quick Sort podem ser mais adequados, apesar de serem baseados em comparações. 