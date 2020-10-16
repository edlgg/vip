from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse

# running 'python main.py' will only print something if there is a syntax error.


def main():

    # print_rows()

    data = " "
    data = data.join(get_tokens())

    parse(data)


main()
