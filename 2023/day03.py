import re

def makeGrid(lines):
    grid = []
    for row in lines:
        grid_row = []
        for i in range(len(row)):
            grid_row.append(row[i])
        grid.append(grid_row)
    return grid


def extract_subgrid(grid, row, col):
    subgrid = []
    for i in range(row - 1, row + 2):
        subgrid_row = []
        for j in range(0, len(grid[0])):
            subgrid_row.append(grid[i][j])
        subgrid.append(subgrid_row)
    return subgrid


def get_numbers(lines):
    numbers_per_row = []
    for i, row in enumerate(lines):
        numbers = re.findall(r'\d+', row)
        indexes = list(re.finditer(r'\d+', row))
        num_i = []
        for j in range(len(numbers)):
            num_i.append([numbers[j], indexes[j].start(0), indexes[j].end(0) - 1])
        print(i, num_i)
        numbers_per_row.append(num_i)
    return numbers_per_row


def sol(part):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    num_characters = "1234567890"
    res = 0
    number_dict = {}  # {[0, 467]: 0, [0, 114]: 5}
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        grid = makeGrid(lines)
        numbers = get_numbers(lines)
        print(numbers)
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char in special_characters:
                    subgrid = extract_subgrid(grid, x, y)
                    for i in range(-1, 2):
                        looking_y = y + i
                        for j in range(-1, 2):
                            looking_x = x + j
                            for number in numbers[looking_y]:
                                # if looking_x == number[1] or looking_x == number[2]:
                                #     number_dict[looking_y, number[0]] = looking_x
                                if (x - 1 <= number[1] <= x + 1) or (x - 1 <= number[2] <= x + 1):
                                    number_dict[number[1], looking_y] = int(number[0])
                    print("---------------")
        print(number_dict)
        for key in number_dict:
            res += number_dict[key]
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    # print(sol(2))
