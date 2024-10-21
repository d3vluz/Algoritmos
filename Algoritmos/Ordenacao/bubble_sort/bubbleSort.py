import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            yield lista, j, j+1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
            yield lista, None, None
        
        if not swapped:
            break

def visualize_bubble_sort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort")
    bar_rects = ax.bar(range(N), lista, align="edge", color='blue')

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * N))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_fig(data, rects, iteration):
        lista, x, y = data
        for rect, val in zip(rects, lista):
            rect.set_height(val)
            rect.set_color('blue')
        if x is not None and y is not None:
            rects[x].set_color('purple')
            rects[y].set_color('purple')
        iteration[0] += 1
        text.set_text("Número de operações: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=bubbleSort(lista), interval=50,
                                   repeat=False)
    plt.show()


def get_sorted_data(N):
    while True:
        print("Escolha o caso para a ordenação Bubble Sort:\n")
        print("1 - Melhor caso")
        print("2 - Pior caso")
        print("3 - Caso médio")
        print("4 - Sair")
        case = input("\nEscolha -> ").strip().lower()
        
        if case == '1' or case == "melhor caso":
            return list(range(N))
        elif case == '2' or case == "pior caso":
            return list(range(N, 0, -1))
        elif case == '3' or case == "caso médio":
            lista = list(range(N))
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
            visualize_bubble_sort(lista)
        else:
            print("O programa foi encerrado pelo usuário.")
            break