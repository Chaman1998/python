items = ["apple", "banana", "orange", "mango", "mango"]

uniqe_item = set()

for item in items:
    if item in uniqe_item:
        print("Dublicate: ", item)
        break
    uniqe_item.add(item)