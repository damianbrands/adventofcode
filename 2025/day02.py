import textwrap


def sol(part):
    res = 0
    all_lists = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            for value in line.split(","):
                if value:
                    all_lists.append(value.split("-"))
        if part == 1:
            for list in all_lists:
                for i in range(int(list[0]), int(list[1]) + 1):
                    string_number = str(i)
                    if len(string_number) % 2 == 1:
                        continue
                    if string_number[:len(string_number) // 2] == str(i)[len(string_number) // 2:]:
                        res += i
        if part == 2:
            for list in all_lists:
                for i in range(int(list[0]), int(list[1]) + 1):
                    string_number = str(i)
                    for j in range(1, 6):
                        if all_same(textwrap.wrap(string_number, j)) and j < len(string_number):
                            res += i
                            break
    return res


def all_same(items):
    return all(x == items[0] for x in items)


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
