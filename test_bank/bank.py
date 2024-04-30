def main():
    welcoming = input("greeting: ")
    welcoming=greeting(welcoming)
    # print(f"${welcoming}")
    print(welcoming)
def greeting(greeting):
    greeting=greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
main()
