grocery = {}


def main():
    arr = []
    while True:
        try:
            items = input("Enter your item: ")
        except EOFError:
            print()
            break
        else:
            arr.append(items)
    into_dict(arr)
    print(grocery)

def into_dict(x):
    print(x)
    for item in x:
        if item in grocery.keys():
            grocery[item] += 1
        else:
            grocery[item] = 1
        
    

main()