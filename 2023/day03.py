import re


def check(num_cur, num_last, symbol_cur, symbol_last):
    yes_numbers = {}
    for number in num_cur:
        number_indexes = [*range(number[1], number[1] + len(str(number[0])), 1)]
        checker = True
        for symbol in symbol_last:
            for index in number_indexes:
                if symbol[1] - 1 == index or symbol[1] == index or symbol[1] + 1 == index:
                    checker = False
        if not checker:
            yes_numbers[int(number[0])] = number[1]
    for number in num_last:
        number_indexes = [*range(number[1], number[1] + len(str(number[0])), 1)]
        checker = True
        for symbol in symbol_cur:
            for index in number_indexes:
                if symbol[1] - 1 == index or symbol[1] == index or symbol[1] + 1 == index:
                    checker = False
        if not checker:
            yes_numbers[int(number[0])] = number[1]
    return yes_numbers


def sol(part):
    first_loop = True
    not_these = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        last_line_numbers = []
        last_line_symbols = []
        for line in lines:
            current_line_numbers = []
            current_line_symbols = []
            line_numbers = re.findall(r'\d+', line)
            line_symbols = re.findall(r'[^.]+', line)
            filtered_list = [item for item in line_symbols if not item.isdigit()]
            line_symbols = filtered_list
            for sym in line_symbols:
                if len(str(sym)) > 1:
                    num = re.sub(r'\D', '', sym)
                    not_these.append(int(num))
            for number in line_numbers:
                index = line.rfind(number)
                current_line_numbers.append([number, index])
            for symbol in line_symbols:
                index = line.rfind(symbol)
                current_line_symbols.append([symbol, index])
            if not first_loop:
                not_numbers = check(current_line_numbers,
                                    last_line_numbers,
                                    current_line_symbols,
                                    last_line_symbols)
                for num in not_numbers:
                    not_these.append(num)
            first_loop = False
            last_line_numbers = current_line_numbers
            last_line_symbols = current_line_symbols
        print(not_these)
    res = sum(not_these)
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    # print(sol(2))
