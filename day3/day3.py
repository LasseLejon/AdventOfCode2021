f = open(r'./test_input.txt')

rows = f.readlines()
gamma = ""
epsilon = ""

for i in range(5):
    bin = {"1": 0, "0": 0}

    for row in rows:
        if  row[i] == "1":
            bin["1"] += 1
        else:
             bin["0"] += 1

    gamma += max(bin, key=bin.get)
    epsilon += min(bin, key=bin.get) 
    
binArr = []

#fill binArr

for row in rows:
    if row[0] == gamma[0]:
        binArr.append(row)
print(binArr)
