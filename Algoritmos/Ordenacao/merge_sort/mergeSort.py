import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def merge_sort(lista_valores, inicio, fim):
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        yield from merge_sort(lista_valores, inicio, meio)
        yield from merge_sort(lista_valores, meio, fim)
        yield from merge(lista_valores, inicio, meio, fim)

def merge(lista_valores, inicio, meio, fim):
    # Cria cópias das duas metades a serem mescladas
    sublista_esquerda = lista_valores[inicio:meio]
    sublista_direita = lista_valores[meio:fim]
    # Índices para percorrer as sublistas
    indice_esquerda = 0
    indice_direita = 0
    
    # Percorre a região da lista original que será substituída
    for posicao_atual in range(inicio, fim):
        # Verifica se devemos pegar o próximo elemento da sublista esquerda:
        # 1. Se ainda houver elementos na sublista esquerda E
        # 2. Se a sublista direita já acabou OU se o elemento atual da esquerda é menor ou igual ao da direita
        if indice_esquerda < len(sublista_esquerda) and (indice_direita >= len(sublista_direita) or sublista_esquerda[indice_esquerda] <= sublista_direita[indice_direita]):
            # Coloca o elemento da sublista esquerda na posição atual
            lista_valores[posicao_atual] = sublista_esquerda[indice_esquerda]
            # Avança para o próximo elemento da sublista esquerda
            indice_esquerda += 1
        else:
            # Caso contrário, coloca o elemento da sublista direita na posição atual
            lista_valores[posicao_atual] = sublista_direita[indice_direita]
            # Avança para o próximo elemento da sublista direita
            indice_direita += 1
        # Retorna o estado atual da lista para visualização
        yield lista_valores, inicio, fim

def visualizar_merge_sort(lista_valores):
    tamanho_lista = len(lista_valores)
    figura, grafico = plt.subplots(figsize=(10, 6))
    grafico.set_title("Visualização do Merge Sort", fontsize=14)
    barras = grafico.bar(range(tamanho_lista), lista_valores, align="edge", color='skyblue', edgecolor='steelblue')
    
    grafico.set_xlim(0, tamanho_lista)
    grafico.set_ylim(0, int(1.1 * tamanho_lista))
    grafico.get_xaxis().set_visible(False)
    grafico.get_yaxis().set_visible(False)
    
    texto_contador = grafico.text(0.02, 0.95, "", transform=grafico.transAxes, fontsize=12)
    contador_operacoes = [0]

    def atualizar_grafico(dados, barras, contador_operacoes):
        lista_atual, inicio_segmento, fim_segmento = dados
        
        for barra, valor in zip(barras, lista_atual):
            barra.set_height(valor)
            barra.set_color('skyblue')
            
        for indice in range(inicio_segmento, fim_segmento):
            barras[indice].set_color('purple')
            
        contador_operacoes[0] += 1
        texto_contador.set_text(f"Operações: {contador_operacoes[0]}")

        if lista_atual == sorted(lista_atual):
            for barra in barras:
                barra.set_color('limegreen')

    animacao = animation.FuncAnimation(
        figura, 
        func=atualizar_grafico,
        fargs=(barras, contador_operacoes), 
        frames=merge_sort(lista_valores, 0, len(lista_valores)), 
        interval=100,
        repeat=False
    )
    
    plt.tight_layout()
    plt.show()

def obter_lista_para_ordenacao(tamanho_lista):
    opcoes = {
        '1': ('Lista Ordenada', lambda: list(range(1, tamanho_lista+1))),
        '2': ('Lista Ordenada Inversamente', lambda: list(range(tamanho_lista, 0, -1))),
        '3': ('Lista Aleatória', lambda: random.sample(range(1, tamanho_lista+1), tamanho_lista)),
        '4': ('Sair', lambda: None)
    }
    
    while True:
        print("\n===== MERGE SORT =====")
        print("Escolha o tipo de lista para a ordenação por mesclagem:\n")
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
    tamanho_lista = 50
    while True:
        limpar_tela()
        lista_valores = obter_lista_para_ordenacao(tamanho_lista)
        if lista_valores is not None:
            visualizar_merge_sort(lista_valores)
        else:
            print("O programa foi encerrado pelo usuário.")
            break