import sys

from src import topology_graph, motion_graph, predecessor_tree
from src.io import parse_or_input_file_name


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("please specify graph type")
    elif sys.argv[1] == 't':
        file_name = parse_or_input_file_name.parse_file_name(sys.argv[2:])
        topology_graph.load_and_view(file_name)
    elif sys.argv[1] == 'm':
        motion_graph.load_and_view(sys.argv[2])
    elif sys.argv[1] == 'm2':
        motion_graph.load_and_view2(sys.argv[2])
    elif sys.argv[1] == 'p':
        predecessor_tree.load_and_view(sys.argv[2])
    else:
        print("unknown graph type: " + sys.argv[1])
