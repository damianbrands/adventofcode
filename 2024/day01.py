def sol(part):
    res = 0
    list1 = []
    list2 = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            input_nr = line.split("   ")
            list1.append(int(input_nr[0]))
            list2.append(int(input_nr[1]))
        if part == 1:
            list1.sort()
            list2.sort()
            for i, ix in enumerate(list1):
                res += abs(list1[i - 1] - list2[i - 1])
        if part == 2:
            for i, ix in enumerate(list1):
                res += ix * list2.count(ix)
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
