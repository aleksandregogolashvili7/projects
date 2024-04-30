import re
import sys


def main():

    print(count(input("Text: ")))
    sys.exit(0)

def count(s):
    s=s.lower().strip()
    word=r"\bum\b"
    number=re.findall(word,s)
    return len(number)

...


if __name__ == "__main__":
    main()
