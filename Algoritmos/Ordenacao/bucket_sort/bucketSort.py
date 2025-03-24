import os
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bucket_sort(lista):
    max_value = max(lista)
    size = max_value / len(lista)
    buckets = [[] for _ in range(len(lista))]
    
    for i in range(len(lista)):
        index = int(lista[i] / size)
        if index != len(lista):
            buckets[index].append(lista[i])
        else:
            buckets[len(lista) - 1].append(lista[i])
        yield lista, i, [bucket[:] for bucket in buckets]

    sorted_list = []
    for bucket in buckets:
        bucket.sort()
        sorted_list.extend(bucket)
        yield sorted_list, None, [bucket[:] for bucket in buckets]

def visualize_bucket_sort(lista):
    N = len(lista)
    fig, (ax_lista, ax_buckets) = plt.subplots(2, 1, figsize=(10, 8))

    ax_lista.set_title("Bucket Sort - Lista")
    bar_rects = ax_lista.bar(range(N), lista, align="edge", color='blue')

    ax_lista.set_xlim(0, N)
    ax_lista.set_ylim(0, int(1.1 * max(lista)))
    ax_lista.get_xaxis().set_visible(False)
    ax_lista.get_yaxis().set_visible(False)

    text = ax_lista.text(0.02, 0.95, "", transform=ax_lista.transAxes)

    ax_buckets.set_title("Bucket Sort - Baldes")
    ax_buckets.set_xlim(0, N)
    ax_buckets.set_ylim(0, int(1.1 * max(lista)))
    ax_buckets.get_xaxis().set_visible(False)
    ax_buckets.get_yaxis().set_visible(False)

    bucket_bars = []
    for i in range(N):
        bucket_bars.append(ax_buckets.bar([i], [0], width=0.8, color='gray'))

    iteration = [0]

    def update_fig(data, rects, iteration):
        lista, highlight, buckets = data
        
        for rect, val in zip(rects, lista):
            rect.set_height(val)
            rect.set_color('blue')
        if highlight is not None:
            rects[highlight].set_color('purple')
        
        iteration[0] += 1
        text.set_text("Número de operações: {}".format(iteration[0]))

        for i, bucket in enumerate(buckets):
            heights = bucket if bucket else [0]
            for rect in bucket_bars[i]:
                rect.set_height(0)
            for j, height in enumerate(heights):
                if j < len(bucket_bars[i]):
                    bucket_bars[i][j].set_height(height)
                    bucket_bars[i][j].set_color('green')
                else:
                    ax_buckets.bar([i], [height], width=0.8, color='yellow')

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=bucket_sort(lista), interval=500,
                                   repeat=False)
    plt.tight_layout()
    plt.show()

def get_sorted_data(N):
    while True:
        print("Escolha o caso para a ordenação Bucket Sort:\n")
        print("1 - Melhor caso")
        print("2 - Pior caso")
        print("3 - Caso médio")
        print("4 - Sair")
        case = input("\nEscolha -> ").strip().lower()
        
        if case == '1' or case == "melhor caso":
            return list(range(N))
        elif case == '2' or case == "pior caso":
            return list(range(N, 0, -1))
        elif case == '3' or case == "caso médio":
            lista = list(range(N))
            random.shuffle(lista)
            return lista
        elif case == '4' or case == "sair":
            print("Saindo do programa.")
            return None
        else:
            print("Escolha inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    N = 20
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        lista = get_sorted_data(N)
        if lista is not None:
            visualize_bucket_sort(lista)
        else:
            print("O programa foi encerrado pelo usuário.")
            break