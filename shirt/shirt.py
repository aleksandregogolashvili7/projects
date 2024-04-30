import sys
from os.path import splitext
from PIL import Image, ImageOps

def main(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    else:
        input = arguments[1]
        output = arguments[2]
        extension1 = splitext(input)[1].lower()
        extension2 = splitext(output)[1].lower()
        allowed_extensions = ['.jpg', '.jpeg', '.png']
        if extension1 in allowed_extensions and extension2 in allowed_extensions:
            if extension1 == extension2:
                try:
                    photo = Image.open(input)
                    shirt = Image.open("shirt.png")
                    size = shirt.size
                    photo = ImageOps.fit(photo, size, bleed=0.0, centering=(0.5, 0.5))
                    photo.paste(shirt,shirt)
                    photo.save(output)

                except FileNotFoundError:
                    sys.exit("Input does not exist")

            else:
                sys.exit("Input and output have different extensions ")
        else:
            sys.exit("Invalid input")

if __name__ == "__main__":
    main(sys.argv)
