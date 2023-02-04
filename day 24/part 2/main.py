import collections
import sys

sys.setrecursionlimit(2000)


def simulate_blizzard(blizzard):
    row, col, direction = blizzard
    if direction == "^":
        if row == 1:
            row = height - 2
        else:
            row -= 1
    elif direction == ">":
        if col == width - 2:
            col = 1
        else:
            col += 1
    elif direction == "v":
        if row == height - 2:
            row = 1
        else:
            row += 1
    else:
        if col == 1:
            col = width - 2
        else:
            col -= 1
    return row, col, direction


states = set()
result = [9999]
steps_when_entered = collections.defaultdict(int)


def solution(current_position, end, step):
    if current_position == end:
        result[0] = min(result[0], step)
        return
    if step > result[0] or step > 1900:
        return
    row, col = current_position
    states.add((row, col, step % len(all_blizzards)))
    steps_when_entered[(row, col, step % len(all_blizzards))] = step
    step += 1

    if (row - 1, col) not in all_blizzards[step % len(all_blizzards)]:
        if (row - 1, col) == end:
            solution((row - 1, col), end, step)
        elif row - 1 > 0 and ((row - 1, col, step % len(all_blizzards)) not in states or step < steps_when_entered[
            (row - 1, col, step % len(all_blizzards))]):
            solution((row - 1, col), end, step)
    if (row, col + 1) not in all_blizzards[step % len(all_blizzards)] and col + 1 < width - 1 and row in range(1,
                                                                                                               height - 1) and (
            (row, col + 1, step % len(all_blizzards)) not in states or step < steps_when_entered[
        (row, col + 1, step % len(all_blizzards))]):
        solution((row, col + 1), end, step)
    if (row + 1, col) not in all_blizzards[step % len(all_blizzards)]:
        if (row + 1, col) == end:
            solution((row + 1, col), end, step)
        elif ((row + 1, col, step % len(all_blizzards)) not in states or step < steps_when_entered[
            (row + 1, col, step % len(all_blizzards))]) and row + 1 < height - 1:
            solution((row + 1, col), end, step)
    if (row, col - 1) not in all_blizzards[step % len(all_blizzards)] and col - 1 > 0 and row < height - 1 and (
            (row, col - 1, step % len(all_blizzards)) not in states or step < steps_when_entered[
        (row, col - 1, step % len(all_blizzards))]):
        solution((row, col - 1), end, step)
    if (row, col) not in all_blizzards[step % len(all_blizzards)] and (
            (row, col, step % len(all_blizzards)) not in states or step < steps_when_entered[
        (row, col, step % len(all_blizzards))]):
        solution((row, col), end, step)


if __name__ == "__main__":

    blizzards = set()
    width = 0
    height = 0

    f = open("input.txt", "r")
    for index, line in enumerate(f):
        line = line.replace("\n", "")
        width = len(line)
        height += 1
        for char_index, char in enumerate(line):
            if char in ["^", ">", "v", "<"]:
                blizzards.add((index, char_index, char))

    all_blizzards = []
    for i in range(9999):
        if i > 0 and blizzards == all_blizzards[0]:
            break
        all_blizzards.append(blizzards)
        new_blizzards_set = set()
        for blizzard in blizzards:
            new_blizzards_set.add(simulate_blizzard(blizzard))
        blizzards = new_blizzards_set
    new_all_blizzards = []
    for blizzard_set in all_blizzards:
        blizzards_without_direction = set([x[:-1] for x in blizzard_set])
        new_all_blizzards.append(blizzards_without_direction)
    all_blizzards = new_all_blizzards
    print(len(all_blizzards))

    start_location = (0, 1)
    end_location = (height - 1, width - 2)
    current_location = start_location

    solution(start_location, end_location, 0)
    steps1 = result[0]
    result = [9999]
    states = set()
    steps_when_entered = collections.defaultdict(int)

    solution(end_location, start_location, steps1)
    steps2 = result[0]
    result = [9999]
    states = set()
    steps_when_entered = collections.defaultdict(int)

    solution(start_location, end_location, steps2)
    print(result)
