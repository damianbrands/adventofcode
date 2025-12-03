def sol(part):
    start_int = 50
    res = 0
    list1 = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            list1.append([line[:1], int(line[1:])])
        if part == 1:
            for i in list1:
                if i[0] == 'L':
                    start_int -= i[1]
                else:
                    start_int += i[1]
                while start_int > 99:
                    start_int -= 100
                while start_int < 0:
                    start_int += 100
                if start_int == 0:
                    res += 1
        if part == 2:
            for i in list1:
                if i[0] == 'L':
                    for i in range(i[1]):
                        start_int -= 1
                        if start_int == 0:
                            res += 1
                        if start_int == -1:
                            start_int = 99
                else:
                    for i in range(i[1]):
                        start_int += 1
                        if start_int == 0:
                            res += 1
                        if start_int == 100:
                            res += 1
                            start_int = 0
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
