import time  # import for time calculation

start_time = time.time()  # start the clock

# open the textfile
with open('Euler_022.txt') as file:
    lines = file.readlines()

# separate each name with comma (,)
names = sorted(lines[0].split(','))

total = 0

for loc in range(0, len(names)):
    person = list(names[loc])
    name_array = []

    for index in range(1, len(names[loc]) - 1):
        value = ord(person[index]) - 64
        name_array.append(value)

    output = sum([x for x in name_array]) * (loc + 1)
    total = output + total

print(total)

print("--- %s seconds ---" % (time.time() - start_time))
