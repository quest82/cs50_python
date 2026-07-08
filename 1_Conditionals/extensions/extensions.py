def get_extension(file):
    reset = file.strip().lower()

    if ".gif" in reset:
        print('image/gif')
    elif ".jpg" in reset:
        print('image/jpeg')
    elif ".jpeg" in reset:
        print('image/jpeg')
    elif ".png" in reset:
        print('image/png')
    elif ".pdf" in reset:
        print('application/pdf')
    elif ".txt" in reset:
        print('text/plain')
    elif ".zip" in reset:
        print('application/zip')
    else:
        print("application/octet-stream")            


def main():
    filename = input("What's your file name? ")
    get_extension(filename)

main()