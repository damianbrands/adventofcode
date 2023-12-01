def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        print(lines)
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
