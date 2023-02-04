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

    print(evaluate("root"))
