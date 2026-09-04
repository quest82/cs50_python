from math import floor

def main():
    while True:
        fraction = input("Fraction on your fuel guage: ")
        try:
            X, Y = fraction.split("/")
        except ValueError:
            continue
        if X.isdigit() and Y.isdigit() and int(X) <= int(Y) and int(Y) > 0:
            fuel_percent = get_percent(X, Y)
            result = check_percent(fuel_percent)
            print(result)
            break
    
def get_percent(a, b):
    return floor((float(a) / float(b)) * 100) 

def check_percent(value):
    if value <= 1:
        return "E"
    elif value >= 99:
        return "F"
    else:
        return f"{value}%"



main()