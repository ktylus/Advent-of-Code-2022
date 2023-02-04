

if __name__ == "__main__":

    sum = 0

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        power = 0
        for char in reversed(line):
            if char == "=":
                sum += (-2) * (5**power)
            elif char == "-":
                sum += (-1) * (5**power)
            elif char == "1":
                sum += 5**power
            elif char == "2":
                sum += 2 * (5**power)
            power += 1

    snafu_result = ""
    power = 0
    while sum > 0:
        remainder = sum % (5**(power + 1))
        if remainder == 0:
            snafu_result += "0"
        elif remainder == 5**power:
            snafu_result += "1"
            sum -= remainder
        elif remainder == 2 * (5**power):
            snafu_result += "2"
            sum -= remainder
        elif remainder == 3 * (5**power):
            snafu_result += "="
            sum += 2 * (5**power)
        elif remainder == 4 * (5**power):
            snafu_result += "-"
            sum += 5**power
        power += 1

    print(snafu_result[::-1])