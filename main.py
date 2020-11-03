from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples


# running 'python main.py' will only print something if there is a syntax error.

# global Q

# Q = Quadruples()


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
    #     b = 2;
    #     c = 7 + 4;
    # }
    # '''
    data = '''
    function test(): void {
        int a;
        return 0;
        a = 1 + 4;
        return a;
    }

    function main {
        int a;
        if (2 < 3) {
            print("Oui");
        } 
        else {
            print("Non");
        }
        print("Fin");
    }
    '''

    print(data)

    '''
    while (2 < 5) {
            b = b + 1;
            print("test", b);
        }
        b = 1;
    '''

    AT = parse(data)

    AT.print_all()


main()
