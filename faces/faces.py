def convert(emoticon):

    if emoticon == "Hello :)":
        return("Hello 🙂")
    elif emoticon == "Hello :( Goodbye :(":
        return("Hello 🙁 Goodbye 🙁")
    elif emoticon == "Hello :) Goodbye :(":
        return("Hello 🙂 Goodbye 🙁")
    elif emoticon == "Hello :) Goodbye :)":
        return("Hello 🙂 Goodbye 🙂")
    elif emoticon == "Hello :( Goodbye :)":
        return("Hello 🙁 Goodbye 🙂")
    elif emoticon == "Goodbye :(":
        return("Goodbye 🙁")
    else:
        return(f"Hello {emoticon}")
def main():
    emoticon = input()
    converted = convert(emoticon)
    print(converted)

main()
input("Press Enter to exit")
