import sys

from src.view import topology_view
from src.io import parse_or_input_file_name, load_json_data


def main(argv):
    file_name = parse_or_input_file_name.parse_file_name(argv)
    data = load_json_data.load(file_name)
    print(len(data))
    topology_view.view(data['floorList'][0]['nodeList'], data['floorList'][0]['edgeList'], {})


if __name__ == '__main__':
    main(sys.argv[1:])
