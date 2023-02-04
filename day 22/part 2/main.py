def parse_commands(line):
    result = []
    single_command = ""
    for i in range(len(line)):
        if line[i] in ["L", "R"]:
            result.append(single_command)
            result.append(line[i])
            single_command = ""
        else:
            single_command += line[i]
    if single_command != "":
        result.append(single_command)
    return result


def get_new_facing(facing, turn):
    facing_sequence = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    index = 0
    for i in range(len(facing_sequence)):
        if facing == facing_sequence[i]:
            index = i
            break
    if turn == "R":
        return facing_sequence[(index + 1) % len(facing_sequence)]
    else:
        return facing_sequence[(index - 1) % len(facing_sequence)]


def get_side_number(row, col):
    if row in range(0, 50) and col in range(50, 100):
        return 1
    if row in range(0, 50) and col in range(100, 150):
        return 2
    if row in range(50, 100):
        return 3
    if row in range(100, 150) and col in range(0, 50):
        return 4
    if row in range(100, 150) and col in range(50, 100):
        return 5
    else:
        return 6


def move(steps, position, facing):
    steps = int(steps)
    for i in range(steps):
        curr_row = position[0]
        curr_col = position[1]
        new_row = position[0] + facing[0]
        new_col = position[1] + facing[1]
        new_facing = facing
        if new_row < column_first_tile_index[curr_col] or \
           new_row > column_last_tile_index[curr_col] or \
           new_col < row_first_tile_index[curr_row] or \
           new_col > row_last_tile_index[curr_row]:
            new_position, new_facing = handle_side_change(curr_row, curr_col, facing)
            new_row = new_position[0]
            new_col = new_position[1]
        if jungle_map[new_row][new_col] == "#":
            break
        position = (new_row, new_col)
        facing = new_facing
    return position, facing


def handle_side_change(curr_row, curr_col, facing):
    if get_side_number(curr_row, curr_col) == 1:
        return handle_cube1(curr_row, curr_col, facing)
    if get_side_number(curr_row, curr_col) == 2:
        return handle_cube2(curr_row, curr_col, facing)
    if get_side_number(curr_row, curr_col) == 3:
        return handle_cube3(curr_row, curr_col, facing)
    if get_side_number(curr_row, curr_col) == 4:
        return handle_cube4(curr_row, curr_col, facing)
    if get_side_number(curr_row, curr_col) == 5:
        return handle_cube5(curr_row, curr_col, facing)
    else:
        return handle_cube6(curr_row, curr_col, facing)


# functions must return (position, facing)
def handle_cube1(curr_row, curr_col, facing):
    if facing == (0, -1):
        return (149 - curr_row, 0), (0, 1)
    if facing == (-1, 0):
        return (curr_col + 100, 0), (0, 1)


def handle_cube2(curr_row, curr_col, facing):
    if facing == (-1, 0):
        return (199, curr_col - 100), (-1, 0)
    if facing == (0, 1):
        return (149 - curr_row, 99), (0, -1)
    if facing == (1, 0):
        return (curr_col - 50, 99), (0, -1)


def handle_cube3(curr_row, curr_col, facing):
    if facing == (0, -1):
        return (100, curr_row - 50), (1, 0)
    if facing == (0, 1):
        return (49, curr_row + 50), (-1, 0)


def handle_cube4(curr_row, curr_col, facing):
    if facing == (0, -1):
        return (149 - curr_row, 50), (0, 1)
    if facing == (-1, 0):
        return (curr_col + 50, 50), (0, 1)


def handle_cube5(curr_row, curr_col, facing):
    if facing == (0, 1):
        return (149 - curr_row, 149), (0, -1)
    if facing == (1, 0):
        return (curr_col + 100, 49), (0, -1)


def handle_cube6(curr_row, curr_col, facing):
    if facing == (0, -1):
        return (0, curr_row - 100), (1, 0)
    if facing == (0, 1):
        return (149, curr_row - 100), (-1, 0)
    if facing == (1, 0):
        return (0, curr_col + 100), (1, 0)


def calculate_score(position, facing):
    facing_sequence = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    index = 0
    for i in range(len(facing_sequence)):
        if facing == facing_sequence[i]:
            index = i
            break
    return 1000 * (position[0] + 1) + 4 * (position[1] + 1) + index


if __name__ == "__main__":

    jungle_map = []
    commands = []
    row_first_tile_index = []
    row_last_tile_index = []
    column_first_tile_index = []
    column_last_tile_index = []
    facing = (0, 1)

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        if line != "" and line[0] in [".", "#", " "]:
            jungle_map.append(line)
        else:
            commands = parse_commands(line)

    max_length = 0
    for row in jungle_map:
        max_length = max(max_length, len(row))

    for i in range(len(jungle_map)):
        jungle_map[i] += (max_length - len(jungle_map[i])) * " "

    for row in jungle_map:
        row_first_tile_index.append(len(row) - len(row.lstrip()))
        row_last_tile_index.append(len(row.rstrip()) - 1)
    for j in range(len(jungle_map[0])):
        first_char_index = -1
        last_char_index = -1
        for i in range(len(jungle_map)):
            if jungle_map[i][j] in [".", "#"]:
                if first_char_index == -1:
                    first_char_index = i
                last_char_index = i
        column_first_tile_index.append(first_char_index)
        column_last_tile_index.append(last_char_index)

    position = (0, row_first_tile_index[0])
    for i, command in enumerate(commands):
        if command.isnumeric():
            position, facing = move(command, position, facing)
        else:
            facing = get_new_facing(facing, command)


    print(calculate_score(position, facing))