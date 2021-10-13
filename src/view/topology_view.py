import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


def view(nodes, edges, objects):
    node_dict = {}
    for node in nodes:
        node_dict[node['nodeLabel']] = node
        plt.scatter(node['xCoordinate'], node['yCoordinate'])
    for edge in edges:
        x1 = node_dict[edge['beginNodeLabel']]['xCoordinate']
        y1 = node_dict[edge['beginNodeLabel']]['yCoordinate']
        x2 = node_dict[edge['endNodeLabel']]['xCoordinate']
        y2 = node_dict[edge['endNodeLabel']]['yCoordinate']
        x = np.linspace(x1, x2, 256, endpoint=True)
        y = np.linspace(y1, y2, 256, endpoint=True)
        plt.plot(x, y)
    plt.show()

