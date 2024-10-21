def mergeSort(arr):
    '''
    - Entrada:
        Uma Lista, que será ordenada
    - Saída:
        A Lista que entrou como argumento ordenada.
    '''

    # Separa o Array estudado em duas metades
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursivamente separa e ordena as metades.
        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        # Mescla as duas metades ordenadas de volta para a lista original
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copia os elementos restantes (se houver) da metade esquerda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia os elementos restantes (se houver) da metade direita
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

'''
#Exemplo de Teste:
entrada = [24,10,85,2003,9,84,9,8,19]
print(entrada)
print(mergeSort(entrada))
'''