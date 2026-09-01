# Create a program that requests for X (>= 0) and Y (>0) and returns X/Y as a percentage rounded to the nearest integer. 

def main ():
    fraction = input("Fraction on your fuel guage: ")
    print(get_percent(fraction))
    
def get_percent(value):
    X, Y = value.split("/")
    return f"{round((int(X)/int(Y)) * 100)}%"


main()