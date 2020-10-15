from diagram_converter.diagram_converter import reader
from parser import parse


lines = reader()
lines = " ".join(lines)
print(lines)

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


