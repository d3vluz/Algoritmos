import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def insertion_sort(lista):
    tamanho = len(lista)
    for indice in range(1, tamanho):
        chave = lista[indice]
        posicao = indice - 1
        
        while posicao >= 0 and lista[posicao] > chave:
            lista[posicao + 1] = lista[posicao]
            yield lista.copy(), posicao, posicao + 1, indice
            posicao -= 1
            
        lista[posicao + 1] = chave
        yield lista.copy(), None, None, indice
    
    yield lista.copy(), None, None, tamanho

def visualizar_insertion_sort(lista):
    tamanho = len(lista)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Visualização do Insertion Sort", fontsize=14)
    barras = ax.bar(range(tamanho), lista, align="edge", color='skyblue', edgecolor='steelblue')

    ax.set_xlim(0, tamanho)
    ax.set_ylim(0, int(1.1 * max(lista)))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    contador = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12)
    operacoes = [0]

    def atualizar_grafico(dados, barras, operacoes):
        lista_atual, indice1, indice2, indice_ordenado = dados
        
        for i, (barra, valor) in enumerate(zip(barras, lista_atual)):
            barra.set_height(valor)
            if i < indice_ordenado:
                barra.set_color('limegreen')
            else:
                barra.set_color('skyblue')
                
        if indice_ordenado == tamanho:
            for barra in barras:
                barra.set_color('limegreen')
                
        if indice1 is not None and indice2 is not None:
            barras[indice1].set_color('red')
            barras[indice2].set_color('red')
            
        operacoes[0] += 1
        contador.set_text(f"Operações: {operacoes[0]}")

    animacao = animation.FuncAnimation(
        fig, 
        func=atualizar_grafico,
        fargs=(barras, operacoes), 
        frames=insertion_sort(lista),
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
        print("\n===== INSERTION SORT =====")
        print("Escolha o caso para a ordenação Insertion Sort:\n")
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
            visualizar_insertion_sort(lista)
        else:
            break