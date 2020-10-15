from diagram_converter.diagram_converter import reader


def main():
    lines = reader()
    lines = " ".join(lines)
    print(lines)


main()
