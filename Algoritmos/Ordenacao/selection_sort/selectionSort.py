import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            yield lista, i, j, min_index, i
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
        yield lista, i, None, min_index, i + 1

    yield lista, None, None, None, n

def visualizar_selection_sort(lista):
    tamanho = len(lista)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Visualização do Selection Sort", fontsize=14)
    barras = ax.bar(range(tamanho), lista, align="edge", color='skyblue', edgecolor='steelblue')

    ax.set_xlim(0, tamanho)
    ax.set_ylim(0, int(1.1 * tamanho))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)
    operacoes = [0]

    def atualizar_grafico(data, barras, operacoes):
        lista, atual, comparando, min_index, ordenado_ate = data
        for i, (barra, valor) in enumerate(zip(barras, lista)):
            barra.set_height(valor)
            barra.set_color('skyblue')
            
        # Destacar elementos já ordenados
        for i in range(ordenado_ate if ordenado_ate is not None else 0):
            barras[i].set_color('limegreen')
            
        # Destacar elemento atual sendo analisado
        if atual is not None:
            barras[atual].set_color('#447F9C')
            
        # Destacar elemento sendo comparado
        if comparando is not None:
            barras[comparando].set_color('#0D4866')
            
        # Destacar o índice do menor elemento encontrado até o momento
        if min_index is not None and min_index != atual:
            barras[min_index].set_color('orange')
        
        operacoes[0] += 1
        contador.set_text(f"Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(
        fig, 
        func=atualizar_grafico,
        fargs=(barras, operacoes), 
        frames=selection_sort(lista),
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
        print("\nEscolha o caso para a ordenação Selection Sort:")
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
            visualizar_selection_sort(lista)
        else:
            break