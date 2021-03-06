import pandas as pd
import math
import os
import copy


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
        if self.shape == "Manual Input":
            string = [f"read({self.text});"]
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


class DiagramConverter():
    def __init__(self) -> None:
        self.r = []

    def get_page_ids(self, df):
        pages = df[df["Name"] == "Page"]
        ids = {}
        for i, row in pages.reset_index().iterrows():
            ids[i+1] = row.Id

        return ids

    def get_page_data(self, df, selected_page):
        ids = self.get_page_ids(df)
        id_ = ids[selected_page]
        data = df[df["Page ID"] == id_]
        return data

    def create_graph(self, data):
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

    def traverse_tree(self, node, pending):
        if not node:
            raise NameError(f"Missing main method")

        string = node.tostrs()
        self.r = self.r + string
        if node.isnan and node.shape == "Decision":
            node.needed_oks -= 1
            if node.needed_oks == 1:
                # print("else {")
                self.r = self.r + ["else {"]
            if node.needed_oks != 0:
                return
        if node.right:
            self.traverse_tree(node.right, pending)
        if node.left:
            self.traverse_tree(node.left, pending)

        return self.r

    def get_main_index(self, roots):
        for i, root in enumerate(roots):
            if "main()" in root.text:
                return i

    def get_rows(self, csv_path, selected_page):
        df = pd.read_csv(csv_path, index_col=0)
        df = df[df["Name"] == "Page"]
        selected_page_index = 1
        tabs = df["Text Area 1"].values
        for i, tab in enumerate(tabs):
            if tab == selected_page:
                selected_page_index = i + 1
        # selected_page_index = d[selected_page]
        df = pd.read_csv(csv_path, index_col=0)

        data = self.get_page_data(df, selected_page_index)

        premain_process = data[data["Name"] == "Predefined Process"]
        premain_lines = ""
        if len(premain_process) > 0:
            premain_text = premain_process.iloc[0]["Text Area 1"]
            premain_rows = premain_text.split(";")[:-1]
            premain_rows = [row.replace("global", "") for row in premain_rows]
            premain_rows = ["global " + row for row in premain_rows]
            premain_lines = ";".join(premain_rows) + ";"

        roots, _ = self.create_graph(data)

        main_index = self.get_main_index(roots)

        f = []
        roots[main_index], roots[-1] = roots[-1], roots[main_index]
        for root in roots:
            pending = []
            self.r = self.traverse_tree(root, pending)
            f = self.r
        f = [premain_lines] + f
        return f

    def print_rows(self, csv_path, selected_page):
        rows = self.get_rows(csv_path, selected_page)
        for row in rows:
            print(row)

    def get_tokens(self, csv_path, selected_page):
        r = self.get_rows(csv_path, selected_page)
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

    def get_string(self, csv_path, selected_page):
        tokens = self.get_tokens(csv_path, selected_page)
        string = "".join(tokens)
        string = string.replace("\n", "")
        string = string.replace(" ", "")
        return string

    def get_example_path(self):
        return "./diagram_converter/examples/csvs/diagrams.csv"


def main():
    dc = DiagramConverter()
    path = dc.get_example_path()
    selected_page = "recursion"  # simple, if, while, lists, functions, all, recursion

    dc.print_rows(path, selected_page)
    # tokens = get_string(path, selected_page)
    # print(tokens)


if __name__ == "__main__":
    main()
