import re


def make_grid(lines):
    grid = []
    for row in lines:
        grid_row = []
        for i in range(len(row)):
            grid_row.append(row[i])
        grid.append(grid_row)
    return grid


def get_numbers(lines):
    numbers_per_row = []
    for i, row in enumerate(lines):
        numbers = re.findall(r'\d+', row)
        indexes = list(re.finditer(r'\d+', row))
        num_i = []
        for j in range(len(numbers)):
            num_i.append([numbers[j], indexes[j].start(0), indexes[j].end(0) - 1])
        numbers_per_row.append(num_i)
    return numbers_per_row


def sol(part):
    special_characters = ""
    if part == 1:
        special_characters = "!@#$%^&*()-+?_=,<>/"
    else:
        special_characters = "*"
    res = 0
    number_dict = {}
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        grid = make_grid(lines)
        numbers = get_numbers(lines)
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char in special_characters:
                    found_boys = {}
                    for i in range(-1, 2):
                        looking_y = y + i
                        for j in range(-1, 2):
                            for number in numbers[looking_y]:
                                if (x - 1 <= number[1] <= x + 1) or (x - 1 <= number[2] <= x + 1):
                                    if part == 1:
                                        number_dict[number[1], looking_y] = int(number[0])
                                    else:
                                        found_boys[number[1], looking_y] = int(number[0])
                    if len(found_boys) == 2 and part == 2:
                        lijstje = []
                        for key in found_boys:
                            lijstje.append(found_boys[key])
                        res += lijstje[0] * lijstje[1]
        if part == 1:
            for key in number_dict:
                res += number_dict[key]
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
