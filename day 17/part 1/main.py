def print_board():
    for i in range(len(board) - 1, 0, -1):
        print(board[i])
    print(board[0])


def can_replace_rock(rock):
    for point in rock:
        if board[point[0]][point[1]] in ["|", "#", "-"]:
            return False
    return True


def get_jet():
    return jets[current_jet[0] % len(jets)]


def simulate_first_rock():
    h = max_height[0] + 4
    rock = [(h, 3), (h, 4), (h, 5), (h, 6)]
    simulate_rock(rock)

def simulate_second_rock():
    h = max_height[0] + 4
    rock = [(h + 2, 4), (h + 1, 3), (h + 1, 4), (h + 1, 5), (h, 4)]
    simulate_rock(rock)

def simulate_third_rock():
    h = max_height[0] + 4
    rock = [(h + 2, 5), (h + 1, 5), (h, 3), (h, 4), (h, 5)]
    simulate_rock(rock)

def simulate_fourth_rock():
    h = max_height[0] + 4
    rock = [(h + 3, 3), (h + 2, 3), (h + 1, 3), (h, 3)]
    simulate_rock(rock)

def simulate_fifth_rock():
    h = max_height[0] + 4
    rock = [(h + 1, 3), (h + 1, 4), (h, 3), (h, 4)]
    simulate_rock(rock)


def simulate_rock(rock):
    is_falling = True
    while is_falling:
        jet = get_jet()
        if jet == ">":
            next_rock = []
            for point in rock:
                next_rock.append((point[0], point[1] + 1))
        else:
            next_rock = []
            for point in rock:
                next_rock.append((point[0], point[1] - 1))
        if can_replace_rock(next_rock):
            rock = next_rock
        next_rock = []
        for point in rock:
            next_rock.append((point[0] - 1, point[1]))
        if can_replace_rock(next_rock):
            rock = next_rock
        else:
            is_falling = False
        current_jet[0] += 1

    for point in rock:
        board[point[0]][point[1]] = "#"
        if point[0] > max_height[0]:
            max_height[0] = point[0]


if __name__ == "__main__":
    f = open("input2.txt", "r")
    jets = f.read()

    current_jet = [0]
    max_height = [0]
    board = [list('+-------+')]
    for i in range(5000):
        board.append(list('|.......|'))

    for i in range(2022):
        if i % 5 == 0:
            simulate_first_rock()
        if i % 5 == 1:
            simulate_second_rock()
        if i % 5 == 2:
            simulate_third_rock()
        if i % 5 == 3:
            simulate_fourth_rock()
        if i % 5 == 4:
            simulate_fifth_rock()
    print(max_height)
