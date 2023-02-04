import collections


def mix(number_tuple, index):
    if number_tuple[0] == 0:
        return
    file.pop(index)
    index_to_insert = (index + number_tuple[0]) % len(file)
    if index_to_insert == 0:
        index_to_insert = len(file)
    file.insert(index_to_insert, number_tuple)


if __name__ == "__main__":

    file = []
    file_copy = []
    numbers_count = collections.defaultdict(int)

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        number = int(line)
        file.append((number, numbers_count[number]))
        file_copy.append(number)
        numbers_count[number] += 1

    numbers_count = collections.defaultdict(int)
    for i in range(len(file_copy)):
        for j in range(len(file)):
            if file[j] == (file_copy[i], numbers_count[file[j][0]]):
                index = j
                numbers_count[file[j][0]] += 1
                break
        mix(file[index], index)

    score = 0
    zero_index = 0
    for i in range(len(file)):
        if file[i][0] == 0:
            zero_index = i

    for i in range(len(file)):
        if i == (zero_index + 1000) % len(file) or i == (zero_index + 2000) % len(file) or i == (zero_index + 3000) % len(file):
            score += file[i][0]

    print(score)
