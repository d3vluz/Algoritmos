import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heap_sort(lista):
    tamanho = len(lista)
    
    # Fase 1: Construção do heap máximo
    for indice in range(tamanho // 2 - 1, -1, -1):
        yield from heapify(lista, tamanho, indice)
    
    # Fase 2: Extrair elementos um por um do heap
    for indice in range(tamanho - 1, 0, -1):
        # Troca a raiz (maior elemento) com o último elemento não ordenado
        lista[0], lista[indice] = lista[indice], lista[0]
        
        # Mostra a troca realizada
        yield lista, 0, indice, indice
        
        # Restaura a propriedade do heap máximo para a raiz
        yield from heapify(lista, indice, 0)
    
    # Lista completamente ordenada
    yield lista, -1, -1, 0

def heapify(lista, tamanho_heap, indice_raiz):
    maior = indice_raiz
    filho_esquerdo = 2 * indice_raiz + 1
    filho_direito = 2 * indice_raiz + 2
    
    # Verifica se o filho esquerdo existe e é maior que a raiz
    if filho_esquerdo < tamanho_heap and lista[filho_esquerdo] > lista[maior]:
        maior = filho_esquerdo
    
    # Verifica se o filho direito existe e é maior que o maior atual
    if filho_direito < tamanho_heap and lista[filho_direito] > lista[maior]:
        maior = filho_direito
    
    # Se o maior não é a raiz, troca e continua a heapificar
    if maior != indice_raiz:
        lista[indice_raiz], lista[maior] = lista[maior], lista[indice_raiz]
        
        # Mostra a troca realizada
        yield lista, indice_raiz, maior, tamanho_heap
        
        # Recursivamente heapifica a subárvore afetada
        yield from heapify(lista, tamanho_heap, maior)

def visualizar_heap_sort(lista):
    tamanho = len(lista)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("Visualização do Heap Sort", fontsize=14)
    
    barras = ax.bar(range(tamanho), lista, align="edge", color='skyblue', edgecolor='steelblue')
    
    ax.set_xlim(0, tamanho)
    ax.set_ylim(0, int(1.1 * max(lista)))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)
    operacoes = [0]
    indices_ordenados = set()
    
    def atualizar_grafico(dados, barras, operacoes):
        lista_atual, indice1, indice2, fim_ordenado = dados

        for i, (barra, valor) in enumerate(zip(barras, lista_atual)):
            barra.set_height(valor)

        for i in range(tamanho):
            if i >= fim_ordenado:
                barras[i].set_color('limegreen')
                indices_ordenados.add(i)
            elif i not in indices_ordenados:
                barras[i].set_color('skyblue')

        if indice1 != -1 and indice2 != -1:
            barras[indice1].set_color('red')
            barras[indice2].set_color('red')
        
        operacoes[0] += 1
        contador.set_text(f"Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(
        fig, 
        func=atualizar_grafico, 
        fargs=(barras, operacoes), 
        frames=heap_sort(lista), 
        interval=150, 
        repeat=False
    )
    
    plt.tight_layout()
    plt.show()

def interface(tamanho_lista):
    opcoes = {
        '1': ('Lista Ordenada', lambda: list(range(1, tamanho_lista+1))),
        '2': ('Lista Ordenada Inversamente', lambda: list(range(tamanho_lista, 0, -1))),
        '3': ('Lista Aleatória', lambda: random.sample(range(1, tamanho_lista+1), tamanho_lista)),
        '4': ('Sair', lambda: None)
    }
    
    while True:
        print("\n===== HEAP SORT =====")
        print("Escolha o caso para a ordenação Heap Sort:\n")
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
    tamanho_lista = 30
    while True:
        limpar_tela()
        lista = interface(tamanho_lista)
        if lista is not None:
            visualizar_heap_sort(lista)
        else:
            break