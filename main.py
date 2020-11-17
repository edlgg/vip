from diagram_converter.diagram_converter import DiagramConverter
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
    function main () {
        int a[1 .. 5], b[1 .. 2][3 .. 6][0 .. 1], c;
        a[4] = 3;
        print(a[4]);
    }
    '''

    data3 = '''
    function main () {
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
    function main () {
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

        function print_this(): int{
            print("this");
            return 0;
        }

        function main () {
            int a, b; a = 3;
            b = 39;
            print(b, a);
            print("hola",b);
            a = b - suma(3,4);
            print(b,"-", suma(3,4), a);
            print(a);
            print_this();
        }
    '''

    data5 = 'function main () { int a , b , c ; a = 1 ; b = 2 ; c = a + b ; print ( " a , b , c: " , a , b , c ) ; }'

    dc = DiagramConverter()
    path = dc.get_example_path()
    print("Printing the intermediate code")
    type_ = "recursion"
    # print_rows(path, type_)
    print("*******************************")
    data6 = dc.get_tokens(path, type_)
    data6 = " ".join(data6)

    # Generate Object code.
    quadruples, constants = parse(data6)

    print("")
    print("")
    print("Virtual Machine output: ")
    vm = VirtualMachine(quadruples, constants)
    vm.run()


main()


'''

int a;
a = 4;
if (if i < 3) .....a
TODO: Arrojar error porque 'i' no esta declarado.

'''
