# Script Name:                  604 Week One - Python Lab Functions
# Author:                       Juan Miguel Cano
# Date of latest revision:      11/01/2024      
# Purpose:                      This Python script is to repeatedly prompt the user for numbers,
#                               track the largest and smallest values, and handle invalid inputs.
# Resources:                    https://www.py4e.com/html3/05-iterations
# Prompt for the file name
fname = input("Enter the file name: ")

# Try to open the file
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

# Initialize variables for counting lines and total confidence
count = 0
total = 0

# Read through each line in the file
for line in fhand:
    # Look for lines that start with the desired text
    if line.startswith("X-DSPAM-Confidence:"):
        # Find the position of the floating point value and extract it
        value = float(line[line.find(":") + 1:].strip())
        # Add to the total and increase the count
        total += value
        count += 1

# Calculate and print the average confidence if count is greater than 0
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No lines found with 'X-DSPAM-Confidence'")
