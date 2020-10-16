from diagram_converter.diagram_converter import get_rows, get_tokens, print_rows
from parser import parse

# running 'python main.py' will only print something if there is a syntax error.
def main():

    #print_rows()

    data = " "
    data = data.join(get_tokens())

    # Temporary test data.
    # TODO(Eduardo): Fix diagram_converter. We must add SEMICOLON at the end 
    # of each 'if' and 'while'.
    data = '''function main {
            int a;
            a = 1;
            while(i < 5) {
            if(i < 3) {
            print("smaller than 3: ", i);
            }
            elif(i == 3) {
            print("3: ", i);
            }
            else {
            print("bigger than 3: ", i);
            };
            print(k);
            };
            }'''

    parse(data)

main()



