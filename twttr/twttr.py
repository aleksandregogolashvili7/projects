def main():
   print(shorten("word"))

def shorten(word):

    vowels = "AaEeIiOoUu"
    return "".join([i for i in word if i not in vowels])

if __name__ == "__main__":
    main()

