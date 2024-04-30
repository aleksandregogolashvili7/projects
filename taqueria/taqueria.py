def main():
    menu={
"Baja Taco": 4.00,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
    }
    total=0
    try:
        # order=input("Iteam: ").strip().lower().title()


        while True:
            order=input("Iteam: ").strip().lower().title()

            while order not in menu:
                order=input("Iteam: ").strip().lower().title()
                continue
            total=total+float(menu[order])

            print(f"Total: ${total:.2f}")

    except (EOFError, KeyError):
        pass
main()
