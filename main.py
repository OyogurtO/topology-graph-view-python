import sys

from src.view import topology_graph_view
from src.io import parse_or_input_file_name, load_json_data


def main(argv):
    file_name = parse_or_input_file_name.parse_file_name(argv)
    data = load_json_data.load(file_name)
    print(data['mapCode'])
    for i in range(len(data['floorList'])):
        print(i)
        floor = data['floorList'][i]
        if i != 0:
            topology_graph_view.change_figure(i)
        topology_graph_view.view(floor['nodeList'], floor['edgeList'], floor['floorNumber'])
    topology_graph_view.show()


if __name__ == '__main__':
    main(sys.argv[1:])
