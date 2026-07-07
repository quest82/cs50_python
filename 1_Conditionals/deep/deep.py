def main():
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ")
    getanswer(answer)

def getanswer(x):
    x = x.lower().strip()
    if x == "42" or x == "forty-two" or x == "forty two":
        print("Yes")
    else:
        print("No")

main()