import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


def view(nodes, edges, objects):
    fig, ax = plt.subplots()

    node_dict = {}
    for node in nodes:
        node_dict[node['nodeLabel']] = node
        plt.scatter(node['xCoordinate'], node['yCoordinate'])
    for edge in edges:
        x1 = node_dict[edge['beginNodeLabel']]['xCoordinate']
        y1 = node_dict[edge['beginNodeLabel']]['yCoordinate']
        x2 = node_dict[edge['endNodeLabel']]['xCoordinate']
        y2 = node_dict[edge['endNodeLabel']]['yCoordinate']
        # x = np.linspace(x1, x2, 256, endpoint=True)
        # y = np.linspace(y1, y2, 256, endpoint=True)
        # plt.plot(x, y)
        dx = x2 - x1
        dy = y2 - y1
        ax.arrow(x1, y1, dx, dy, length_includes_head=True, head_width=0.1, head_length=0.2, fc='black')
    plt.show()

