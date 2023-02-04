import collections


def update_edge_weight(first, second, value, graph):
    neighbors = graph[0]
    edge_weights = graph[1]
    if edge_weights[(first, second)] == 0 and value > 0:
        neighbors[first].append(second)
        neighbors[second].append(first)
    edge_weights[(first, second)] = value
    edge_weights[(second, first)] = value
    if value == 0:
        edge_weights.pop((first, second))
        edge_weights.pop((second, first))
        neighbors[first].remove(second)
        neighbors[second].remove(first)


def delete_vertex(vertex, graph):
    neighbors = graph[0]
    length = len(neighbors[vertex])
    for _ in range(length):
        update_edge_weight(vertex, neighbors[vertex][0], 0, graph)
    neighbors.pop(vertex)
    vertex_values.pop(vertex)
    for v in neighbors.keys():
        if vertex in neighbors[v]:
            neighbors[v].remove(vertex)


def compress_vertex(vertex, graph):
    neighbors = graph[0]
    edge_weights = graph[1]
    if len(neighbors[vertex]) == 2:
        first_neighbor = neighbors[vertex][0]
        second_neighbor = neighbors[vertex][1]
        new_edge_weight = edge_weights[(first_neighbor, vertex)] + edge_weights[(vertex, second_neighbor)]
        if new_edge_weight < edge_weights[(first_neighbor, second_neighbor)] or edge_weights[(first_neighbor, second_neighbor)] == 0:
            update_edge_weight(first_neighbor, second_neighbor, new_edge_weight, graph)
        delete_vertex(vertex, graph)


def solution(current_vertex, previous_vertex, score, enabled_valves, time, opened_valve, time_without_valve):
    scores = [score]
    if time <= 1 or time_without_valve >= 2:
        return max(scores)
    for v in neighbors[current_vertex]:
        if opened_valve or v != previous_vertex:
            scores.append(solution(v, current_vertex, score, enabled_valves, time - edge_weights[(current_vertex, v)], False, time_without_valve + 1))
    if current_vertex not in enabled_valves and current_vertex != "AA":
        scores.append(solution(current_vertex, previous_vertex, score + (time - 1) * vertex_values[current_vertex], enabled_valves + [current_vertex], time - 1, True, 0))
    return max(scores)


if __name__ == "__main__":
    vertex_values = collections.defaultdict(int)
    neighbors = collections.defaultdict(list)
    edge_weights = collections.defaultdict(int)
    start_vertex = "AA"

    f = open("input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        current_vertex = line.split(" ")[1]
        flow_rate = int(line.split("=")[1].split(";")[0])
        for i in range(9, len(line.split(" "))):
            if i == len(line.split(" ")) - 1:
                neighbors[current_vertex].append(line.split(" ")[i])
            else:
                neighbors[current_vertex].append(line.split(" ")[i][:-1:])
        vertex_values[current_vertex] = flow_rate

    for vertex in neighbors.keys():
        for neighbor in neighbors[vertex]:
            edge_weights[(vertex, neighbor)] += 1

    g = (neighbors, edge_weights)
    zero_value_vertices = list(filter(lambda x: vertex_values[x] == 0 and x != "AA", vertex_values.keys()))
    for vertex in zero_value_vertices:
        compress_vertex(vertex, g)

    print(solution(start_vertex, None, 0, [], 30, False, 0))


