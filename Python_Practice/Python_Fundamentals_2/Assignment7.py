# Design a program to continiously input a number n print if it is positive or negative. Only stop when the user types "Quit"

num = input("enter a number input or Quit : ")
# Quit = "Quit"
while num != "Quit":

    if "-" in num:

        print(num+" is negative")

    else:
        print(num+" is positive ")

    num = input("enter a next number or quit : ")
