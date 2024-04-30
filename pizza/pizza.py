import sys
import csv
from tabulate import tabulate

try:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    if len(sys.argv) != 2:
        sys.exit("Invalid number of command-line arguments")

    file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        table=[]
        header=[]
        a=csv.reader(file)
        i=0
        for line in a:
            if i==0:
                header=line
                i+=1
            else:
                table.append(line)

        print(tabulate(table,header,tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid command-line arguments")

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        table = list(csv_reader)
        header = table.pop(0)
        print(tabulate(table, header, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")