import time
import cython

def get_points_just_outside(sensor, distance):
    result = []
    current = (sensor[0], sensor[1] - distance - 1)
    for i in range(distance):
        current = (current[0] + 1, current[1] + 1)
        if current[0] >= 0 and current[0] <= 4000000 and current[1] >= 0 and current[1] <= 4000000:
            result.append(current)
    for i in range(distance):
        current = (current[0] - 1, current[1] + 1)
        if current[0] >= 0 and current[0] <= 4000000 and current[1] >= 0 and current[1] <= 4000000:
            result.append(current)
    for i in range(distance):
        current = (current[0] - 1, current[1] - 1)
        if current[0] >= 0 and current[0] <= 4000000 and current[1] >= 0 and current[1] <= 4000000:
            result.append(current)
    for i in range(distance):
        current = (current[0] + 1, current[1] - 1)
        if current[0] >= 0 and current[0] <= 4000000 and current[1] >= 0 and current[1] <= 4000000:
            result.append(current)
    return result

def is_point_in_area(sensor, distance, point):
    sensor_point_distance = max(sensor[0], point[0]) - min(sensor[0], point[0]) + (max(sensor[1], point[1]) - min(sensor[1], point[1]))
    return sensor_point_distance <= distance

if __name__ == "__main__":
    f = open("input.txt", "r")
    distances = []
    sensor_location = []
    closest_beacon = []

    for line in f:
        line = line.replace("\n", "")
        print(line)
        data = line.split(" ")
        sensor_location.append((int(data[2][2:-1:]), int(data[3][2:-1:])))
        closest_beacon.append((int(data[8][2:-1:]), int(data[9][2::])))
        distances.append(max(sensor_location[-1][0], closest_beacon[-1][0]) - min(sensor_location[-1][0], closest_beacon[-1][0]) + (max(sensor_location[-1][1], closest_beacon[-1][1]) - min(sensor_location[-1][1], closest_beacon[-1][1])))

    s1 = time.time()

    points_just_outside = []
    for i in range(len(sensor_location)):
        result = get_points_just_outside(sensor_location[i], distances[i])
        for point in result:
            points_just_outside.append(point)
    print(len(points_just_outside))

    s2 = time.time()

    l = len(sensor_location)
    s = 0
    for point in points_just_outside:
        flag = False
        i = 0
        while i < l and not flag:
            if is_point_in_area(sensor_location[i], distances[i], point):
                flag = True
            i += 1
        if not flag:
            print(point)
            print(point[0] * 4000000 + point[1])
            break

    s3 = time.time()

    print()
    print(s2-s1)
    print(s3-s2)
    print(s3-s1)