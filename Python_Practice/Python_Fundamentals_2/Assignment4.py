# Write a function to count the number of digits in a number n

def digits_count(num):
    count = 0

    if num == 0:

        return 1
    else:
        while num > 0:

            count += 1

            num = num//10

        return count


print(digits_count(0))
