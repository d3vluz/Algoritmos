# Algoritmo Selection Sort
## Descrição
O Selection Sort é um algoritmo de ordenação simples e intuitivo. Ele funciona encontrando, a cada iteração, o menor (ou maior, dependendo da ordem desejada) elemento da lista e trocando-o com o primeiro elemento não ordenado. Esse processo se repete até que toda a lista esteja ordenada. O algoritmo mantém duas partes da lista: a parte ordenada (no início) e a parte não ordenada. Em cada passagem, ele escolhe o menor valor da parte não ordenada e o adiciona à parte ordenada, repetindo até que toda a lista esteja organizada. O Selection Sort é um algoritmo de ordenação in-place, o que significa que ele não requer memória adicional significativa além da lista original.

## História Prática do Selection Sort
Imagine que você é um(a) professor(a) em uma escola e está prestes a organizar uma fila de estudantes por altura, do menor ao maior. Você decide fazer isso de forma metódica, escolhendo sempre o menor aluno disponível e colocando-o na posição correta na fila.

Primeiro, você anda ao longo da fila inteira para identificar o aluno mais baixo entre todos. Depois de encontrá-lo, você o coloca na frente da fila, assumindo que aquele lugar é, agora, a posição correta dele. Com o primeiro aluno já na posição certa, você decide repetir o processo, mas agora começando pelo próximo aluno na fila. Você novamente percorre a fila restante, procurando o mais baixo dentre os que ainda não foram posicionados.

Este processo continua por toda a fila, sempre olhando para os estudantes que ainda não foram organizados e selecionando o próximo mais baixo para colocá-lo na posição correta. À medida que você vai ordenando, os estudantes começam a se alinhar, da menor à maior altura. Cada vez que você seleciona o menor aluno da parte restante da fila, você reduz a lista dos desordenados e aumenta a parte da fila que já está em ordem. Isso segue até que todos estejam finalmente no lugar certo.
## Conclusão
A analogia dos alunos na fila demonstra a essência do Selection Sort: a busca constante pelo próximo menor elemento e sua inserção na posição correta. Este método é fácil de compreender e aplicar em casos de listas pequenas. No entanto, para um grande número de alunos, essa abordagem se torna ineficiente, pois é necessário percorrer toda a lista para encontrar o próximo menor valor, tornando-a uma tarefa trabalhosa e repetitiva.

## Notação Assintótica
| Tipo de Caso  | Complexidade de Tempo | Complexidade de Espaço |
|:-------------:|:---------------------:|:----------------------:|
| Melhor Caso   | O(n²)                 | O(1)                   |
| Caso Médio    | O(n²)                 | O(1)                   |
| Pior Caso     | O(n²)                 | O(1)                   |

## Vantagens
- **Simples de Implementar**: A lógica do Selection Sort é fácil de entender e implementar, especialmente para iniciantes.
- **Pouca Memória Adicional**: O algoritmo é um algoritmo **in-place**, ou seja, ele não usa memória extra significativa, tornando-o útil quando o espaço é um fator crítico.
- **Número Fixo de Trocas**: O Selection Sort faz no máximo **n - 1** trocas, o que é menor que a quantidade de trocas feitas por outros algoritmos de ordenação, como o Bubble Sort.

## Desvantagens
- **Ineficiente para Grandes Listas**: A complexidade de tempo O(n²) torna o Selection Sort inadequado para listas grandes, pois se torna muito lento em comparação a outros algoritmos de ordenação mais eficientes, como Merge Sort ou Quick Sort.

## Fontes para Estudo
+ [GeeksforGeeks](https://www.geeksforgeeks.org/insertion-sort-algorithm/)
+ [Programiz](https://www.programiz.com/dsa/insertion-sort)
+ [Youtube](https://www.youtube.com/watch?v=g-PGLbMth_g)
+ [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)

## Considerações
O Selection Sort é uma escolha razoável quando:
- **Tamanho da Lista é Pequeno**: Para listas pequenas (geralmente com menos de 50 elementos), a simplicidade do algoritmo faz com que seja uma boa escolha.
- **Memória é Limitada**: Quando há pouca memória disponível, o fato de ser um algoritmo **in-place** pode ser vantajoso em comparação com algoritmos que exigem mais memória adicional.
- **Baixa Frequência de Trocas é Preferível**: O Selection Sort minimiza o número de trocas, sendo útil quando trocar elementos é uma operação mais cara do que comparar, por exemplo, ao lidar com estruturas de dados específicas como listas ligadas.

No entanto, para listas maiores, o Selection Sort se torna inviável devido à sua complexidade quadrática, e algoritmos mais sofisticados, como Merge Sort, Quick Sort ou Heap Sort, são preferíveis.