# item_list = []

# try:
#     while True:
#         item = input().upper().strip()
#         item_list.append(item)
#         item_list_ABCD=sorted(item_list)

# except EOFError:
#     pass
# for item in item_list_ABCD:
#     item_number=item_list_ABCD.count(item)
#     if item in item_list_ABCD:
#         print(item_number,item)
item_list = []

try:
    while True:
        item = input().upper().strip()
        item_list.append(item)

except EOFError:
    pass

# Count the occurrences of each item
item_counts = {}
for item in item_list:
    item_counts[item] = item_counts.get(item, 0) + 1

# Print the counts and item names
for item, count in sorted(item_counts.items()):
    print(f"{count} {item}")