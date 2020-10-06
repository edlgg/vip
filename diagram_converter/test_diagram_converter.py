import pytest


diagram_path = "/Users/edg/repos/vip/diagram_converter/examples/example1.csv"

result = [
    "function main {",
    "int a;",
    "a = 1;"
    "while (i < 5) {",
    "if (i < 3) {",
    "print(\"smaller than 3: \", i);",
    "}",
    "elif (i == 3) {",
    "print(\"3: \", i);",
    "}",
    "else {",
    "print(\"bigger than 3: \", i);",
    "};",
    "i = i + 1;",
    "};",
    "};"
]
