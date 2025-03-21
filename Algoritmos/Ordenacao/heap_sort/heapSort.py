import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heap_sort(lista):
    tamanho_lista = len(lista)
    
    # Fase 1: Construção do heap máximo
    # Começamos a partir do último nó não-folha e aplicamos heapify de baixo para cima
    for indice in range(tamanho_lista // 2 - 1, -1, -1):
        yield from heapify(lista, tamanho_lista, indice)
    
    # Fase 2: Extrair elementos um por um do heap
    for indice in range(tamanho_lista - 1, 0, -1):
        # Troca a raiz (maior elemento) com o último elemento não ordenado
        lista[0], lista[indice] = lista[indice], lista[0]
        
        # Mostra a troca realizada
        yield lista, 0, indice, indice
        
        # Restaura a propriedade do heap máximo para a raiz
        yield from heapify(lista, indice, 0)
    
    # Lista completamente ordenada
    yield lista, -1, -1, 0

def heapify(lista, tamanho_heap, indice_raiz):
    maior = indice_raiz  # Inicializa o maior como raiz
    indice_filho_esquerdo = 2 * indice_raiz + 1
    indice_filho_direito = 2 * indice_raiz + 2
    
    # Verifica se o filho esquerdo existe e é maior que a raiz
    if indice_filho_esquerdo < tamanho_heap and lista[indice_filho_esquerdo] > lista[maior]:
        maior = indice_filho_esquerdo
    
    # Verifica se o filho direito existe e é maior que o maior atual
    if indice_filho_direito < tamanho_heap and lista[indice_filho_direito] > lista[maior]:
        maior = indice_filho_direito
    
    # Se o maior não é a raiz, troca e continua a heapificar
    if maior != indice_raiz:
        lista[indice_raiz], lista[maior] = lista[maior], lista[indice_raiz]
        
        # Mostra a troca realizada
        yield lista, indice_raiz, maior, tamanho_heap
        
        # Recursivamente heapifica a subárvore afetada
        yield from heapify(lista, tamanho_heap, maior)

def visualizar_heap_sort(lista):
    tamanho_lista = len(lista)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("Heap Sort")
    
    barras = ax.bar(range(tamanho_lista), lista, align="edge", color='royalblue', alpha=0.7)
    
    ax.set_xlim(0, tamanho_lista)
    ax.set_ylim(0, int(1.1 * max(lista)))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    contador_texto = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)

    contador_operacoes = [0]
    indices_ordenados = set()
    
    def atualizar_grafico(dados, barras, contador_operacoes):
        lista_atual, indice1, indice2, fim_ordenado = dados

        for i, (barra, valor) in enumerate(zip(barras, lista_atual)):
            barra.set_height(valor)

        for i in range(tamanho_lista):
            if i >= fim_ordenado:
                barras[i].set_color('limegreen')
                indices_ordenados.add(i)
            elif i not in indices_ordenados:
                barras[i].set_color('royalblue')

        if indice1 != -1 and indice2 != -1:
            barras[indice1].set_color('crimson')
            barras[indice2].set_color('darkorange')
        
        contador_operacoes[0] += 1
        contador_texto.set_text(f"Número de operações: {contador_operacoes[0]}")

    anim = animation.FuncAnimation(
        fig, 
        func=atualizar_grafico, 
        fargs=(barras, contador_operacoes), 
        frames=heap_sort(lista), 
        interval=200, 
        repeat=False
    )
    
    plt.tight_layout()
    plt.show()

def obter_dados_ordenacao(tamanho):
    while True:
        print("\n===== HEAP SORT =====")
        print("Escolha o caso para a ordenação Heap Sort:\n")
        print("1 - Lista Ordenada")
        print("2 - Lista Ordenada Inversamente")
        print("3 - Lista Aleatória")
        print("4 - Sair")
        opcao = input("\nEscolha -> ").strip().lower()
        
        if opcao in ['1', 'lista ordenada', 'melhor caso']:
            return list(range(1, tamanho + 1))
        elif opcao in ['2', 'lista ordenada inversamente', 'pior caso']:
            return list(range(tamanho, 0, -1))
        elif opcao in ['3', 'lista aleatória', 'caso médio']:
            lista = list(range(1, tamanho + 1))
            random.shuffle(lista)
            return lista
        elif opcao in ['4', 'sair']:
            print("Saindo do programa.")
            return None
        else:
            print("Escolha inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    tamanho_padrao = 40
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        lista = obter_dados_ordenacao(tamanho_padrao)
        
        if lista is not None:
            visualizar_heap_sort(lista)
        else:
            print("O programa foi encerrado pelo usuário.")
            break