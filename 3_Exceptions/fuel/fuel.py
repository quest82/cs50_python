# Create a program that requests for X (>= 0) and Y (>0) and returns X/Y as a percentage rounded to the nearest integer. 
# If 1% or less or 99% or greater, return E or F respectively
from math import floor

def main():
    while True:
        fraction = input("Fraction on your fuel guage: ")
        X, Y = fraction.split("/")

        if X.isdigit() and Y.isdigit() and int(X) <= int(Y) and int(Y) > 0:
                fuel_percent = get_percent(X, Y)
                print(fuel_percent)
                break
#     check_percent = check_percent(fuel_percent)

def get_percent(a, b):
    return floor((float(a) / float(b)) * 100) 

# def check_percent(value):
#     if value <= 1:
#         print("E")
#     elif value >= 99:
#         print("F")
#     return f"{value}%"



main()