grocery = {}

def main():
    while True:
        try:
            item = input()
        except EOFError:
            print()
            break
        else:
            into_dict(item)
    print(get_result())

def into_dict(x):
        if x in grocery.keys():
            grocery[x] += 1
        else:
            grocery[x] = 1
def get_result():
    result = ''
    for key in sorted(grocery.keys()):
        value = grocery[key]
        result += f"{value} {key.upper()}\n"
    return result
            
    

main()