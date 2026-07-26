def main():
    shortened = shorten(input("What word will you like to shorten? "))
    print(shortened)


def shorten(word):
    result = ""
    for letter in word:
        if letter not in 'AEIOUaeiou':
            result += letter
        else:
            continue
    return result

main()
