from src.io import load_json_data
from src.view import predecessor_tree_view


def load_and_view(file_name):
    data = load_json_data.load(file_name)
    predecessor_tree_view.view(data, file_name)
