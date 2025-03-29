import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        pivo_idx = yield from partition(lista, inicio, fim)
        yield lista, pivo_idx, None, None, fim
        yield from quick_sort(lista, inicio, pivo_idx - 1)
        yield from quick_sort(lista, pivo_idx + 1, fim)
    else:
        yield lista, None, None, None, fim

def partition(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
        yield lista, i, j, fim, fim
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    yield lista, i + 1, None, None, fim
    return i + 1

def visualizar_quicksort(lista):
    tamanho = len(lista)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Visualização do Quick Sort", fontsize=14)
    barras = ax.bar(range(tamanho), lista, align="edge", color='skyblue', edgecolor='steelblue')

    ax.set_xlim(0, tamanho)
    ax.set_ylim(0, int(1.1 * tamanho))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)
    operacoes = [0]

    def atualizar_grafico(data, barras, operacoes):
        lista, pivo_idx, indice1, indice2, fim_atual = data
        for i, (barra, valor) in enumerate(zip(barras, lista)):
            barra.set_height(valor)
            barra.set_color('skyblue')
        
        # Destacar elementos sendo comparados
        if indice1 is not None:
            barras[indice1].set_color('#0D4866')
        if indice2 is not None:
            barras[indice2].set_color('#0D4866')
            
        # Destacar o pivô (que está no fim do subarray)
        if fim_atual is not None and fim_atual < len(lista):
            barras[fim_atual].set_color('#447F9C')
        
        operacoes[0] += 1
        contador.set_text(f"Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(
        fig, 
        func=atualizar_grafico,
        fargs=(barras, operacoes), 
        frames=quick_sort(lista, 0, len(lista) - 1),
        interval=100, 
        repeat=False
    )
    plt.show()

def interface(N):
    opcoes = {
        '1': ('Lista Ordenada', lambda: list(range(1, N+1))),
        '2': ('Lista Ordenada Inversamente', lambda: list(range(N, 0, -1))),
        '3': ('Lista Aleatória', lambda: random.sample(range(1, N+1), N)),
        '4': ('Sair', lambda: None)
    }
    
    while True:
        print("\nEscolha o caso para a ordenação Quick Sort:")
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
    N = 20
    while True:
        limpar_tela()
        lista = interface(N)
        if lista is not None:
            visualizar_quicksort(lista)
        else:
            break