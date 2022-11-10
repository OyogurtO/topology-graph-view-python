import matplotlib
import matplotlib.pyplot as plt
import math
import random

matplotlib.use('TkAgg')


angle_bias = math.pi/180*5
location_bias = 0.3


def get_x(node):
    pose = node['pose']
    x = pose['x']
    a = pose['theta']
    return x + math.cos(a + angle_bias) * location_bias


def get_y(node):
    pose = node['pose']
    y = pose['y']
    a = pose['theta']
    return y + math.sin(a + angle_bias) * location_bias


def get_name(node):
    return node['name']


def get_detail(node):
    return '(' + str(node['pose']['x']) + ',' + str(node['pose']['y']) + ')'


def random_color():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])


def view(edges, name):
    fig, ax = plt.subplots()
    ax.set_title(name)

    node_map = {}
    for edge in edges:
        src = edge['src']
        node_map[src['id']] = src
        tgt = edge['tgt']
        node_map[tgt['id']] = tgt

    nodes = list(node_map.values())

    xs = []
    ys = []
    for node in nodes:
        x = get_x(node)
        y = get_y(node)
        # plt.text(x - 0.25, y + 0.05, get_name(node), ha='left', va='bottom', fontsize=8)
        xs.append(x)
        ys.append(y)
    sc = plt.scatter(xs, ys)

    for edge in edges:
        src = edge['src']
        tgt = edge['tgt']
        x1 = get_x(src)
        y1 = get_y(src)
        x2 = get_x(tgt)
        y2 = get_y(tgt)
        plt.text(x2, y2 + 0.05, str(round(edge['cost'], 2)), ha='left', va='bottom', fontsize=8)
        ax.arrow(x1, y1, x2 - x1, y2 - y1, length_includes_head=True, head_width=0.05, head_length=0.1, color=random_color())

    anno = ax.annotate(text="", xy=(0, 0), xytext=(10, -20), textcoords="offset points",
                       bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    anno.set_visible(False)

    # If the graph only contains one path, the arrows may be too large. So force the image height >= 10.
    ylim = ax.get_ylim()
    if ylim[1] - ylim[0] < 10:
        mid = (ylim[0] + ylim[1]) / 2
        ax.set_ylim([mid - 5, mid + 5])

    def update_anno(ind):
        i = ind["ind"][0]
        anno.xy = sc.get_offsets()[i]
        anno.set_text(get_detail(nodes[i]))
        anno.set_x(-30)
        # ay = -12 * (len(nodes[i])+2)
        # anno.set_y(ay)
        anno.get_bbox_patch().set_alpha(0.8)

    #  handle mouse move event. check if cursor is on a node
    def on_move(event):
        vis = anno.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_anno(ind)
                anno.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    anno.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_move)

    plt.show()
