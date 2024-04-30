def main():
    gauge=input("fraction: ")
    gauge=convert(gauge)
    if gauge==0 or gauge==1:
        print("E")
    elif gauge==100 or gauge==99:
        print("F")
    else:
        print(str(gauge).replace(".0","")+"%")

def convert(x):
    while  "/" not in x:
        x=input("fraction: ")
        continue

    x=x.split("/")
    while not (x[0].isdigit() and x[1].isdigit()):
         x=input("fraction: ")
         continue
    x1=int(x[0])
    x2=int(x[1])
    if x1>x2:
        while True:
         x=input("fraction: ")
         continue
    else:

        return round(100*(x1/x2))

main()