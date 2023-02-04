def print_tiles(tiles):
    for i in range(15):
        for j in range(490, 510):
            print(tiles[i][j], end="")
        print()

# returns y value of sand at the end of the simulation
def simulate_sand_unit():
    x = 500
    y = 0
    while True:
        if tiles[y + 1][x - 1] in blocks and tiles[y + 1][x] in blocks and tiles[y + 1][x + 1] in blocks:
            tiles[y][x] = "o"
            return y
        if tiles[y + 1][x] not in blocks:
            y += 1
        elif tiles[y + 1][x - 1] not in blocks:
            x -= 1
            y += 1
        elif tiles[y + 1][x + 1] not in blocks:
            x += 1
            y += 1



if __name__ == "__main__":
    n = 1000
    blocks = ["#", "o"]
    tiles = [["." for i in range(n)] for j in range(n)]
    max_y = 0

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            cur_x = int(points[i].split(",")[0])
            cur_y = int(points[i].split(",")[1])
            next_x = int(points[i+1].split(",")[0])
            next_y = int(points[i+1].split(",")[1])
            max_y = max(cur_y, next_y, max_y)
            if cur_y == next_y and cur_x <= next_x:
                while cur_x <= next_x:
                    tiles[cur_y][cur_x] = "#"
                    cur_x += 1
            elif cur_y == next_y and cur_x >= next_x:
                while cur_x >= next_x:
                    tiles[cur_y][cur_x] = "#"
                    cur_x -= 1
            elif cur_x == next_x and cur_y <= next_y:
                while cur_y <= next_y:
                    tiles[cur_y][cur_x] = "#"
                    cur_y += 1
            elif cur_x == next_x and cur_y >= next_y:
                while cur_y >= next_y:
                    tiles[cur_y][cur_x] = "#"
                    cur_y -= 1
        tiles[0][500] = "+"
    for i in range(1000):
        tiles[max_y + 2][i] = "#"

    sand_units = 0
    while tiles[0][500] != "o":
        simulate_sand_unit()
        sand_units += 1

    print(sand_units)
