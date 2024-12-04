def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        grid = []
        for line in lines:
            grid.append(list(line))
        if part == 1:
            locations = search(grid, "XMAS")
            res += len(locations)
        if part == 2:
            locations = search_mas(grid, "MAS")
            locations.sort()
            final_loc = []
            for location in locations:
                if locations.count(location) > 1:
                    final_loc.append(location)
            res += int(len(final_loc) / 2)
        return res

def search_mas(grid, word):
    directions = {
        "diagonal-up-left": (-1, -1),
        "diagonal-up-right": (-1, 1),
        "diagonal-down-left": (1, -1),
        "diagonal-down-right": (1, 1)
    }
    locations = []
    width = len(grid)
    height = len(grid[0])

    for x in range(width):
        for y in range(height):
            if grid[x][y] == word[0]:
                for dirX, dirY in directions.values():
                    if find_word(grid, width, height, word, 0, x, y, dirX, dirY):
                        locations.append([x + dirX, y + dirY])
    return locations


def search(grid, word):
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
        "diagonal-up-left": (-1, -1),
        "diagonal-up-right": (-1, 1),
        "diagonal-down-left": (1, -1),
        "diagonal-down-right": (1, 1)
    }
    locations = []
    width = len(grid)
    height = len(grid[0])

    for x in range(width):
        for y in range(height):
            if grid[x][y] == word[0]:
                for dirX, dirY in directions.values():
                    if find_word(grid, width, height, word, 0, x, y, dirX, dirY):
                        locations.append([x, y])
    return locations


def find_word(grid, width, height, word, index, x, y, dirX, dirY):
    if index == len(word):
        return True

    if is_valid(x, y, width, height) and word[index] == grid[x][y]:
        return find_word(grid, width, height, word, index + 1, x + dirX, y + dirY, dirX, dirY)
    return False


def is_valid(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
