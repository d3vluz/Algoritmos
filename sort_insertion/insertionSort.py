def insertionSort(lista):
    '''
    - Entrada:
        Uma Lista, que será ordenada
    - Saída:
        A Lista que entrou como argumento ordenada.
    '''
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        # Armazena o elemento atual
        key = lista[i]
        # Percorre a lista (da esquerda para a direita)
        j = i-1
        # Enquanto j for maior que 0 e o elemento anterior (j) for maior que key, move o elemento anterior para a direita
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        # Insere o elemento atual (key) na posição correta
        lista[j+1] = key
    return lista


#Exemplo de Teste:
entrada = [24,10,85,2003,9,84,9,8,19]
print(entrada)
print(insertionSort(entrada))