import math

def total_number_of_items(monkeys_items):
    total = 0
    for i in range(len(monkeys_items)):
        total += len(monkeys_items[i])
    return total


if __name__ == "__main__":
    monkeys_items = [[]]
    monkeys_operations = []
    monkeys_tests = []
    monkeys_throws = []

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        if line == "":
            monkeys_items.append([])
        if line.startswith("  Starting"):
            items = line.split(", ")
            items[0] = items[0].split(": ")[1]
            for item in items:
                monkeys_items[-1].append(int(item))
        if line.startswith("  Operation"):
            monkeys_operations.append((line.split(" ")[-2], line.split(" ")[-1]))
        if line.startswith("  Test"):
            monkeys_tests.append(int(line.split(" ")[-1]))
        if line.startswith("    If true"):
            throw = ("", "")
            throw = (line.split(" ")[-1], "")
        if line.startswith("    If false"):
            throw = (throw[0], line.split(" ")[-1])
            monkeys_throws.append(throw)

    monkeys_inspections = [0] * len(monkeys_items)

    for round in range(10000):
        for i in range(len(monkeys_items)):
            l = len(monkeys_items[i])
            for j in range(l):
                item = monkeys_items[i].pop(0)
                item = int(item)
                monkeys_inspections[i] += 1
                if monkeys_operations[i][1] == "old":
                    if monkeys_operations[i][0] == "+":
                        item = 2 * item
                    else:
                        item = item * item
                else:
                    if monkeys_operations[i][0] == "+":
                        item += int(monkeys_operations[i][1])
                    else:
                        item *= int(monkeys_operations[i][1])
                item = item // 3
                if item % monkeys_tests[i] == 0:
                    monkeys_items[int(monkeys_throws[i][0])].append(item)
                else:
                    monkeys_items[int(monkeys_throws[i][1])].append(item)

    print(monkeys_inspections[-1] * monkeys_inspections[-2])