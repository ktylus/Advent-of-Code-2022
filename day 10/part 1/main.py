def signal_strength_sum_increase(cycle, register):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * register
    else:
        return 0


if __name__ == "__main__":
    f = open("input.txt", "r")

    cycle = 1
    register = 1
    signal_strength_sum = 0
    for line in f:
        command = line.replace("\n", "").split(" ")
        if command[0] == "noop":
            cycle += 1
            signal_strength_sum += signal_strength_sum_increase(cycle, register)
        else: # addx n
            for i in range(2):
                cycle += 1
                if i == 1:
                    register += int(command[1])
                signal_strength_sum += signal_strength_sum_increase(cycle, register)

    print(signal_strength_sum)
