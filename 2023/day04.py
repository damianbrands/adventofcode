def sol(part):
    res = 0
    wins = []
    cards = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        for j, line in enumerate(lines):
            numbers = line.split(':')[1]
            winning = numbers.strip().split('|')[0].split()
            yours = numbers.strip().split('|')[1].split()
            won_numbers = []
            multiplier = 0

            for i in range(len(winning)):
                winning[i] = int(winning[i])
            for i in range(len(yours)):
                yours[i] = int(yours[i])

            for item in yours:
                if item in winning:
                    won_numbers.append(item)
            if part == 2:
                for i in range(len(won_numbers)):
                    multiplier += 1
                wins.append(multiplier)
            if part == 1:
                for i in range(len(won_numbers)):
                    if multiplier == 0:
                        multiplier += 1
                    else:
                        multiplier = multiplier * 2
                res += multiplier
    if part == 2:
        for i in range(len(wins)):
            cards.append(1)
        for j, win in enumerate(wins):
            for k in range(cards[j]):
                for i in range(1, win + 1):
                    cards[j + i] += 1
        res = sum(cards)
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
