counter = 0
contains_counter = 0

f = open("input.txt", "r")
for line in f.readlines():
    line = line.strip('\n')
    lists = line.split(',')

    container1 = []
    container2 = []

    for i in range(int(lists[0].split('-')[0]), int(lists[0].split('-')[-1]) + 1):
        container1.append(i)

    for i in range(int(lists[1].split('-')[0]), int(lists[1].split('-')[-1]) + 1):
        container2.append(i)

    if set(container1).issubset(container2) or set(container2).issubset(container1):
        print(str(container1) + " - " + str(container2))
        counter += 1

    for item in container1:
        if container2.__contains__(item):
            contains_counter += 1
            break

print(counter)
print(contains_counter)
