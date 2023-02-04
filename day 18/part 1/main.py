if __name__ == "__main__":

    cubes = set()

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        z = int(line.split(",")[2])
        cubes.add((x, y, z))

    surface_area = 0
    for cube in cubes:
        surface_area += 6
        x = cube[0]
        y = cube[1]
        z = cube[2]
        neighboring_tiles = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        for tile in neighboring_tiles:
            if tile in cubes:
                surface_area -= 1

    print(surface_area)