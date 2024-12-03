def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for report in lines:
            levels = report.split(" ")
            levels = int_convert(levels)
            if part == 1:
                levels_asc = sorted(levels)
                levels_des = sorted(levels, reverse=True)
                if not (levels == levels_asc or levels == levels_des):
                    continue
                for i, level in enumerate(levels):
                    if i == 0:
                        continue
                    if 1 <= abs(level - levels[i - 1]) <= 3:
                        if len(levels) == i + 1:
                            res += 1
                        continue
                    break
            if part == 2:
                og_res = res
                levels_asc = sorted(levels)
                levels_des = sorted(levels, reverse=True)
                if levels == levels_asc or levels == levels_des:
                    for i, level in enumerate(levels):
                        if i == 0:
                            continue
                        if 1 <= abs(level - levels[i - 1]) <= 3:
                            if len(levels) == i + 1:
                                res += 1
                            continue
                        break
                if res != og_res:
                    continue

                variations = []
                for i in range(len(levels)):
                    new_list = levels[:i] + levels[i + 1:]
                    variations.append(new_list)
                for var_levels in variations:
                    safe = 0
                    levels_asc = sorted(var_levels)
                    levels_des = sorted(var_levels, reverse=True)

                    # Ascending
                    if var_levels == levels_asc:
                        if step_check(var_levels):
                            safe += 1
                    # Descending
                    elif var_levels == levels_des:
                        if step_check(var_levels):
                            safe += 1
                    if safe > 0:
                        res += 1
                        break
    return res


def int_convert(convert_list):
    for i in range(len(convert_list)):
        convert_list[i] = int(convert_list[i])
    return convert_list


def step_check(var_levels):
    for i, level in enumerate(var_levels):
        if i == 0:
            continue
        if 1 <= abs(level - var_levels[i - 1]) <= 3:
            if len(var_levels) == i + 1:
                return True
            continue
        return False


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
