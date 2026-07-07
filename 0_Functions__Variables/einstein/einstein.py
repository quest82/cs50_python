def main():
    mass = int(input("What's the mass of your product in kilograms: "))
    energy(mass)

def energy(x):
    print( x * (300000000 **2))

main()