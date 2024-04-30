from sys import argv
import csv

if not argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
if len(argv) > 3:
    exit("Too many command-line arguments")
if len(argv) < 3:
    exit("Too few command-line arguments")
else:
    with open(argv[1]) as file:
        csv_file=csv.DictReader(file)
        with open(argv[2], "w", newline="") as File:
            writer=csv.DictWriter(File,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in csv_file:
                full,house=row['name'],row['house']
                last,first=full.split(", ")
                writer.writerow({'first':first,'last':last,'house':house})

























# else:
#     after=[]
#     with open(argv[1], "r") as file:
#         csv_file = csv.reader(file)
#         for line in csv_file:
#             line0 = line[0].split(",")
#             if len(line0) > 1:
#                 after.append(",".join([line0[1],line0[0],line[1]]))

#                 with open(argv[2],"w") as File:

#                     for i in range(len(line)):
#                         paragraph = "\n".join(after)
#                         File.write(str(paragraph))

