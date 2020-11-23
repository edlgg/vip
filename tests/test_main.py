import pytest
from diagram_converter.diagram_converter import get_tokens, get_example_path

path = get_example_path()
tokens = get_tokens(path, "simple")
tokens = " ".join(tokens)
print(tokens)
