import re
from sys import exit
def main():
    a=input("Hours: ")
    result=convert(a)
    print(result)
def convert(s):
    match = re.match(r"^(\d{1,2})((:)(\d{2}))?\s(AM|PM) to (\d{1,2})((:)(\d{2}))?\s(AM|PM)$", s)
    if match:
        # s = s.split(" to ")
        if match.group(2) and match.group(7):
            if int(match.group(4))>59 or int(match.group(1))>12 or int(match.group(6))>12 or int(match.group(9))>59:
                raise ValueError
            else:
                if match.group(5)=="AM":
                    if int(match.group(1))==12:
                        left_Hour="0"
                    else:
                        left_Hour=match.group(1)

                    if match.group(2):
                        left_Minute=match.group(4)
                else:
                    if int(match.group(6))==12:
                        left_Hour="12"
                    else:
                        left_Hour=int(match.group(1))+12
                    if match.group(2):
                        left_Minute=match.group(4)
                if match.group(10)=="AM":
                    if int(match.group(6))==12:
                        right_Hour="0"
                    else:
                        right_Hour=match.group(6)
                    if match.group(2):
                        right_Minute=match.group(9)
                else:
                    if int(match.group(6))==12:
                        right_Hour="12"
                    else:
                        right_Hour=int(match.group(6))+12
                    if match.group(2):
                        right_Minute=match.group(9)
                if int(left_Hour)<10 and not int(right_Hour)<10:
                    return (f"0{left_Hour}:{left_Minute} to {right_Hour}:{right_Minute}")
                elif not int(left_Hour)<10 and int(right_Hour)<10:
                    return (f"{left_Hour}:{left_Minute} to 0{right_Hour}:{right_Minute}")
                elif int(left_Hour)<10 and int(right_Hour)<10:
                    return (f"0{left_Hour}:{left_Minute} to 0{right_Hour}:{right_Minute}")

                else:
                    return (f"{left_Hour}:{left_Minute} to {right_Hour}:{right_Minute}")
        else:
            # if int(int(match.group(1))>12 or int(match.group(6))>12:
            #     raise ValueError
            # else:
            if match.group(5)=="AM":
                if int(match.group(1))==12:
                    left_Hour="0"
                else:
                    left_Hour=match.group(1)
            else:
                if int(match.group(6))==12:
                    left_Hour="12"
                else:
                    left_Hour=int(match.group(1))+12
            if match.group(10)=="AM":
                if int(match.group(6))==12:
                    right_Hour="0"
                else:
                    right_Hour=match.group(6)
            else:
                if int(match.group(6))==12:
                    right_Hour="12"
                else:
                    right_Hour=int(match.group(6))+12
            if int(left_Hour)<10 and not int(right_Hour)<10:
                return (f"0{left_Hour}:00 to {right_Hour}:00")
            elif not int(left_Hour)<10 and int(right_Hour)<10:
                return (f"{left_Hour}:00 to 0{right_Hour}:00")
            elif int(left_Hour)<10 and int(right_Hour)<10:
                return (f"0{left_Hour}:00 to 0{right_Hour}:00")
            else:
                return (f"{left_Hour}:00 to {right_Hour}:00")
    else:
        raise ValueError
        # return match.group(5)>59

if __name__ == "__main__":
    main()