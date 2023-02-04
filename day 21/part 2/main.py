def evaluate(name):
    if name in number_monkeys.keys():
        return number_monkeys[name]
    calculation = calculating_monkeys[name]
    monkey1 = calculation.split(" ")[0]
    monkey2 = calculation.split(" ")[2]
    operation = calculation.split(" ")[1]
    if operation == "+":
        return evaluate(monkey1) + evaluate(monkey2)
    if operation == "-":
        return evaluate(monkey1) - evaluate(monkey2)
    if operation == "*":
        return evaluate(monkey1) * evaluate(monkey2)
    if operation == "/":
        return evaluate(monkey1) / evaluate(monkey2)


def check_for_humn(root):
    if root == "humn":
        return True
    if root in number_monkeys.keys():
        return False
    return check_for_humn(calculating_monkeys[root].split(" ")[0]) or check_for_humn(calculating_monkeys[root].split(" ")[2])


def calculate_humn(root, wanted_number):
    left = calculating_monkeys[root].split(" ")[0]
    if left == "humn":
        return calculate_wanted_number_in_left_node(wanted_number, root)
    else:
        return calculate_wanted_number_in_right_node(wanted_number, root)


def calculate_wanted_number_in_left_node(wanted_number, root):
    operation = calculating_monkeys[root].split(" ")[1]
    right = calculating_monkeys[root].split(" ")[2]
    if operation == "+":
        return wanted_number - evaluate(right)
    if operation == "-":
        return wanted_number + evaluate(right)
    if operation == "*":
        return wanted_number / evaluate(right)
    if operation == "/":
        return wanted_number * evaluate(right)


def calculate_wanted_number_in_right_node(wanted_number, root):
    operation = calculating_monkeys[root].split(" ")[1]
    left = calculating_monkeys[root].split(" ")[0]
    if operation == "+":
        return wanted_number - evaluate(left)
    if operation == "-":
        return evaluate(left) - wanted_number
    if operation == "*":
        return wanted_number / evaluate(left)
    if operation == "/":
        return evaluate(left) / wanted_number


def part2(root, wanted_number):
    left = calculating_monkeys[root].split(" ")[0]
    right = calculating_monkeys[root].split(" ")[2]
    if left == "humn" or right == "humn":
        return calculate_humn(root, wanted_number)
    if root == "root":
        if check_for_humn(left):
            return part2(left, evaluate(right))
        else:
            return part2(right, evaluate(left))
    else:
        if check_for_humn(left):
            return part2(left, calculate_wanted_number_in_left_node(wanted_number, root))
        else:
            return part2(right, calculate_wanted_number_in_right_node(wanted_number, root))


if __name__ == "__main__":

    number_monkeys = {}
    calculating_monkeys = {}

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        name = line.split(": ")[0]
        calculation = line.split(": ")[1]
        if calculation.isnumeric():
            number_monkeys[name] = int(calculation)
        else:
            calculating_monkeys[name] = calculation

    print(part2("root", 0))

