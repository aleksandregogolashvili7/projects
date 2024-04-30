import validators
try:
    email_harvard = input("What's your email address? ")

    username, domain = email_harvard.split("@")
    if validators.email(email_harvard) and domain == "harvard.edu" or domain == "cs50.harvard.edu":
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    print("Invalid")




# def main():
#     print(validation(input("What's your email address? ")))
# def validation(Email):
#     matches=re.match(r"^\w+@{1}harvard{1}\.{1}edu$",Email)
#     if matches:
#         return "valid"
#     else:
#         return "invalid"
# main()
