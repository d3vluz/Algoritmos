import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def merge_sort(lista, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(lista, start, mid)
        yield from merge_sort(lista, mid, end)
        yield from merge(lista, start, mid, end)

def merge(lista, start, mid, end):
    left = lista[start:mid]
    right = lista[mid:end]
    i = j = 0
    for k in range(start, end):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1
        yield lista, start, end

def visualize_merge_sort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Merge Sort")
    bar_rects = ax.bar(range(N), lista, align="edge", color='blue')
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * N))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_fig(data, rects, iteration):
        lista, start, end = data
        for rect, val in zip(rects, lista):
            rect.set_height(val)
            rect.set_color('blue')
        for i in range(start, end):
            rects[i].set_color('purple')
        iteration[0] += 1
        text.set_text("Número de operações: {}".format(iteration[0]))

        if lista == sorted(lista):
            for rect in rects:
                rect.set_color('green')

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=merge_sort(lista, 0, len(lista)), interval=50,
                                   repeat=False)
    plt.show()

def get_sorted_data(N):
    while True:
        print("Escolha o caso para a ordenação Merge Sort:\n")
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
    N = 100
    while True:
        os.system('cls')
        lista = get_sorted_data(N)
        if lista is not None:
            visualize_merge_sort(lista)
        else:
            print("O programa foi encerrado pelo usuário.")
            break