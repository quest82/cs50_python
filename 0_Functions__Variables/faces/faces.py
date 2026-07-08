def main():
    mood = input("What's your mood? ")
    emojiConvert(mood)


def emojiConvert(str):
    splitted = str.split()
    for i, x in enumerate(splitted):
        if x == ":)":
            splitted[i] = "🙂"
        if x == ":(":
            splitted[i] = "🙁"
    print(" ".join(splitted))
    # if ":)" in str :
    #     new = str.replace(":)", )
    #     print(new)
    # if ":(" in str :
    #     new = str.replace(":(", )
    #     print(new)


main()