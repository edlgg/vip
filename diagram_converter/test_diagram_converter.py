import pytest
from diagram_converter import DiagramConverter

simple_expected_result = """
    function main() {
    int a, b, c;
    a = 1;
    b = 2;
    c = a+b;
    print("a, b, c: ", a, b, c);
    }
"""

if_expected_result = """
function main() {
    int i;
    a = 6;
    if(i < 3) {
        print("smaller than 3: ", i);
    }
    elif(i == 3) {
        print("3: ", i);
    }
    else {
        print("bigger than 3: ", i);
    }
}
"""

while_expected_result = """
function main() {
    int a, b;
    a = 1;
    b = 5;
    while(a < b) {
        print(a, " smaller than 3: ", b);
        a = a + 1;
    }
}
"""

lists_expected_result = """
function main() {
    int a[1 .. 5], b[1 .. 5], c, d;
    a[4] = 1;
    b[2] = 4;
    c = a[4];
    d = a[b[2]];
    print("a[4], c: ", a[4], c);
    print("a[4] b[2], a[b[2]]: ", a[4], b[2], a[b[2]]);
}
"""

functions_expected_result = """
function bark():void {
    print("waff waff");
}

function suma(int a, int b): int {
    int c;
    c = a+b;
    return c; 
}

function main() {
    int a, b, c;
    a= 1;
    b=2;
    c = suma(a, b);
    bark();
    print("c: ", c);
}   
"""

all_expected_result = """
function bark() {
print("waff waff");
}

function suma(int a, int b): int {
int c;
c = a+b;
return c; 
}

function main() {
int i, a;
i = 1;
a = 5;
int l[1 .. a];
while(i < a) {
    l[i] = 42;
    if(i < 3) {
        print(a, "+", i, "=", suma(a,i));
    }
    elif(i == 3) {
        print("l[i-1]: ", l[i-1]);
    }
    else {
        print(bark());
    }
    i = i + 1;
}
}
"""

recursion_excpected_result = """
function fib(int i): int {
int res;
if(i < 2){
    res = 1;
}else{
    res = fib(i-1) + fib(i - 2);
}
return res; 
}

function main() {
    int i;
    i = 5;
    print("fib: ", i, " = ", fib(i));
}   
"""


@pytest.mark.parametrize(
    "a, b",
    [
        ("simple", simple_expected_result),
        ("if", if_expected_result),
        ("while", while_expected_result),
        ("lists", lists_expected_result),
        ("functions", functions_expected_result),
        ("all", all_expected_result),
        ("recursion", recursion_excpected_result)
    ],
)
def test_diagram_conversion(a, b):
    dc = DiagramConverter()
    expected_result = b.replace("\n", "")
    expected_result = expected_result.replace(" ", "")

    path = dc.get_example_path()
    string = dc.get_string(path, a)
    assert len(string) == len(expected_result)
