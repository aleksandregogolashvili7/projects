file = input("file name: ").lower().strip()
if file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".zip"):
    print("application/zip")
elif file.endswith(".txt"):
    file=file.split(".")
    print(f"text/{file[0]}")
else:
    print("application/octet-stream")