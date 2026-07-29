# Write a program that takes salary as input. Using conditional statements calculate the final tax rates:
# If salary< 30,000 -> 5%
# If salary= 30,000-70,000 -> 15%
# If salary> 70,000 -> 25%

salary = int(input("enter salary :"))

if (salary < 30000):

    print("tax would be 5 %")
elif (salary in range(30000, 70001)):

    print("tax would be 15 %")

else:

    print("tax would be 25 %")
