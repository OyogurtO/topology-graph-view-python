from src.view import motion_graph_view
from src.io import load_json_data


def load_and_view(file_name):
    data = load_json_data.load(file_name)
    motion_graph_view.view(data['nodes'], data['edges'], 'test')
