import pandas as pd
import math
import os
import copy

r = []


def get_page_ids(df):
    pages = df[df["Name"] == "Page"]
    ids = {}
    for i, row in pages.reset_index().iterrows():
        ids[i+1] = row.Id

    return ids


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
            is_end = self.isnan or not "(" in self.text
            if not is_end:
                string = [f"function {self.text} {{"]
            else:
                temp = "" if self.isnan else f"return {self.text};"
                string = [f"{temp}}}"]
            # string = ["}" if self.isnan else f"function {self.text} {{"]

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
    roots = []
    for index, row in blocks.iterrows():
        text = row["Text Area 1"]
        type_ = row["Name"]
        isnan = False if type(text) == str else True
        text = "" if type(text) == float else text
        node = Node(id_=index, shape=row.Name, text=text, isnan=isnan)
        nodes[index] = node

        if type_ == "Terminator" and "(" in text:
            roots.append(node)

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

    return roots, nodes


def traverse_tree(node, pending):
    global r
    if not node:
        raise NameError(f"Missing main method")

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


def get_main_index(roots):
    for i, root in enumerate(roots):
        if "main()" in root.text:
            return i


def get_rows(csv_path, selected_page):
    d = {
        "simple": 1,
        "if": 2,
        "while": 3,
        "lists": 4,
        "functions": 5,
        "all": 6,
        "recursion": 7
    }
    selected_page_index = d[selected_page]
    df = pd.read_csv(csv_path, index_col=0)

    data = get_page_data(df, selected_page_index)
    roots, _ = create_graph(data)

    main_index = get_main_index(roots)

    f = []
    roots[main_index], roots[-1] = roots[-1], roots[main_index]
    for root in roots:
        pending = []
        r = traverse_tree(root, pending)
        f = r
    return f


def print_rows(csv_path, selected_page):
    rows = get_rows(csv_path, selected_page)
    for row in rows:
        print(row)


def get_tokens(csv_path, selected_page):
    r = get_rows(csv_path, selected_page)
    r = " ".join(r)
    r = r.replace("(", " ( ")
    r = r.replace(")", " ) ")
    r = r.replace("[", " [ ")
    r = r.replace("]", " ] ")
    r = r.replace(";", " ; ")
    r = r.replace(",", " , ")
    r = r.replace("+", " + ")
    r = r.replace("-", " - ")
    r = r.replace("\"", " \" ")
    r = r.replace("\n", "")
    r = r.split(" ")

    r = list(filter(lambda x: x != "", r))
    return r


def get_string(csv_path, selected_page):
    tokens = get_tokens(csv_path, selected_page)
    string = "".join(tokens)
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


def get_example_path():
    example_path = "/Users/davidsouza/Documents/ITESM/11vo semestre/Compiladores/"
    HOME = os.environ["HOME"]
    if HOME == "/Users/edg":
        example_path = f"{HOME}/repos/vip/diagram_converter/examples/example2.csv"

    return example_path


def main():
    path = get_example_path()
    selected_page = "all"  # simple, if, while, lists, functions, all

    print_rows(path, selected_page)
    # tokens = get_string(path, selected_page)
    # print(tokens)


if __name__ == "__main__":
    main()
