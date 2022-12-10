import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots() # Hay 02 vairables. La primera es la figura fig, luego ax se rfiere a las coordenadas
    ax.bar(labels, values)
    plt.savefig(f"./imgs/{name}.png")
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots() # Hay 02 vairables. La primera es la figura fig, luego ax se rfiere a las coordenadas
    ax.pie(values, labels=labels)
    ax.axis("equal") # Con esto se centra la gráfica
    plt.savefig("pie.png")
    plt.close
    
if __name__ == "__main__":
    labels =["a","b","c"]
    values = [10,40,800]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
    



