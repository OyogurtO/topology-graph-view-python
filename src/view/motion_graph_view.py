import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def get_x(node):
    return node['time']


def get_y(node):
    return node['robotId'] - 10000


def view(nodes, edges, name):
    fig, ax = plt.subplots()

    ax.set_title(name)

    xs = []
    ys = []
    for node in nodes:
        x = get_x(node)
        y = get_y(node)
        plt.text(x-0.25, y + 0.05, round(node['time'], 2), ha='left', va='bottom', fontsize=8)
        xs.append(x)
        ys.append(y)
    sc = plt.scatter(xs, ys)

    for edge in edges:
        src = edge['source']
        x1 = get_x(src)
        y1 = get_y(src)
        tgt = edge['target']
        x2 = get_x(tgt)
        y2 = get_y(tgt)
        color = 'blue'
        if y1 != y2:
            color = 'green'
        ax.arrow(x1, y1, x2 - x1, y2 - y1, length_includes_head=True, head_width=0.1, head_length=0.2, color=color)
        if y1 == y2 and round(x2 - x1, 2) > round(edge['cost'], 2):
            ax.arrow(x1, y1, edge['cost'], 0, length_includes_head=True, head_width=0.2,
                     head_length=0.2, color='blue')
            ax.arrow(x1 + edge['cost'], y1, x2 - x1 - edge['cost'], 0, length_includes_head=True, head_width=0.2,
                     head_length=0.2, color='red')

    anno = ax.annotate(text="", xy=(0, 0), xytext=(10, -20), textcoords="offset points",
                       bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    anno.set_visible(False)

    plt.show()
