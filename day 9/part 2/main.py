import math


def is_adjacent(head, tail):
    if abs(head[0] - tail[0]) > 1:
        return False
    if abs(head[1] - tail[1]) > 1:
        return False
    return True

def update_tail_position(head, tail):
    tail_position = []
    tail_position.append(tail[0])
    tail_position.append(tail[1])

    if head[0] == tail[0]:
        if(head[1] > tail[1]):
            tail_position[1] += 1
        else:
            tail_position[1] -= 1
    elif head[1] == tail[1]:
        if(head[0] > tail[0]):
            tail_position[0] += 1
        else:
            tail_position[0] -= 1
    else:
        if(head[0] == tail[0] - 1 and head[1] == tail[1] + 2) or (head[0] == tail[0] - 2 and head[1] == tail[1] + 1):
            tail_position[0] -= 1
            tail_position[1] += 1
        if(head[0] == tail[0] + 1 and head[1] == tail[1] + 2) or (head[0] == tail[0] + 2 and head[1] == tail[1] + 1):
            tail_position[0] += 1
            tail_position[1] += 1
        if(head[0] == tail[0] + 1 and head[1] == tail[1] - 2) or (head[0] == tail[0] + 2 and head[1] == tail[1] - 1):
            tail_position[0] += 1
            tail_position[1] -= 1
        if(head[0] == tail[0] - 1 and head[1] == tail[1] - 2) or (head[0] == tail[0] - 2 and head[1] == tail[1] - 1):
            tail_position[0] -= 1
            tail_position[1] -= 1
        if head[0] == tail[0] + 2 and head[1] == tail[1] + 2:
            tail_position[0] += 1
            tail_position[1] += 1
        if head[0] == tail[0] + 2 and head[1] == tail[1] - 2:
            tail_position[0] += 1
            tail_position[1] -= 1
        if head[0] == tail[0] - 2 and head[1] == tail[1] - 2:
            tail_position[0] -= 1
            tail_position[1] -= 1
        if head[0] == tail[0] - 2 and head[1] == tail[1] + 2:
            tail_position[0] -= 1
            tail_position[1] += 1


    tail_position = (tail_position[0], tail_position[1])
    return tail_position


if __name__ == "__main__":
    f = open("input.txt", "r")
    moves = []
    tail_positions = [(0, 0)]
    head_position = (0, 0)
    tail_position = (0, 0)
    rope = []
    for i in range(10):
        rope.append((0, 0))

    for line in f:
        moves.append(line.replace("\n", "").split(" "))

    for move in moves:
        direction = move[0]
        steps = move[1]
        for i in range(int(steps)):
            if direction == 'R':
                head_position = (head_position[0] + 1, head_position[1])
            elif direction == 'D':
                head_position = (head_position[0], head_position[1] - 1)
            elif direction == 'L':
                head_position = (head_position[0] - 1, head_position[1])
            else:
                head_position = (head_position[0], head_position[1] + 1)
            rope[0] = head_position
            for j in range(9):
                if not is_adjacent(rope[j], rope[j+1]):
                    rope[j+1] = update_tail_position(rope[j], rope[j+1])
                    tail_positions.append(rope[9])

    asd = set(tail_positions)
    print(len(asd))