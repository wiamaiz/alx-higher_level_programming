#!/usr/bin/python3

def add(a, b):
    """Addition function

    Args:
        a: first number
        b: second number

    Returns:
        The sum of a and b
    """
    return a + b


def sub(a, b):
    """Subtraction function

    Args:
        a: first number
        b: second number

    Returns:
        The difference between a and b
    """
    return a - b


def mul(a, b):
    """Multiplication function

    Args:
        a: first number
        b: second number

    Returns:
        The product of a and b
    """
    return a * b


def div(a, b):
    """Division function

    Args:
        a: first number
        b: second number

    Returns:
        The quotient of a divided by b
    """
    return a / b


def main():
    # Example usage
    x = 5
    y = 3

    print("Addition:", add(x, y))
    print("Subtraction:", sub(x, y))
    print("Multiplication:", mul(x, y))
    print("Division:", div(x, y))


if __name__ == '__main__':
    main()

