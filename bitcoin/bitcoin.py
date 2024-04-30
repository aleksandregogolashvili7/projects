from sys import argv
import requests

if len(argv)!=2:
    exit("Command-line argument is not a number")

try:
    bitcoin_num=float(argv[1])
    bit_info=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    # print(bit_info)
    rate=bit_info["bpi"]["USD"]["rate"]
    rate=rate.replace(",","")
    rate=float(rate)
    result=rate*bitcoin_num
    formated_result=format(result,",")
    print(f"${formated_result}")

except ValueError:
    exit("Command-line argument is not a number")
