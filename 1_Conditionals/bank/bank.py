def main():
    greeting = input('Hello!')
    hello(greeting)

def hello(response):
    response = response.strip().lower()
    if response.startswith('hello'):
        print ("$0")
    elif response.startswith('h'):
        print ("$20")
    else:
        print ("$100")

main()
