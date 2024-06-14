def bubbleSort(lista):
    '''
    - Entrada:
        Uma Lista, que será ordenada
    - Saída:
        A Lista que entrou como argumento ordenada.
    '''

    # Faz um "for" que pecorre todo array, passando o tamanho da lista como parâmetro através de "len(lista)"
    for i in range(len(lista)):
        # Pecorre toda a lista, porém vai diminuindo os elementos comparados ao decorrer da execução
        for j in range(len(lista)-i-1):
            # Verifica se o sucessor de "j" é maior que ele, caso seja troca ambos de lugares
            if lista[j] > lista[j+1]:
                lista [j], lista [j+1] = lista[j+1],lista[j]
    return lista

'''
#Exemplo de Teste:
entrada = [24,10,85,2003,9,84,9,8,19]
print(entrada)
print(bubbleSort(entrada))
'''