from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples

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
    function test(int b): int {
        int a;
        a = 1 + 3 + 2.4;
        return a;
    }

    function main {
        int a;
        a = "hola";
        test(a);
    }
    '''

    '''
    while (2 < 5) {
            b = b + 1;
            print("test", b);
        }
        b = 1;
    '''

    obj_code = parse(data)

main()
