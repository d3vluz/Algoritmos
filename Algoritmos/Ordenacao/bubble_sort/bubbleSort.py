import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort(lista):
    n = len(lista)
    sorted_idx = n
    for i in range(n):
        trocou = False
        for j in range(n - i - 1):
            yield lista, j, j + 1, sorted_idx
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
            yield lista, None, None, sorted_idx
        sorted_idx -= 1
        if not trocou:
            sorted_idx = 0
            yield lista, None, None, sorted_idx
            break

def visualizar_bubble_sort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort")
    barras = ax.bar(range(N), lista, align="edge", color='blue')

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * N))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    operacoes = [0]

    def atualizar_grafico(data, barras, operacoes):
        lista, x, y, sorted_idx = data
        for i, (barra, valor) in enumerate(zip(barras, lista)):
            barra.set_height(valor)
            if i >= sorted_idx:
                barra.set_color('green')
            else:
                barra.set_color('blue')
        if x is not None and y is not None:
            barras[x].set_color('purple')
            barras[y].set_color('purple')
        operacoes[0] += 1
        contador.set_text(f"Número de Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(fig, func=atualizar_grafico,
                                       fargs=(barras, operacoes), frames=bubble_sort(lista),
                                       interval=200, repeat=False)
    plt.show()

def interface(N):
    while True:
        print("\nEscolha o caso para a ordenação Bubble Sort:")
        print("1 - Lista Ordenada")
        print("2 - Lista Ordenada Inversamente")
        print("3 - Lista Aleatoria")
        print("4 - Sair")
        
        opcao = input("\nEscolha -> ").strip().lower()
        
        if opcao in ['1', 'lista ordenada']:
            return list(range(1, N+1))
        elif opcao in ['2', 'lista ordenada inversamente']:
            return list(range(N, 0, -1))
        elif opcao in ['3', 'lista aleatoria']:
            lista = list(range(1, N+1))
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
            visualizar_bubble_sort(lista)
        else:
            break