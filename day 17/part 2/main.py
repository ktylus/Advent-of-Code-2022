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

    # jak znalezc cykle:

    #if current_jet[0] % len(jets) == 4:
    #    print(max_height)
    #if current_jet[0] % len(jets) == 1:
    #    print(max_height)


if __name__ == "__main__":
    f = open("input2.txt", "r")
    jets = f.read()

    current_jet = [0]
    max_height = [0]
    board = [list('+-------+')]
    for i in range(500000):
        board.append(list('|.......|'))

    for i in range(100000):
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
        #if max_height[0] % 2647 == 11:
        #    print((max_height, i))
        #if i == 30160:
        #    print(max_height)
        if max_height[0] % 53 == 42:
            print((max_height, i))
        if i == 120:
            print(max_height)
    print(max_height)


    #202200 iteracji:   313002
    #20220:             31307
    #2022:              3133

    #1000:              1568
    #10000:             15488
    #100000:            154818
    #1000000:           1547958 - brak wyników w current_jet[0] % len(jets) == 0


    #co 1710 iteracji max_height wzrasta o 2647 (od pewnego punktu startowego, mozemy przyjac i = 29072, height = 45010
    #szukamy wysokosci po 1000000000000 iteracjach
    #zatem liczymy:
    x = ((1000000000000 - 29072) // 1710) * 2647 + 45010
    print((1000000000000 - 29072) % 1710) # -> 1088 zatem od punktu startowego musimy jeszcze wykonac 1088 iteracji i sprawdzic
                                          # o ile zwieksza to wysokosc -> obliczono 1696

    x += 1696 # -> 1547953171384 - zla odpowiedz (za malo)
    print(x - 1)


    '''#dla przykladowego inputu:

    #co 35 iteracji wysokosc wzrasta o 53 (od i = 92, height = 148)
    #zatem liczymy:
    x = ((1000000000000 - 92) // 35) * 53 + 148
    additional = (1000000000000 - 92) % 35 # zatem jeszcze 28 iteracji od pkt startowego -> policzono wzrost o 37
    print(x)
    print(additional)

    x += 37
    print(x)'''
