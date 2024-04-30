#defines the squear function
def squear(n):
    return n*n
#user inputs the mass in kilograms and program counts the energy in joules from E=mc^2
def main():
    mass = int(input("m: "))
    c=300000000
    Energy = mass*squear(c)
    print(Energy)
main()