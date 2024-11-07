import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        yield lista, 0, i, i
        yield from heapify(lista, i, 0)
    
    yield lista, -1, -1, 0

def heapify(lista, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lista[i] < lista[left]:
        largest = left

    if right < n and lista[largest] < lista[right]:
        largest = right

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        yield lista, i, largest, n
        yield from heapify(lista, n, largest)

def visualize_heap_sort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Heap Sort")
    bar_rects = ax.bar(range(N), lista, align="edge", color='blue')
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * N))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    ordered_indices = set()

    def update_fig(data, rects, iteration):
        lista, index1, index2, end_sorted = data
        for rect, val in zip(rects, lista):
            rect.set_height(val)

        for i in range(N):
            if i >= end_sorted:
                rects[i].set_color('green')
                ordered_indices.add(i)
            elif i not in ordered_indices:
                rects[i].set_color('blue')

        if index1 != -1 and index2 != -1:
            rects[index1].set_color('purple')
            rects[index2].set_color('purple')

        iteration[0] += 1
        text.set_text("Número de operações: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=heap_sort(lista), interval=200,
                                   repeat=False)
    plt.show()

def get_sorted_data(N):
    while True:
        print("Escolha o caso para a ordenação Heap Sort:\n")
        print("1 - Lista Ordenada")
        print("2 - Lista Ordenada Inversamente")
        print("3 - Lista Aleatoria")
        print("4 - Sair")
        case = input("\nEscolha -> ").strip().lower()
        
        if case == '1' or case == "lista ordenada":
            return list(range(1, N+1))
        elif case == '2' or case == "lista ordenada inversamente":
            return list(range(N, 0, -1))
        elif case == '3' or case == "lista aleatoria":
            lista = list(range(1, N+1))
            random.shuffle(lista)
            return lista
        elif case == '4' or case == "sair":
            print("Saindo do programa.")
            return None
        else:
            print("Escolha inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    N = 20
    while True:
        os.system('cls')
        lista = get_sorted_data(N)
        if lista is not None:
            visualize_heap_sort(lista)
        else:
            print("O programa foi encerrado pelo usuário.")
            break