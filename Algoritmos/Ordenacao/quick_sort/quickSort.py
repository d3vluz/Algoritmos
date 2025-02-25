import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo_idx = yield from partition(lista, inicio, fim)
        yield lista, pivo_idx, inicio, fim, False
        yield from quicksort(lista, inicio, pivo_idx - 1)
        yield from quicksort(lista, pivo_idx + 1, fim)
    else:
        yield lista, None, None, None, True

def partition(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
        yield lista, i, j, fim, False
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    yield lista, i + 1, None, None, False
    return i + 1

def visualizar_quicksort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Quick Sort")
    barras = ax.bar(range(N), lista, align="edge", color='blue')

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * N))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    operacoes = [0]

    def atualizar_grafico(data, barras, operacoes):
        lista, pivo_idx, x, y, sorted_flag = data
        for i, (barra, valor) in enumerate(zip(barras, lista)):
            barra.set_height(valor)
            if sorted_flag:
                barra.set_color('green')
            elif i == pivo_idx:
                barra.set_color('orange')
            elif i < pivo_idx:
                barra.set_color('green')
            else:
                barra.set_color('blue')
        if x is not None and y is not None:
            barras[x].set_color('purple')
            barras[y].set_color('purple')
        operacoes[0] += 1
        contador.set_text(f"Número de Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(fig, func=atualizar_grafico,
                                       fargs=(barras, operacoes), frames=quicksort(lista, 0, len(lista) - 1),
                                       interval=200, repeat=False, save_count=len(lista)*len(lista))
    plt.show()

def interface(N):
    while True:
        print("\nEscolha o caso para a ordenação Quick Sort:")
        print("1 - Lista Ordenada")
        print("2 - Lista Ordenada Inversamente")
        print("3 - Lista Aleatória")
        print("4 - Sair")

        opcao = input("\nEscolha -> ").strip().lower()

        if opcao in ['1', 'lista ordenada']:
            return list(range(1, N + 1))
        elif opcao in ['2', 'lista ordenada inversamente']:
            return list(range(N, 0, -1))
        elif opcao in ['3', 'lista aleatória']:
            lista = list(range(1, N + 1))
            random.shuffle(lista)
            return lista
        elif opcao in ['4', 'sair']:
            print("Saindo do programa.")
            return None
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    N = 20
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        lista = interface(N)
        if lista is not None:
            visualizar_quicksort(lista)
        else:
            break