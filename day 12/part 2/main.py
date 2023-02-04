import collections


if __name__ == "__main__":
    tiles = [[]]
    S = ()
    E = ()

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        for c in line:
            if c == "E":
                tiles[-1].append("z")
                E = (len(tiles) - 1, len(tiles[-1]) - 1)
            elif c == "S":
                tiles[-1].append("a")
                S = (len(tiles) - 1, len(tiles[-1]) - 1)
            else:
                tiles[-1].append(c)
        tiles.append([])
    tiles.pop(len(tiles) - 1)

    graph = {}

    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            graph[(i, j)] = []
            if j < len(tiles[0]) - 1 and ord(tiles[i][j+1]) - ord(tiles[i][j]) <= 1:
                graph[(i, j)].append((i, j+1))
            if i < len(tiles) - 1 and ord(tiles[i+1][j]) - ord(tiles[i][j]) <= 1:
                graph[(i, j)].append((i+1, j))
            if i > 0 and ord(tiles[i-1][j]) - ord(tiles[i][j]) <= 1:
                graph[(i, j)].append((i-1, j))
            if j > 0 and ord(tiles[i][j-1]) - ord(tiles[i][j]) <= 1:
                graph[(i, j)].append((i, j-1))

    visited = []
    queue = []
    distances = collections.defaultdict(int)

    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)
        while queue:
            m = queue.pop(0)
            for neighbour in graph[m]:
                if neighbour not in visited:
                    distances[neighbour] = 1 + distances[m]
                    visited.append(neighbour)
                    queue.append(neighbour)

    min_distance = 1000
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            if tiles[i][j] == "a":
                S = (i, j)
                visited = []
                queue = []
                distances = collections.defaultdict(int)
                bfs(visited, graph, S)
                if distances[E] < min_distance and distances[E] > 0:
                    min_distance = distances[E]

    print()
    print(min_distance)
