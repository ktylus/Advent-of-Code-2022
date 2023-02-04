
if __name__ == "__main__":
    f = open("input.txt", "r")
    distances = []
    sensor_location = []
    closest_beacon = []
    covered_intervals = []

    for line in f:
        line = line.replace("\n", "")
        print(line)
        data = line.split(" ")
        sensor_location.append((int(data[2][2:-1:]), int(data[3][2:-1:])))
        closest_beacon.append((int(data[8][2:-1:]), int(data[9][2::])))
        distances.append(max(sensor_location[-1][0], closest_beacon[-1][0]) - min(sensor_location[-1][0], closest_beacon[-1][0]) + (max(sensor_location[-1][1], closest_beacon[-1][1]) - min(sensor_location[-1][1], closest_beacon[-1][1])))
    print(sensor_location)
    print(closest_beacon)
    print(distances)

    for i in range(len(distances)):
        y_distance_to_ten = max(2000000, sensor_location[i][1]) - min(sensor_location[i][1], 2000000)
        if y_distance_to_ten <= distances[i]:
            left_end = sensor_location[i][0] - (distances[i] - y_distance_to_ten)
            right_end = sensor_location[i][0] + (distances[i] - y_distance_to_ten)
            covered_intervals.append((left_end, right_end))

    blocked_positions = [0] * 12000000

    for i in range(len(blocked_positions)):
        for j in range(len(covered_intervals)):
            if i - 4000000 in range(covered_intervals[j][0], covered_intervals[j][1] + 1):
                blocked_positions[i] = 1

    total = 0
    for i in range(len(blocked_positions)):
        if blocked_positions[i] == 1:
            total += 1

    for beacon in set(closest_beacon):
        if beacon[1] == 2000000:
            total -= 1

    print(total)
