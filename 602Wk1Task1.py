# Script Name:                  602 Week One - Python Lab Functions
# Author:                       Juan Miguel Cano
# Date of latest revision:      10/05/2024      
# Purpose:                      This Python script calculates an employee's gross pay using a function as assigned in this lab. 
# Resources:                     - Severance, C. R. (n.d.). Python for everybody: Exploring data using Python 3. Retrieved from
#                               https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
#                                - Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming
#                               (2nd ed.). No Starch Press. Retrieved from 
#                               https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch08.xhtml#ch08lev1sec1



# Define the computepay function by computing the total gross pay based on hours worked and hourly rate.
def computepay(hours, rate_per_hour):
    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate_per_hour) + (overtime_hours * rate_per_hour * 1.5)
    else:
        gross_pay = hours * rate_per_hour
    return gross_pay

# Prompt user for hours and rate
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))

# Call the function to compute the pay
gross_pay = computepay(hours, rate_per_hour)

# Print the result
print("Gross Pay:", gross_pay)
