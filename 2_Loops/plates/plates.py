def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if char_len(s) and starter(s) and onlyAlphaNum(s) and charOrder(s):
        return True
    else:
        return False

def char_len(str):     # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if 2 <= len(str) <= 6:
        return True

def starter(str): # “All vanity plates must start with at least two letters.”
    if str[:2].isalpha():
        return True

def onlyAlphaNum(str): # “No periods, spaces, or punctuation marks are allowed.”
    for char in str:
        if char.isalnum():
            return True

def charOrder(str): # “Numbers cannot be used in the middle of a plate; they must come at the end. "
    has_num = False

    for char in str:
        if char.isdigit():
            if char == 0:
                return False
            has_num = True
                
        elif has_num:
            return False
    return True

main()


