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
        if new_edge_weight < edge_weights[(first_neighbor, second_neighbor)] or edge_weights[
            (first_neighbor, second_neighbor)] == 0:
            update_edge_weight(first_neighbor, second_neighbor, new_edge_weight, graph)
        delete_vertex(vertex, graph)


def solution2(curr_v, prev_v, curr_v_ele, prev_v_ele, score, valves, time, wait_time, wait_time_ele, opened_valve,
              opened_valve_ele, time_without_valve, time_without_valve_ele):
    scores = [score]
    if time <= 1 or time_without_valve >= 4 or time_without_valve_ele >= 6:
        return max(scores)

    # BOTH WAIT
    if wait_time > 0 and wait_time_ele > 0:
        elapsed_time = min(wait_time, wait_time_ele)
        scores.append(solution2(curr_v, prev_v, curr_v_ele, prev_v_ele, score, valves, time - elapsed_time,
                                wait_time - elapsed_time, wait_time_ele - elapsed_time, opened_valve, opened_valve_ele,
                                time_without_valve + elapsed_time, time_without_valve_ele + elapsed_time))

    # ELEPHANT WAITS
    elif wait_time_ele > 0:
        for v in neighbors[curr_v]:
            if opened_valve or v != prev_v:
                scores.append(
                    solution2(v, curr_v, curr_v_ele, prev_v_ele, score, valves, time - 1, edge_weights[(curr_v, v)] - 1,
                              wait_time_ele - 1, False, False, time_without_valve + 1, time_without_valve_ele + 1))
        if curr_v not in valves and curr_v != "AA":
            scores.append(solution2(curr_v, prev_v, curr_v_ele, prev_v_ele, score + (time - 1) * vertex_values[curr_v],
                                    valves + [curr_v], time - 1, 0, wait_time_ele - 1, True, False, 0,
                                    time_without_valve_ele + 1))

    # HUMAN WAITS
    elif wait_time > 0:
        for v in neighbors[curr_v_ele]:
            if opened_valve_ele or v != prev_v_ele:
                scores.append(solution2(curr_v, prev_v, v, curr_v_ele, score, valves, time - 1, wait_time - 1,
                                        edge_weights[(curr_v_ele, v)] - 1, False, False, time_without_valve + 1,
                                        time_without_valve_ele + 1))
        if curr_v_ele not in valves and curr_v_ele != "AA":
            scores.append(
                solution2(curr_v, prev_v, curr_v_ele, prev_v_ele, score + (time - 1) * vertex_values[curr_v_ele],
                          valves + [curr_v_ele], time - 1, wait_time - 1, 0, False, True, time_without_valve + 1, 0))

    # NO ONE WAITS
    else:
        # both travel
        for v1 in neighbors[curr_v]:
            for v2 in neighbors[curr_v_ele]:
                if (opened_valve or v1 != prev_v) and (opened_valve_ele or v2 != prev_v_ele):
                    scores.append(
                        solution2(v1, curr_v, v2, curr_v_ele, score, valves, time - 1, edge_weights[(curr_v, v1)] - 1,
                                  edge_weights[(curr_v_ele, v2)] - 1, False, False, time_without_valve + 1,
                                  time_without_valve_ele + 1))
        # human travels, elephant opens a valve
        for v1 in neighbors[curr_v]:
            if (opened_valve or v1 != prev_v) and (curr_v_ele not in valves and curr_v_ele != "AA"):
                scores.append(
                    solution2(v1, curr_v, curr_v_ele, prev_v_ele, score + (time - 1) * vertex_values[curr_v_ele],
                              valves + [curr_v_ele], time - 1, edge_weights[(curr_v, v1)] - 1, 0, False, True,
                              time_without_valve + 1, 0))
        # human opens a valve, elephant travels
        for v2 in neighbors[curr_v_ele]:
            if (opened_valve_ele or v2 != prev_v_ele) and (curr_v not in valves and curr_v != "AA"):
                scores.append(solution2(curr_v, prev_v, v2, curr_v_ele, score + (time - 1) * vertex_values[curr_v],
                                        valves + [curr_v], time - 1, 0, edge_weights[(curr_v_ele, v2)] - 1, True, False,
                                        0, time_without_valve_ele + 1))
        # both open valve
        if (curr_v not in valves and curr_v != "AA") and (
                curr_v_ele not in valves and curr_v_ele != "AA") and curr_v != curr_v_ele:
            scores.append(solution2(curr_v, prev_v, curr_v_ele, prev_v_ele,
                                    score + (time - 1) * (vertex_values[curr_v] + vertex_values[curr_v_ele]),
                                    valves + [curr_v, curr_v_ele], time - 1, 0, 0, True, True, 0, 0))

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

    print(solution2(start_vertex, None, start_vertex, None, 0, [], 26, 0, 0, False, False, 0, 0))

    '''
    pomysły:

    solution2 pewnie lepiej by było zrobić ze wspólnym czasem dla człowieka i słonia, z dodaniem
    parametru waiting dla obu z nich, określającego ile muszą czekać (mogą wykonywać operację trwającą
    dłużej niż 1 minutę, czyli przechodzenie po skompresowanej ścieżce)

    otworzone zawory można ustawić na 0 (tylko w danym wywołaniu rekurencyjnym) ponieważ ich wartość już
    nas nie interesuje - służą one tylko do przechodzenia pomiędzy punktami, więc można je skompresować
    przy kolejnych iteracjach
    przewiduję, że to bardzo polepszy czas wykonania, ponieważ im głębiej, tym więcej równoległych iteracji,
    a jednocześnie więcej otwartych zaworów, więc będą się wykonywać na prostszych grafach
    z drugiej strony kompresja nie zmniejsza liczby sąsiadów wierzchołków sąsiadujących
    może jednak bardzo pomóc wtedy, gdy już istnieje ścieżka pomiędzy sąsiadami i jest ona krótsza, wtedy można
    za darmo pozbyć się złożoności

    wprowadzic licznik ruchow bez otwarcia zaworu - mozna latwo ograniczyc bezsensowne ścieżki wykonania
    polegające na chodzeniu bez otwierania - wiadomo, że nie są optymalne (liczyć np. do 6 lub 10, zależy od grafu)

    '''

    '''
    wyniki pomiaru czaru solution na przykładzie:
    pierwszy pomiar (wersja która przeszła rano):                                       2.27s
    drugi pomiar (licznik bez otwarcia zaworu - przy >= 5 return na początku):          0.15s



    na inpucie właściwym:

    czas 30:
    z licznikiem (>= 5 - return):                                                       217.51s
    po usunięciu sprawdzania czy mamy czas na pojscie krawedzia (niepotrzebne):         71.16s
    z licznikiem (>= 2 - return) (co ciekawe działa):                                   0.01s

    czas 26:
    z licznikiem (>= 5 - return):                                                       22.95s
    po usunięciu sprawdzania czy mamy czas na pojscie krawedzia (niepotrzebne):         7.63s
    z licznikiem (>= 2 - return) (co ciekawe działa):                                   0.01s
    '''

