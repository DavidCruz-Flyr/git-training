with open("./data.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()

for num in data:
    print(num)

with open("./data.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(data))