import collections

if __name__ == "__main__":

    elves_positions = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent_in_direction = {
        (-1, 0): [(-1, -1), (-1, 0), (-1, 1)],
        (1, 0): [(1, 1), (1, 0), (1, -1)],
        (0, -1): [(1, -1), (0, -1), (-1, -1)],
        (0, 1): [(-1, 1), (0, 1), (1, 1)]
    }
    adjacent_tiles = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    f = open("input.txt", "r")
    i = 0
    for line in f:
        line = line.replace("\n", "")
        for j in range(len(line)):
            if line[j] == "#":
                elves_positions.add((i, j))
        i += 1

    rounds = 10
    for i in range(rounds):
        # tile -> list of elves wanting to move there
        proposed_moves = collections.defaultdict(list)
        # first half of the round
        for elf in elves_positions:
            any_neighbors = False
            for tile in adjacent_tiles:
                if (elf[0] + tile[0], elf[1] + tile[1]) in elves_positions:
                    any_neighbors = True
                    break
            if not any_neighbors:
                continue

            for dir in directions:
                allowed_to_move = True
                for pos in adjacent_in_direction[dir]:
                    if (elf[0] + pos[0], elf[1] + pos[1]) in elves_positions:
                        allowed_to_move = False
                if allowed_to_move:
                    proposed_moves[(elf[0] + dir[0], elf[1] + dir[1])].append(elf)
                    break

        # second half of the round
        for tile in proposed_moves.keys():
            if len(proposed_moves[tile]) == 1:
                elves_positions.remove(proposed_moves[tile][0])
                elves_positions.add(tile)

        first_dir = directions.pop(0)
        directions.append(first_dir)


    width = max([x[0] for x in elves_positions]) - min([x[0] for x in elves_positions]) + 1
    height = max([x[1] for x in elves_positions]) - min([x[1] for x in elves_positions]) + 1

    print(width * height - len(elves_positions))
