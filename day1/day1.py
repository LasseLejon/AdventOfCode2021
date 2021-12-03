f = open(r"C:\Users\Thinkpad\AoC21\day1\input.txt")
rows = f.readlines()


""" number_of_times_greater_depth = 0
previous_depth = int(rows[0])
for row in rows:
    if int(row) > previous_depth:
        number_of_times_greater_depth += 1
    previous_depth = int(row) """

#print(number_of_times_greater_depth)


sum_of_depth = []
for i in range(len(rows)):
    if (i + 2) < len(rows):
        sum_of_depth.append(int(rows[i]))
        sum_of_depth[i] += int(rows[i + 1])
        sum_of_depth[i] += int(rows[i + 2])
print(sum_of_depth)


number_of_times_greater_depth = 0
for i in range(len(sum_of_depth) - 1):
    if sum_of_depth[i] < sum_of_depth[i + 1]:
        number_of_times_greater_depth += 1
print(number_of_times_greater_depth)
