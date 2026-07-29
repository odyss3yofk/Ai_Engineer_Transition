# Write a function that prints the digits of a number

def digits(num):

    a = 0

    while num > 0:
        a = num % 10
        num = num//10
        print(a)


digits(123)
