# Write a function to return the sum of the digits of a number n

def digits_sum(num):

    a = 0
    sum = 0

    while num > 0:

        a = num % 10

        num = num//10

        sum += a

    return sum


print(digits_sum(125))
