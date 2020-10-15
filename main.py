from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse


def main():

    print_rows()

    print(" ")
    data = " "
    data = data.join(get_tokens())

    parse(data)

main()



