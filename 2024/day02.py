def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for report in lines:
            levels = report.split(" ")
            levels = intConvert(levels)
            if part == 1:
                levels_asc = sorted(levels)
                levels_des = sorted(levels, reverse=True)
                if not (levels == levels_asc or levels == levels_des):
                    continue
                for i, level in enumerate(levels):
                    if i == 0:
                        continue
                    if 1 <= abs(level - levels[i - 1]) <= 3:
                        if len(levels) == i + 1:
                            res += 1
                        continue
                    break
    return res

def intConvert(convertlist):
    for i in range(len(convertlist)):
        convertlist[i] = int(convertlist[i])
    return convertlist


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))