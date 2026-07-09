def interpret(values):
    arr = values.split()
    x, y, z = arr
    if y == '+':
        print(float(x) + float(z))
    elif y == '/':
        print(float(x) / float(z))
    elif y == '-':
        print(float(x) - float(z))
    elif y == '*':
        print(float(x) * float(z))

def main():
    calc = input('Enter your calculation: ')
    interpret(calc)

main()