text = input("camelCase: ")
camel = ""
for c in text:
    if c.isupper():
        camel += "_" + c.lower()
    else:
        camel += c

print("snake_case: " + camel)