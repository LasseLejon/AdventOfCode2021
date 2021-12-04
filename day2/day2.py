f = open(r'./input.txt')
rows = f.readlines()

#position = {"horizontal": 0, "depth": 0}

""" 
for row in rows:
    data = row.split()
    direction = data [0]
    value = data[1]
    if direction == "forward":
        position["horizontal"] += int(value)
    if direction == "up":
        position["depth"] -= int(value)
    elif direction == "down":
        position["depth"] += int(value)


print(position["depth"] * position["horizontal"]) """


#part2
position = {"horizontal": 0, "depth": 0}
aim = 0
for row in rows:
    data = row.split()
    direction = data [0]
    value = data[1]
    if direction == "forward":
        position["horizontal"] += int(value)
        if aim > 0:
            position["depth"] += int(value) * aim
    elif direction == "up":
        aim -= int(value)
    elif direction == "down":
        aim += int(value)

print(position["depth"] * position["horizontal"])

