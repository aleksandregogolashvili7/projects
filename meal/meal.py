# # In the given task, you need to create a program that tells the user what meal should be eaten at a particular time.
# The meals are breakfast, lunch, and dinner, and the meal times are between 7:-8:, 12:-13:, and 18:-19:, respectively.
# If not mealtime, the program should not output anything.

# # The program should prompt the user to enter the time in 24-hour format as a string with a colon between the hours and minutes,
# # such as "7:30" or "12:45".

# # You should structure your program by defining a function named "convert" that converts the time in string format to the corresponding number of hours as a float.
# # For instance, if the time is "7:30", the convert function should return 7.5 (7 hours and 30 minutes is equivalent to 7.5 hours).
# # This function should be called by the main function of the program.


#ამითი ვაშორებთ ":"-ს

def main():
    time = convert(input("what time is it? "))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print(None)

def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min) / 60
    time = hour + min
    return time

main()
input("Press Enter to exit")