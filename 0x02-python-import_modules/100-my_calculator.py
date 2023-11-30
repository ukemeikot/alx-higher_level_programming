#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operators = ['+', '-', '*', '/']
    size = len(argv)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    match operator:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
