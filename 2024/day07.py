import operator
from itertools import product


def sol(part):
    res = 0
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            full_line = line.split(':')
            answer, pre_split_numbers = full_line
            numbers = pre_split_numbers.strip().split(' ')
            answer = int(answer)
            if part == 1:
                operators = ['+', '*']
            if part == 2:
                operators = ['+', '*', '||']
            operator_combinations = product(operators, repeat=len(numbers) - 1)

            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])

            for operator_list in operator_combinations:
                result = numbers[0]

                for i, operator in enumerate(operator_list):
                    if operator == '+':
                        result += numbers[i + 1]
                    elif operator == '*':
                        result *= numbers[i + 1]
                    elif operator == '||':
                        result = int(str(result) + str(numbers[i + 1]))
                if result == answer:
                    res += answer
                    break
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
