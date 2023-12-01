def sol(part):
    id_lol = 0
    res = 0
    with open("../input.txt") as file:
        # for line in file:
        lines = file.read().strip().split('\n')
        dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }
        for line in lines:
            print(line)
            value = ""
            valdict = {}
            val = []
            if part == 2:
                for c in line:
                    if c.isdigit():
                        index = line.find(c)
                        if index != -1:
                            valdict[id_lol] = [int(c), index]
                            id_lol = id_lol + 1
                for key in dict:
                    index = line.find(key)
                    if index != -1:
                        valdict[id_lol] = [dict[key], index]
                        id_lol = id_lol + 1

                # for i in line:
                #     value = value + str(i)
                #     print(i)
                #     print(value)
                #     for key in dict:
                #         if key in value:
                #             value = value.replace(key, str(dict[key]))
                # for char in line:
                #     value = value + (str(char))
                #     for key in dict:
                #         if key in value:
                #             value = value.replace(key, str(dict[key]))
            print(valdict)
            print(sorted(valdict.items(), key=lambda item: item[1][1]))
            sorted_list = sorted(valdict.items(), key=lambda item: item[1][1])
            print(sorted_list)
            new_list = []
            for i in range(len(sorted_list)):
                new_list.append(sorted_list[i][1][0])
            print(new_list)
            # print(str(sorted_list[1][0]))
            # print(str(sorted_list[1][-1]))
            if part == 2:
                if len(new_list) > 0:
                    print(int(str(new_list[0]) + str(new_list[-1])))
                    res = res + int(str(new_list[0]) + str(new_list[-1]))
            if part == 1:
                for char in value:
                    if char.isdigit():
                        val.append(char)
                if len(val) > 0:
                    print(int(str(val[0]) + str(val[-1])))
                    res = res + int(str(val[0]) + str(val[-1]))
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
