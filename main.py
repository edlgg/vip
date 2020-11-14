from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples
from VirtualMachine import VirtualMachine


def main():
    # print('We are testing our diagram converter here:')
    # print_rows()
    # print('We are done testing our diagram converter')

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
    function main {
        int a[1 .. 5], b[1 .. 2][3 .. 6][0 .. 1], c;
        a[4] = 3;
        print(a[4]);
    }
    '''

    data3 = '''
    function main {
        int a[1 .. 5], c;
        int cont;
        cont = 1;
        while (cont <= 5) {
            a[cont] = cont;
            cont = cont + 1;
        }
        cont = 1;
        while (cont <= 5) {
            print(a[cont]);
            cont = cont + 1;
        }
    }
    '''

    data2 = '''
    function main {
        int a;
        a = 4;
        print("value of a: ");
        print(a);
        if (a < 5) {
            print("a is less than 5");
        }
        else {
            print("a is not less than 5");
        }
    }
    '''

    data4 = '''
        function suma(int a, int b): int {
            int c;
            return a + b;
        }

        function main {
            int a, b;
            a = 3;
            b = 2;
            a = suma(3,4);
            print(a);
        }
    '''

    # Generate Object code.
    quadruples, constants = parse(data)

    print("")
    print("")
    print("Virtual Machine output: ")
    vm = VirtualMachine(quadruples, constants)
    vm.run()


main()
