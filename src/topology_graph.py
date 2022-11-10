from src.view import topology_graph_view
from src.io import load_json_data


def load_and_view(file_name):
    data = load_json_data.load(file_name)
    print(data['mapCode'])
    for i in range(len(data['floorList'])):
        print(i)
        floor = data['floorList'][i]
        if i != 0:
            topology_graph_view.change_figure(i)
        topology_graph_view.view(floor['nodeList'], floor['edgeList'], file_name + ' [' + floor['floorNumber']+']')
    topology_graph_view.show()
