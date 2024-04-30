from datetime import date
import inflect
import sys


def main():
    try:
        user = input("date of birth format yyyy-mm-dd:  ")
        print(read_numbers(days_minutes(calculate(user))))
    except ValueError:
        sys.exit("invalid date")
    calculate(user)


def calculate(birth):
    today = date.today()
    birth = date.fromisoformat(birth)
    new_today = today - birth
    return  new_today.days

def read_numbers(number):
    return inflect.engine().number_to_words(number, andword="")

def days_minutes(days):
    return days*24*60

if __name__ == "__main__":
    main()