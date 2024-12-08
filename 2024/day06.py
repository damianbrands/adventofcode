def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        grid = []
        start_coords = []
        current_coords = []
        direction = "up"
        for x, line in enumerate(lines):
            temp_list = []
            line = list(line)
            for y, character in enumerate(line):
                if character == '^':
                    start_coords = [x, y]
                    current_coords = [x, y]
                    temp_list.append(['.', 1])
                else:
                    temp_list.append([character, 0])
            grid.append(temp_list)
        while True:
            result = step(grid, current_coords, direction)
            if result is None:
                break
            grid, current_coords, direction = result
        for row in grid:
            for col in row:
                if col[1] == 1:
                    res += 1
        return res

def inbounds(grid, current_coords):
    return -1 < current_coords[0] < len(grid) and -1 < current_coords[1] < len(grid[0])


def step(grid, current_coords, direction):
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
    }
    direction_order = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up",
    }
    og_x = current_coords[0]
    og_y = current_coords[1]


    for i in range(4):
        x_movement = directions[direction][0]
        y_movement = directions[direction][1]
        new_coords = [og_x + x_movement, og_y + y_movement]

        if inbounds(grid, new_coords):
            next_pos = grid[new_coords[0]][new_coords[1]]
            if next_pos[0] == '.':
                grid[new_coords[0]][new_coords[1]] = ['.', 1]
                return [grid, new_coords, direction]
            direction = direction_order[direction]
    return None


if __name__ == "__main__":
    print(sol(1))
