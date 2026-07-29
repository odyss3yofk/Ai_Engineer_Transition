# Design a simple calculator

def calculator(a, b, opr):

    if opr == "+":

        return a+b
    elif opr == "-":

        return a-b
    elif opr == "*":

        return a*b
    elif opr == "/":

        return a/b
    else:
        return ("invalid operation")


print(calculator(1, 2, "-"))
