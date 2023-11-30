stack1 = ["R", "N", "P", "G"]
stack2 = ["T", "J", "B", "L", "C", "S", "V", "H"]
stack3 = ["T", "D", "B", "M", "N", "L"]
stack4 = ["R", "V", "P", "S", "B"]
stack5 = ["G", "C", "Q", "S", "W", "M", "V", "H"]
stack6 = ["W", "Q", "S", "C", "D", "B", "J"]
stack7 = ["F", "Q", "L"]
stack8 = ["W", "M", "H", "T", "D", "L", "F", "V"]
stack9 = ["L", "P", "B", "V", "M", "J", "F"]

stacks = {
    1: stack1,
    2: stack2,
    3: stack3,
    4: stack4,
    5: stack5,
    6: stack6,
    7: stack7,
    8: stack8,
    9: stack9,
}

f = open("input2.txt", "r")
for line in f.readlines():
    line1 = line.strip("move ")
    line2 = line1.strip("\n")
    line3 = line2.split(' from ')
    l = [line3[0], line3[1].split(' to ')[0], line3[1].split(' to ')[1]]

    from_stack = int(l[1])
    to_stack = int(l[2])

    for i in range(0, int(l[0])):
        item = stacks[from_stack].pop()
        stacks[to_stack].append(item)

    print(l)

string = ""
for stack in stacks.values():
    string += stack[-1]

print(string)