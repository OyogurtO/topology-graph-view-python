import matplotlib
import matplotlib.pyplot as plt
import math
import random

matplotlib.use('TkAgg')


def get_x(node):
    return node['pose']['x'] + (node['robotId'] - 10000) * 0.1


def get_y(node):
    return node['pose']['y'] + (node['robotId'] - 10000) * 0.1


def get_detail(node):
    pose = node['pose']
    return str(node['robotId']) + '(' + str(pose['x']) + ', ' + str(pose['y']) + ', ' + str(math.degrees(pose['theta'])) + ')'


def random_color():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])


def view(nodes, edges, name):
    fig, ax = plt.subplots()

    ax.set_title(name)

    rc = {}
    xs = []
    ys = []
    cs = []
    ft = []
    for node in nodes:
        r = node['robotId']
        x = get_x(node)
        y = get_y(node)
        if len(ft) != 0 and y not in ft:
            continue
        # plt.text(x - 0.25, y + 0.05, '({},{})'.format(round(x, 2), round(y, 2)), ha='left', va='bottom', fontsize=8)
        xs.append(x)
        ys.append(y)
        rc[r] = rc.setdefault(r, random_color())
        cs.append(rc[r])
    sc = plt.scatter(xs, ys, c=cs)

    for edge in edges:
        src = edge['source']
        tgt = edge['target']
        # if 'info' not in edge:
        #     continue
        r1 = src['robotId']
        x1 = get_x(src)
        y1 = get_y(src)
        r2 = tgt['robotId']
        x2 = get_x(tgt)
        y2 = get_y(tgt)
        if len(ft) != 0 and ((r1 not in ft) or (r2 not in ft)):
            continue
        # # action color
        # color = 'blue'
        # if r1 != r2:
        #     # dependency color
        #     color = 'green'
        color = rc[r2]
        ax.arrow(x1, y1, x2 - x1, y2 - y1, length_includes_head=True, head_width=0.1, head_length=0.2, color=color)

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
