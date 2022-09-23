import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


def change_figure(i):
    plt.figure(i)


def view(nodes, edges, name):
    fig, ax = plt.subplots()

    ax.set_title(name)

    node_dict = {}
    xs = []
    ys = []

    #  node view
    for node in nodes:
        node_dict[node['nodeLabel']] = node
        x = node['xCoordinate']
        y = node['yCoordinate']
        plt.text(x+0.1, y+0.05, node['nodeLabel'], ha='left', va='bottom', fontsize=8)
        xs.append(x)
        ys.append(y)
    sc = plt.scatter(xs, ys)

    #  edge view
    for edge in edges:
        x1 = node_dict[edge['beginNodeLabel']]['xCoordinate']
        y1 = node_dict[edge['beginNodeLabel']]['yCoordinate']
        x2 = node_dict[edge['endNodeLabel']]['xCoordinate']
        y2 = node_dict[edge['endNodeLabel']]['yCoordinate']
        dx = x2 - x1
        dy = y2 - y1
        ax.arrow(x1, y1, dx, dy, length_includes_head=True, head_width=0.1, head_length=0.2, fc='black')

    #  tag view of node. (need to update when node has changed)
    anno = ax.annotate(text="", xy=(0, 0), xytext=(10, -20), textcoords="offset points",
                       bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    anno.set_visible(False)

    #  update anno data when cursor is on a node
    def update_anno(ind):
        i = ind["ind"][0]
        anno.xy = sc.get_offsets()[i]
        txt = "({}, {})\n".format(nodes[i]["xCoordinate"], nodes[i]["yCoordinate"])
        for (k,v) in nodes[i].items():
            txt += "{}:{}\n".format(k, v)
        anno.set_text(txt)
        ay = -12 * (len(nodes[i])+2)
        anno.set_y(ay)
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


def show():
    plt.show()


def format_node(node):
    result = ""
    for k in node.keys():
        result += ""+k+": "+str(node[k])+"\n"
    return result

