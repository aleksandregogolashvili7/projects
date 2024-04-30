# try:
#     Names=[]
#     while True:
#         name=input("name= ")
#         Names.append(name)
#         Names.append(",")
#         continue
# except EOFError:
#     n=len(Names)
#     Names[n-3]="and"
#     Names[n-1]=""
#     print(sep="\n")
#     print("Adieu, adieu, to",end=" ")
#     for i in range(n):
#         print(Names[i],end=" ")
from inflect import engine
try:
    p=engine()
    Names=[]
    while True:
        name=input("name= ")
        Names.append(name)
        continue
except EOFError:
    n=len(Names)
    print(sep="\n")
    print("Adieu, adieu, to",p.join(Names))
