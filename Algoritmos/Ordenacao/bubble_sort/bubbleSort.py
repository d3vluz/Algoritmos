import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort(lista):
    n = len(lista)
    limite_ordenado = n
    for i in range(n):
        trocou = False
        for j in range(limite_ordenado - 1):
            yield lista, j, j + 1, limite_ordenado
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
            yield lista, None, None, limite_ordenado
        limite_ordenado -= 1
        if not trocou:
            limite_ordenado = 0
            yield lista, None, None, limite_ordenado
            break

def visualizar_bubble_sort(lista):
    tamanho = len(lista)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Visualização do Bubble Sort", fontsize=14)
    barras = ax.bar(range(tamanho), lista, align="edge", color='skyblue', edgecolor='steelblue')

    ax.set_xlim(0, tamanho)
    ax.set_ylim(0, int(1.1 * tamanho))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)
    operacoes = [0]

    def atualizar_grafico(data, barras, operacoes):
        lista, indice1, indice2, limite_ordenado = data
        for i, (barra, valor) in enumerate(zip(barras, lista)):
            barra.set_height(valor)
            if i >= limite_ordenado:
                barra.set_color('limegreen')
            else:
                barra.set_color('skyblue')
        if indice1 is not None and indice2 is not None:
            barras[indice1].set_color('red')
            barras[indice2].set_color('red')
        operacoes[0] += 1
        contador.set_text(f"Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(
        fig, 
        func=atualizar_grafico,
        fargs=(barras, operacoes), 
        frames=bubble_sort(lista),
        interval=100, 
        repeat=False
    )
    plt.show()

def interface(tamanho_lista):
    opcoes = {
        '1': ('Lista Ordenada', lambda: list(range(1, tamanho_lista+1))),
        '2': ('Lista Ordenada Inversamente', lambda: list(range(tamanho_lista, 0, -1))),
        '3': ('Lista Aleatória', lambda: random.sample(range(1, tamanho_lista+1), tamanho_lista)),
        '4': ('Sair', lambda: None)
    }
    
    while True:
        print("\nEscolha o caso para a ordenação Bubble Sort:")
        for key, (desc, _) in opcoes.items():
            print(f"{key} - {desc}")
        
        opcao = input("\nEscolha -> ").strip()
        
        if opcao in opcoes:
            return opcoes[opcao][1]()
        else:
            print("Opção inválida. Tente novamente.")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    tamanho_lista = 20
    while True:
        limpar_tela()
        lista = interface(tamanho_lista)
        if lista is not None:
            visualizar_bubble_sort(lista)
        else:
            break