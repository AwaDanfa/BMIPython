""" Write a program that calculates a user’s BMI. BMI is calculated as follows:
BMI = weight ÷ height2
Weight is measured in kilograms and height is measured in metres. """

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
BMI = round(weight/(height*height), 2)
print("At age " + str(age) + " your BMI is " + str(BMI))
