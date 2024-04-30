def main():
    license_plate = input("Enter the license plate number: ")

    if is_valid_license_plate(license_plate):
        print("Valid license plate")
    else:
        print("Invalid license plate")


def is_valid_license_plate(plate):
    # Check the length of the license plate
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Check if the license plate contains only alphanumeric characters
    if not plate.isalnum():
        return False

    # Check the first two characters are alphabets
    if not plate[:2].isalpha():
        return False

    # Check the third character is not '0'
    if plate[2] == '0':
        return False

    # Check if any digit is present in the center part of the license plate
    center = plate[2:-2]
    if any(char.isdigit() for char in center):
        return False

    return True


if __name__ == "__main__":
    main()