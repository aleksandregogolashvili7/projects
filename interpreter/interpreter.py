# Prompt user for input
expression = input("Enter an arithmetic expression (in the form 'x y z'): ")

# Split the input into three parts: x, y, and z
x, y, z = expression.split()

# Convert x and z to integers
x = int(x)
z = int(z)

# Calculate the result based on the operator
if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z

# Print the result formatted to one decimal place
print(f"{result:.1f}")
