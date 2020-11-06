from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples
from VirtualMachine import VirtualMachine


def main():
    # print_rows()

    # data = " "
    # data = data.join(get_tokens())

    # function test(int a, int b, int c): int {
    #     int d, e
    #     string f
    #     return 1
    # }

    # data = '''
    # function main {
    #     int b, c;
    #     b = 1 * (1 + 4);
    # }
    # '''
    data = '''
    function test(int a, int b): int {
        int c;
        c = -3.0;
        return c;
    }

    function main {
        int a, b;
        a = 12;
        b = 3;
        test(a, b);
    }
    '''

    '''
    while (2 < 5) {
            b = b + 1;
            print("test", b);
        }
        b = 1;
    '''

    # Generate Object code.
    quadruples, constants = parse(data)

    vm = VirtualMachine(quadruples, constants)
    vm.run()


main()
