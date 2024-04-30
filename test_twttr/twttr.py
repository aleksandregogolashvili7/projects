def main():
    word=str(input("sad: "))
    print(shorten(word))
def shorten(word):
    vowels = "AaEeIiOoUu"
    twttr=[]
    for char in word:
        if char not in vowels:
            twttr.append(char)
    return "".join(twttr)
main()


