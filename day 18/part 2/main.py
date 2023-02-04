import collections

visited = set()   # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.add(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == "__main__":

    cubes = set()

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        z = int(line.split(",")[2])
        cubes.add((x, y, z))

    air_pockets_just_outside = set()
    graph = collections.defaultdict(list)
    just_outside_cube = set()

    for cube in cubes:
        x = cube[0]
        y = cube[1]
        z = cube[2]
        neighboring_tiles = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        for tile in neighboring_tiles:
            if tile not in cubes:
                just_outside_cube.add(tile)

    for tile in just_outside_cube:
        x = tile[0]
        y = tile[1]
        z = tile[2]
        neighboring_tiles = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        for neighbor in neighboring_tiles:
            if neighbor not in cubes:
                graph[tile].append(neighbor)
                graph[neighbor].append(tile)

    added = True
    while added:
        added = False
        new_graph = graph.copy()
        for tile in graph.keys():
            x = tile[0]
            y = tile[1]
            z = tile[2]
            neighboring_tiles = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
            for neighbor in neighboring_tiles:
                if neighbor not in graph[tile] and neighbor not in cubes and neighbor[0] in range(-2, 22) and neighbor[1] in range(-2, 22) and neighbor[2] in range(-2, 22):
                    new_graph[tile].append(neighbor)
                    new_graph[neighbor].append(tile)
                    added = True
        graph = new_graph


    tile_to_reach = (21, 21, 21)
    for tile in just_outside_cube:
        bfs(visited, graph, tile)
        if not tile_to_reach in visited:
            air_pockets_just_outside.add(tile)
        visited = set()
        queue = []


    surface_area = 0
    for cube in cubes:
        surface_area += 6
        x = cube[0]
        y = cube[1]
        z = cube[2]
        neighboring_tiles = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        for tile in neighboring_tiles:
            if tile in cubes or tile in air_pockets_just_outside:
                surface_area -= 1


    print(surface_area)
