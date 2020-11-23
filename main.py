from diagram_converter.diagram_converter import DiagramConverter
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples
from VirtualMachine import VirtualMachine
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    type_ = sys.argv[1]

    print_diagram(type_)

    converted_diagram = convert_diagram(type_=type_)

    # Generate Object code.
    quadruples, constants = parse(converted_diagram)

    if len(sys.argv) > 2:
        print(quadruples)
        print(constants)

    print("")
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
    print("Printing the intermediate code")
    if len(sys.argv) > 3:
        dc.print_rows(path, type_)
    print("*******************************")
    dc = DiagramConverter()
    converted_diagram = dc.get_tokens(path, type_)
    converted_diagram = " ".join(converted_diagram)
    return converted_diagram


if __name__ == "__main__":
    main()
