def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if char_length(s) and starts_with_two_letters(s):
        return True

def char_length(str):
    if 2 <= len(str) <= 6:
        return True
    else:
        return False

def starts_with_two_letters(s):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x, y = list(s[:2])
    if x in letters and y in letters:
        return True
    else:
        return False
    
def middle_verified(s):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    if len(s) > 2 and len(s) <= 6:
        arr = list(s[2:])
        loop_length = len(arr) - 1

        count = 0
        while count < loop_length:
            if arr[count] in numbers and arr[loop_length] in letters:
                print(False)
            else:
                print(True)
            count +=1


middle_verified('AAA222')

# main()