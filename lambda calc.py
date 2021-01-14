operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y
}


def calculate():
    num_x_chars = int(input(" insert character for x"))
    operation = input("type operator value")
    num_y_chars = int(input(" insert character for y"))
    for char in operations:
        if char.isdigit():
            if operation is None:
                num_x_chars += char
            else:
                num_y_chars += char
        elif char in operations:
            operation = char
        elif char.isspace:
            pass
        else:
            raise Exception("invalid character: " + char)
        return operations[operation](int(num_x_chars), int(num_y_chars))
calculate()
