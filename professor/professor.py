from random import randint


def main():
    try:
        level=get_level()
        Error=0
        for i in range(9):
            n1=generate_integer(level)
            n2=generate_integer(level)
            n3=n1+n2
            print(n1,"+",n2,"=",end=" ")
            result=int(input())
            if result==n3:
                continue
            else:
                for i in range(2):
                    print("EEE")
                    print(n1,"+",n2,"=",end=" ")
                    result=int(input())
                    if result==n3:
                        Error+=1
                        break
                    else:
                        continue
                print(n1,"+",n2,"=",n3)
                Error+=1

        print("Score:",10-Error)
    except ValueError:
        print("nela entertan vax. tavidan daiwye")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                print("Invalid level")
            else:
                return level
        except ValueError:
            print("Invalid input.")



def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)

if __name__ == "__main__":
    main()
    input("Press Enter to exit")