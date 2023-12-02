def sol(part):
    res = 0
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        game_id = 0

        for game in lines:
            game_id += 1
            red_cur = 0
            green_cur = 0
            blue_cur = 0

            sets = []
            bag = game.split(':')[1]
            cur_set = bag.split(';')
            for item in cur_set:
                item.strip()
                cube_set = item.split(', ')
                cubes = []
                for cube in cube_set:
                    cube.strip()
                    cubes.append(cube.strip().split(' '))
                sets.append(cubes)
            for set1 in sets:
                for cube in set1:
                    if cube[1] == 'red':
                        red_cur = red_cur + int(cube[0])
                    if cube[1] == 'green':
                        green_cur = green_cur + int(cube[0])
                    if cube[1] == 'blue':
                        blue_cur = blue_cur + int(cube[0])
            if red_cur <= red_cubes and green_cur <= green_cubes and blue_cur <= blue_cubes:
                res += game_id

    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    # print(sol(2))
