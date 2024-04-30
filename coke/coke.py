coin_left=50
while True:
    print(f"Amount Due: {coin_left}")
    coin=int(input("Insert coin: "))
    valid_coin=[25,10,5]
    while coin not in valid_coin:
        print(f"Amount Due: {coin_left}")
        coin=int(input("Insert coin: "))
        valid_coin=[25,10,5]
        continue

    coin_left-=coin
    if coin_left<=0:
        print(f"Change Owed: {abs(coin_left)}")
        break
    else:
        continue
