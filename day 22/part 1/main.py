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


def move(steps, position):
    steps = int(steps)
    for i in range(steps):
        new_row = position[0] + facing[0]
        new_column = position[1] + facing[1]
        if new_row < column_first_tile_index[position[1]]:
            new_row = column_last_tile_index[position[1]]
        elif new_row > column_last_tile_index[position[1]]:
            new_row = column_first_tile_index[position[1]]
        elif new_column > row_last_tile_index[position[0]]:
            new_column = row_first_tile_index[position[0]]
        elif new_column < row_first_tile_index[position[0]]:
            new_column = row_last_tile_index[position[0]]
        if jungle_map[new_row][new_column] == "#":
            break
        position = (new_row, new_column)
    return position


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
            position = move(command, position)
        else:
            facing = get_new_facing(facing, command)


    print(calculate_score(position, facing))