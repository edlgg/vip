import pandas as pd
import math
import os

r = []


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
        self.needed_oks = 0

    def tostrs(self):
        string = []
        if self.shape == "Decision":  # if
            string = "}" if self.isnan else f"({self.text}) {{"
            string = string.replace("(if", "if(")
            string = string.replace("(elif", "elif(")
            string = [string.replace("( ", "(")]

        if self.shape == "Display":  # print
            string = [f"print({self.text});"]
        if self.shape == "Manual Operation":  # while
            string = "}" if self.isnan else f"({self.text}) {{"
            string = string.replace("(while", "while(")
            string = [string.replace("( ", "(")]
        if self.shape == "Process":  # instruction
            string = f"{self.text}"
            string = self.split(string)
        if self.shape == "Terminator":
            string = ["}" if self.isnan else f"function {self.text} {{"]

        return string

    def desc(self):
        left_id = self.left.id_ if self.left else -1
        right_id = self.right.id_ if self.right else -1
        return f"DESC {self.id_} {self.shape} {self.text} {self.isnan} {left_id} {right_id}"

    def split(self, s):
        split = s.split(";")
        if split[-1] != '':
            return ['ERROR missing ;']
        s2 = [word+";" for word in split if word != ""]
        return s2


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

        if nodes[destination].shape == "Decision":
            nodes[destination].needed_oks += 1

    return root, nodes


def traverse_tree(node, pending):
    global r
    string = node.tostrs()
    r = r + string
    if node.isnan and node.shape == "Decision":
        node.needed_oks -= 1
        if node.needed_oks == 1:
            # print("else {")
            r = r + ["else {"]
        if node.needed_oks != 0:
            return
    if node.right:
        traverse_tree(node.right, pending)
    if node.left:
        traverse_tree(node.left, pending)

    return r


def get_rows():
    HOME = os.environ["HOME"]
    example_path = f"{HOME}/repos/vip/diagram_converter/examples/example1.csv"
    # example_path = "/Users/davidsouza/Documents/ITESM/11vo semestre/Compiladores/vip/diagram_converter/examples/example1.csv"
    df = pd.read_csv(example_path, index_col=0)

    selected_page = 2

    data = get_page_data(df, selected_page)
    root, _ = create_graph(data)

    pending = []
    r = traverse_tree(root, pending)
    return r


def print_rows():
    rows = get_rows()
    for row in rows:
        print(row)


def get_tokens():
    r = get_rows()
    r = " ".join(r)
    r = r.replace("(", " ( ")
    r = r.replace(")", " ) ")
    r = r.replace("[", " [ ")
    r = r.replace("]", " ] ")
    r = r.replace(";", " ; ")
    r = r.replace(",", " , ")
    r = r.replace("\"", " \" ")
    r = r.split(" ")

    r = list(filter(lambda x: x != "", r))
    return r
