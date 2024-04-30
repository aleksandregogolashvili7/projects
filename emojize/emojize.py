emojys={
    ":1st_place_medal:" :"🥇", ":money_bag:":"💰", ":candy:":"🍬"
                }

while True:
    input=input("input: ")
    if input in emojys:
        print("output:",emojys[input])
        break
    else:
        continue
