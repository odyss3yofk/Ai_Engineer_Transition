# Number guessing game

sec_num = 55

num = int(input("enter your number"))

while (num != sec_num):

    if (num > sec_num):

        print("Too High")
    else:
        print("Two Low")

    num = int(input("guess again"))

print("spot on")
