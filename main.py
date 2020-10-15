from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse


def main():
    tokens = get_rows()
    print(tokens)

    data = '''
    function sum(int a, int b): int {
    int res;
    res = a + b;
    return res;
    }

    function main {
        int res;
        print("Hello my friends!");
        
        res = sum(4, 4);
        print(res);
    }
    '''

    parse(data)

main()



