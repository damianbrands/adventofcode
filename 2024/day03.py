import re


def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        line = ''.join(lines)

        if part == 1:
            search_list = re.findall(r"mul\(\d+,\d+\)", line)
            clean_list = []
            for mul in search_list:
                digits = (mul.lstrip("mul(").rstrip(")")).split(',')
                digits_but_ints = [int(x) for x in digits]
                clean_list.append(digits_but_ints)
            for multiply_ints in clean_list:
                res += multiply_ints[0] * multiply_ints[1]

        if part == 2:
            ultimate_filtered = []
            divided_on_do = line.split("do()")
            for divided_string in divided_on_do:
                if "don't()" in divided_string:
                    ultimate_filtered.append(divided_string.split("don't")[0])
                else:
                    ultimate_filtered.append(divided_string)
            for filtered_line in ultimate_filtered:
                search_list = re.findall(r"mul\(\d+,\d+\)", filtered_line)
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
