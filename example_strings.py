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
        int a;
        a = 1;
        if (not a){
            print("not a 1");
        }
        a = 0;
        if (not a){
            print("not a 2");
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
            c = a + b;
            return c;
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

factorial_recursivo = '''
    function factorial_recursivo(int i): int {
        if (i < 2) {
            return 1;
        }
        return i * factorial_recursivo(i - 1);
    }

    function main () {
        print(factorial_recursivo(5));
    }
    '''

fibonacci_ciclo = """
    function fibonacci_ciclo(int n): int{
        int i, a, b, c;
        a = 1;
        b = 1;
        i = 1;
        while (i < n - 1) {
            c = a + b;
            a = b;
            b = c;
            i = i + 1;
        }
        return c;
    }
    function main() {
        int res;
        res = fibonacci_ciclo(f);
        print("res: ", res);
    }
    """

find = """
    
    function main() {
        int l[1 .. 10], i, n, wanted;
        n = 1;
        while (n < 11) {
            l[n] = n * 2 + 1;
            n = n + 1;
        }

        n = 1;
        while (n < 11){
            print(l[n]);
            n = n + 1;
        }

        n = 1;
        wanted = 11;
        while (n < 11){
            if (l[n] == wanted) {
                print("wanted: ", l[n], n);
            }
            n = n + 1;
        }
    }
    """

sort = """

    function main(){
        int l[1 .. 10], i, j, n, sign, min_index, pointer, temp, a;
        n = 1;
        sign = -1;
        while (n < 11) {
            l[n] = sign * (n * 2 + 1);
            sign = sign * -1;
            n = n + 1;
        }

        n=1;
        while (n < 11) {
            print(l[n]);
            n = n + 1;
        }


        i = 1;
        while (i < 11){
            j = i;
            min_index = i;
            while (j < 11) {
                if (l[j] < l[min_index]) {
                    min_index = j;
                }else {
                    a = 1;
                }
                j = j + 1;
            }
            temp = l[i];
            l[i] = l[min_index];
            l[min_index] = temp;

            i = i + 1;
        }

        print("******");

        n=1;
        while (n < 11) {
            print(l[n]);
            n = n + 1;
        }
    }
    """

mat_mult = """
        function main() {
            int A[0 .. 1][0 .. 2], B[0 .. 2][0 .. 1], C[0 .. 1][0 .. 1];
            int m, n, p, q, i, j, k;
            m = 2;
            n = 3;
            p = 3;
            q = 2;

            A[0][0] = 0;
            A[0][1] = 3;
            A[0][2] = 7;
            A[1][0] = 5;
            A[1][1] = 5;
            A[1][2] = 2;

            B[0][0] = 3;
            B[0][1] = 3;
            B[1][0] = 3;
            B[1][1] = 4;
            B[2][0] = -2;
            B[2][1] = -2;

            i = 0;
            while (i < m) {
                j = 0;
                while (j < q){
                    k = 0;
                    C[i][j] = 0;
                    while (k < p){
                        C[i][j] = C[i][j] + (A[i][k] * B[k][j]);
                        k = k + 1;
                    }
                    j = j + 1;
                }
                i = i + 1;
            }

            print(C[0][0],C[0][1]);
            print(C[1][0],C[1][1]);
        }

    """

input = """
function main () {
    int d;
    print("Insert var");
    read(d);
    print("var == ", d);
}
"""
