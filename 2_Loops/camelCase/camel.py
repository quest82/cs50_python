def main():
    variable = input("What's your variable name? ")
    to_snake_case(variable)

def to_snake_case(x):
    converted = ''
    for text in x:
        if text.isupper():
            converted += '_'
            converted += text.lower()
        else:
            converted += text  
    print(converted)
main()