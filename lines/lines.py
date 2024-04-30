import sys
try:
    if sys.argv[1].endswith(".py"):
        pass
    else:
        sys.exit("Not a Python file")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        name=sys.argv[1].strip()
        count=0
        with open(name,"r") as file:

            for line in file:
                if line.strip().startswith("#"):
                    continue
                elif line.strip()=="":
                    continue
                else:
                    count+=1
            print(count)


except FileNotFoundError:
    sys.exit("File does not exist")
