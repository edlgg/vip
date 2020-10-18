from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse
from semantic.AddressTable import AddressTable
from semantic.Quadruples import Quadruples


# running 'python main.py' will only print something if there is a syntax error.

global Q

Q = Quadruples()


def main():
    # print_rows()

    # data = " "
    # data = data.join(get_tokens())

    # function test(int a, int b, int c): int {
    #     int d, e
    #     string f
    #     return 1
    # }

    data = '''
    function main {
        int b;
        b = 9 - 1 * 4 + 3;
        }
    '''

    AT = parse(data)
    AT.print_all()


main()
