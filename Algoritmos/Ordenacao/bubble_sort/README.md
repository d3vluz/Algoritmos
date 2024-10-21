# Algoritmo Bubble Sort
## Descrição 
O algoritmo Bubble Sort é um algoritmo de ordenação simples que compara elementos adjacentes em uma lista e os troca de posição se estiverem na ordem errada. Ele repete esse processo para todos os pares de elementos adjacentes na lista até que a lista esteja ordenada.

## História Prática do Bubble Sort
Imagine uma biblioteca com uma prateleira de livros desorganizada, onde cada livro é colocado aleatoriamente. O bibliotecário, novato no seu trabalho, decide organizar os livros em ordem alfabética para facilitar a localização pelos visitantes. 

Começando da esquerda para a direita, o bibliotecário compara dois livros adjacentes. Se o livro à esquerda deveria vir após o livro à direita em ordem alfabética, ele troca os dois de lugar. Esse processo é repetido ao longo da prateleira. Ao chegar ao final da prateleira, o bibliotecário retorna ao início e repete o processo. A cada passagem completa, o livro que deveria estar na posição mais à direita da sequência desorganizada 'borbulha' para a sua posição correta.

Por exemplo, se a prateleira tiver livros com títulos começando com "D", "C", "B", e "A", na primeira passagem, o "D" será comparado com o "C", e trocados de lugar. Depois, "D" será comparado com "B", e novamente trocado. Finalmente, "D" será comparado com "A", e mais uma vez trocado, acabando na posição mais à direita. Este método continua até que todos os livros estejam em ordem alfabética, e o bibliotecário possa ter certeza de que nenhuma troca adicional é necessária.

## Conclusão
Esse método, embora eficaz para uma pequena quantidade de livros, torna-se muito demorado à medida que o número de livros aumenta, pois cada livro pode potencialmente ser movido muitas vezes antes de estar na posição correta. Por isso, o bibliotecário logo aprende que para uma grande coleção de livros, métodos mais eficientes de organização poderiam ser mais adequados. No entanto, para um iniciante que está apenas aprendendo sobre organização e ordenação, este método oferece uma excelente forma visual e prática de entender os princípios básicos da ordenação.

## Notação Assintótica
| Caso        | Complexidade de Tempo | Custo de Memória |
|:-----------:|:---------------------:|:----------------:|
| Melhor Caso | O(n)                  | O(1)             |
| Caso Médio  | O(n²)                 | O(1)             |
| Pior Caso   | O(n²)                 | O(1)             |

## Vantagens
+ Simples de entender e implementar
+ Não requer memória adicional

## Desvantagens
+ Lentidão: O Bubble Sort é um algoritmo lento, especialmente para listas grandes.
+ Ineficiente para listas grandes: o número de comparações aumenta exponencialmente com o tamanho da lista.

## Fontes para Estudo
+ [GeeksforGeeks](https://www.geeksforgeeks.org/bubble-sort/?ref=header_search)
+ [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)
+ [Youtube](https://www.youtube.com/watch?v=xli_FI7CuzA)

## Considerações
Em geral, o Bubble Sort não é recomendado para uso em aplicações reais devido à sua baixa eficiência. Porém é bastante usado para aprendizado, principalmente nos primeiros contatos com métodos de ordenação