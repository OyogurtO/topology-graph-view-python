import sys

from src import topology_graph, motion_graph
from src.io import parse_or_input_file_name


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        file_name = parse_or_input_file_name.parse_file_name(sys.argv[1:])
        topology_graph.load_and_view(file_name)
    else:
        motion_graph.load_and_view(sys.argv[1])
