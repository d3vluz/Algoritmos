import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def selection_sort(lista):
    n = len(lista)
    already_sorted = True
    iteration_count = 0

    is_worst_case = True
    for i in range(n - 1):
        if lista[i] < lista[i + 1]:
            is_worst_case = False
            break

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
                already_sorted = False
            yield lista, i, j, min_index, i
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
            yield lista, i, min_index, min_index, i + 1

        iteration_count += 1

        if already_sorted:
            break

        if is_worst_case and iteration_count >= n // 2:
            break

    yield lista, -1, -1, -1, n

def visualize_selection_sort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Selection Sort")
    bar_rects = ax.bar(range(N), lista, align="edge", color='blue')
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * max(lista)))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_fig(data, rects, iteration):
        lista, index1, index2, min_index, sorted_upto = data
        for rect, val in zip(rects, lista):
            rect.set_height(val)

        for i in range(N):
            rects[i].set_color('blue')

        for i in range(sorted_upto):
            rects[i].set_color('green')

        if min_index != -1 and min_index < N:
            rects[min_index].set_color('orange')

        if index1 != -1 and index2 != -1:
            rects[index1].set_color('purple')
            rects[index2].set_color('purple')

        iteration[0] += 1
        text.set_text("Número de operações: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=selection_sort(lista), interval=80,
                                   repeat=False)
    plt.show()

def get_sorted_data(N):
    while True:
        print("Escolha o caso para a ordenação Selection Sort:\n")
        print("1 - Lista Ordenada")
        print("2 - Lista Ordenada Inversamente")
        print("3 - Lista Aleatória")
        print("4 - Sair")
        case = input("\nEscolha -> ").strip().lower()
        
        if case == '1' or case == "lista ordenada":
            return list(range(1, N+1))
        elif case == '2' or case == "lista ordenada inversamente":
            return list(range(N, 0, -1))
        elif case == '3' or case == "lista aleatória":
            lista = list(range(1, N+1))
            random.shuffle(lista)
            return lista
        elif case == '4' or case == "sair":
            print("Saindo do programa.")
            return None
        else:
            print("Escolha inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    N = 40
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        lista = get_sorted_data(N)
        if lista is not None:
            visualize_selection_sort(lista)
        else:
            print("O programa foi encerrado pelo usuário.")
            break