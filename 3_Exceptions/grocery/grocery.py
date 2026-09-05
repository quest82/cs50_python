grocery = {}

def main():
    while True:
        try:
            item = input("Enter your item: ")
        except EOFError:
            print()
            break
        else:
            into_dict(item)
    print(grocery)

def into_dict(x):
        if x in grocery.keys():
            grocery[x] += 1
        else:
            grocery[x] = 1
        
    

main()