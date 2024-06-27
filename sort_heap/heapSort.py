def heapify(arr, n, i):
  """
  Função para transformar uma subárvore em um heap máximo.

  Args:
      arr: Lista a ser ordenada.
      n: Tamanho do heap.
      i: Índice da raiz da subárvore.
  """
  largest = i  # Inicializa o maior como raiz
  l = 2 * i + 1  # Filho esquerdo
  r = 2 * i + 2  # Filho direito

  # Verifica se o filho esquerdo existe e é maior que a raiz
  if l < n and arr[largest] < arr[l]:
    largest = l

  # Verifica se o filho direito existe e é maior que a raiz
  if r < n and arr[largest] < arr[r]:
    largest = r

  # Se o maior não for a raiz
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # Troca a raiz

    # Recursivamente, transforma a subárvore afetada em um heap
    heapify(arr, n, largest)


def heap_sort(arr):
  """
  Função para realizar a ordenação heapsort.

  Args:
      arr: Lista a ser ordenada.
  """
  n = len(arr)

  # Constrói um heap máximo
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # Extrai elementos do heap, um por vez
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]  # Troca o elemento raiz (maior) com o último elemento
    heapify(arr, i, 0)  # Chama o heapify na subárvore reduzida


# Exemplo de uso:
arr = [12, 11, 13, 5, 6, 7]
print(arr)
heap_sort(arr)
print(arr)