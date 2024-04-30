"""
implement a program that prompts the user
for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42
or (case-insensitively) forty-two or forty two. Otherwise output No.
"""
Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
if Answer == "42" or Answer.lower() == "forty-two" or Answer.lower() == "forty two":
    print("Yes")
else:
    print("No")