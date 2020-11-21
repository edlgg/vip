from diagram_converter.diagram_converter import DiagramConverter
from parser import parse
from AddressTable import AddressTable
from Quadruples import Quadruples
from VirtualMachine import VirtualMachine


def main():
    
    data = '''
    global int d;

    function test(): void {
        int d;
        d = 145;
        print(d);
    }

    function main () {
        int a[1 .. 5], b[1 .. 2][3 .. 6][0 .. 1], c;
        d = 14;
        # a[4] = 3;
        # print(a[4]);
        c = d + 3;
        print(c);
        test();
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
            print(b,"-", suma(3,4), "=", a);
            print(a);
            print_this();
        }
    '''

    data5 = 'function main () { int a , b , c ; a = 1 ; b = 2 ; c = a + b ; print ( " a , b , c: " , a , b , c ) ; }'


    data7 = '''
    function print_hello(): void {
        print("hello");
    }

    function suma(int a, int b): int {
        print_hello();
        return (a + b);
    }

    function recursiva(int a): int {
        print(a);
        a = a - 1;
        if (a < 2) {
            print("Se acabo");
            return 1;
        }
        return recursiva(a);
    }

    function main () {
        int a, b;
        a = 1;
        b = recursiva(6);
        # read(b);
        print(suma(a,b));
    }
    '''

    # ************************************************
    dc = DiagramConverter()
    path = dc.get_example_path()
    print("Printing the intermediate code")
    type_ = "global"
    dc.print_rows(path, type_)
    print("*******************************")
    dc = DiagramConverter()
    data6 = dc.get_tokens(path, type_)
    data6 = " ".join(data6)
    # ************************************************

    # Generate Object code.
    quadruples, constants = parse(data6)

    print("")
    print("")
    print("Virtual Machine output: ")
    vm = VirtualMachine(quadruples, constants)
    vm.run()


main()

