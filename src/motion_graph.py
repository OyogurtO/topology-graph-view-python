from src.view import motion_graph_view
from src.view import motion_graph_view_v2
from src.io import load_json_data


def load_and_view(file_name):
    data = load_json_data.load(file_name)
    motion_graph_view.view(data['nodes'], data['edges'], file_name)


def load_and_view2(file_name):
    data = load_json_data.load(file_name)
    motion_graph_view_v2.view(data['nodes'], data['edges'], file_name)
