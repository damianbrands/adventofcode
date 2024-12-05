def sol(part):
    res = 0
    order_rules = []
    update_orders = []
    with open("../input.txt") as file:
        lines = file.read().strip().split('\n')
        if part == 1:
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
            # Update check
            for update_order in update_orders:
                correct = True
                for update in update_order:
                    for order_rule in order_rules:
                        if update == order_rule[0] and update_order.__contains__(order_rule[1]):
                            if update_order.index(update) > update_order.index(order_rule[1]):
                                correct = False
                if correct:
                    res += update_order[len(update_order) // 2]
    return res


if __name__ == "__main__":
    print(sol(1))
    print("----------------")
    print(sol(2))
