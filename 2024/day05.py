def sol(part):
    res = 0
    order_rules = []
    update_orders = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        # Parsing
        for line in lines:
            if line.__contains__("|"):
                order_rule = []
                for item in line.split('|'):
                    order_rule.append(int(item))
                order_rules.append(order_rule)
            elif line.__contains__(","):
                update = []
                for item in line.split(','):
                    update.append(int(item))
                update_orders.append(update)

    wrong_orders = []
    # Update check

    for update_order in update_orders:
        correct = True
        for update in update_order:
            for order_rule in order_rules:
                if update == order_rule[0] and update_order.__contains__(order_rule[1]):
                    if update_order.index(update) > update_order.index(order_rule[1]):
                        correct = False
        if correct:
            if part == 1:
                res += update_order[len(update_order) // 2]
        if not correct:
            wrong_orders.append(update_order)

    if part == 2:
        for update_order in wrong_orders:
            while True:
                swapped = False
                for rule in order_rules:
                    if rule[0] in update_order and rule[1] in update_order:
                        index_a = update_order.index(rule[0])
                        index_b = update_order.index(rule[1])
                        if index_a > index_b:
                            update_order[index_a], update_order[index_b] = update_order[index_b], update_order[index_a]
                            swapped = True
                            break
                if not swapped:
                    break
            res += update_order[len(update_order) // 2]
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
