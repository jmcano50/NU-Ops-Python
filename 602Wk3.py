# Script Name:                  602 Week Three - Python Lab Functions
# Author:                       Juan Miguel Cano
# Date of latest revision:      10/19/2024      
# Purpose:                      This Python script is to repeatedly prompt the user for numbers,
#                               track the largest and smallest values, and handle invalid inputs.
# Resources:                    https://www.py4e.com/html3/05-iterations


largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        value = int(num)
        if largest is None or value > largest:
            largest = value
        if smallest is None or value < smallest:
            smallest = value
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
