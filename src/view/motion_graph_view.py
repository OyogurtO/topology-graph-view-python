import matplotlib
import matplotlib.pyplot as plt
import math

matplotlib.use('TkAgg')


def get_x(node):
    return node['departureTime']


def get_y(node):
    return node['robotId'] - 10000


def parse_pose(pose):
    return '('+str(pose['x'])+', '+str(pose['y'])+', '+str(math.degrees(pose['theta']))+')'


def view(nodes, edges, name):
    fig, ax = plt.subplots()

    ax.set_title(name)

    xs = []
    ys = []
    for node in nodes:
        x = get_x(node)
        y = get_y(node)
        plt.text(x-0.25, y + 0.05, round(x, 2), ha='left', va='bottom', fontsize=8)
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
        # blue arrow represents action
        color = 'blue'
        if y1 != y2:
            # green arrow represents dependency
            color = 'green'
        ax.arrow(x1, y1, x2 - x1, y2 - y1, length_includes_head=True, head_width=0.1, head_length=0.2, color=color)
        # If wait cost present, use blue arrow represents action cost, and use red arrow represents wait cost
        if y1 == y2 and round(x2 - x1, 2) > round(edge['cost'], 2):
            ax.arrow(x1, y1, edge['cost'], 0, length_includes_head=True, head_width=0.2,
                     head_length=0.2, color='blue')
            ax.arrow(x1 + edge['cost'], y1, x2 - x1 - edge['cost'], 0, length_includes_head=True, head_width=0.2,
                     head_length=0.2, color='red')

    anno = ax.annotate(text="", xy=(0, 0), xytext=(10, -20), textcoords="offset points",
                       bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    anno.set_visible(False)

    # If the graph only contains one path, the arrows may be too large. So force the image height >= 10.
    ylim = ax.get_ylim()
    if ylim[1]-ylim[0] < 10:
        mid = (ylim[0]+ylim[1])/2
        ax.set_ylim([mid-5, mid+5])

    def update_anno(ind):
        i = ind["ind"][0]
        anno.xy = sc.get_offsets()[i]
        anno.set_text(parse_pose(nodes[i]['pose']))
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
