import re
from _operator import itemgetter

def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        words = {
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
            if part == 1:
                end_values = []
                for char in line:
                    if char.isdigit():
                        end_values.append(char)
                if len(end_values) > 0:
                    res = res + int(str(end_values[0]) + str(end_values[-1]))
            if part == 2:
                calibration_values = []
                for number in numbers:
                    for i, letter in enumerate(line):
                        if letter.isdigit():
                            if int(letter) == number:
                                calibration_values.append([int(letter), i])
                for key in words:
                    indexes = [m.start() for m in re.finditer(key, line)]
                    if len(indexes) > 0:
                        for index in indexes:
                            calibration_values.append([words[key], index])
                sorted_list = sorted(calibration_values, key=itemgetter(1))
                final_list = []
                for i in range(len(sorted_list)):
                    final_list.append(sorted_list[i][0])
                if len(final_list) > 0:
                    res = res + int(str(final_list[0]) + str(final_list[-1]))
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
