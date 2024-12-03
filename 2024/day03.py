import re

def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            if part == 1:
                print(line)
                search_list = re.findall(r"mul\(\d+,\d+\)", line)
                clean_list = []
                for mul in search_list:
                    digits = (mul.lstrip("mul(").rstrip(")")).split(',')
                    digits_but_ints = [int(x) for x in digits]
                    clean_list.append(digits_but_ints)
                for multiply_ints in clean_list:
                    res += multiply_ints[0] * multiply_ints[1]
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))