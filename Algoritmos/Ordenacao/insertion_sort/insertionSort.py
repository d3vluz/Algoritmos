import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            yield lista, j, j + 1, i
            j -= 1
        lista[j + 1] = chave
        yield lista, None, None, i
    yield lista, None, None, n 

def visualizar_insertion_sort(lista):
    N = len(lista)
    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort")
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
            if i < sorted_idx:
                barra.set_color('green')
            else:
                barra.set_color('blue')
        if sorted_idx == N:
            for barra in barras:
                barra.set_color('green')
        if x is not None and y is not None:
            barras[x].set_color('purple')
            barras[y].set_color('purple')
        operacoes[0] += 1
        contador.set_text(f"Número de Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(fig, func=atualizar_grafico,
                                       fargs=(barras, operacoes), frames=insertion_sort(lista),
                                       interval=200, repeat=False)
    plt.show()

def interface(N):
    while True:
        print("\nEscolha o caso para a ordenação Insertion Sort:")
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
            visualizar_insertion_sort(lista)
        else:
            break