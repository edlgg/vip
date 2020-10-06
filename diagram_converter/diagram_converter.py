import pandas as pd
import math


def get_page_ids(df):
    pages = df[df["Name"] == "Page"]
    ids = {}
    for i, row in pages.reset_index().iterrows():
        ids[i+1] = row.Id

    return ids


def select_page(df):
    ids = get_page_ids(df)

    print(f"{len(ids)} pages detectd. Select page: ")
    selected_page = int(input())

    if selected_page < 1 or selected_page > len(ids):
        return None
    return selected_page


def get_page_data(df, selected_page):
    ids = get_page_ids(df)
    id_ = ids[selected_page]
    data = df[df["Page ID"] == id_]
    return data


class Node:
    def __init__(self, id_, shape, text, isnan, right=None, left=None):
        self.id_ = id_
        self.shape = shape
        self.text = text
        self.isnan = isnan
        self.right = None
        self.left = None

    def get_str_rep(self):
        return f"{self.id_} {self.shape} {self.text} {self.isnan}"


def create_graph(data):
    lines = data[data["Name"] == "Line"]
    blocks = data[data["Name"] != "Line"]

    nodes = {}
    root = None
    for index, row in blocks.iterrows():
        text = row["Text Area 1"]
        isnan = False if type(text) == str else True
        node = Node(id_=index, shape=row.Name, text=text, isnan=isnan)
        nodes[index] = node

        if text == "main":
            root = node

    for index, row in lines.iterrows():
        source = row["Line Source"]
        destination = row["Line Destination"]
        text = row["Text Area 1"]
        # print(source, destination, text)
        if text == "No":
            nodes[source].left = nodes[destination]
        else:
            nodes[source].right = nodes[destination]

    return root


def traverse_tree(node, pending):
    print(node.get_str_rep())
    if node.isnan and pending:
        traverse_tree(pending[0], pending[1:])
    if node.right:
        traverse_tree(node.right, pending)
    if node.left:
        traverse_tree(node.left, pending)


def main():
    example_path = "/Users/edg/repos/vip/diagram_converter/examples/example1.csv"
    df = pd.read_csv(example_path, index_col=0)
    # selected_page = select_page(df)

    # if not selected_page:
    #     print("Invalid Page")
    #     return

    selected_page = 2

    data = get_page_data(df, selected_page)
    root = create_graph(data)

    pending = []
    traverse_tree(root, pending)


main()
