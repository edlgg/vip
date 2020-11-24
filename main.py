from diagram_converter.diagram_converter import DiagramConverter
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples
from VirtualMachine import VirtualMachine
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from constants import Type
from example_strings import *


def main():
    type_ = sys.argv[1]

    quadruples, constants = None, None
    if type_ == "examples":
        quadruples, constants = parse(test)
    else:
        # Convert diagram to vip code.
        converted_diagram = convert_diagram(type_=type_)
        # Generate Object code.
        quadruples, constants = parse(converted_diagram)

    if len(sys.argv) > 2:
        if sys.argv[2] == "1":
            # Print png diagram and vip converted code.
            print_diagram(type_)
        if len(sys.argv) == 4:
            if sys.argv[3] == "1":
                # Print quadruples and address table content.
                print("Quadruples:")
                for i, q in enumerate(quadruples):
                    print(i, q)
                print("Constants:")
                for key, value in constants.items():
                    print(key, value)

    print("Virtual Machine output: ")
    vm = VirtualMachine(quadruples, constants)
    vm.run()


def print_diagram(type_):
    HOME = os.environ["HOME"]
    if HOME == "/Users/edg":
        img = mpimg.imread(
            f"/Users/edg/repos/vip/diagram_converter/examples/images/{type_}.png")
        plt.imshow(img)
        plt.show()


def convert_diagram(type_):
    dc = DiagramConverter()
    path = dc.get_example_path()
    if len(sys.argv) > 3:
        print("Printing the intermediate code")
        dc.print_rows(path, type_)
        print("*******************************")
    dc = DiagramConverter()
    converted_diagram = dc.get_tokens(path, type_)
    converted_diagram = " ".join(converted_diagram)
    return converted_diagram


if __name__ == "__main__":
    main()
