#601Wk4B Python Task 2
# Script Name:                  Week Four - Python Lab
# Author:                       Juan Miguel Cano
# Date of latest revision:      09/27/2024      
# Purpose:                      This Python script coverts a numerical score into a letter grade. 
# Resource:                     Severance, C. R. (n.d.). Python for everybody: Exploring data using Python 3. Retrieved from
#                               https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf

""""" This Python program asks the user to enter a score between 0.0 and 1.0 and then it converts
that score into a letter grade based on a grading scale. It then uses the input() function to collect 
the score and the float() function to convert the input into a number to compare. if
the score is outside the valid range, the program prints an error message and exits.The program uses 
if-elif statements to compare the score to the grade and prints the correct grade."""""

# Prompt user for the score
score = float(input("Enter score between 0.0 and 1.0: "))

# Check if score is valid and print the correct grade
if score < 0.0 or score > 1.0:
    print("Error: Score is out of range")
elif score >= 0.9:
    print("Grade: A")
elif score >= 0.8:
    print("Grade: B")
elif score >= 0.7:
    print("Grade: C")
elif score >= 0.6:
    print("Grade: D")
else:
    print("Grade: F")
